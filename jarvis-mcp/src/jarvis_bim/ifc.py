"""Lectura de modelos IFC con IfcOpenShell (solo lectura)."""
from __future__ import annotations

import importlib.util
from functools import lru_cache
from pathlib import Path


def _ifcopenshell():
    try:
        import ifcopenshell
        import ifcopenshell.util.element
        import ifcopenshell.util.unit
        return ifcopenshell
    except ImportError as exc:  # pragma: no cover
        raise RuntimeError("Instala IfcOpenShell:  pip install ifcopenshell") from exc


@lru_cache(maxsize=4)
def _abrir(ruta: str, mtime: float):
    return _ifcopenshell().open(ruta)


def abrir(ruta: str):
    p = Path(ruta).expanduser().resolve()
    if not p.exists():
        raise FileNotFoundError(f"No existe el archivo IFC: {p}")
    return _abrir(str(p), p.stat().st_mtime)


@lru_cache(maxsize=1)
def _analizador():
    """Reutiliza el analizador de scripts/03_ifc_a_obsidian.py (una sola fuente de verdad)."""
    script = Path(__file__).resolve().parents[3] / "scripts" / "03_ifc_a_obsidian.py"
    spec = importlib.util.spec_from_file_location("ifc_a_obsidian", script)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def resumen(ruta: str) -> dict:
    info = _analizador().analizar(Path(ruta).expanduser().resolve())
    return {
        "archivo": str(info["ruta"]), "esquema": info["esquema"], "proyecto": info["proyecto"],
        "software_origen": info["cabecera"]["software"], "mvd": info["cabecera"]["mvd"],
        "unidad_longitud": info["unidad"], "disciplina": info["disciplina"],
        "elementos_totales": info["elementos_totales"], "tipos": info["tipos"], "espacios": info["espacios"],
        "proxies": info["proxies"], "pisos": [{"nombre": n, "elevacion": None if e != e else e} for n, e in info["pisos"]],
        "clases": dict(info["conteo"].most_common(40)), "materiales": info["materiales"],
        "clasificaciones": info["clasificaciones"], "qto": info["qtos"],
        "sin_contenedor": info["sin_contenedor"], "guids_duplicados": info["guids_duplicados"],
        "diagnostico": _analizador().lecciones(info),
    }


def elementos(ruta: str, clase: str, limite: int = 50) -> dict:
    m = abrir(ruta)
    try:
        lista = m.by_type(clase)
    except RuntimeError as exc:
        raise ValueError(f"Clase IFC inválida para el esquema {m.schema}: {clase}") from exc
    util = _ifcopenshell().util.element
    filas = []
    for e in lista[:limite]:
        cont = util.get_container(e)
        tipo = util.get_type(e)
        filas.append({"GlobalId": e.GlobalId, "clase": e.is_a(), "nombre": e.Name,
                      "tipo": tipo.Name if tipo else None, "contenedor": cont.Name if cont else None})
    return {"clase": clase, "total": len(lista), "mostrados": len(filas), "elementos": filas}


def propiedades(ruta: str, global_id: str) -> dict:
    m = abrir(ruta)
    try:
        e = m.by_guid(global_id)
    except RuntimeError as exc:
        raise KeyError(f"No existe el GlobalId {global_id} en el modelo") from exc
    util = _ifcopenshell().util.element
    tipo = util.get_type(e)
    cont = util.get_container(e)
    mats = util.get_materials(e) if hasattr(util, "get_materials") else []
    return {"GlobalId": global_id, "clase": e.is_a(), "nombre": getattr(e, "Name", None),
            "tipo": tipo.Name if tipo else None, "contenedor": cont.Name if cont else None,
            "materiales": [getattr(x, "Name", str(x)) for x in mats],
            "psets": util.get_psets(e, psets_only=True), "qtos": util.get_psets(e, qtos_only=True)}
