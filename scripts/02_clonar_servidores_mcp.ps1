<#
.SYNOPSIS
    JARVIS BIM - Clona (NO instala ni ejecuta) los servidores MCP y agentes comunitarios
    para Revit, Dynamo, AutoCAD/Civil 3D, Navisworks, ETABS/SAP2000, Robot, Tekla, Excel y Obsidian.

.DESCRIPTION
    Deja cada repositorio en <Base>\04_MCP_SERVERS\<Programa>\<repositorio> para que puedas
    LEER su codigo y su README antes de instalarlo (regla 7 de "JARVIS - Seguridad y gobernanza").
    Requiere Git para Windows (git-scm.com).

.EXAMPLE
    powershell -ExecutionPolicy Bypass -File .\scripts\02_clonar_servidores_mcp.ps1
#>
[CmdletBinding()]
param(
    [string]$Base = "C:\Users\JHORDAN\Documents\1.APP CREADOS\APP PARA BIM"
)

$ErrorActionPreference = "Continue"
$Destino = Join-Path $Base "04_MCP_SERVERS"

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Host "Git no esta instalado. Instala Git para Windows (https://git-scm.com) y vuelve a ejecutar." -ForegroundColor Red
    exit 1
}

# Programa | propietario/repositorio | descripcion
$Servidores = @(
    @("Revit",       "mcp-servers-for-revit/mcp-servers-for-revit",       "MCP comunitario Revit 2020-2026 (TS + plugin C#), MIT"),
    @("Revit",       "LuDattilo/RevitCortex",                             "MCP Revit 2023-2027, ~170 herramientas"),
    @("Revit",       "KenLP/RevitMCPServer",                              "MCP Revit 2025-2027, operaciones en una transaccion deshacible"),
    @("Revit",       "bimwright/rvt-mcp",                                 "MCP Revit 2022-2027"),
    @("Revit",       "SquareZero-Inc/bibim-revit",                        "Agente BIBIM: lenguaje natural a C# dentro de Revit (no MCP)"),
    @("Dynamo",      "SquareZero-Inc/bibim-dynamo",                       "Agente BIBIM para Dynamo (genera Python)"),
    @("AutoCAD",     "puran-water/autocad-mcp",                           "MCP AutoCAD/LT via AutoLISP + ezdxf sin AutoCAD"),
    @("Navisworks",  "mikhalchankasm/NavisWorksMaster",                   "MCP Navisworks Manage 2024-2027, dry-run por defecto"),
    @("Navisworks",  "Aitology/Navisworks_MCP",                           "MCP Navisworks: clash, sets, viewpoints"),
    @("Navisworks",  "HorizunGroup/naviscoord-mcp",                       "MCP Navisworks 2024-2026: coordinacion asistida"),
    @("CSI",         "mdvaleed7/ETABS-mcp",                               "MCP ETABS v19-v22 (Python, comtypes), 69 herramientas"),
    @("CSI",         "Aaradhya-Dev-Tamrakar/sap2000-mcp",                 "MCP SAP2000 via OAPI"),
    @("Robot",       "TranTriLuc/robot-structural-mcp",                   "MCP Robot: modelo, cargas, calculo, resultados"),
    @("Robot",       "nhantruong96/rsap-mcp",                             "MCP Robot 2027 via RobotOM, 35 herramientas"),
    @("Tekla",       "teknovizier/tekla_mcp_server",                      "MCP Tekla Structures (FastMCP)"),
    @("Tekla",       "YuriyKirillov/TeklaMCPServer",                      "MCP Tekla Structures"),
    @("Tekla",       "pawellisowski/tekla-api-mcp",                       "MCP de documentacion Tekla Open API + ejemplos"),
    @("Excel",       "haris-musa/excel-mcp-server",                       "MCP Excel sin Excel instalado (openpyxl), MIT"),
    @("APS",         "autodesk-platform-services/aps-aecdm-mcp-dotnet",   "Ejemplo oficial APS: AEC Data Model + Viewer"),
    @("Obsidian",    "msdanyg/smart-connections-mcp",                     "Busqueda semantica sobre embeddings de Smart Connections")
)

$Indice = New-Object System.Collections.Generic.List[object]
foreach ($s in $Servidores) {
    $programa, $repo, $desc = $s
    $nombre = ($repo -split "/")[1]
    $carpeta = Join-Path (Join-Path $Destino $programa) $nombre
    Write-Host ""
    Write-Host "==> [$programa] $repo" -ForegroundColor Cyan
    if (Test-Path -LiteralPath (Join-Path $carpeta ".git")) {
        & git -C "$carpeta" pull --ff-only | Out-Host
    } else {
        New-Item -ItemType Directory -Force -Path (Split-Path $carpeta -Parent) | Out-Null
        & git -c core.longpaths=true clone --depth 1 "https://github.com/$repo.git" "$carpeta" | Out-Host
    }
    $estado = if ($LASTEXITCODE -eq 0) { "OK" } else { "ERROR" }
    $Indice.Add([pscustomobject]@{ Programa = $programa; Repositorio = $repo; Carpeta = $carpeta; Estado = $estado; Descripcion = $desc })
}

$csv = Join-Path $Destino "INDICE_SERVIDORES_MCP.csv"
$Indice | Export-Csv -LiteralPath $csv -NoTypeInformation -Encoding UTF8
Write-Host ""
Write-Host "Indice: $csv" -ForegroundColor Green
Write-Host "IMPORTANTE: estos servidores actuan sobre tus modelos con tus permisos." -ForegroundColor Yellow
Write-Host "Lee cada README, revisa el codigo y pruebalos primero en COPIAS de modelos." -ForegroundColor Yellow
Write-Host "Configuracion de Claude: ver JARVIS-BIM\50 JARVIS\Configuracion de clientes MCP.md"
