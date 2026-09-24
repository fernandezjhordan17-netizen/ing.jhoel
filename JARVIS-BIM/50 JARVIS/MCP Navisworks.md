---
tipo: mcp
tags: [mcp, software/autodesk, navisworks, coordinacion]
aliases: [Navisworks MCP]
actualizado: 2026-09-24
---
# MCP — Navisworks

## Opciones comunitarias
| Repositorio | Versiones | Enfoque |
|---|---|---|
| `mikhalchankasm/NavisWorksMaster` | Manage 2024–2027 | Suite de plugins + servidor MCP local para coordinadores; interferencias, coloreado, puntos de vista, propiedades, reportes; **dry-run por defecto** |
| `HorizunGroup/naviscoord-mcp` | Manage 2024–2026 | Interferencias asistidas, análisis de causa raíz, planes de coordinación |
| `Aitology/Navisworks_MCP` | — | 30+ operaciones: interferencias, agrupación, sets de selección/búsqueda, vistas, propiedades, colores |
| `livpasdiora/Navis-MCP-ClashDetective` | Manage 2026 | Coordinación MEP con Clash Detective (basado en la prueba de concepto de kikki) |
| `meococ/navis-mcp` | Manage 2026 | Puente local, "evidence packs", reportes con rutas protegidas |
| `ScanBIM-Labs/navisworks-mcp` | Nube (APS) | Coordinación multiarchivo |
| HMK Pilot | Comercial | 90+ acciones incl. TimeLiner |

## Flujo objetivo
1. Anexar NWC compartidos → guardar NWF ([[Federacion de modelos]]).
2. Ejecutar pruebas de la matriz de choques.
3. Agrupar choques (nivel/sistema/elemento causante) con ayuda del modelo de IA.
4. Exportar BCF + reporte → [[Plantilla - Reporte de interferencias]].
5. Crear tareas por responsable → [[MCP Gestion de Proyectos]].

↑ [[MOC JARVIS y MCP]] · Software: [[Navisworks]] · [[Coordinacion BIM y deteccion de interferencias]]
