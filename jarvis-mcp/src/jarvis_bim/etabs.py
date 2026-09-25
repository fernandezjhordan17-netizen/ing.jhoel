"""
Puente a ETABS / SAP2000 mediante la CSI OAPI (COM) — Windows.

Reglas (ver "JARVIS - Seguridad y gobernanza"):
* Todas las llamadas COM se ejecutan en UN hilo dedicado con CoInitialize (la OAPI es STA).
* Se adjunta a la instancia ya abierta; nunca abre ni cierra el programa por su cuenta.
* Las operaciones de escritura son dry-run por defecto y hacen copia de respaldo del archivo.
Estado: EXPERIMENTAL — probar primero en una copia del modelo.
"""
from __future__ import annotations

import datetime as dt
import queue
import shutil
import sys
import threading
from pathlib import Path

PROGID = {"ETABS": "CSI.ETABS.API.ETABSObject", "SAP2000": "CSI.SAP2000.API.SapObject"}
TABLA_DERIVAS = "Story Drifts"
TABLA_REACCIONES = "Base Reactions"


class ErrorCSI(RuntimeError):
    pass


def _ret(resultado) -> int:
    """La OAPI devuelve 0 si todo salió bien; con comtypes puede venir como int o al final de una lista."""
    if isinstance(resultado, (list, tuple)):
        return int(resultado[-1])
    return int(resultado)


class PuenteCSI:
    def __init__(self, programa: str = "ETABS", conector=None):
        """conector: función que devuelve un SapModel (solo para pruebas sin ETABS)."""
        programa = programa.upper()
        if programa not in PROGID:
            raise ErrorCSI(f"Programa no soportado: {programa}. Opciones: {', '.join(PROGID)} "
                           "(SAFE: consultar el ProgID en la ayuda de su API).")
        self.programa = programa
        self._cola: queue.Queue = queue.Queue()
        self._hilo: threading.Thread | None = None
        self._sap = None
        self._conector = conector

    # ---- hilo COM -------------------------------------------------------------------------
    def _trabajador(self) -> None:
        if self._conector is None:
            import comtypes
            comtypes.CoInitialize()
        while True:
            funcion, respuesta = self._cola.get()
            try:
                if self._sap is None:
                    self._sap = (self._conector or self._conectar)()
                respuesta.put(("ok", funcion(self._sap)))
            except Exception as exc:  # se reenvía al hilo que llamó
                if "RPC" in str(exc) or "disconnected" in str(exc).lower():
                    self._sap = None  # el programa se cerró: reconectar en la próxima llamada
                respuesta.put(("error", exc))

    def _conectar(self):
        import comtypes.client
        helper = comtypes.client.CreateObject(f"{self.programa}v1.Helper")
        modulo = getattr(comtypes.gen, f"{self.programa}v1")
        helper = helper.QueryInterface(modulo.cHelper)
        try:
            objeto = helper.GetObject(PROGID[self.programa])
        except Exception as exc:
            raise ErrorCSI(f"No hay una instancia de {self.programa} abierta con un modelo. Ábrelo y reintenta.") from exc
        return objeto.SapModel

    def ejecutar(self, funcion, timeout: float = 900):
        if self._conector is None and sys.platform != "win32":
            raise ErrorCSI(f"El puente {self.programa} solo funciona en Windows con el programa instalado.")
        if self._hilo is None or not self._hilo.is_alive():
            self._hilo = threading.Thread(target=self._trabajador, name=f"COM-{self.programa}", daemon=True)
            self._hilo.start()
        respuesta: queue.Queue = queue.Queue()
        self._cola.put((funcion, respuesta))
        estado, valor = respuesta.get(timeout=timeout)
        if estado == "error":
            raise valor
        return valor

    # ---- lectura --------------------------------------------------------------------------
    def estado(self) -> dict:
        def _f(sap):
            archivo = sap.GetModelFilename()
            version = sap.GetVersion()
            return {"programa": self.programa, "archivo": archivo,
                    "version": version[0] if isinstance(version, (list, tuple)) else str(version),
                    "unidades": int(sap.GetPresentUnits()),
                    "bloqueado": bool(sap.GetModelIsLocked())}
        return self.ejecutar(_f)

    def leer_tabla(self, clave: str, casos: list[str] | None = None, grupo: str = "All", max_filas: int = 5000) -> dict:
        """Lee cualquier tabla de la base de datos interactiva (DatabaseTables.GetTableForDisplayArray)."""
        def _f(sap):
            if casos:
                sap.DatabaseTables.SetLoadCasesSelectedForDisplay(list(casos))
            r = sap.DatabaseTables.GetTableForDisplayArray(clave, [], grupo, 0, [], 0, [])
            if _ret(r) != 0:
                raise ErrorCSI(f"No se pudo leer la tabla '{clave}' (¿análisis sin correr o nombre incorrecto?).")
            campos, n, datos = list(r[2]), int(r[3]), list(r[4])
            if not campos or len(datos) != n * len(campos):
                raise ErrorCSI("Respuesta de la tabla con formato inesperado; revisa la versión de la OAPI.")
            filas = [dict(zip(campos, datos[i * len(campos):(i + 1) * len(campos)])) for i in range(min(n, max_filas))]
            return {"tabla": clave, "campos": campos, "filas_totales": n, "filas": filas}
        return self.ejecutar(_f)

    def derivas(self, casos: list[str]) -> dict:
        """Máxima deriva por piso y dirección desde la tabla 'Story Drifts'."""
        t = self.leer_tabla(TABLA_DERIVAS, casos)
        maximos: dict[tuple, float] = {}
        for f in t["filas"]:
            try:
                clave = (f.get("Story"), f.get("Direction"))
                valor = abs(float(f.get("Drift", 0)))
            except (TypeError, ValueError):
                continue
            maximos[clave] = max(valor, maximos.get(clave, 0.0))
        filas = [{"piso": p, "direccion": d, "deriva_elastica": v} for (p, d), v in maximos.items()]
        return {"casos": casos, "filas": filas}

    def reacciones_base(self, casos: list[str]) -> dict:
        t = self.leer_tabla(TABLA_REACCIONES, casos)
        return {"casos": casos, "filas": [{k: f.get(k) for k in ("OutputCase", "StepType", "FX", "FY", "FZ")}
                                          for f in t["filas"]]}

    # ---- escritura (dry-run por defecto) --------------------------------------------------
    def _respaldo(self, sap) -> str | None:
        archivo = sap.GetModelFilename()
        if not archivo or not Path(archivo).exists():
            return None
        destino = Path(archivo).with_name(f"{Path(archivo).stem}_JARVIS_{dt.datetime.now():%Y%m%d_%H%M%S}{Path(archivo).suffix}")
        shutil.copy2(archivo, destino)
        return str(destino)

    def crear_espectro(self, nombre: str, periodos: list[float], valores: list[float],
                       amortiguamiento: float = 0.05, dry_run: bool = True) -> dict:
        """Crea/reemplaza una función de espectro de usuario (Func.FuncRS.SetUser)."""
        if len(periodos) != len(valores) or len(periodos) < 2:
            raise ErrorCSI("periodos y valores deben tener la misma longitud (≥ 2).")
        plan = {"accion": f"Crear función de espectro '{nombre}' en {self.programa}", "puntos": len(periodos),
                "amortiguamiento": amortiguamiento, "T_max": max(periodos), "Sa_max_g": max(valores)}
        if dry_run:
            return {"dry_run": True, **plan, "siguiente_paso": "Confirma y vuelve a llamar con dry_run=false."}

        def _f(sap):
            if sap.GetModelIsLocked():
                raise ErrorCSI("El modelo está bloqueado (tiene resultados). Desbloquéalo tú en el programa: "
                               "eso borra los resultados del análisis.")
            respaldo = self._respaldo(sap)
            r = sap.Func.FuncRS.SetUser(nombre, len(periodos), list(periodos), list(valores), amortiguamiento)
            if _ret(r) != 0:
                raise ErrorCSI(f"La OAPI rechazó la función (código {_ret(r)}).")
            return {"dry_run": False, **plan, "respaldo": respaldo,
                    "nota": "Función creada. Asígnala a los casos de respuesta espectral SX/SY y guarda el modelo."}
        return self.ejecutar(_f)

    def correr_analisis(self, confirmar: bool = False) -> dict:
        if not confirmar:
            return {"dry_run": True, "accion": f"Ejecutar el análisis del modelo abierto en {self.programa}",
                    "siguiente_paso": "Confirma con confirmar=true (puede tardar varios minutos)."}

        def _f(sap):
            respaldo = self._respaldo(sap)
            r = sap.Analyze.RunAnalysis()
            if _ret(r) != 0:
                raise ErrorCSI(f"El análisis devolvió el código {_ret(r)}. Revisa el log del programa.")
            return {"dry_run": False, "analisis": "completado", "respaldo": respaldo}
        return self.ejecutar(_f, timeout=7200)


    def crear_combinaciones(self, plan: list[dict], dry_run: bool = True) -> dict:
        """Crea combinaciones (RespCombo.Add + SetCaseList). plan = salida de e060.plan_combinaciones."""
        resumen = [{"nombre": p["nombre"], "tipo": p["tipo"],
                    "detalle": p.get("casos") or p.get("combinaciones")} for p in plan]
        if dry_run:
            return {"dry_run": True, "combinaciones": resumen,
                    "siguiente_paso": "Revisa los factores y confirma con dry_run=false."}

        def _f(sap):
            if sap.GetModelIsLocked():
                raise ErrorCSI("El modelo está bloqueado (tiene resultados). Desbloquéalo tú en el programa.")
            respaldo = self._respaldo(sap)
            creadas, fallidas = [], []
            for p in plan:
                envolvente = p["tipo"] == "envolvente"
                if _ret(sap.RespCombo.Add(p["nombre"], 1 if envolvente else 0)) != 0:
                    fallidas.append(f"{p['nombre']} (¿ya existe?)")
                    continue
                items = [(c, 1.0) for c in p["combinaciones"]] if envolvente else p["casos"]
                tipo_nombre = 1 if envolvente else 0  # 0 = caso de carga, 1 = combinación
                errores = [c for c, sf in items if _ret(sap.RespCombo.SetCaseList(p["nombre"], tipo_nombre, c, sf)) != 0]
                (fallidas if errores else creadas).append(p["nombre"] if not errores else f"{p['nombre']} {errores}")
            return {"dry_run": False, "creadas": creadas, "fallidas": fallidas, "respaldo": respaldo}
        return self.ejecutar(_f)


_PUENTES: dict[str, PuenteCSI] = {}


def puente(programa: str = "ETABS") -> PuenteCSI:
    programa = programa.upper()
    if programa not in _PUENTES:
        _PUENTES[programa] = PuenteCSI(programa)
    return _PUENTES[programa]
