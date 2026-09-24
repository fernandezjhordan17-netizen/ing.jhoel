---
tipo: recurso
tags: [recurso, ia, revit, dynamo]
aliases: [IA para BIM, BIBIM, NotebookLM, Veras]
actualizado: 2026-09-24
---
# Herramientas de IA para BIM

| Herramienta | Costo | Uso |
|---|---|---|
| **Claude** (y otros LLM) | Freemium | Escribir scripts de **Dynamo** y **pyRevit**, redactar EIR/PEB, revisar normas; con MCP opera los programas → [[JARVIS - Arquitectura]] |
| **NotebookLM** | Gratis | Resumir documentos largos (ISO 19650, un BEP de 80 páginas) con citas |
| **BIBIM** (`SquareZero-Inc/bibim-revit`) | Gratis, open source | Agente dentro de Revit: lenguaje natural → **código C#** validado (Roslyn) y ejecutado; versiones Revit 2022–2027; trae tu propia clave de Claude. Variante para Dynamo (`bibim-dynamo`, genera Python) |
| **Veras** (EvolveLAB) | De pago (prueba de 15 días) | Renders con IA dentro de Revit |
| **Autodesk Assistant** | Incluido (Revit/Dynamo 2027) | Asistente oficial con DynamoMCP → [[MCP Dynamo]] |

## Cómo encajan con JARVIS
- **BIBIM** es un excelente **complemento** (y referencia de diseño): su patrón *generar código → validar → ejecutar* es el mismo que JARVIS debe seguir para acciones complejas en Revit, con las reglas de [[JARVIS - Seguridad y gobernanza]].
- **NotebookLM** sirve para estudiar; JARVIS guarda lo aprendido en la bóveda (memoria permanente) → [[Red neuronal de conocimiento]].

> [!warning] Código generado por IA
> Ejecutarlo siempre primero en una **copia** del modelo; revisar transacciones y elementos afectados.

↑ [[Caja de herramientas BIM]] · [[IA y Machine Learning en AEC]]
