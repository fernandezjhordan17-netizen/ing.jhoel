---
tipo: jarvis
tags: [mcp, arquitectura, com, dotnet]
aliases: [Puentes MCP, Bridge patterns, Como conectar software de escritorio]
actualizado: 2026-09-24
---
# Patrones de puente MCP para software de escritorio

El software AEC es **de escritorio, Windows, y muchas veces de un solo hilo**. Hay seis formas de conectarlo a MCP:

| # | Patrón | Cómo funciona | Programas |
|---|---|---|---|
| 1 | **MCP del fabricante** | El programa trae su propio servidor MCP | Revit 2027 (Technical Preview), Dynamo 4.2 (DynamoMCP) |
| 2 | **Automatización COM desde fuera** | Servidor MCP en Python (`comtypes`/`pywin32`) que se adjunta al programa abierto | ETABS, SAP2000, SAFE (CSI OAPI), Robot (RobotOM), AutoCAD (ActiveX), Excel (xlwings), Navisworks (COM) |
| 3 | **Add-in dentro del programa + IPC** | Plugin .NET cargado en el programa abre un canal (WebSocket, HTTP local, *named pipe*); el servidor MCP (TS/Python/C#) reenvía comandos | Revit, Navisworks, AutoCAD/Civil 3D .NET |
| 4 | **API .NET fuera de proceso** | App externa en C# referencia las DLL y se conecta al programa en ejecución | Tekla Open API |
| 5 | **Archivos / sin interfaz** | Script por archivos (AutoLISP con cola de archivos), consola (`accoreconsole`), librerías (ezdxf, IfcOpenShell, openpyxl) | AutoCAD LT, DXF, IFC, Excel |
| 6 | **Nube** | APIs REST/GraphQL | APS (Design Automation, AEC Data Model), ACC, Speckle |

## Reglas técnicas críticas
> [!danger] Hilos
> - **COM (STA)**: los objetos COM de CSI/Robot deben usarse desde el **mismo hilo** que los creó. Un servidor asíncrono (FastMCP) debe delegar a un **hilo trabajador dedicado** con `CoInitialize()` y una cola de comandos.
> - **Revit API**: solo es válida en el contexto de la API (hilo principal). Desde un servidor IPC hay que usar **`ExternalEvent` / `IExternalEventHandler`** y envolver cambios en `Transaction` (o `TransactionGroup` para deshacer en bloque).
> - **Navisworks/AutoCAD**: igual — invocar en el hilo de la interfaz (`Application.Invoke`, `DocumentLock` en AutoCAD).

## Plantilla de herramienta segura
1. `dry_run=True` por defecto → devuelve lo que **haría**.
2. Validar entradas (unidades, rangos, existencia de elementos).
3. Ejecutar en transacción con nombre `JARVIS: <acción>`.
4. Devolver resultado + IDs afectados + cómo deshacer.
5. Registrar en la bitácora ([[Plantilla - Diario JARVIS]]).
6. Operaciones largas (análisis): patrón **iniciar → consultar estado → leer resultados**, con tiempo máximo.

## Esqueleto (Python + COM en hilo dedicado)
```python
import queue, threading
import comtypes, comtypes.client
from mcp.server.fastmcp import FastMCP

cola = queue.Queue()

def trabajador():
    comtypes.CoInitialize()
    helper = comtypes.client.CreateObject("ETABSv1.Helper")
    helper = helper.QueryInterface(comtypes.gen.ETABSv1.cHelper)
    sap = helper.GetObject("CSI.ETABS.API.ETABSObject").SapModel
    while True:
        funcion, respuesta = cola.get()
        try:
            respuesta.put(("ok", funcion(sap)))
        except Exception as e:
            respuesta.put(("error", str(e)))

threading.Thread(target=trabajador, daemon=True).start()

def en_etabs(funcion):
    r = queue.Queue(); cola.put((funcion, r)); estado, valor = r.get(timeout=600)
    if estado == "error": raise RuntimeError(valor)
    return valor

mcp = FastMCP("etabs-jarvis")

@mcp.tool()
def nombre_modelo() -> str:
    """Devuelve la ruta del modelo ETABS abierto."""
    return en_etabs(lambda sap: sap.GetModelFilename())

if __name__ == "__main__":
    mcp.run()
```

↑ [[MOC JARVIS y MCP]] · [[JARVIS - Arquitectura]] · [[JARVIS - Seguridad y gobernanza]]
