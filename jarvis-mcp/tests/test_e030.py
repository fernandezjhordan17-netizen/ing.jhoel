import math

import pytest

from jarvis_bim import e030
from jarvis_bim.e030 import ErrorNorma


@pytest.mark.parametrize("vs, perfil", [(900, "S0"), (800, "S0"), (700, "S1"), (550, "S1"),
                                        (420, "S2"), (350, "S2"), (250, "S3"), (150, "S4")])
def test_perfil_por_vs30(vs, perfil):
    assert e030.perfil_por_vs30(vs) == perfil


def test_interpolacion_s2_zona4_punto_medio():
    p = e030.parametros_sitio(4, "S2", vs30=450)
    assert (p.S, p.TP, p.TL) == (1.05, 0.5, 2.25)


def test_s2_sin_vs30_usa_extremo_desfavorable():
    p = e030.parametros_sitio(4, "S2")
    assert (p.S, p.TP, p.TL) == (1.10, 0.6, 2.0)
    assert any("Sin Vs30" in n for n in p.notas)


def test_continuidad_entre_perfiles_en_350():
    s2 = e030.parametros_sitio(3, "S2", vs30=350)
    s3 = e030.parametros_sitio(3, "S3", vs30=350)
    assert (s2.S, s2.TP, s2.TL) == (s3.S, s3.TP, s3.TL)


def test_zona4_s4_exige_estudio_de_sitio():
    with pytest.raises(ErrorNorma):
        e030.parametros_sitio(4, "S4")


def test_s5_prohibido():
    with pytest.raises(ErrorNorma):
        e030.parametros_sitio(2, "S5")


def test_ts_mayor_cambia_al_perfil_siguiente():
    p = e030.parametros_sitio(4, "S2", vs30=450, categoria="A2", ts=0.40)
    assert p.perfil == "S3"
    assert (p.S, p.TP, p.TL) == (1.20, 0.9, 1.6)


def test_ts_cumple_mantiene_perfil():
    p = e030.parametros_sitio(4, "S2", vs30=450, categoria="B", ts=0.30)
    assert p.perfil == "S2"


def test_aviso_ts_obligatorio_en_zona4():
    p = e030.parametros_sitio(4, "S1", categoria="B")
    assert any("Ts" in n for n in p.notas)


def test_factor_c_tramos():
    assert e030.factor_c(0.3, 0.6, 2.0) == 2.5
    assert math.isclose(e030.factor_c(1.2, 0.6, 2.0), 1.25)
    assert math.isclose(e030.factor_c(4.0, 0.6, 2.0), 0.1875)


def test_factor_r_con_irregularidades():
    R, r0, ia, ip = e030.factor_r("concreto_dual", ["torsional", "masa", "piso_blando"])
    assert (r0, ia, ip) == (7.0, 0.75, 0.75)
    assert math.isclose(R, 7 * 0.75 * 0.75)


def test_emdl_r0_2026():
    assert e030.R0["concreto_emdl"] == 3.5


def test_cortante_basal_estatica():
    r = e030.cortante_estatica(4, "C", "concreto_dual", peso=10000, T=0.4, perfil="S1")
    assert math.isclose(r["V"], 0.45 * 1.0 * 2.5 * 1.0 / 7 * 10000, rel_tol=1e-4)
    assert not r["minimo_C_R_aplicado"]


def test_minimo_c_sobre_r():
    r = e030.cortante_estatica(4, "C", "concreto_dual", peso=10000, T=5.0, perfil="S1")
    assert r["minimo_C_R_aplicado"]
    assert math.isclose(r["V"], 0.45 * 0.11 * 10000, rel_tol=1e-6)


def test_distribucion_en_altura_suma_v():
    r = e030.cortante_estatica(2, "C", "albanileria", peso=3000, T=0.2, perfil="S2", vs30=400,
                               pesos_niveles=[1000, 1000, 1000], alturas_niveles=[2.7, 5.4, 8.1])
    assert math.isclose(sum(f["F"] for f in r["fuerzas_por_nivel"]), r["V"], rel_tol=1e-3)
    assert r["k"] == 1.0


def test_exponente_k():
    assert e030.exponente_k(0.5) == 1.0
    assert math.isclose(e030.exponente_k(1.0), 1.25)
    assert e030.exponente_k(4.0) == 2.0


def test_escalamiento_dinamico():
    r = e030.escalamiento_dinamico(1000, 1500, regular=True)
    assert r["factor_escala"] == 1.2
    assert e030.escalamiento_dinamico(1400, 1500, regular=True)["cumple_sin_escalar"]


def test_derivas():
    r = e030.verificar_derivas([0.001, 0.0015], R=7, material="concreto", regular=True)
    assert r["filas"][0]["cumple"] and not r["filas"][1]["cumple"]
    assert r["pendientes"]


def test_restricciones():
    assert any("EMDL" in x for x in e030.verificar_restricciones("C", 4, "concreto_emdl", pisos=6))
    assert any("aislamiento" in x for x in e030.verificar_restricciones("A1", 4, "concreto_dual"))
    assert e030.verificar_restricciones("C", 4, "concreto_dual", ["torsional_extrema"])
    assert not e030.verificar_restricciones("C", 2, "concreto_dual", ["torsional_extrema"], pisos=2)
    assert not e030.verificar_restricciones("B", 1, "concreto_porticos", ["torsional_extrema"])


def test_espectro():
    esp = e030.espectro(4, "C", "concreto_dual", perfil="S2", vs30=450)
    p = esp["parametros"]
    assert esp["periodos_s"][0] == 0.0
    assert math.isclose(esp["sa_g"][0], p["Z"] * p["U"] * 2.5 * p["S"] / p["R"], rel_tol=1e-4)
    assert p["TP"] in esp["periodos_s"]
    assert len(esp["sa_g"]) == len(esp["periodos_s"])


def test_a1_con_aislamiento_u_1():
    u, _ = e030.factor_u("A1", aislamiento=True, zona=4)
    assert u == 1.0
