"""
Norma E.020 "Cargas" (RNE, DS 011-2006-VIVIENDA; texto oficial en la bóveda: [[Texto oficial - E020]]).

Solo valores verificados en el texto oficial. Unidades: kPa (1 kPa = 100 kgf/m²) y kN/m³.
"""
from __future__ import annotations

NORMA = "E.020 Cargas (RNE)"


class ErrorE020(ValueError):
    """Uso o material fuera de las tablas verificadas."""


# Anexo 1: concreto simple de grava 23,0 kN/m³ + 1,0 para concreto armado
PESO_CONCRETO_ARMADO = 24.0  # kN/m³

# Anexo 1: losas aligeradas en una dirección (vigueta 0,10 m cada 0,40 m, losa superior 0,05 m) — peso propio kPa
ALIGERADOS = {0.17: 2.8, 0.20: 3.0, 0.25: 3.5, 0.30: 4.2}

# Art. 6.1, Tabla 1 — cargas vivas mínimas repartidas (kPa)
CARGA_VIVA = {
    "vivienda": 2.0, "vivienda_corredores": 2.0,
    "oficinas": 2.5, "oficinas_corredores": 4.0, "oficinas_archivo": 5.0,
    "hospital_cuartos": 2.0, "hospital_operaciones": 3.0, "hospital_corredores": 4.0,
    "hotel_cuartos": 2.0, "hotel_corredores": 4.0,
    "asamblea_asientos_fijos": 3.0, "asamblea_asientos_movibles": 4.0,
    "tiendas": 5.0, "tiendas_corredores": 5.0,
}
# Art. 7.1 a) — techos con inclinación hasta 3°
CARGA_VIVA_TECHO = 1.0

REFERENCIAS = {
    "concreto_armado": "E.020, Anexo 1 (concreto simple de grava 23,0 kN/m³ + 1,0)",
    "aligerado": "E.020, Anexo 1 (losas aligeradas en una dirección)",
    "carga_viva": "E.020, art. 6.1, Tabla 1",
    "techo": "E.020, art. 7.1 a)",
    "tabiqueria_movil": "E.020, art. 6.3 (mín. 0,50 kPa media altura; 1,0 kPa altura completa)",
}


def peso_aligerado(espesor_m: float) -> float:
    """Peso propio del aligerado (kPa) según el Anexo 1."""
    for e, w in ALIGERADOS.items():
        if abs(e - espesor_m) < 1e-6:
            return w
    raise ErrorE020(f"Aligerado de {espesor_m} m fuera del Anexo 1. Espesores: {', '.join(map(str, ALIGERADOS))} m.")


def carga_viva(uso: str) -> float:
    if uso == "techo":
        return CARGA_VIVA_TECHO
    if uso not in CARGA_VIVA:
        raise ErrorE020(f"Uso '{uso}' no tabulado. Opciones: techo, {', '.join(CARGA_VIVA)}.")
    return CARGA_VIVA[uso]
