"""Pruebas del puente CSI con un SapModel simulado (sin ETABS)."""
import threading
from types import SimpleNamespace

import pytest

from jarvis_bim.etabs import ErrorCSI, PuenteCSI


class SapFalso:
    def __init__(self, archivo, bloqueado=False):
        self.archivo = archivo
        self.bloqueado = bloqueado
        self.hilos = set()
        self.espectros = {}
        filas = [["Story2", "SX", "Max", "X", "0.0012"], ["Story2", "SX", "Max", "X", "0.0015"],
                 ["Story1", "SX", "Max", "X", "0.0009"], ["Story1", "SY", "Max", "Y", "0.0011"]]
        self._tablas = {"Story Drifts": (["Story", "OutputCase", "StepType", "Direction", "Drift"], filas)}
        self.DatabaseTables = SimpleNamespace(SetLoadCasesSelectedForDisplay=lambda casos: 0,
                                              GetTableForDisplayArray=self._tabla)
        self.Func = SimpleNamespace(FuncRS=SimpleNamespace(SetUser=self._set_user))
        self.Analyze = SimpleNamespace(RunAnalysis=lambda: 0)
        self.combos = {}
        self.RespCombo = SimpleNamespace(Add=self._combo_add, SetCaseList=self._combo_case)

    def _registrar(self):
        self.hilos.add(threading.get_ident())

    def GetModelFilename(self):
        self._registrar()
        return self.archivo

    def GetVersion(self):
        return ["22.0.0", 22.0, 0]

    def GetPresentUnits(self):
        return 6

    def GetModelIsLocked(self):
        return self.bloqueado

    def _tabla(self, clave, campos, grupo, version, incluidos, n, datos):
        self._registrar()
        if clave not in self._tablas:
            return [[], 0, [], 0, [], 1]
        cab, filas = self._tablas[clave]
        plano = [x for f in filas for x in f]
        return [cab, 1, cab, len(filas), plano, 0]

    def _combo_add(self, nombre, tipo):
        if nombre in self.combos:
            return 1
        self.combos[nombre] = {"tipo": tipo, "items": []}
        return 0

    def _combo_case(self, nombre, tipo_nombre, caso, sf):
        self.combos[nombre]["items"].append((tipo_nombre, caso, sf))
        return [tipo_nombre, 0]

    def _set_user(self, nombre, n, periodos, valores, amort):
        self._registrar()
        self.espectros[nombre] = (periodos, valores, amort)
        return [periodos, valores, 0]


@pytest.fixture
def modelo(tmp_path):
    edb = tmp_path / "edificio.EDB"
    edb.write_bytes(b"modelo")
    return SapFalso(str(edb))


def test_estado_y_hilo_unico(modelo):
    p = PuenteCSI("ETABS", conector=lambda: modelo)
    e = p.estado()
    p.leer_tabla("Story Drifts")
    assert e["archivo"].endswith("edificio.EDB") and e["unidades"] == 6
    assert len(modelo.hilos) == 1 and threading.get_ident() not in modelo.hilos


def test_derivas_maximas_por_piso(modelo):
    d = PuenteCSI(conector=lambda: modelo).derivas(["SX", "SY"])
    tabla = {(f["piso"], f["direccion"]): f["deriva_elastica"] for f in d["filas"]}
    assert tabla[("Story2", "X")] == 0.0015 and tabla[("Story1", "Y")] == 0.0011


def test_tabla_inexistente(modelo):
    with pytest.raises(ErrorCSI):
        PuenteCSI(conector=lambda: modelo).leer_tabla("No existe")


def test_espectro_dry_run_no_escribe(modelo):
    r = PuenteCSI(conector=lambda: modelo).crear_espectro("E030", [0, 1], [0.4, 0.2])
    assert r["dry_run"] and not modelo.espectros


def test_espectro_escribe_con_respaldo(modelo, tmp_path):
    r = PuenteCSI(conector=lambda: modelo).crear_espectro("E030", [0, 1], [0.4, 0.2], dry_run=False)
    assert "E030" in modelo.espectros and r["respaldo"]
    assert len(list(tmp_path.glob("edificio_JARVIS_*.EDB"))) == 1


def test_modelo_bloqueado_no_se_modifica(tmp_path):
    edb = tmp_path / "b.EDB"
    edb.write_bytes(b"x")
    m = SapFalso(str(edb), bloqueado=True)
    with pytest.raises(ErrorCSI):
        PuenteCSI(conector=lambda: m).crear_espectro("E030", [0, 1], [0.4, 0.2], dry_run=False)
    assert not m.espectros


def test_sin_windows_sin_conector():
    import sys
    if sys.platform == "win32":
        pytest.skip("solo aplica fuera de Windows")
    with pytest.raises(ErrorCSI):
        PuenteCSI("ETABS").estado()


def test_crear_combinaciones(modelo):
    from jarvis_bim import e060
    plan = e060.plan_combinaciones(["Dead"], ["Live"], ["SX"])
    p = PuenteCSI(conector=lambda: modelo)
    assert p.crear_combinaciones(plan)["dry_run"] and not modelo.combos
    r = p.crear_combinaciones(plan, dry_run=False)
    assert set(r["creadas"]) == {"U1", "U2_SX", "U3_SX", "ENV_E060"} and not r["fallidas"]
    assert modelo.combos["ENV_E060"]["tipo"] == 1
    assert (0, "Dead", 1.4) in modelo.combos["U1"]["items"]
    r2 = p.crear_combinaciones(plan, dry_run=False)
    assert len(r2["fallidas"]) == 4  # ya existen: no se sobrescriben
