---
tipo: mcp
tags: [mcp, software/autodesk, estructural, robot]
aliases: [Robot MCP, RSA MCP]
actualizado: 2026-09-24
---
# MCP — Robot Structural Analysis

## Opciones comunitarias
| Repositorio | Capacidades |
|---|---|
| `TranTriLuc/robot-structural-mcp` | Leer modelo (nudos, barras, paneles, secciones, materiales, apoyos), casos y combinaciones, ejecutar cálculo, resultados (fuerzas en barras, desplazamientos, reacciones). Script de instalación crea el entorno virtual y escribe la configuración MCP |
| `nhantruong96/rsap-mcp` | Crear modelos (nudos, barras), secciones de bases de datos (IPE, HEA…), materiales, cargas, análisis y resultados vía **RobotOM** |

## Notas
- RobotOM es COM → mismo cuidado con hilos que CSI.
- Útil como **segunda opinión** para verificar resultados de [[ETABS]] (análisis independiente) y para el enlace con el modelo analítico de [[Revit]].

↑ [[MOC JARVIS y MCP]] · Software: [[Robot Structural Analysis]]
