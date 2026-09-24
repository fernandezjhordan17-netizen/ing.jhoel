<#
.SYNOPSIS
    JARVIS BIM - Instala el servidor MCP propio "jarvis-bim" y lo registra en Claude Desktop.

.DESCRIPTION
    1. Crea un entorno virtual en jarvis-mcp\.venv e instala el paquete (con IfcOpenShell y comtypes).
    2. Ejecuta las pruebas automaticas (salvo -SinPruebas).
    3. Agrega "jarvis-bim" a %APPDATA%\Claude\claude_desktop_config.json (con copia de respaldo y confirmacion).

.EXAMPLE
    powershell -ExecutionPolicy Bypass -File .\scripts\07_instalar_jarvis_mcp.ps1
#>
[CmdletBinding()]
param(
    [switch]$SinPruebas,
    [switch]$SinConfigurarClaude,
    [switch]$Si   # no pedir confirmacion al modificar la configuracion de Claude
)

$ErrorActionPreference = "Stop"
$Repo = Split-Path $PSScriptRoot -Parent
$Paquete = Join-Path $Repo "jarvis-mcp"
$Boveda = Join-Path $Repo "JARVIS-BIM"
$Venv = Join-Path $Paquete ".venv"

function Buscar-Python {
    foreach ($c in @(@("py", "-3"), @("python"), @("python3"))) {
        if (Get-Command $c[0] -ErrorAction SilentlyContinue) {
            $extra = @()
            if ($c.Length -gt 1) { $extra = $c[1..($c.Length - 1)] }
            $ver = & $c[0] @extra -c "import sys; print('%d.%d' % sys.version_info[:2])" 2>$null
            if ($LASTEXITCODE -eq 0 -and [version]$ver -ge [version]"3.10") { return ,@($c[0], $extra) }
        }
    }
    throw "Se necesita Python 3.10 o superior (python.org, marca 'Add to PATH')."
}

Write-Host "==> Python" -ForegroundColor Cyan
$py = Buscar-Python
$pyExe = $py[0]
$pyArgs = $py[1]
Write-Host "   usando: $pyExe $pyArgs"

Write-Host "==> Entorno virtual: $Venv" -ForegroundColor Cyan
if (-not (Test-Path -LiteralPath $Venv)) { & $pyExe @pyArgs -m venv "$Venv" }
$VenvPy = Join-Path $Venv "Scripts\python.exe"
$Ejecutable = Join-Path $Venv "Scripts\jarvis-bim-mcp.exe"
if (-not (Test-Path -LiteralPath $VenvPy)) {   # Linux/macOS (pruebas)
    $VenvPy = Join-Path $Venv "bin/python"
    $Ejecutable = Join-Path $Venv "bin/jarvis-bim-mcp"
}
& $VenvPy -m pip install --quiet --upgrade pip | Out-Host
& $VenvPy -m pip install --quiet -e "$Paquete[todo,test]" | Out-Host
if ($LASTEXITCODE -ne 0) { throw "Fallo la instalacion del paquete jarvis-bim-mcp." }
Write-Host "   instalado: $Ejecutable"

if (-not $SinPruebas) {
    Write-Host "==> Pruebas automaticas" -ForegroundColor Cyan
    Push-Location $Paquete
    try { & $VenvPy -m pytest -q | Out-Host } finally { Pop-Location }
    if ($LASTEXITCODE -ne 0) { throw "Hay pruebas fallando: revisa la salida antes de conectar JARVIS." }
}

if ($SinConfigurarClaude) { return }

Write-Host "==> Configuracion de Claude Desktop" -ForegroundColor Cyan
$DirClaude = Join-Path $env:APPDATA "Claude"
$Config = Join-Path $DirClaude "claude_desktop_config.json"
New-Item -ItemType Directory -Force -Path $DirClaude | Out-Null
$datos = [pscustomobject]@{}
if (Test-Path -LiteralPath $Config) {
    $texto = Get-Content -LiteralPath $Config -Raw
    if ($texto.Trim()) { $datos = $texto | ConvertFrom-Json }
}
if (-not ($datos.PSObject.Properties.Name -contains "mcpServers")) {
    $datos | Add-Member -NotePropertyName mcpServers -NotePropertyValue ([pscustomobject]@{})
}
$entrada = [pscustomobject]@{
    command = $Ejecutable
    args    = @()
    env     = [pscustomobject]@{ JARVIS_BOVEDA = $Boveda }
}
$existe = $datos.mcpServers.PSObject.Properties.Name -contains "jarvis-bim"
Write-Host "   archivo: $Config"
Write-Host "   $(if ($existe) { 'se REEMPLAZA' } else { 'se AGREGA' }) el servidor 'jarvis-bim' -> $Ejecutable"
if (-not $Si) {
    $r = Read-Host "   Confirmar cambio en la configuracion de Claude Desktop? (s/n)"
    if ($r -notin @("s", "S", "si", "SI", "y")) { Write-Host "   Cancelado. Nada modificado."; return }
}
if (Test-Path -LiteralPath $Config) {
    $respaldo = "$Config.respaldo-$(Get-Date -Format 'yyyyMMdd-HHmmss')"
    Copy-Item -LiteralPath $Config -Destination $respaldo
    Write-Host "   respaldo: $respaldo"
}
$datos.mcpServers | Add-Member -NotePropertyName "jarvis-bim" -NotePropertyValue $entrada -Force
$json = $datos | ConvertTo-Json -Depth 10
[System.IO.File]::WriteAllText($Config, $json, (New-Object System.Text.UTF8Encoding($false)))
Write-Host ""
Write-Host "Listo. Reinicia Claude Desktop (cerrar tambien desde la bandeja del sistema) y pregunta:" -ForegroundColor Green
Write-Host "   'JARVIS, calcula el espectro E.030 para zona 4, suelo S2 con Vs30 = 420 m/s, categoria C, sistema dual'"
