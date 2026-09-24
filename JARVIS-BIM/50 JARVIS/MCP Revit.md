---
tipo: mcp
tags: [mcp, software/autodesk, revit]
aliases: [Revit MCP, MCP para Revit]
actualizado: 2026-09-24
---
# MCP — Revit

## Opciones (septiembre 2026)
| Opción | Tipo | Versiones | Notas |
|---|---|---|---|
| **Revit Public MCP Server** (Autodesk) | Oficial, *Technical Preview* | Revit 2027 (2027.2+) | Complemento separado que se descarga desde **accounts.autodesk.com** (derechos de Revit 2027); configura Claude Desktop o Cursor automáticamente. Autodesk publica artículos de soporte ("Usage of Revit 2027 MCP Server", solución si no aparece en Claude). Revit 2027 también trae *Autodesk Assistant* |
| **mcp-servers-for-revit** (GitHub `mcp-servers-for-revit/mcp-servers-for-revit`) | Comunitario, MIT | Revit 2020–2026 | Servidor TypeScript ↔ WebSocket ↔ plugin C# + "command set". Se instala copiando el ZIP de la versión a `%AppData%\Autodesk\Revit\Addins\<año>\` y configurando el servidor vía npm |
| **RevitCortex** (`LuDattilo/RevitCortex`) | Comunitario | 2023–2027 | ~170 herramientas, descubrimiento dinámico, reconstrucción IFC, Power BI |
| **RevitMCPServer** (`KenLP/RevitMCPServer`) | Comunitario | 2025–2027 | Operaciones de varios pasos como **una sola transacción deshacible** |
| **BIMwright rvt-mcp** (`bimwright/rvt-mcp`) | Comunitario | 2022–2027 | Servidor MCP para Revit multi-versión |
| `armanwu/revit-2027-mcp`, `oakplank/RevitMCP`, `PiggyAndrew/revit_mcp` | Comunitarios | Varias | Alternativas / referencia de código |
| **BIBIM** (`SquareZero-Inc/bibim-revit`, `bibim-dynamo`) | Agente open source (no MCP) | Revit 2022–2027 | Dentro de Revit: lenguaje natural → **C#** validado con Roslyn y ejecutado; índice local de RevitAPI.xml; *trae tu propia clave* (Claude). Ver [[Herramientas de IA para BIM]] |
| **HMK Pilot** | Comercial | Revit, AutoCAD, Civil 3D, Navisworks | Cientos de acciones en un solo producto |
| **APS AEC Data Model MCP** (`autodesk-platform-services/aps-aecdm-mcp-dotnet`) | Ejemplo oficial en la nube | Modelos publicados en ACC | Consulta de elementos vía GraphQL |

## Recomendación para JARVIS
1. Si tienes **Revit 2027**: empezar con el **MCP oficial** (menor riesgo, soporte).
2. Si usas 2024–2026: `mcp-servers-for-revit` (el más difundido, MIT) **en un modelo de prueba**.
3. Para funciones que falten: add-in propio en C# (.NET 8) con el SDK MCP de C# siguiendo [[Patrones de puente MCP para software de escritorio]].

## Herramientas que JARVIS necesita (lista objetivo)
- Lectura: info del proyecto, niveles, ejes, elementos por categoría, parámetros, tablas, vínculos, advertencias, vistas/planos.
- Escritura: fijar parámetros en lote, crear niveles/ejes/muros/columnas por coordenadas, crear vistas/planos, exportar IFC/NWC/PDF.
- Calidad: auditoría contra el EIR/IDS → [[Control de calidad de modelos BIM]].

## Prueba de aceptación
"Lista las 10 familias más usadas y los elementos sin `Codigo_Partida`" sobre un modelo de [[MOC Proyectos de Estudio]] (o Snowdon Towers).

↑ [[MOC JARVIS y MCP]] · Software: [[Revit]]
