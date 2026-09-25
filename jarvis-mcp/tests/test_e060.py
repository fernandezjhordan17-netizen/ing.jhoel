import math

import pytest

from jarvis_bim import e060
from jarvis_bim.e060 import ErrorE060


def test_combinaciones_sismo():
    c = {x["nombre"]: x["factores"] for x in e060.combinaciones()}
    assert c["U1"] == {"CM": 1.4, "CV": 1.7}
    assert c["US1"] == {"CM": 1.25, "CV": 1.25, "CS": 1.0}
    assert c["US4"] == {"CM": 0.9, "CS": -1.0}
    assert len(c) == 5


def test_beta1():
    assert e060.beta1(21) == 0.85
    assert math.isclose(e060.beta1(35), 0.80)
    assert e060.beta1(80) == 0.65


def test_flexion_viga_conocida():
    r = e060.flexion_viga(120, 300, 600, fc=21, fy=420)
    d = r["d_mm"]
    # verificación independiente: φMn con el As de diseño >= Mu
    assert r["phi_Mn_kNm"] >= 120 - 0.01
    a = r["As_diseno_mm2"] * 420 / (0.85 * 21 * 300)
    assert math.isclose(0.9 * r["As_diseno_mm2"] * 420 * (d - a / 2) / 1e6, 120, rel_tol=1e-3)
    assert r["cumple_maximo"] and r["barras"]


def test_flexion_rige_minimo():
    r = e060.flexion_viga(5, 300, 600)
    assert r["rige_minimo"]
    assert r["As_diseno_mm2"] == r["As_min_mm2"]


def test_flexion_seccion_insuficiente():
    with pytest.raises(ErrorE060):
        e060.flexion_viga(2000, 250, 400)


def test_cortante_viga():
    r = e060.cortante_viga(150, 300, 540, fc=21, fy=420)
    vc = 0.17 * math.sqrt(21) * 300 * 540 / 1e3
    assert math.isclose(r["phi_Vc_kN"], round(0.85 * vc, 2))
    assert r["s_diseno_mm"] <= 270 and r["s_diseno_mm"] % 25 == 0


def test_cortante_excesivo():
    with pytest.raises(ErrorE060):
        e060.cortante_viga(2000, 250, 400)


def test_columna_axial():
    r = e060.columna_axial(1500, 400, 400, 8 * 284, fc=28, fy=420)
    po = 0.85 * 28 * (160000 - 2272) + 420 * 2272
    assert math.isclose(r["phi_Pn_max_kN"], round(0.8 * 0.7 * po / 1e3, 1))
    assert r["cuantia_ok"] and r["cumple"]


def test_barras_entran_en_la_seccion():
    for op in e060.sugerir_barras(1500, 300):
        assert op["As_mm2"] >= 1500 and op["espacio_libre_mm"] >= 25


def test_plan_combinaciones_espectral():
    plan = {p["nombre"]: p for p in e060.plan_combinaciones(["Dead", "SCP"], ["Live"], ["SX", "SY"])}
    assert set(plan) == {"U1", "U2_SX", "U3_SX", "U2_SY", "U3_SY", "ENV_E060"}
    assert ("Dead", 1.4) in plan["U1"]["casos"] and ("Live", 1.7) in plan["U1"]["casos"]
    assert ("SX", 1.0) in plan["U2_SX"]["casos"] and ("Live", 1.25) in plan["U2_SX"]["casos"]
    assert all(c != "Live" for c, _ in plan["U3_SX"]["casos"])
    assert len(plan["ENV_E060"]["combinaciones"]) == 5


def test_plan_combinaciones_estatico_con_signos():
    nombres = [p["nombre"] for p in e060.plan_combinaciones(["CM"], ["CV"], ["SX"], sismo_espectral=False, envolvente=None)]
    assert nombres == ["U1", "U2_SX+", "U3_SX+", "U2_SX-", "U3_SX-"]


def test_cortante_excepcion_vigas_chatas():
    # 11.5.6.1 c): h ≤ máx(250 mm; 0,5·bw) no exige Av mín si no hace falta Vs
    r = e060.cortante_viga(12, 200, 142.5, h_mm=200)
    assert r["exceptuada_11_5_6_1c"] and not r["requiere_estribos"]
    r2 = e060.cortante_viga(12, 200, 142.5)
    assert r2["requiere_refuerzo_minimo"] and r2["s_diseno_mm"] <= 142.5 / 2
