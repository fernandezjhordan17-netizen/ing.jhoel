#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
03_ifc_a_obsidian.py - Convierte modelos IFC en notas de Obsidian para JARVIS BIM.

Lee cada archivo .ifc con IfcOpenShell, extrae su estructura (esquema, software de
origen, pisos, clases IFC, materiales, Psets, clasificaciones, calidad) y escribe una
nota Markdown enlazada a las "neuronas" de conocimiento de la boveda JARVIS-BIM.

Uso (Windows, desde la carpeta del repositorio):
    python scripts\\03_ifc_a_obsidian.py ^
        --entrada "C:\\Users\\JHORDAN\\Documents\\1.APP CREADOS\\APP PARA BIM\\02_PROYECTOS_BIM" ^
        --boveda JARVIS-BIM

Requisitos: pip install ifcopenshell
"""
from __future__ import annotations

import argparse
import collections
import datetime as dt
import re
import sys
from pathlib import Path

try:
    import ifcopenshell
    import ifcopenshell.util.element as ue
except ImportError:  # pragma: no cover
    sys.exit("Falta IfcOpenShell. Instala con:  pip install ifcopenshell")

CARPETA_NOTAS = Path("70 PROYECTOS") / "Proyectos de estudio"
NOTA_CLASES = Path("30 NORMAS") / "Clases IFC principales.md"

ARQ = {"IfcWall", "IfcWallStandardCase", "IfcDoor", "IfcWindow", "IfcSpace", "IfcCovering",
       "IfcCurtainWall", "IfcRailing", "IfcStair", "IfcStairFlight", "IfcRoof",
       "IfcFurnishingElement", "IfcFurniture"}
EST = {"IfcBeam", "IfcColumn", "IfcFooting", "IfcPile", "IfcMember", "IfcPlate",
       "IfcReinforcingBar", "IfcReinforcingMesh", "IfcTendon", "IfcStructuralCurveMember",
       "IfcStructuralSurfaceMember"}
MEP_PREFIJOS = ("IfcFlow", "IfcDistribution", "IfcPipe", "IfcDuct", "IfcCable", "IfcAirTerminal",
                "IfcSanitaryTerminal", "IfcLightFixture", "IfcOutlet", "IfcPump", "IfcValve",
                "IfcElectric", "IfcEnergyConversionDevice", "IfcFlowTerminal", "IfcSwitchingDevice",
                "IfcProtectiveDevice", "IfcUnitaryEquipment", "IfcFan", "IfcTank", "IfcBoiler")
INFRA = {"IfcAlignment", "IfcRoad", "IfcBridge", "IfcRailway", "IfcMarineFacility",
         "IfcEarthworksCut", "IfcEarthworksFill", "IfcCourse", "IfcPavement", "IfcTrackElement",
         "IfcGeotechnicalStratum", "IfcBorehole", "IfcFacility", "IfcFacilityPart"}
NO_ELEMENTOS = {"IfcSite", "IfcBuilding", "IfcBuildingStorey", "IfcSpace", "IfcOpeningElement",
                "IfcAnnotation", "IfcGrid", "IfcVirtualElement", "IfcProject", "IfcFacility",
                "IfcFacilityPart", "IfcBridge", "IfcRoad", "IfcRailway", "IfcMarineFacility",
                "IfcAlignment", "IfcAlignmentHorizontal", "IfcAlignmentVertical",
                "IfcAlignmentSegment", "IfcAlignmentCant", "IfcReferent"}


def nombre_seguro(texto: str) -> str:
    texto = re.sub(r'[\\/:*?"<>|#^\[\]]', " ", texto)
    return re.sub(r"\s+", " ", texto).strip()[:120] or "Modelo"


def texto(valor) -> str:
    if valor is None:
        return ""
    return str(valor).replace("|", "/").replace("\n", " ").strip()


def encabezados_clases(boveda: Path) -> set[str]:
    ruta = boveda / NOTA_CLASES
    if not ruta.exists():
        return set()
    return set(re.findall(r"^###\s+(Ifc\w+)\s*$", ruta.read_text(encoding="utf-8"), re.M))


def enlace_clase(clase: str, disponibles: set[str]) -> str:
    if clase in disponibles:
        return f"[[Clases IFC principales#{clase}|{clase}]]"
    if clase == "IfcWallStandardCase" and "IfcWall" in disponibles:
        return "[[Clases IFC principales#IfcWall|IfcWallStandardCase]]"
    return f"`{clase}`"


def cabecera(modelo) -> dict:
    datos = {"mvd": "", "software": "", "autor": "", "organizacion": "", "fecha": ""}
    try:
        h = modelo.header
        desc = h.file_description.description
        datos["mvd"] = texto(desc[0] if desc else "")
        fn = h.file_name
        partes = [texto(fn.originating_system), texto(fn.preprocessor_version)]
        datos["software"] = " · ".join(dict.fromkeys(p for p in partes if p))
        datos["autor"] = texto(", ".join(a for a in fn.author if a))
        datos["organizacion"] = texto(", ".join(o for o in fn.organization if o))
        datos["fecha"] = texto(fn.time_stamp)
    except Exception:
        pass
    return datos


def unidad_longitud(modelo) -> str:
    try:
        proyecto = modelo.by_type("IfcProject")[0]
        for u in proyecto.UnitsInContext.Units:
            if getattr(u, "UnitType", None) == "LENGTHUNIT":
                prefijo = getattr(u, "Prefix", None) or ""
                nombre = getattr(u, "Name", None) or ""
                return f"{prefijo}{nombre}".lower() or "desconocida"
    except Exception:
        pass
    return "desconocida"


def analizar(ruta: Path) -> dict:
    modelo = ifcopenshell.open(str(ruta))
    esquema = modelo.schema
    info = {"ruta": ruta, "esquema": esquema, "cabecera": cabecera(modelo),
            "unidad": unidad_longitud(modelo)}

    proyectos = modelo.by_type("IfcProject")
    info["proyecto"] = texto(proyectos[0].Name if proyectos else "") or ruta.stem
    info["proyecto_desc"] = texto(proyectos[0].LongName if proyectos and hasattr(proyectos[0], "LongName") else "")

    sitios = []
    for s in modelo.by_type("IfcSite"):
        lat = s.RefLatitude
        lon = s.RefLongitude
        def dms(v):
            if not v:
                return ""
            signo = "-" if any(x < 0 for x in v) else ""
            g, m, sg = (abs(x) for x in (list(v) + [0, 0])[:3])
            return f"{signo}{g}°{m}'{sg}\""
        sitios.append((texto(s.Name) or "(sin nombre)", dms(lat), dms(lon)))
    info["sitios"] = sitios
    info["edificios"] = [texto(b.Name) or "(sin nombre)" for b in modelo.by_type("IfcBuilding")]
    pisos = []
    for p in modelo.by_type("IfcBuildingStorey"):
        elev = p.Elevation if p.Elevation is not None else float("nan")
        pisos.append((texto(p.Name) or "(sin nombre)", elev))
    pisos.sort(key=lambda x: (x[1] != x[1], x[1]))
    info["pisos"] = pisos

    conteo = collections.Counter(p.is_a() for p in modelo.by_type("IfcProduct"))
    info["conteo"] = conteo
    elementos = {c: n for c, n in conteo.items() if c not in NO_ELEMENTOS}
    info["elementos_totales"] = sum(elementos.values())
    info["tipos"] = len(modelo.by_type("IfcTypeObject"))
    info["espacios"] = conteo.get("IfcSpace", 0)
    info["proxies"] = conteo.get("IfcBuildingElementProxy", 0)

    materiales = collections.Counter()
    for m in modelo.by_type("IfcMaterial"):
        materiales[texto(m.Name) or "(sin nombre)"] += 1
    info["materiales"] = [m for m, _ in materiales.most_common(15)]
    info["n_materiales"] = len(materiales)

    psets = collections.Counter(texto(p.Name) for p in modelo.by_type("IfcPropertySet"))
    info["psets"] = psets.most_common(12)
    info["qtos"] = len(modelo.by_type("IfcElementQuantity"))
    info["clasificaciones"] = sorted({texto(c.Name) for c in modelo.by_type("IfcClassification")} - {""})

    sin_contenedor = 0
    muestra = 0
    for e in modelo.by_type("IfcElement"):
        if e.is_a() in NO_ELEMENTOS:
            continue
        muestra += 1
        try:
            if ue.get_container(e) is None and not ue.get_aggregate(e):
                sin_contenedor += 1
        except Exception:
            pass
    info["sin_contenedor"] = sin_contenedor
    info["elementos_revisados"] = muestra

    guids = [p.GlobalId for p in modelo.by_type("IfcRoot")]
    info["guids_duplicados"] = len(guids) - len(set(guids))
    info["georref"] = bool(modelo.by_type("IfcMapConversion")) if esquema != "IFC2X3" else False

    arq = sum(n for c, n in conteo.items() if c in ARQ)
    est = sum(n for c, n in conteo.items() if c in EST)
    mep = sum(n for c, n in conteo.items() if c.startswith(MEP_PREFIJOS))
    infra = sum(n for c, n in conteo.items() if c in INFRA)
    info["mezcla"] = {"ARQ": arq, "EST": est, "MEP": mep, "INFRA": infra}
    total = max(arq + est + mep + infra, 1)
    principales = [d for d, n in info["mezcla"].items() if n / total >= 0.25]
    info["disciplina"] = "+".join(principales) if principales else "MIXTO"
    return info


def lecciones(info: dict) -> list[str]:
    salida = []
    tot = max(info["elementos_totales"], 1)
    ratio_proxy = info["proxies"] / tot
    if ratio_proxy > 0.05:
        salida.append(f"⚠️ {info['proxies']} `IfcBuildingElementProxy` ({ratio_proxy:.0%} de los elementos): "
                      "mapeo de clases IFC deficiente en la exportación → [[Control de calidad de modelos BIM]].")
    else:
        salida.append("✅ Pocos o ningún proxy: la exportación usa clases IFC específicas → [[Clases IFC principales]].")
    if len(info["sitios"]) > 1:
        salida.append(f"⚠️ {len(info['sitios'])} `IfcSite` en un solo modelo: probablemente familias exportadas con la "
                      "clase IFC equivocada (revisar el mapeo de exportación) → [[Clases IFC principales]].")
    if not info["pisos"]:
        salida.append("⚠️ Sin `IfcBuildingStorey`: los elementos no están organizados por niveles "
                      "(estructura espacial incompleta) → [[IFC - Estructura del esquema]].")
    if not info["clasificaciones"]:
        salida.append("⚠️ Sin `IfcClassification`: los elementos no llevan códigos Uniclass/OmniClass → [[Sistemas de clasificacion]].")
    else:
        salida.append(f"✅ Clasificación presente ({', '.join(info['clasificaciones'])}) → [[Sistemas de clasificacion]].")
    if info["sin_contenedor"]:
        salida.append(f"⚠️ {info['sin_contenedor']} elementos sin piso/espacio contenedor → revisar la estructura espacial "
                      "([[IFC - Estructura del esquema]]).")
    else:
        salida.append("✅ Todos los elementos revisados están contenidos en la estructura espacial.")
    if info["guids_duplicados"]:
        salida.append(f"⛔ {info['guids_duplicados']} GlobalId duplicados: rompe BCF y comparaciones → [[BCF - BIM Collaboration Format]].")
    if info["esquema"] == "IFC2X3":
        salida.append("ℹ️ IFC2x3: sin georreferenciación completa (`IfcMapConversion` llega en IFC4) → [[BIM y GIS]].")
    elif not info["georref"]:
        salida.append("ℹ️ Sin `IfcMapConversion`: el modelo no está georreferenciado → [[BIM y GIS]].")
    if info["qtos"] == 0:
        salida.append("ℹ️ Sin `IfcElementQuantity` (Qto): los metrados deberán calcularse desde la geometría → [[BIM 5D - Costos y metrados]].")
    else:
        salida.append(f"✅ {info['qtos']} conjuntos de cantidades (Qto) útiles para metrados → [[BIM 5D - Costos y metrados]].")
    return salida


def enlaces_disciplina(disciplina: str) -> list[str]:
    mapa = {"ARQ": "[[BIM 3D - Modelado]]", "EST": "[[MOC Ingenieria Estructural]]",
            "MEP": "[[Coordinacion BIM y deteccion de interferencias]]", "INFRA": "[[BIM para infraestructura]]",
            "MIXTO": "[[Federacion de modelos]]"}
    return [mapa[d] for d in disciplina.split("+") if d in mapa]


def escribir_nota(info: dict, boveda: Path, raiz: Path, raiz_mostrada: str | None, clases_ok: set[str],
                  titulo: str) -> Path:
    ruta: Path = info["ruta"]
    try:
        relativa = ruta.relative_to(raiz).as_posix()
    except ValueError:
        relativa = ruta.name
    ubicacion = f"{raiz_mostrada.rstrip('/')}/{relativa}" if raiz_mostrada else str(ruta)
    tam_mb = ruta.stat().st_size / 1_048_576
    cab = info["cabecera"]
    nota = boveda / CARPETA_NOTAS / f"Estudio - {titulo}.md"
    nota.parent.mkdir(parents=True, exist_ok=True)

    esq = info["esquema"].upper()
    esquema_link = ("IFC 4.3 (ISO 16739-1:2024)" if esq.startswith("IFC4X3") else
                    {"IFC2X3": "IFC2x3 (ISO/PAS 16739:2005)", "IFC4": "IFC4 (ISO 16739-1:2018)"}.get(esq, esq))
    L = []
    L += ["---", "tipo: proyecto-estudio", f'esquema: {info["esquema"]}', f'disciplina: {info["disciplina"]}',
          f'elementos_totales: {info["elementos_totales"]}', f'pisos: {len(info["pisos"])}',
          f'espacios: {info["espacios"]}', f'proxies: {info["proxies"]}', f'tamano_mb: {tam_mb:.1f}',
          f'archivo: "{ubicacion}"', f'software_origen: "{cab["software"]}"',
          f'generado: {dt.date.today().isoformat()}', "tags: [proyecto, estudio, ifc]", "---", ""]
    L += [f"# Estudio — {titulo}", ""]
    L += ["> [!info] Nota generada automáticamente por `scripts/03_ifc_a_obsidian.py`",
          f"> Modelo: `{ubicacion}` · {tam_mb:.1f} MB · esquema **{esquema_link}** → [[IFC - ISO 16739]]", ""]
    L += ["## 1. Ficha del modelo", "| Campo | Valor |", "|---|---|",
          f'| Proyecto (IfcProject) | {info["proyecto"]} {("— " + info["proyecto_desc"]) if info["proyecto_desc"] else ""} |',
          f'| Software de origen | {cab["software"] or "—"} |',
          f'| Autor / organización | {cab["autor"] or "—"} / {cab["organizacion"] or "—"} |',
          f'| Fecha del archivo | {cab["fecha"] or "—"} |',
          f'| Vista (MVD) declarada | {cab["mvd"] or "—"} → [[MVD - Model View Definition]] |',
          f'| Unidad de longitud | {info["unidad"]} |',
          f'| Disciplina inferida | **{info["disciplina"]}** → {" · ".join(enlaces_disciplina(info["disciplina"]))} |',
          f'| Elementos / tipos / espacios | {info["elementos_totales"]} / {info["tipos"]} / {info["espacios"]} |', ""]

    L += ["## 2. Estructura espacial → [[IFC - Estructura del esquema]]"]
    for nombre, lat, lon in info["sitios"] or [("(sin IfcSite)", "", "")]:
        geo = f" (lat {lat}, lon {lon})" if lat or lon else ""
        L.append(f"- **Sitio**: {nombre}{geo}")
    for b in info["edificios"] or ["(sin IfcBuilding)"]:
        L.append(f"  - **Edificio**: {b}")
    for nombre, elev in info["pisos"]:
        elev_txt = "—" if elev != elev else f"{elev:.2f}"
        L.append(f"    - Piso: {nombre} (elevación {elev_txt})")
    L.append("")

    L += ["## 3. Clases IFC presentes → [[Clases IFC principales]]", "| Clase | Cantidad |", "|---|---|"]
    for clase, n in info["conteo"].most_common(40):
        L.append(f"| {enlace_clase(clase, clases_ok)} | {n} |")
    if len(info["conteo"]) > 40:
        L.append(f"| … ({len(info['conteo']) - 40} clases más) | |")
    L.append("")
    mez = info["mezcla"]
    L += [f"**Mezcla por disciplina**: ARQ {mez['ARQ']} · EST {mez['EST']} · MEP {mez['MEP']} · INFRA {mez['INFRA']}", ""]

    L += ["## 4. Información (datos) → [[LOIN - Nivel de Informacion Necesaria]]",
          f"- Materiales distintos: {info['n_materiales']} → " + (", ".join(info["materiales"]) or "—"),
          f"- Conjuntos de cantidades (Qto): {info['qtos']}",
          f"- Clasificaciones: {', '.join(info['clasificaciones']) or 'ninguna'}",
          "- Property Sets más frecuentes:"]
    for nombre, n in info["psets"]:
        L.append(f"  - `{nombre}` × {n}")
    L.append("")

    L += ["## 5. Diagnóstico de calidad → [[Control de calidad de modelos BIM]]"]
    L += [f"- {x}" for x in lecciones(info)]
    L.append("")

    L += ["## 6. Preguntas de estudio para JARVIS y para ti",
          f"1. ¿Qué [[Usos BIM]] permite este modelo con la información que contiene?",
          f"2. Redacta 3 reglas [[IDS - Information Delivery Specification]] que este modelo debería cumplir y verifica si las cumple.",
          f"3. ¿Cómo lo federarías con otras disciplinas? → [[Federacion de modelos]]",
          f"4. ¿Qué LOD aparente tienen sus elementos principales? → [[LOD - Nivel de Desarrollo]]", ""]
    L += ["↑ [[MOC Proyectos de Estudio]] · [[Resumen de modelos de estudio]] · [[Indice de proyectos]]", ""]
    nota.write_text("\n".join(L), encoding="utf-8")
    return nota


def escribir_resumen(boveda: Path) -> Path:
    """Tabla con todas las notas de estudio existentes (incluye corridas anteriores)."""
    carpeta = boveda / CARPETA_NOTAS
    existentes = {}
    for nota in sorted(carpeta.glob("Estudio - *.md")):
        contenido = nota.read_text(encoding="utf-8")
        cab = contenido.split("---")[1] if contenido.startswith("---") else ""
        existentes[nota.stem] = dict(re.findall(r"^(\w+):\s*(.*)$", cab, re.M))
    L = ["---", "tipo: moc", "tags: [proyecto, estudio, moc]", "aliases: [Modelos de estudio, Resumen IFC]",
         f"actualizado: {dt.date.today().isoformat()}", "---", "", "# Resumen de modelos de estudio", "",
         "Tabla regenerada por `scripts/03_ifc_a_obsidian.py` (no requiere Dataview).", "",
         "| Modelo | Esquema | Disciplina | Elementos | Pisos | Proxies | MB |", "|---|---|---|---|---|---|---|"]
    for nombre, c in existentes.items():
        L.append(f"| [[{nombre}]] | {c.get('esquema', '')} | {c.get('disciplina', '')} | {c.get('elementos_totales', '')} "
                 f"| {c.get('pisos', '')} | {c.get('proxies', '')} | {c.get('tamano_mb', '')} |")
    L += ["", "↑ [[MOC Proyectos de Estudio]] · [[Descarga de proyectos BIM]]", ""]
    ruta = carpeta / "Resumen de modelos de estudio.md"
    ruta.write_text("\n".join(L), encoding="utf-8")
    return ruta


def main() -> int:
    ap = argparse.ArgumentParser(description="IFC -> notas de Obsidian (JARVIS BIM)")
    ap.add_argument("--entrada", required=True, help="Archivo .ifc o carpeta (se busca recursivamente)")
    ap.add_argument("--boveda", default=str(Path(__file__).resolve().parent.parent / "JARVIS-BIM"),
                    help="Ruta de la boveda JARVIS-BIM")
    ap.add_argument("--max-mb", type=float, default=300.0, help="Omitir archivos mas grandes (MB)")
    ap.add_argument("--excluir", nargs="*", default=["_ESTANDARES", "_APRENDIZAJE", ".git"],
                    help="Carpetas a ignorar (casos de prueba de IDS/BCF, material de aprendizaje)")
    ap.add_argument("--raiz-mostrada", default=None,
                    help="Texto a mostrar como ruta base en las notas (por defecto la ruta absoluta)")
    args = ap.parse_args()

    entrada = Path(args.entrada).expanduser().resolve()
    boveda = Path(args.boveda).expanduser().resolve()
    if not boveda.exists():
        print(f"No existe la boveda: {boveda}")
        return 2
    excluir = {e.lower() for e in args.excluir}
    archivos = [entrada] if entrada.is_file() else sorted(
        p for p in entrada.rglob("*")
        if p.suffix.lower() == ".ifc" and not excluir.intersection(x.lower() for x in p.relative_to(entrada).parts[:-1]))
    if not archivos:
        print(f"No se encontraron archivos .ifc en {entrada}")
        return 1
    raiz = entrada if entrada.is_dir() else entrada.parent
    clases_ok = encabezados_clases(boveda)
    repetidos = collections.Counter(p.stem.lower() for p in archivos)

    def titulo_de(ruta: Path) -> str:
        """Nombre unico: si el mismo nombre aparece en varias carpetas, agrega la ruta relativa."""
        if repetidos[ruta.stem.lower()] == 1:
            return nombre_seguro(ruta.stem)
        partes = [x for x in ruta.relative_to(raiz).parts[:-1]]
        return nombre_seguro(" - ".join([ruta.stem] + partes[-2:]))

    ok, fallos = [], []
    for ruta in archivos:
        mb = ruta.stat().st_size / 1_048_576
        if mb > args.max_mb:
            print(f"[omitido] {ruta.name} ({mb:.0f} MB > {args.max_mb:.0f} MB)")
            continue
        try:
            print(f"[analizando] {ruta.name} ({mb:.1f} MB)...", flush=True)
            info = analizar(ruta)
            nota = escribir_nota(info, boveda, raiz, args.raiz_mostrada, clases_ok, titulo_de(ruta))
            ok.append((nota.stem, info))
            print(f"   -> {nota.relative_to(boveda)}  [{info['esquema']}, {info['disciplina']}, "
                  f"{info['elementos_totales']} elementos]")
        except Exception as exc:  # archivo corrupto o no soportado
            fallos.append((ruta, exc))
            print(f"[error] {ruta.name}: {exc}")
    resumen = escribir_resumen(boveda)
    print(f"\nNotas generadas: {len(ok)} · errores: {len(fallos)} · resumen: {resumen.relative_to(boveda)}")
    return 0 if not fallos else 3


if __name__ == "__main__":
    sys.exit(main())
