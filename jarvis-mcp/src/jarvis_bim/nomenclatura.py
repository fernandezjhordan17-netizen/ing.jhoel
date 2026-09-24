"""Validación de nombres de contenedores de información (ISO 19650-2, estructura del Anexo Nacional UK).

PROYECTO-ORIGINADOR-VOLUMEN-NIVEL-TIPO-ROL-NUMERO   p. ej.  PRJ01-ABC-ZZ-01-M3-S-0001
Los códigos se pueden sustituir por los del EIR/Guía Nacional BIM del proyecto.
"""
from __future__ import annotations

import re
from pathlib import Path

TIPOS = {
    "AF": "animación", "BQ": "lista de cantidades", "CA": "cálculos", "CM": "modelo combinado/federado",
    "CO": "correspondencia", "CP": "costos", "DB": "base de datos", "DR": "plano", "FN": "nota de archivo",
    "HS": "salud y seguridad", "IE": "archivo de intercambio", "MI": "minuta/acta", "MR": "modelo de representación",
    "MS": "método", "M2": "modelo 2D", "M3": "modelo 3D", "PP": "presentación", "PR": "programa/cronograma",
    "RD": "hoja de datos de habitaciones", "RI": "solicitud de información (RFI)", "RP": "reporte",
    "SA": "horario de cuentas", "SH": "planilla/tabla", "SN": "nota de inspección", "SP": "especificación",
    "SU": "levantamiento", "VS": "visualización",
}
ROLES = {
    "A": "arquitectura", "B": "ingeniería de edificación", "C": "ingeniería civil", "D": "drenaje/carreteras",
    "E": "ingeniería eléctrica", "F": "gestión de instalaciones", "G": "geotecnia/topografía", "H": "calefacción/ventilación",
    "I": "diseño de interiores", "K": "cliente", "L": "paisajismo", "M": "ingeniería mecánica", "P": "sanitarias",
    "Q": "costos", "S": "estructuras", "T": "urbanismo", "W": "contratista", "X": "subcontratista", "Y": "especialista",
    "Z": "general (no disciplinar)",
}
CAMPOS = ["proyecto", "originador", "volumen", "nivel", "tipo", "rol", "numero"]
PATRONES = {
    "proyecto": r"[A-Z0-9]{2,6}", "originador": r"[A-Z0-9]{3,6}", "volumen": r"[A-Z0-9]{1,4}",
    "nivel": r"[A-Z0-9]{2,4}", "tipo": r"[A-Z0-9]{2}", "rol": r"[A-Z]{1,2}", "numero": r"\d{4,6}",
}


def validar_nombre(nombre: str, tipos: dict | None = None, roles: dict | None = None,
                   separador: str = "-") -> dict:
    """Valida un nombre (con o sin extensión) y devuelve campos, errores y sugerencias."""
    tipos, roles = tipos or TIPOS, roles or ROLES
    base = Path(nombre).stem if "." in Path(nombre).name else nombre
    partes = base.split(separador)
    errores: list[str] = []
    if len(partes) != len(CAMPOS):
        return {"nombre": nombre, "valido": False, "campos": {},
                "errores": [f"Se esperaban {len(CAMPOS)} campos separados por '{separador}' "
                            f"({'-'.join(c.upper() for c in CAMPOS)}); hay {len(partes)}."]}
    campos = dict(zip(CAMPOS, partes))
    for c, v in campos.items():
        if not re.fullmatch(PATRONES[c], v):
            errores.append(f"Campo {c} '{v}' no cumple el patrón {PATRONES[c]} (mayúsculas, sin espacios ni tildes).")
    if campos["tipo"] not in tipos:
        errores.append(f"Tipo '{campos['tipo']}' no está en la lista acordada (p. ej. M3 modelo, DR plano, SP especificación).")
    if campos["rol"] not in roles:
        errores.append(f"Rol '{campos['rol']}' no está en la lista acordada (p. ej. A, S, M, E, P).")
    return {"nombre": nombre, "valido": not errores, "campos": campos, "errores": errores,
            "descripcion": {"tipo": tipos.get(campos["tipo"], "?"), "rol": roles.get(campos["rol"], "?")}}


def validar_carpeta(ruta: str, extensiones: tuple[str, ...] = (".rvt", ".ifc", ".nwc", ".nwd", ".dwg", ".pdf",
                                                                 ".xlsx", ".docx", ".edb", ".sdb", ".fdb")) -> dict:
    carpeta = Path(ruta).expanduser()
    if not carpeta.is_dir():
        raise FileNotFoundError(f"No existe la carpeta: {carpeta}")
    resultados = [validar_nombre(p.name) for p in sorted(carpeta.rglob("*"))
                  if p.is_file() and p.suffix.lower() in extensiones]
    no_conformes = [r for r in resultados if not r["valido"]]
    return {"carpeta": str(carpeta), "revisados": len(resultados), "conformes": len(resultados) - len(no_conformes),
            "no_conformes": no_conformes[:200]}
