---
tipo: mcp
tags: [mcp, software/trimble, tekla]
aliases: [Tekla MCP]
actualizado: 2026-09-24
---
# MCP — Tekla Structures

## Opciones comunitarias
| Repositorio | Enfoque |
|---|---|
| `teknovizier/tekla_mcp_server` | Automatización con lenguaje natural; arquitectura modular (FastMCP) con proveedores: selección, vistas, propiedades, componentes, operaciones, planos |
| `YuriyKirillov/TeklaMCPServer` | Puente entre IA y Tekla para acelerar el modelado |
| `pawellisowski/tekla-api-mcp` (npm `tekla-api-mcp`) | **Documentación** de Tekla Open API + 50+ ejemplos de código (ideal para que JARVIS escriba macros correctas) |
| Servidor de martin9020 (PulseMCP) | ~80 herramientas: geometría, selección, planos, exportaciones, búsqueda semántica de atributos |

## Notas técnicas
- La Open API se conecta a un Tekla **en ejecución** y exige ensamblados de la **misma versión** (NuGet por versión).
- Usar primero el servidor de documentación para generar **macros C#** revisables, luego automatizar.

## Casos de uso
Numeración, creación de planos de taller en lote, reportes de piezas/pernos a [[Excel]], verificación de propiedades antes de exportar IFC.

↑ [[MOC JARVIS y MCP]] · Software: [[Tekla Structures]]
