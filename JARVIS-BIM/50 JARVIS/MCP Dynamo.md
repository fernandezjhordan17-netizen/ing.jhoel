---
tipo: mcp
tags: [mcp, software/autodesk, dynamo]
aliases: [DynamoMCP, Dynamo MCP]
actualizado: 2026-09-24
---
# MCP — Dynamo

## Estado
- **Dynamo 4.2 (incluido en Revit 2027.3)** integra el *Autodesk Assistant* como panel y **DynamoMCP**, que permite al asistente leer y editar el grafo: colocar y conectar nodos, fijar entradas, ejecutar, leer advertencias, agrupar/anotar y guardar. Dentro de Revit se habla con el Assistant embebido en Revit.
- Autodesk tiene además un programa alfa de "Agentic Node" para Dynamo (feedback.autodesk.com).

> [!todo] Verificar
> Si DynamoMCP puede usarse desde **clientes externos** (Claude Desktop) o solo desde Autodesk Assistant. Revisar notas de versión de Dynamo 4.2 en GitHub (DynamoDS/Dynamo wiki) y el foro de Dynamo.

## Alternativas para JARVIS
1. **Generar archivos `.dyn`** (JSON) por código y ejecutarlos con **Dynamo Player** — el grafo queda versionado en git.
2. Ejecutar la lógica directamente con la API de Revit vía [[MCP Revit]] (sin Dynamo).
3. Nodo Python dentro de Dynamo que llama a un servicio local (avanzado).

## Uso típico
"Crea un grafo que numere las habitaciones por nivel de izquierda a derecha" → JARVIS genera el `.dyn`, lo explica y lo guarda en la bóveda.

↑ [[MOC JARVIS y MCP]] · Software: [[Dynamo]]
