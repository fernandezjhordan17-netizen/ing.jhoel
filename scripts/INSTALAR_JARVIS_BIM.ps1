<#
.SYNOPSIS
    JARVIS BIM - Instalador principal (ejecuta todos los pasos en orden).

.DESCRIPTION
    1. Crea la estructura de carpetas en <Base>.
    2. Descarga modelos BIM abiertos y recopila los ejemplos instalados (01_descargar_proyectos_bim.ps1).
    3. Clona los servidores MCP comunitarios para revisarlos (02_clonar_servidores_mcp.ps1).
    4. Instala IfcOpenShell y convierte cada IFC en una nota de Obsidian (03_ifc_a_obsidian.py).
    5. Verifica la salud de la red de notas (04_salud_red_neuronal.py).

.EXAMPLE
    cd "C:\Users\JHORDAN\Documents\1.APP CREADOS\APP PARA BIM\ing.jhoel"
    powershell -ExecutionPolicy Bypass -File .\scripts\INSTALAR_JARVIS_BIM.ps1
#>
[CmdletBinding()]
param(
    [string]$Base = "C:\Users\JHORDAN\Documents\1.APP CREADOS\APP PARA BIM",
    [switch]$IncluirPesados,
    [switch]$SinServidoresMCP,
    [switch]$SinArchivosLocales
)

$ErrorActionPreference = "Continue"
$Repo = Split-Path $PSScriptRoot -Parent
$Boveda = Join-Path $Repo "JARVIS-BIM"

Write-Host "JARVIS BIM - instalacion" -ForegroundColor Green
Write-Host "Base:    $Base"
Write-Host "Boveda:  $Boveda"

# 1. Estructura de carpetas
foreach ($c in @("02_PROYECTOS_BIM", "03_PROYECTOS_REALES", "04_MCP_SERVERS", "05_RESPALDOS")) {
    New-Item -ItemType Directory -Force -Path (Join-Path $Base $c) | Out-Null
}

# 2. Modelos BIM
$args01 = @{ Base = $Base }
if ($IncluirPesados) { $args01.IncluirPesados = $true }
if ($SinArchivosLocales) { $args01.SinArchivosLocales = $true }
& (Join-Path $PSScriptRoot "01_descargar_proyectos_bim.ps1") @args01

# 3. Servidores MCP
if (-not $SinServidoresMCP) {
    & (Join-Path $PSScriptRoot "02_clonar_servidores_mcp.ps1") -Base $Base
}

# 4. Python: IfcOpenShell + notas de Obsidian
$pyExe = $null
$pyArgs = @()
if (Get-Command py -ErrorAction SilentlyContinue) { $pyExe = "py"; $pyArgs = @("-3") }
elseif (Get-Command python -ErrorAction SilentlyContinue) { $pyExe = "python" }

if ($pyExe) {
    Write-Host ""
    Write-Host "==> Instalando dependencias de Python (IfcOpenShell)" -ForegroundColor Cyan
    & $pyExe @pyArgs -m pip install --upgrade -r (Join-Path $PSScriptRoot "requirements.txt") | Out-Host
    Write-Host ""
    Write-Host "==> Generando notas de Obsidian desde los IFC" -ForegroundColor Cyan
    & $pyExe @pyArgs (Join-Path $PSScriptRoot "03_ifc_a_obsidian.py") --entrada (Join-Path $Base "02_PROYECTOS_BIM") --boveda $Boveda --raiz-mostrada "02_PROYECTOS_BIM" | Out-Host
    Write-Host ""
    Write-Host "==> Salud de la red neuronal" -ForegroundColor Cyan
    & $pyExe @pyArgs (Join-Path $PSScriptRoot "04_salud_red_neuronal.py") --boveda $Boveda | Out-Host
} else {
    Write-Host "Python no encontrado. Instala Python 3.11+ (python.org, marca 'Add to PATH') y ejecuta:" -ForegroundColor Yellow
    Write-Host "   python scripts\03_ifc_a_obsidian.py --entrada `"$Base\02_PROYECTOS_BIM`" --boveda JARVIS-BIM --raiz-mostrada 02_PROYECTOS_BIM"
}

Write-Host ""
Write-Host "Listo. Proximos pasos:" -ForegroundColor Green
Write-Host " 1. Abre Obsidian > 'Abrir carpeta como boveda' > $Boveda"
Write-Host " 2. Lee la nota 'JARVIS BIM - Inicio' y 'Como usar esta boveda'"
Write-Host " 3. Conecta Claude Desktop con jarvis\claude_desktop_config.ejemplo.json"
