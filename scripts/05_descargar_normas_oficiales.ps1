<#
.SYNOPSIS
    JARVIS BIM - Descarga los PDF oficiales de normas y guias (RNE, Plan BIM Peru, Guia Nacional BIM,
    Ley 32069, DG-2018, metrados, guias ISO 19650, LOD 2025, PxP v3) y los convierte en notas de Obsidian.

.DESCRIPTION
    Lee scripts\catalogo_normas.csv. Para cada documento prueba sus URLs en orden (fuente oficial primero,
    espejos despues), verifica que el archivo descargado sea un PDF real (cabecera %PDF) y lo guarda en:
        JARVIS-BIM\90 RECURSOS\Adjuntos\Normas\<carpeta>\<id>.pdf
    Luego ejecuta 06_pdf_a_obsidian.py para que el texto quede dentro de la boveda (Smart Connections
    y JARVIS solo "absorben" texto Markdown, no PDF).

    Los PDF quedan en tu PC (estan excluidos de git). Las normas ISO no se descargan: son de pago.

.EXAMPLE
    powershell -ExecutionPolicy Bypass -File .\scripts\05_descargar_normas_oficiales.ps1
#>
[CmdletBinding()]
param(
    [string]$Destino = "",
    [switch]$SinConvertir,   # solo descarga, no genera notas
    [switch]$Forzar          # vuelve a descargar aunque ya exista
)

$ErrorActionPreference = "Continue"
$ProgressPreference = "SilentlyContinue"
[Net.ServicePointManager]::SecurityProtocol = [Net.ServicePointManager]::SecurityProtocol -bor [Net.SecurityProtocolType]::Tls12

$Repo = Split-Path $PSScriptRoot -Parent
$Boveda = Join-Path $Repo "JARVIS-BIM"
if (-not $Destino) { $Destino = Join-Path $Boveda (Join-Path "90 RECURSOS" (Join-Path "Adjuntos" "Normas")) }
$Catalogo = Join-Path $PSScriptRoot "catalogo_normas.csv"
$Navegador = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"

function Es-PdfValido([string]$Ruta) {
    if (-not (Test-Path -LiteralPath $Ruta)) { return $false }
    if ((Get-Item -LiteralPath $Ruta).Length -lt 1024) { return $false }
    $fs = [System.IO.File]::OpenRead($Ruta)
    try {
        $buf = New-Object byte[] 5
        $null = $fs.Read($buf, 0, 5)
        return ([System.Text.Encoding]::ASCII.GetString($buf) -eq "%PDF-")
    } finally { $fs.Dispose() }
}

$filas = Import-Csv -LiteralPath $Catalogo
$Estado = New-Object System.Collections.Generic.List[object]
Write-Host "Descargando $($filas.Count) documentos a: $Destino" -ForegroundColor Green

foreach ($f in $filas) {
    $carpeta = Join-Path $Destino $f.carpeta
    New-Item -ItemType Directory -Force -Path $carpeta | Out-Null
    $salida = Join-Path $carpeta "$($f.id).pdf"
    Write-Host ""
    Write-Host "==> [$($f.codigo)] $($f.titulo)" -ForegroundColor Cyan

    if ((-not $Forzar) -and (Es-PdfValido $salida)) {
        Write-Host "   (ya existe)"
        $Estado.Add([pscustomobject]@{ id = $f.id; codigo = $f.codigo; estado = "OK (existente)"; url = ""; archivo = $salida })
        continue
    }

    $ok = $false
    $usada = ""
    foreach ($u in @($f.url1, $f.url2, $f.url3)) {
        if (-not $u) { continue }
        try {
            Invoke-WebRequest -Uri $u -OutFile $salida -UseBasicParsing -UserAgent $Navegador -TimeoutSec 180 -MaximumRedirection 5 -ErrorAction Stop
            if (Es-PdfValido $salida) {
                $ok = $true
                $usada = $u
                $mb = [math]::Round((Get-Item -LiteralPath $salida).Length / 1MB, 2)
                Write-Host "   OK  $mb MB  <- $u"
                break
            } else {
                Write-Host "   (no es PDF, se descarta) $u" -ForegroundColor Yellow
                Remove-Item -LiteralPath $salida -Force -ErrorAction SilentlyContinue
            }
        } catch {
            Write-Host "   fallo: $u ($($_.Exception.Message))" -ForegroundColor Yellow
            Remove-Item -LiteralPath $salida -Force -ErrorAction SilentlyContinue
        }
    }
    if (-not $ok) { Write-Host "   NO DESCARGADO: busca '$($f.codigo) $($f.version) pdf' en gob.pe o elperuano.pe y guardalo como $salida" -ForegroundColor Red }
    $Estado.Add([pscustomobject]@{ id = $f.id; codigo = $f.codigo; estado = $(if ($ok) { "OK" } else { "FALTA" }); url = $usada; archivo = $salida })
}

$csv = Join-Path $Destino "ESTADO_DESCARGA.csv"
$Estado | Export-Csv -LiteralPath $csv -NoTypeInformation -Encoding UTF8
$okCount = @($Estado | Where-Object { $_.estado -like "OK*" }).Count
Write-Host ""
Write-Host "Descargados: $okCount de $($filas.Count). Detalle: $csv" -ForegroundColor Green

if ($SinConvertir) { return }

$pyExe = $null
$pyArgs = @()
if (Get-Command py -ErrorAction SilentlyContinue) { $pyExe = "py"; $pyArgs = @("-3") }
elseif (Get-Command python -ErrorAction SilentlyContinue) { $pyExe = "python" }
elseif (Get-Command python3 -ErrorAction SilentlyContinue) { $pyExe = "python3" }
if (-not $pyExe) {
    Write-Host "Python no encontrado: instala Python 3.11+ y ejecuta scripts\06_pdf_a_obsidian.py" -ForegroundColor Yellow
    return
}
Write-Host ""
Write-Host "==> Convirtiendo PDF a notas de Obsidian (texto por articulos)" -ForegroundColor Cyan
& $pyExe @pyArgs -m pip install --quiet --upgrade pymupdf | Out-Host
& $pyExe @pyArgs (Join-Path $PSScriptRoot "06_pdf_a_obsidian.py") --entrada $Destino --boveda $Boveda --catalogo $Catalogo | Out-Host
