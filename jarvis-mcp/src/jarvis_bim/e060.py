"""
Norma E.060 "Concreto Armado" (DS 010-2009-VIVIENDA) — cálculos de verificación y predimensionamiento.
Unidades: MPa, mm, kN, kN·m.  Resultados = borrador para el ingeniero responsable.
"""
from __future__ import annotations

import math

NORMA = "E.060-2009 (DS 010-2009-VIVIENDA)"
PENDIENTES: dict[str, str] = {}  # todo verificado contra el texto oficial (SENCICO, DS 010-2009-VIVIENDA)
REFERENCIAS = {
    "combinaciones": "E.060 9.2.1–9.2.5 (ec. 9-1 a 9-7); 9.2.4: no combinar sismo y viento",
    "phi": "E.060 9.3.2.1–9.3.2.5",
    "beta1": "E.060 10.2.7.3",
    "as_max": "E.060 10.3.4: As ≤ 0,75·Asb",
    "as_min": "E.060 10.5.2 (ec. 10-3): As mín = 0,22·√f'c/fy·bw·d",
    "vc": "E.060 11.3.1.1 (ec. 11-3): Vc = 0,17·√f'c·bw·d",
    "s_max": "E.060 11.5.5.1 (d/2 ≤ 600 mm) y 11.5.5.3 (mitad si Vs > 0,33·√f'c·bw·d)",
    "av_min": "E.060 11.5.6.2 (ec. 11-13): Av mín = 0,062·√f'c·bw·s/fyt ≥ 0,35·bw·s/fyt",
    "vs_max": "E.060 11.5.7.9: Vs ≤ 0,66·√f'c·bw·d",
    "pn_max": "E.060 10.3.6.1 (espiral, ec. 10-1: 0,85) y 10.3.6.2 (estribos, ec. 10-2: 0,80)",
    "cuantia_columna": "E.060 10.9.1: 0,01 ≤ Ast/Ag ≤ 0,06",
}

# Art. 9.3.2 — factores de reducción de resistencia
PHI = {"flexion": 0.90, "traccion": 0.90, "cortante": 0.85, "torsion": 0.85,
       "compresion_estribos": 0.70, "compresion_espiral": 0.75, "aplastamiento": 0.70}

# Barras corrugadas comerciales en Perú: diámetro (mm), área (mm²)
BARRAS = {
    "6mm": (6.0, 28), "8mm": (8.0, 50), "3/8": (9.5, 71), "12mm": (12.0, 113), "1/2": (12.7, 129),
    "5/8": (15.9, 199), "3/4": (19.1, 284), "1": (25.4, 510), "1 3/8": (35.8, 1006),
}


class ErrorE060(ValueError):
    pass


def combinaciones(sismo: bool = True, viento: bool = False, empuje: bool = False) -> list[dict]:
    """Art. 9.2: combinaciones de resistencia requerida U (CM muerta, CV viva, CS sismo, CVi viento, CE empuje)."""
    c = [{"nombre": "U1", "expresion": "1,4 CM + 1,7 CV", "factores": {"CM": 1.4, "CV": 1.7}}]
    if viento:
        c += [{"nombre": "UV1", "expresion": "1,25 (CM + CV + CVi)", "factores": {"CM": 1.25, "CV": 1.25, "CVi": 1.25}},
              {"nombre": "UV2", "expresion": "1,25 (CM + CV - CVi)", "factores": {"CM": 1.25, "CV": 1.25, "CVi": -1.25}},
              {"nombre": "UV3", "expresion": "0,9 CM + 1,25 CVi", "factores": {"CM": 0.9, "CVi": 1.25}},
              {"nombre": "UV4", "expresion": "0,9 CM - 1,25 CVi", "factores": {"CM": 0.9, "CVi": -1.25}}]
    if sismo:
        c += [{"nombre": "US1", "expresion": "1,25 (CM + CV) + CS", "factores": {"CM": 1.25, "CV": 1.25, "CS": 1.0}},
              {"nombre": "US2", "expresion": "1,25 (CM + CV) - CS", "factores": {"CM": 1.25, "CV": 1.25, "CS": -1.0}},
              {"nombre": "US3", "expresion": "0,9 CM + CS", "factores": {"CM": 0.9, "CS": 1.0}},
              {"nombre": "US4", "expresion": "0,9 CM - CS", "factores": {"CM": 0.9, "CS": -1.0}}]
    if empuje:
        c.append({"nombre": "UE1", "expresion": "1,4 CM + 1,7 CV + 1,7 CE", "factores": {"CM": 1.4, "CV": 1.7, "CE": 1.7}})
    return c


def beta1(fc: float) -> float:
    """Art. 10.2.7.3: 0,85 hasta 28 MPa, baja 0,05 cada 7 MPa, mínimo 0,65."""
    if fc <= 28:
        return 0.85
    return max(0.65, 0.85 - 0.05 * (fc - 28) / 7)


def rho_balanceada(fc: float, fy: float) -> float:
    return 0.85 * beta1(fc) * fc / fy * 600 / (600 + fy)


def _validar(fc: float, fy: float, *dims: float) -> None:
    if fc < 17:
        raise ErrorE060("f'c mínimo 17 MPa (21 MPa en elementos sismorresistentes).")
    if not 200 <= fy <= 550:
        raise ErrorE060("fy fuera de rango (grado 60 = 420 MPa).")
    if any(d <= 0 for d in dims):
        raise ErrorE060("Las dimensiones deben ser positivas.")


def sugerir_barras(as_mm2: float, ancho_mm: float, recubrimiento_mm: float = 40, estribo: str = "3/8",
                   max_opciones: int = 3) -> list[dict]:
    """Opciones de n barras de un mismo diámetro que cubren As y entran en una capa (s libre ≥ máx(25 mm, db))."""
    d_est = BARRAS[estribo][0]
    libre_total = ancho_mm - 2 * (recubrimiento_mm + d_est)
    opciones = []
    for nombre, (db, area) in BARRAS.items():
        if db < 12 or db > 26:
            continue
        n = max(2, math.ceil(as_mm2 / area))
        espacio = (libre_total - n * db) / (n - 1)
        if espacio >= max(25.0, db):
            opciones.append({"barras": f"{n} Ø {nombre}", "As_mm2": n * area,
                             "exceso_%": round(100 * (n * area / as_mm2 - 1), 1) if as_mm2 else None,
                             "espacio_libre_mm": round(espacio, 1)})
    opciones.sort(key=lambda o: o["As_mm2"])
    return opciones[:max_opciones]


def flexion_viga(mu_knm: float, b_mm: float, h_mm: float, fc: float = 21, fy: float = 420,
                 recubrimiento_mm: float = 40, estribo: str = "3/8", barra_supuesta: str = "5/8") -> dict:
    """Diseño a flexión de sección rectangular simplemente reforzada (art. 10): As requerido, mín., máx. y barras."""
    _validar(fc, fy, b_mm, h_mm)
    d = h_mm - recubrimiento_mm - BARRAS[estribo][0] - BARRAS[barra_supuesta][0] / 2
    phi = PHI["flexion"]
    mu = abs(mu_knm) * 1e6  # N·mm
    k = 1 - 2 * mu / (phi * 0.85 * fc * b_mm * d ** 2)
    if k < 0:
        raise ErrorE060("La sección no resiste Mu como simplemente reforzada: aumenta peralte/ancho o usa acero en compresión.")
    as_req = 0.85 * fc * b_mm * d / fy * (1 - math.sqrt(k))
    as_min = 0.22 * math.sqrt(fc) / fy * b_mm * d
    rho_b = rho_balanceada(fc, fy)
    as_max = 0.75 * rho_b * b_mm * d
    as_diseno = max(as_req, as_min)
    a = as_diseno * fy / (0.85 * fc * b_mm)
    phi_mn = phi * as_diseno * fy * (d - a / 2) / 1e6
    return {
        "norma": NORMA, "d_mm": round(d, 1), "phi": phi,
        "formula": "Mu = φ·As·fy·(d − a/2);  a = As·fy/(0,85·f'c·b)",
        "As_requerido_mm2": round(as_req, 1), "As_min_mm2": round(as_min, 1), "As_max_mm2": round(as_max, 1),
        "As_diseno_mm2": round(as_diseno, 1), "rige_minimo": as_req < as_min,
        "cuantia": round(as_diseno / (b_mm * d), 5), "cuantia_balanceada": round(rho_b, 5),
        "cumple_maximo": as_diseno <= as_max, "phi_Mn_kNm": round(phi_mn, 2),
        "barras": sugerir_barras(as_diseno, b_mm, recubrimiento_mm, estribo),
        "referencias": [REFERENCIAS[k] for k in ("as_min", "as_max", "beta1", "phi")],
    }


def cortante_viga(vu_kn: float, b_mm: float, d_mm: float, fc: float = 21, fy: float = 420,
                  estribo: str = "3/8", ramas: int = 2) -> dict:
    """Diseño por cortante (art. 11): φVc, Vs requerido, espaciamiento calculado y máximo."""
    _validar(fc, fy, b_mm, d_mm)
    phi = PHI["cortante"]
    vu = abs(vu_kn) * 1e3
    vc = 0.17 * math.sqrt(fc) * b_mm * d_mm
    vs_req = max(vu / phi - vc, 0.0)
    vs_lim = 0.66 * math.sqrt(fc) * b_mm * d_mm
    if vs_req > vs_lim:
        raise ErrorE060(f"Vs requerido {vs_req / 1e3:.1f} kN > 0,66·√f'c·b·d = {vs_lim / 1e3:.1f} kN: agranda la sección.")
    av = ramas * BARRAS[estribo][1]
    s_max = min(d_mm / 2, 600) if vs_req <= 0.33 * math.sqrt(fc) * b_mm * d_mm else min(d_mm / 4, 300)
    s_calc = av * fy * d_mm / vs_req if vs_req > 0 else float("inf")
    av_min_s = max(0.062 * math.sqrt(fc), 0.35) * b_mm / fy  # Av/s mínimo
    s_min_ref = av / av_min_s
    requiere_minimo = vu > 0.5 * phi * vc
    s = min(s_calc, s_max, s_min_ref if requiere_minimo else float("inf"))
    s_diseno = math.floor(s / 25) * 25
    return {
        "norma": NORMA, "phi": phi, "phi_Vc_kN": round(phi * vc / 1e3, 2), "Vs_requerido_kN": round(vs_req / 1e3, 2),
        "Av_mm2": av, "s_calculado_mm": None if s_calc == float("inf") else round(s_calc, 1),
        "s_maximo_mm": round(s_max, 1), "s_diseno_mm": s_diseno,
        "estribos": f"Ø {estribo} ({ramas} ramas) @ {s_diseno} mm",
        "requiere_refuerzo_minimo": requiere_minimo,
        "nota": "En vigas sismorresistentes (cap. 21) rigen además el confinamiento en 2h y el diseño por capacidad.",
        "referencias": [REFERENCIAS[k] for k in ("vc", "s_max", "av_min", "vs_max")],
    }


def columna_axial(pu_kn: float, b_mm: float, h_mm: float, as_total_mm2: float, fc: float = 21, fy: float = 420,
                  espiral: bool = False) -> dict:
    """Resistencia axial máxima (art. 10.3.6) y cuantía 1 %–6 % (art. 10.9.1)."""
    _validar(fc, fy, b_mm, h_mm)
    ag = b_mm * h_mm
    rho = as_total_mm2 / ag
    phi = PHI["compresion_espiral" if espiral else "compresion_estribos"]
    factor = 0.85 if espiral else 0.80
    po = 0.85 * fc * (ag - as_total_mm2) + fy * as_total_mm2
    phi_pn = factor * phi * po / 1e3
    return {
        "norma": NORMA, "Ag_mm2": ag, "cuantia": round(rho, 4), "cuantia_ok": 0.01 <= rho <= 0.06,
        "formula": f"φPn(máx) = {factor}·φ·[0,85·f'c·(Ag − Ast) + fy·Ast]", "phi": phi,
        "phi_Pn_max_kN": round(phi_pn, 1), "Pu_kN": pu_kn, "cumple": pu_kn <= phi_pn,
        "uso_%": round(100 * pu_kn / phi_pn, 1),
        "nota": "Solo carga axial: con flexión, verifica con el diagrama de interacción (ETABS/SAP2000).",
        "referencias": [REFERENCIAS["pn_max"], REFERENCIAS["cuantia_columna"]],
    }


def plan_combinaciones(cm: list[str], cv: list[str], sismo: list[str] | None = None, sismo_espectral: bool = True,
                       viento: list[str] | None = None, envolvente: str | None = "ENV_E060") -> list[dict]:
    """Traduce las combinaciones del art. 9.2 a combinaciones de ETABS/SAP2000 con los nombres de casos del modelo.

    Con sismo espectral (resultados en valor absoluto) solo se crean las combinaciones con +CS; con sismo estático
    se crean ±CS. Una combinación por dirección de sismo/viento."""
    if not cm or not cv:
        raise ErrorE060("Indica al menos un caso de carga muerta (cm) y uno de viva (cv).")
    sismo, viento = sismo or [], viento or []
    plan = []

    def agregar(nombre, factores_base, extra=None, sf_extra=0.0):
        casos = [(c, factores_base["CM"]) for c in cm]
        if factores_base.get("CV"):
            casos += [(c, factores_base["CV"]) for c in cv]
        if extra:
            casos.append((extra, sf_extra))
        plan.append({"nombre": nombre, "tipo": "suma lineal", "casos": casos})

    agregar("U1", {"CM": 1.4, "CV": 1.7})
    for s in sismo:
        signos = (1.0,) if sismo_espectral else (1.0, -1.0)
        for sg in signos:
            sufijo = s if sismo_espectral else f"{s}{'+' if sg > 0 else '-'}"
            agregar(f"U2_{sufijo}", {"CM": 1.25, "CV": 1.25}, s, sg)
            agregar(f"U3_{sufijo}", {"CM": 0.9}, s, sg)
    for w in viento:
        for sg in (1.0, -1.0):
            sufijo = f"{w}{'+' if sg > 0 else '-'}"
            agregar(f"UV1_{sufijo}", {"CM": 1.25, "CV": 1.25}, w, 1.25 * sg)
            agregar(f"UV2_{sufijo}", {"CM": 0.9}, w, 1.25 * sg)
    if envolvente:
        plan.append({"nombre": envolvente, "tipo": "envolvente", "combinaciones": [p["nombre"] for p in plan]})
    return plan
