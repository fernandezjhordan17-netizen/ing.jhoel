---
tipo: software
tags: [software/autodesk, cad]
aliases: [Autodesk AutoCAD, DWG, AutoCAD LT]
fabricante: Autodesk
formatos: [DWG, DXF, DWT, DWS]
actualizado: 2026-09-24
---
# AutoCAD

CAD 2D/3D de propósito general. En BIM se usa para detalles, planos complementarios, levantamientos y como base de [[Civil 3D]].

## Automatización / API
| Vía | Detalle |
|---|---|
| **AutoLISP / Visual LISP** | Scripts `.lsp`; desde **AutoCAD LT 2024** también disponible en LT |
| **.NET API** | C# (`Autodesk.AutoCAD.*`), comandos personalizados, plugins |
| **ObjectARX** | C++ nativo |
| **ActiveX / COM** | Automatización externa (VBA, Python `pywin32`/`comtypes`) |
| **Scripts `.scr`** y **AutoCAD Core Console** (`accoreconsole.exe`) | Procesamiento por lotes sin interfaz |
| **Design Automation API** | AutoCAD en la nube → [[Autodesk Platform Services y ACC]] |
| **ezdxf (Python)** | Leer/escribir DXF sin AutoCAD |
| **MCP** | → [[MCP AutoCAD y Civil 3D]] |

## Estándares
Capas, estilos, cajetines → [[Normas de documentacion CAD]].

↑ [[MOC Software AEC]]
