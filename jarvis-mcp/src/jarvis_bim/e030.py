"""
Motor de cálculo de la Norma E.030 "Diseño Sismorresistente" — edición 2026
(RM N.° 183-2026-VIVIENDA, El Peruano 03-05-2026).

Todo valor sale de tablas explícitas de este módulo, citadas por artículo/tabla de la
edición 2026. Los valores que no se pudieron confirmar en el texto 2026 están marcados
en PENDIENTES y se reportan como advertencia en cada resultado que los use.

Unidades: periodos en s, alturas en m, pesos/fuerzas en las unidades que entregue el usuario.
"""
from __future__ import annotations

from dataclasses import dataclass, field, asdict

NORMA = "E.030-2026 (RM 183-2026-VIVIENDA)"

PENDIENTES = {
    "factor_c": "Expresión de C para T > TP tomada de ediciones previas (2,5·TP/T y 2,5·TP·TL/T²); confirmar en Tabla N.° 6 del PDF 2026.",
    "derivas": "Límites de distorsión de la edición 2019 (en 2026 es la Tabla N.° 14); confirmar valores en el PDF 2026.",
    "desplazamientos": "Factores 0,75·R (regular) y 0,85·R (irregular) de la edición 2019; confirmar en el PDF 2026.",
}

# Art. 11, Tabla N.° 1
Z = {1: 0.10, 2: 0.25, 3: 0.35, 4: 0.45}

# Art. 14, Tablas N.° 2 y 3 — límites inferiores de Vs30 (m/s) por perfil
VS30_MIN = {"S0": 800.0, "S1": 550.0, "S2": 350.0, "S3": 200.0, "S4": 0.0}
VS30_RANGO = {"S2": (350.0, 550.0), "S3": (200.0, 350.0)}
ORDEN_PERFILES = ["S0", "S1", "S2", "S3", "S4", "S5"]

# Art. 17, Tabla N.° 4 — factor S. Tuplas = rango (valor en el extremo rígido, valor en el extremo blando).
# None = la norma exige análisis de respuesta de sitio específico.
S = {
    4: {"S0": 0.80, "S1": 1.00, "S2": (1.00, 1.10), "S3": (1.10, 1.20), "S4": None},
    3: {"S0": 0.80, "S1": 1.00, "S2": (1.00, 1.15), "S3": (1.15, 1.20), "S4": 1.30},
    2: {"S0": 0.80, "S1": 1.00, "S2": (1.00, 1.30), "S3": (1.30, 1.40), "S4": 1.70},
    1: {"S0": 0.80, "S1": 1.00, "S2": (1.00, 1.30), "S3": (1.30, 1.60), "S4": 2.40},
}
# Art. 17, Tabla N.° 5 — TP y TL (tuplas = (extremo rígido, extremo blando))
TP = {"S0": 0.3, "S1": 0.4, "S2": (0.4, 0.6), "S3": (0.6, 0.9), "S4": 1.2}
TL = {"S0": 3.0, "S1": 2.5, "S2": (2.5, 2.0), "S3": (2.0, 1.6), "S4": 1.6}

# Art. 19, Tabla N.° 7
U = {"A1": 1.5, "A2": 1.5, "B": 1.3, "C": 1.0}

# Art. 22, Tabla N.° 10 — R0
R0 = {
    "acero_smf": 8.0, "acero_imf": 5.0, "acero_omf": 4.0,
    "acero_scbf": 7.0, "acero_ocbf": 4.0, "acero_ebf": 8.0,
    "concreto_porticos": 8.0, "concreto_dual": 7.0, "concreto_muros": 6.0,
    "concreto_emdl": 3.5,
    "albanileria": 3.0, "madera": 7.0, "pendulo_invertido": 2.5,
}
DESCRIPCION_SISTEMAS = {
    "acero_smf": "Acero – pórticos especiales resistentes a momentos (SMF)",
    "acero_imf": "Acero – pórticos intermedios resistentes a momentos (IMF)",
    "acero_omf": "Acero – pórticos ordinarios resistentes a momentos (OMF)",
    "acero_scbf": "Acero – pórticos especiales concéntricamente arriostrados (SCBF)",
    "acero_ocbf": "Acero – pórticos ordinarios concéntricamente arriostrados (OCBF)",
    "acero_ebf": "Acero – pórticos excéntricamente arriostrados (EBF)",
    "concreto_porticos": "Concreto armado – pórticos",
    "concreto_dual": "Concreto armado – dual",
    "concreto_muros": "Concreto armado – muros estructurales",
    "concreto_emdl": "Concreto armado – muros de ductilidad limitada (EMDL, máx. 5 pisos)",
    "albanileria": "Albañilería armada o confinada",
    "madera": "Madera (esfuerzos admisibles)",
    "pendulo_invertido": "Estructuras tipo péndulo invertido",
}

# Art. 24, Tablas N.° 11 (Ia) y N.° 12 (Ip)
IA = {"piso_blando": 0.75, "piso_debil": 0.75, "rigidez_extrema": 0.50, "resistencia_extrema": 0.50,
      "masa": 0.90, "geometrica_vertical": 0.90, "discontinuidad": 0.80, "discontinuidad_extrema": 0.60}
IP = {"torsional": 0.75, "torsional_extrema": 0.60, "esquinas_entrantes": 0.90,
      "discontinuidad_diafragma": 0.85, "sistemas_no_paralelos": 0.90}
EXTREMAS = {"rigidez_extrema", "resistencia_extrema", "discontinuidad_extrema", "torsional_extrema"}

# Art. 36 — CT
CT = {"porticos": 35.0, "porticos_con_muros_en_cajas": 45.0, "acero_arriostrado": 45.0,
      "albanileria": 60.0, "dual": 60.0, "muros": 60.0, "emdl": 60.0}

# Art. 31 — fracción de carga viva en el peso sísmico
FRACCION_CV = {"A1": 0.50, "A2": 0.50, "B": 0.50, "C": 0.25}

# Distorsiones máximas (edición 2019, pendiente de confirmar Tabla 14 de 2026)
DERIVA_MAX = {"concreto": 0.007, "acero": 0.010, "albanileria": 0.005, "madera": 0.010, "emdl": 0.005}


class ErrorNorma(ValueError):
    """Situación que la E.030 no permite resolver con los parámetros normales."""


def perfil_por_vs30(vs30: float) -> str:
    """Art. 14, Tabla 3: perfil de suelo según Vs30 (m/s)."""
    if vs30 <= 0:
        raise ErrorNorma("Vs30 debe ser positivo.")
    for perfil in ("S0", "S1", "S2", "S3"):
        if vs30 >= VS30_MIN[perfil]:
            return perfil
    return "S4"


def _interpolar(valor, perfil: str, vs30: float | None, usar_blando: bool):
    if not isinstance(valor, tuple):
        return valor
    rigido, blando = valor
    if usar_blando or vs30 is None:
        return blando
    v_min, v_max = VS30_RANGO[perfil]
    t = min(max((vs30 - v_min) / (v_max - v_min), 0.0), 1.0)  # 0 = extremo blando, 1 = extremo rígido
    return round(blando + t * (rigido - blando), 4)


@dataclass
class ParametrosSitio:
    zona: int
    perfil: str
    vs30: float | None
    Z: float
    S: float
    TP: float
    TL: float
    ts: float | None = None
    notas: list[str] = field(default_factory=list)


def parametros_sitio(zona: int, perfil: str | None = None, vs30: float | None = None,
                     categoria: str = "C", ts: float | None = None) -> ParametrosSitio:
    """Arts. 11, 14 y 17: Z, perfil, S, TP y TL (con interpolación por Vs30 y verificación de Ts)."""
    if zona not in Z:
        raise ErrorNorma("La zona sísmica debe ser 1, 2, 3 o 4 (Anexo II).")
    notas: list[str] = []
    if perfil is None:
        if vs30 is None:
            raise ErrorNorma("Indica el perfil de suelo (S0–S5) o el Vs30 del EMS.")
        perfil = perfil_por_vs30(vs30)
        notas.append(f"Perfil {perfil} asignado por Vs30 = {vs30:g} m/s (Tabla N.° 3).")
    perfil = perfil.upper()
    if perfil == "S5":
        raise ErrorNorma("Perfil S5 (suelos excepcionales): la E.030-2026 prohíbe construir salvo estudio de sitio "
                         "específico con mejoramiento del estrato (art. 14).")
    if perfil not in ORDEN_PERFILES:
        raise ErrorNorma(f"Perfil desconocido: {perfil}.")
    if vs30 is not None and perfil in VS30_RANGO:
        lo, hi = VS30_RANGO[perfil]
        if not lo <= vs30 <= hi:
            notas.append(f"⚠️ Vs30 = {vs30:g} m/s está fuera del rango de {perfil} ({lo:g}–{hi:g}); se acota al rango.")

    usar_blando = False
    if ts is not None and categoria.upper() in ("A1", "A2", "B") and zona == 4 and perfil in ("S1", "S2", "S3", "S4"):
        tp_prov = _interpolar(TP[perfil], perfil, vs30, False)
        if ts > 0.65 * tp_prov:
            siguiente = ORDEN_PERFILES[ORDEN_PERFILES.index(perfil) + 1]
            notas.append(f"⚠️ Ts = {ts:g} s > 0,65·TP = {0.65 * tp_prov:.3f} s (art. 14.8): se pasa del perfil {perfil} "
                         f"al {siguiente} con el límite superior de TP, o se hace un estudio de sitio (art. 13).")
            perfil = siguiente
            usar_blando = True
            if perfil == "S5":
                raise ErrorNorma("El cambio por Ts lleva a S5: se requiere estudio de sitio específico.")
        else:
            notas.append(f"Ts = {ts:g} s ≤ 0,65·TP = {0.65 * tp_prov:.3f} s: cumple el art. 14.8.")
    elif categoria.upper() in ("A1", "A2", "B") and zona == 4 and perfil != "S0" and ts is None:
        notas.append("⚠️ Categoría A/B en Zona 4: la E.030-2026 exige medir el periodo del suelo Ts (H/V, SESAME) "
                     "y verificar Ts ≤ 0,65·TP (art. 14.8).")

    s_val = S[zona][perfil]
    if s_val is None:
        raise ErrorNorma("Zona 4 con perfil S4: la Tabla N.° 4 exige análisis de respuesta de sitio específico.")
    if vs30 is None and isinstance(s_val, tuple):
        notas.append("Sin Vs30 medido: se toman el mayor S del rango y el TP/TL del extremo blando (nota de las Tablas 4 y 5).")
    return ParametrosSitio(
        zona=zona, perfil=perfil, vs30=vs30, Z=Z[zona],
        S=_interpolar(s_val, perfil, vs30, usar_blando),
        TP=_interpolar(TP[perfil], perfil, vs30, usar_blando),
        TL=_interpolar(TL[perfil], perfil, vs30, usar_blando),
        ts=ts, notas=notas)


def factor_c(T: float, TP_: float, TL_: float) -> float:
    """Art. 18, Tabla 6 (forma de ediciones previas; ver PENDIENTES['factor_c'])."""
    if T < 0:
        raise ErrorNorma("El periodo no puede ser negativo.")
    if T <= TP_:
        return 2.5
    if T <= TL_:
        return 2.5 * TP_ / T
    return 2.5 * TP_ * TL_ / T ** 2


def factor_u(categoria: str, aislamiento: bool = False, zona: int | None = None) -> tuple[float, list[str]]:
    """Art. 19, Tabla 7."""
    cat = categoria.upper()
    if cat not in U:
        raise ErrorNorma("Categoría debe ser A1, A2, B o C.")
    notas = []
    if cat == "A1" and zona in (3, 4) and not aislamiento:
        notas.append("⛔ A1 nueva en zona 3 o 4: aislamiento sísmico obligatorio (art. 19; Norma E.031).")
    if cat == "A1" and aislamiento:
        return 1.0, notas + ["A1 con aislamiento sísmico: U = 1 (art. 19)."]
    return U[cat], notas


def factor_r(sistema: str, irregularidades: list[str] | None = None) -> tuple[float, float, float, float]:
    """Arts. 22–26: devuelve (R, R0, Ia, Ip). Ia/Ip = menor valor de las irregularidades presentes."""
    if sistema not in R0:
        raise ErrorNorma(f"Sistema desconocido '{sistema}'. Opciones: {', '.join(R0)}.")
    irregularidades = irregularidades or []
    desconocidas = [i for i in irregularidades if i not in IA and i not in IP]
    if desconocidas:
        raise ErrorNorma(f"Irregularidades desconocidas: {desconocidas}. Opciones: {sorted(IA) + sorted(IP)}.")
    ia = min([IA[i] for i in irregularidades if i in IA], default=1.0)
    ip = min([IP[i] for i in irregularidades if i in IP], default=1.0)
    return R0[sistema] * ia * ip, R0[sistema], ia, ip


def verificar_restricciones(categoria: str, zona: int, sistema: str, irregularidades: list[str] | None = None,
                            pisos: int | None = None, altura_m: float | None = None, perfil: str | None = None,
                            aislamiento: bool = False) -> list[str]:
    """Tablas 8, 9 y 13 y art. 20/22.4: lista de incumplimientos (⛔) y advertencias (⚠️)."""
    cat, irr = categoria.upper(), set(irregularidades or [])
    out: list[str] = []
    if sistema == "concreto_emdl" and pisos is not None and pisos > 5:
        out.append("⛔ EMDL: máximo 5 pisos en la edición 2026 (art. 20).")
    if perfil and perfil.upper() in ("S4", "S5") and sistema == "tierra":
        out.append("⛔ Construcciones de tierra prohibidas en S4 y S5.")
    # Tabla 9 — sistemas permitidos
    ductiles_a = {"acero_scbf", "acero_ebf", "concreto_dual", "concreto_muros", "albanileria"}
    permitidos_b = ductiles_a | {"acero_smf", "acero_imf", "acero_ocbf", "concreto_porticos", "madera"}
    if cat == "A1" and zona in (3, 4) and not aislamiento:
        out.append("⛔ A1 en zonas 3–4: solo con aislamiento sísmico (Tabla 9).")
    if cat == "A1" and zona in (1, 2) and not aislamiento and sistema not in ductiles_a:
        out.append("⛔ A1 en zonas 1–2: sistema no permitido por la Tabla 9.")
    if cat == "A2" and zona in (2, 3, 4) and sistema not in ductiles_a:
        out.append("⛔ A2 en zonas 2–4: sistema no permitido por la Tabla 9.")
    if cat == "B" and zona in (2, 3, 4) and sistema not in permitidos_b:
        out.append("⛔ B en zonas 2–4: sistema no permitido por la Tabla 9.")
    # Tabla 13 — irregularidades
    extremas = irr & EXTREMAS
    if cat in ("A1", "A2"):
        if zona in (2, 3, 4) and irr:
            out.append("⛔ Categoría A en zonas 2–4: no se permiten irregularidades (Tabla 13).")
        elif zona == 1 and extremas:
            out.append("⛔ Categoría A en zona 1: no se permiten irregularidades extremas (Tabla 13).")
    elif cat == "B" and zona in (2, 3, 4) and extremas:
        out.append("⛔ Categoría B en zonas 2–4: no se permiten irregularidades extremas (Tabla 13).")
    elif cat == "C" and extremas:
        if zona in (3, 4):
            out.append("⛔ Categoría C en zonas 3–4: no se permiten irregularidades extremas (Tabla 13).")
        elif zona == 2:
            pequeno = (pisos is not None and pisos <= 2) or (altura_m is not None and altura_m <= 8)
            if not pequeno:
                out.append("⛔ Categoría C en zona 2: irregularidades extremas solo en edificios de hasta 2 pisos u 8 m (Tabla 13).")
    return out


def periodo_aproximado(altura_m: float, tipo_ct: str) -> float:
    """Art. 36: T = hn / CT."""
    if tipo_ct not in CT:
        raise ErrorNorma(f"Tipo de CT desconocido. Opciones: {', '.join(CT)}.")
    return altura_m / CT[tipo_ct]


def exponente_k(T: float) -> float:
    """Art. 35."""
    return 1.0 if T <= 0.5 else min(0.75 + 0.5 * T, 2.0)


def peso_sismico(carga_muerta: float, carga_viva: float, categoria: str) -> float:
    """Art. 31 (edificaciones comunes; depósitos, azoteas y tanques requieren tratamiento aparte)."""
    return carga_muerta + FRACCION_CV[categoria.upper()] * carga_viva


def espectro(zona: int, categoria: str, sistema: str, perfil: str | None = None, vs30: float | None = None,
             irregularidades: list[str] | None = None, ts: float | None = None, aislamiento: bool = False,
             t_max: float = 6.0, dt: float = 0.05) -> dict:
    """Art. 41: espectro inelástico Sa/g = Z·U·C·S/R, listo para cargar en ETABS/SAP2000."""
    sitio = parametros_sitio(zona, perfil, vs30, categoria, ts)
    u, notas_u = factor_u(categoria, aislamiento, zona)
    R, r0, ia, ip = factor_r(sistema, irregularidades)
    n = int(round(t_max / dt))
    periodos = [round(i * dt, 4) for i in range(n + 1)]
    for especial in (sitio.TP, sitio.TL):
        if especial <= t_max and especial not in periodos:
            periodos.append(especial)
    periodos.sort()
    sa = [round(sitio.Z * u * factor_c(t, sitio.TP, sitio.TL) * sitio.S / R, 5) for t in periodos]
    return {
        "norma": NORMA,
        "parametros": {"Z": sitio.Z, "U": u, "S": sitio.S, "TP": sitio.TP, "TL": sitio.TL,
                       "R0": r0, "Ia": ia, "Ip": ip, "R": round(R, 4), "perfil": sitio.perfil,
                       "vs30": sitio.vs30, "ts": sitio.ts, "categoria": categoria.upper(),
                       "sistema": DESCRIPCION_SISTEMAS[sistema]},
        "periodos_s": periodos,
        "sa_g": sa,
        "sa_vertical_g": [round(2 / 3 * x, 5) for x in sa],
        "notas": sitio.notas + notas_u + verificar_restricciones(categoria, zona, sistema, irregularidades,
                                                                 perfil=sitio.perfil, aislamiento=aislamiento),
        "pendientes": [PENDIENTES["factor_c"]],
    }


def cortante_estatica(zona: int, categoria: str, sistema: str, peso: float, T: float,
                      perfil: str | None = None, vs30: float | None = None,
                      irregularidades: list[str] | None = None, ts: float | None = None,
                      aislamiento: bool = False, pesos_niveles: list[float] | None = None,
                      alturas_niveles: list[float] | None = None) -> dict:
    """Arts. 34–35: V = Z·U·C·S/R·P con C/R ≥ 0,11 y distribución Fi = αi·V."""
    sitio = parametros_sitio(zona, perfil, vs30, categoria, ts)
    u, notas_u = factor_u(categoria, aislamiento, zona)
    R, r0, ia, ip = factor_r(sistema, irregularidades)
    C = factor_c(T, sitio.TP, sitio.TL)
    c_sobre_r = max(C / R, 0.11)
    V = sitio.Z * u * c_sobre_r * sitio.S * peso
    res = {
        "norma": NORMA,
        "formula": "V = Z·U·C·S/R · P   (C/R ≥ 0,11)",
        "Z": sitio.Z, "U": u, "S": sitio.S, "TP": sitio.TP, "TL": sitio.TL, "T": T, "C": round(C, 4),
        "R": round(R, 4), "C_sobre_R": round(c_sobre_r, 4), "minimo_C_R_aplicado": C / R < 0.11,
        "P": peso, "V": round(V, 3), "V_sobre_P": round(V / peso, 5), "k": exponente_k(T),
        "notas": sitio.notas + notas_u, "pendientes": [PENDIENTES["factor_c"]] if T > sitio.TP else [],
    }
    if pesos_niveles and alturas_niveles:
        if len(pesos_niveles) != len(alturas_niveles):
            raise ErrorNorma("pesos_niveles y alturas_niveles deben tener la misma longitud.")
        k = res["k"]
        base = [p * h ** k for p, h in zip(pesos_niveles, alturas_niveles)]
        total = sum(base)
        res["fuerzas_por_nivel"] = [{"nivel": i + 1, "altura_m": h, "peso": p, "alfa": round(b / total, 5),
                                     "F": round(b / total * V, 3)}
                                    for i, (p, h, b) in enumerate(zip(pesos_niveles, alturas_niveles, base))]
    return res


def escalamiento_dinamico(v_dinamica: float, v_estatica: float, regular: bool) -> dict:
    """Art. 44: cortante dinámica ≥ 80 % (regular) / 90 % (irregular) de la estática."""
    minimo = (0.80 if regular else 0.90) * v_estatica
    factor = max(1.0, minimo / v_dinamica) if v_dinamica > 0 else float("inf")
    return {"porcentaje_minimo": 80 if regular else 90, "V_minima": round(minimo, 3),
            "V_dinamica": v_dinamica, "factor_escala": round(factor, 4),
            "cumple_sin_escalar": factor == 1.0,
            "nota": "Escalar todos los resultados excepto los desplazamientos (art. 44)."}


def verificar_derivas(derivas_elasticas: list[float], R: float, material: str, regular: bool,
                      etiquetas: list[str] | None = None) -> dict:
    """Derivas inelásticas = factor·R·elásticas vs límite (valores 2019, ver PENDIENTES)."""
    if material not in DERIVA_MAX:
        raise ErrorNorma(f"Material desconocido. Opciones: {', '.join(DERIVA_MAX)}.")
    factor = 0.75 if regular else 0.85
    limite = DERIVA_MAX[material]
    filas = []
    for i, d in enumerate(derivas_elasticas):
        inel = factor * R * d
        filas.append({"nivel": etiquetas[i] if etiquetas else i + 1, "deriva_elastica": d,
                      "deriva_inelastica": round(inel, 6), "limite": limite, "cumple": inel <= limite,
                      "uso_%": round(100 * inel / limite, 1)})
    return {"norma": NORMA, "factor": f"{factor}·R", "R": R, "limite": limite, "filas": filas,
            "cumple_todo": all(f["cumple"] for f in filas),
            "pendientes": [PENDIENTES["derivas"], PENDIENTES["desplazamientos"]]}


def resumen_parametros(**kwargs) -> dict:
    """Parámetros de sitio como diccionario (útil para la memoria de cálculo)."""
    return asdict(parametros_sitio(**kwargs))
