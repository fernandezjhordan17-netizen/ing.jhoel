<#
.SYNOPSIS
    JARVIS BIM - Descarga modelos BIM abiertos y recopila los ejemplos que ya trae tu software.

.DESCRIPTION
    1) Descarga modelos IFC reales y abiertos (buildingSMART, Duplex, Revit ARC/STR/MEP, SampleHouse...).
    2) Descarga los estandares openBIM (IDS, BCF) con sus ejemplos.
    3) Busca en tu PC los proyectos de ejemplo instalados con Revit, Dynamo, Navisworks, Robot,
       ETABS, SAP2000, SAFE, AutoCAD/Civil 3D y Tekla, y los copia a una sola carpeta.
    4) Genera MANIFIESTO.csv con todo lo obtenido.

    Todo se guarda en:  <Base>\02_PROYECTOS_BIM

.EXAMPLE
    powershell -ExecutionPolicy Bypass -File .\scripts\01_descargar_proyectos_bim.ps1

.EXAMPLE
    powershell -ExecutionPolicy Bypass -File .\scripts\01_descargar_proyectos_bim.ps1 -IncluirPesados -AbrirPaginas
#>
[CmdletBinding()]
param(
    [string]$Base = "C:\Users\JHORDAN\Documents\1.APP CREADOS\APP PARA BIM",
    [switch]$IncluirPesados,      # agrega repositorios grandes (Community Sample Files con Git LFS, Dynamo Primer)
    [switch]$SinArchivosLocales,  # no busca ejemplos instalados en el PC
    [switch]$AbrirPaginas         # abre en el navegador las paginas de descarga manual
)

$ErrorActionPreference = "Continue"
$ProgressPreference = "SilentlyContinue"
[Net.ServicePointManager]::SecurityProtocol = [Net.ServicePointManager]::SecurityProtocol -bor [Net.SecurityProtocolType]::Tls12

$Destino = Join-Path $Base "02_PROYECTOS_BIM"
$Manifiesto = New-Object System.Collections.Generic.List[object]
$TieneGit = [bool](Get-Command git -ErrorAction SilentlyContinue)

function Mostrar-Paso([string]$Texto) {
    Write-Host ""
    Write-Host "==> $Texto" -ForegroundColor Cyan
}

function Agregar-Manifiesto([string]$Fuente, [string]$Programa, [string]$Ruta, [string]$Origen) {
    $mb = ""
    $item = Get-Item -LiteralPath $Ruta -ErrorAction SilentlyContinue
    if ($item -and -not $item.PSIsContainer) { $mb = [math]::Round($item.Length / 1MB, 2) }
    $Manifiesto.Add([pscustomobject]@{
        Fuente   = $Fuente
        Programa = $Programa
        Archivo  = $Ruta
        TamanoMB = $mb
        Origen   = $Origen
    })
}

function Descargar-Archivo([string]$Url, [string]$Salida) {
    if ((Test-Path -LiteralPath $Salida) -and ((Get-Item -LiteralPath $Salida).Length -gt 0)) {
        Write-Host "   (ya existe) $(Split-Path $Salida -Leaf)"
        return $true
    }
    New-Item -ItemType Directory -Force -Path (Split-Path $Salida -Parent) | Out-Null
    for ($i = 1; $i -le 3; $i++) {
        try {
            Invoke-WebRequest -Uri $Url -OutFile $Salida -UseBasicParsing -ErrorAction Stop
            Write-Host "   OK  $(Split-Path $Salida -Leaf)"
            return $true
        } catch {
            Write-Host "   intento $i fallido: $($_.Exception.Message)" -ForegroundColor Yellow
            Start-Sleep -Seconds (2 * $i)
        }
    }
    Write-Host "   ERROR: no se pudo descargar $Url" -ForegroundColor Red
    return $false
}

function Obtener-Repositorio([string]$Propietario, [string]$Repo, [string]$Rama, [string]$Carpeta) {
    $url = "https://github.com/$Propietario/$Repo"
    if ($TieneGit) {
        if (Test-Path -LiteralPath (Join-Path $Carpeta ".git")) {
            Write-Host "   actualizando $Repo (git pull)"
            & git -C "$Carpeta" pull --ff-only | Out-Host
        } else {
            Write-Host "   clonando $Repo (rama $Rama)"
            & git -c core.longpaths=true clone --depth 1 --branch $Rama "$url.git" "$Carpeta" | Out-Host
        }
        return ($LASTEXITCODE -eq 0)
    }
    # Sin git: descarga el ZIP de la rama
    $zip = Join-Path $env:TEMP "$Repo-$Rama.zip"
    if (-not (Descargar-Archivo "$url/archive/refs/heads/$Rama.zip" $zip)) { return $false }
    $tmp = Join-Path $env:TEMP "$Repo-$Rama-extraido"
    if (Test-Path -LiteralPath $tmp) { Remove-Item -LiteralPath $tmp -Recurse -Force }
    try {
        Expand-Archive -LiteralPath $zip -DestinationPath $tmp -Force -ErrorAction Stop
        $interior = Get-ChildItem -LiteralPath $tmp -Directory | Select-Object -First 1
        New-Item -ItemType Directory -Force -Path $Carpeta | Out-Null
        Copy-Item -Path (Join-Path $interior.FullName "*") -Destination $Carpeta -Recurse -Force -ErrorAction Stop
        return $true
    } catch {
        Write-Host "   ERROR al extraer $Repo : $($_.Exception.Message)" -ForegroundColor Red
        Write-Host "   Sugerencia: instala Git para Windows (git-scm.com) y vuelve a ejecutar." -ForegroundColor Yellow
        return $false
    } finally {
        if (Test-Path -LiteralPath $tmp) { Remove-Item -LiteralPath $tmp -Recurse -Force -ErrorAction SilentlyContinue }
    }
}

# ---------------------------------------------------------------------------------------------
Mostrar-Paso "Carpeta de destino: $Destino"
New-Item -ItemType Directory -Force -Path $Destino | Out-Null
if (-not $TieneGit) {
    Write-Host "   Git no esta instalado: se usaran descargas ZIP (mas lento, sin Git LFS)." -ForegroundColor Yellow
}

# 1) Modelos IFC de ejemplo (repositorio youshengCode/IfcSampleFiles) ---------------------------
Mostrar-Paso "1/4 Modelos IFC de ejemplo (Duplex, Revit ARC/STR/MEP, SampleHouse, SampleCastle...)"
$ArchivosIfc = @(
    "Ifc2s3_Duplex_Electrical.ifc", "Ifc2x3_Duplex_Architecture.ifc", "Ifc2x3_Duplex_MEP.ifc",
    "Ifc2x3_Duplex_Mechanical.ifc", "Ifc2x3_Duplex_Plumbing.ifc", "Ifc2x3_SampleCastle.ifc",
    "Ifc4_BasinFacetedBrep.ifc", "Ifc4_CubeAdvancedBrep.ifc", "Ifc4_Revit_ARC.ifc",
    "Ifc4_Revit_ARC_FireRatingAdded.ifc", "Ifc4_Revit_MEP.ifc", "Ifc4_Revit_STR.ifc",
    "Ifc4_SampleHouse.ifc", "Ifc4_SampleHouse_0_GroundFloor.ifc", "Ifc4_SampleHouse_1_Roof.ifc",
    "Ifc4_SampleHouse_IfcWallStandardCase.ifc", "Ifc4_SampleHouse_IfcWindow.ifc", "Ifc4_WallElementedCase.ifc"
)
$CarpetaIfc = Join-Path $Destino "IfcSampleFiles"
foreach ($f in $ArchivosIfc) {
    $salida = Join-Path $CarpetaIfc $f
    if (Descargar-Archivo "https://raw.githubusercontent.com/youshengCode/IfcSampleFiles/main/$f" $salida) {
        Agregar-Manifiesto "github.com/youshengCode/IfcSampleFiles" "IFC" $salida "Internet"
    }
}

# 2) Repositorios oficiales buildingSMART ------------------------------------------------------
Mostrar-Paso "2/4 Repositorios buildingSMART (certificacion, IFC 4.3 infraestructura, IDS, BCF)"
$Repos = @(
    @{ P = "buildingSMART"; R = "Sample-Test-Files";        B = "main";        C = "buildingSMART_Sample-Test-Files" },
    @{ P = "buildingSMART"; R = "IFC4.3.x-sample-models";   B = "main";        C = "buildingSMART_IFC4.3_sample-models" },
    @{ P = "buildingSMART"; R = "IDS";                      B = "development"; C = "_ESTANDARES\IDS" },
    @{ P = "buildingSMART"; R = "BCF-XML";                  B = "release_3_0"; C = "_ESTANDARES\BCF-XML" }
)
if ($IncluirPesados) {
    $Repos += @{ P = "buildingsmart-community"; R = "Community-Sample-Test-Files"; B = "main"; C = "buildingSMART_Community-Sample-Test-Files" }
    $Repos += @{ P = "DynamoDS"; R = "DynamoPrimerNew"; B = "master"; C = "_APRENDIZAJE\DynamoPrimer" }
    if ($TieneGit) {
        & git lfs version *> $null
        if ($LASTEXITCODE -eq 0) { & git lfs install | Out-Host }
        else { Write-Host "   Git LFS no instalado: Community-Sample-Test-Files traera punteros en lugar de modelos." -ForegroundColor Yellow }
    }
}
foreach ($r in $Repos) {
    $carpeta = Join-Path $Destino $r.C
    if (Obtener-Repositorio $r.P $r.R $r.B $carpeta) {
        Agregar-Manifiesto "github.com/$($r.P)/$($r.R)" "Repositorio" $carpeta "Internet"
    }
}

# 3) Ejemplos instalados con tu software -------------------------------------------------------
if (-not $SinArchivosLocales) {
    Mostrar-Paso "3/4 Buscando proyectos de ejemplo instalados en este PC (puede tardar varios minutos)"
    $Reglas = @(
        @{ Programa = "Revit";           Patrones = @("*.rvt") },
        @{ Programa = "Dynamo";          Patrones = @("*.dyn") },
        @{ Programa = "Navisworks";      Patrones = @("*.nwd", "*.nwf") },
        @{ Programa = "Robot";           Patrones = @("*.rtd") },
        @{ Programa = "ETABS";           Patrones = @("*.edb", "*.e2k", '*.$et') },
        @{ Programa = "SAP2000";         Patrones = @("*.sdb", "*.s2k", '*.$2k') },
        @{ Programa = "SAFE";            Patrones = @("*.fdb", "*.f2k") },
        @{ Programa = "AutoCAD_Civil3D"; Patrones = @("*.dwg") },
        @{ Programa = "IFC_local";       Patrones = @("*.ifc") }
    )
    $Raices = @(
        "C:\Program Files\Autodesk", "C:\ProgramData\Autodesk", "C:\Users\Public\Documents\Autodesk",
        "C:\Program Files\Computers and Structures", "C:\Program Files\Tekla Structures",
        "C:\ProgramData\Trimble", "C:\TeklaStructuresModels"
    ) | Where-Object { Test-Path -LiteralPath $_ }
    $FiltroRuta = '(?i)sample|example|tutorial|ejemplo|verification|muestra|training|demo'
    $Patrones = @($Reglas | ForEach-Object { $_.Patrones })

    foreach ($raiz in $Raices) {
        Write-Host "   explorando $raiz"
        $encontrados = Get-ChildItem -Path $raiz -Recurse -File -Include $Patrones -ErrorAction SilentlyContinue
        foreach ($f in $encontrados) {
            if ($f.FullName -notmatch $FiltroRuta) { continue }
            if ($f.Length -gt 500MB) { Write-Host "   (omitido >500 MB) $($f.Name)"; continue }
            $ext = $f.Extension.ToLower()
            $regla = $Reglas | Where-Object { $_.Patrones -contains "*$ext" } | Select-Object -First 1
            if (-not $regla) { continue }
            $version = ""
            if ($f.FullName -match '(20\d{2})') { $version = $Matches[1] + "_" }
            $carpeta = Join-Path $Destino ("LOCAL_" + $regla.Programa)
            New-Item -ItemType Directory -Force -Path $carpeta | Out-Null
            $salida = Join-Path $carpeta ($version + $f.Name)
            if (-not (Test-Path -LiteralPath $salida)) {
                Copy-Item -LiteralPath $f.FullName -Destination $salida -ErrorAction SilentlyContinue
                Write-Host "   + $($regla.Programa): $($f.Name)"
            }
            Agregar-Manifiesto "Instalacion local" $regla.Programa $salida $f.FullName
        }
        # Modelos de Tekla: son carpetas completas (*.db1); solo se registran
        Get-ChildItem -Path $raiz -Recurse -File -Filter "*.db1" -ErrorAction SilentlyContinue | ForEach-Object {
            Agregar-Manifiesto "Instalacion local" "Tekla (carpeta de modelo)" $_.DirectoryName $_.DirectoryName
            Write-Host "   + Tekla: $($_.DirectoryName)"
        }
    }
} else {
    Mostrar-Paso "3/4 Busqueda local omitida (-SinArchivosLocales)"
}

# 4) Manifiesto y descargas manuales ------------------------------------------------------------
Mostrar-Paso "4/4 Manifiesto"
$csv = Join-Path $Destino "MANIFIESTO.csv"
$Manifiesto | Export-Csv -LiteralPath $csv -NoTypeInformation -Encoding UTF8
Write-Host "   $($Manifiesto.Count) entradas -> $csv"

$Manuales = @(
    @{ T = "Revit - proyectos de muestra (incluye Snowdon Towers desde 2024)"; U = "https://help.autodesk.com/view/RVT/2026/ENU/?guid=GUID-61EF2F22-3A1F-4317-B925-1E85F138BE88" },
    @{ T = "Tekla Warehouse - modelos y extensiones de ejemplo";               U = "https://warehouse.tekla.com" },
    @{ T = "CSI (ETABS/SAP2000/SAFE) - manuales y ejemplos de verificacion";  U = "https://www.csiamerica.com" },
    @{ T = "buildingSMART Validation Service (validar tus IFC)";              U = "https://validate.buildingsmart.org" }
)
Write-Host ""
Write-Host "Descargas que requieren inicio de sesion o licencia (hazlas a mano y guardalas en $Destino):" -ForegroundColor Green
foreach ($m in $Manuales) {
    Write-Host " - $($m.T): $($m.U)"
    if ($AbrirPaginas) { Start-Process $m.U }
}
Write-Host ""
Write-Host "Siguiente paso: genera las notas de Obsidian con" -ForegroundColor Green
Write-Host "   python scripts\03_ifc_a_obsidian.py --entrada `"$Destino`" --boveda JARVIS-BIM --raiz-mostrada 02_PROYECTOS_BIM"
