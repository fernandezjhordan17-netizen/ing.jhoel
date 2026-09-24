---
tipo: mcp
tags: [mcp, software/autodesk, autocad, civil3d]
aliases: [AutoCAD MCP, Civil 3D MCP]
actualizado: 2026-09-24
---
# MCP — AutoCAD y Civil 3D

## Opciones
| Opción | Tipo | Notas |
|---|---|---|
| **autocad-mcp** (`puran-water/autocad-mcp`) | Comunitario | 8 herramientas consolidadas (dibujo, entidades, capas, bloques, anotación, P&ID, vista, sistema); **dos backends**: IPC por archivos con AutoLISP para AutoCAD/AutoCAD LT 2024+ en Windows, y **ezdxf** sin AutoCAD (genera DXF); Python 3.10+ con `uv` |
| `ks40-academy/autocad-mcp` y otros | Comunitarios | Variantes vía COM/AutoLISP |
| **HMK Pilot** | Comercial | AutoCAD (80+ acciones) y **Civil 3D** (50+ acciones: alineamientos, perfiles, superficies, corredores) |
| **Propio (.NET)** | A construir | Plugin NETLOAD con canal IPC; necesario para objetos de Civil 3D (`Autodesk.Civil.*`) si no usas HMK |

## Particularidades
- AutoCAD LT desde 2024 soporta AutoLISP → automatizable.
- **Headless**: `accoreconsole.exe` + scripts `.scr` para procesos por lotes (plotear, purgar, auditar capas) sin abrir la interfaz.
- Civil 3D: operaciones pesadas (corredores) deben ejecutarse con bloqueo de documento y en el hilo principal.

## Casos de uso JARVIS
- Auditoría de capas vs [[Normas de documentacion CAD]].
- Crear alineamiento + perfil desde CSV de topografía.
- Cuadro de áreas/cubicación a [[Excel]].

↑ [[MOC JARVIS y MCP]] · Software: [[AutoCAD]] · [[Civil 3D]]
