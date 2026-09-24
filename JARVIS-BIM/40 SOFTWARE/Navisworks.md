---
tipo: software
tags: [software/autodesk, coordinacion, 4d, 5d]
aliases: [Autodesk Navisworks, Navisworks Manage, NWD, NWF, NWC]
fabricante: Autodesk
formatos: [NWC, NWF, NWD]
actualizado: 2026-09-24
---
# Navisworks

Plataforma de **revisión y coordinación** de modelos federados (Manage / Simulate / Freedom).

## Formatos
| Formato | Qué es |
|---|---|
| `NWC` | Caché generado al abrir/exportar un archivo nativo (RVT, DWG, IFC…) |
| `NWF` | Archivo de trabajo **federado** que guarda referencias a los modelos + pruebas, sets, vistas |
| `NWD` | Archivo **publicado** con todo embebido (instantánea) |

## Herramientas
- **Clash Detective** (interferencias duras, holgura, duplicados) → [[Coordinacion BIM y deteccion de interferencias]]
- **TimeLiner** (4D) → [[BIM 4D - Planificacion]]
- **Quantification** (5D) → [[BIM 5D - Costos y metrados]]
- Selection/Search Sets, Viewpoints, Redlines, Animator, Appearance Profiler.
- Exporta reportes (XML/HTML) e incidencias (vía plugins) a [[BCF - BIM Collaboration Format]].

## API
.NET API (plugins `AddInPlugin`, `DockPanePlugin`, `EventWatcherPlugin`), COM API, **Automation API** para procesos por lotes fuera de la interfaz. MCP comunitarios → [[MCP Navisworks]].

↑ [[MOC Software AEC]] · [[Federacion de modelos]]
