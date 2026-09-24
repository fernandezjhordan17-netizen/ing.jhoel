---
tipo: jarvis
tags: [jarvis, agentes, multiagente]
aliases: [Subagentes JARVIS, Equipo de agentes]
actualizado: 2026-09-24
---
# JARVIS — Agentes especializados

JARVIS actúa como **orquestador** y delega en agentes con conocimiento y herramientas acotadas. En Claude Code se definen en `.claude/agents/` del repositorio (ya incluidos).

| Agente | Archivo | Conocimiento base | Herramientas MCP |
|---|---|---|---|
| **Coordinador BIM** | `jarvis-coordinador-bim.md` | [[MOC Metodologia BIM]], [[ISO 19650-2 - Fase de desarrollo]], [[Guia Nacional BIM Peru]] | Revit, Navisworks, BCF, Obsidian |
| **Ingeniero estructural** | `jarvis-estructural.md` | [[MOC Ingenieria Estructural]], [[E.030 - Diseno Sismorresistente]], [[E.060 - Concreto Armado]] | ETABS, SAP2000, SAFE, Robot, Excel |
| **Gestor de proyectos** | `jarvis-gestor-proyectos.md` | [[MOC Gestion de Proyectos]], [[PMBOK 7]], [[Last Planner System]] | Asana/Linear, Calendar, Gmail, Excel |
| **Auditor de calidad y normativa** | `jarvis-auditor-calidad.md` | [[Control de calidad de modelos BIM]], [[IDS - Information Delivery Specification]], [[RNE - Reglamento Nacional de Edificaciones]] | IfcOpenShell, Revit (lectura) |
| **Metrados y costos** *(futuro)* | — | [[BIM 5D - Costos y metrados]] | Revit, Excel |
| **Documentador** *(futuro)* | — | Plantillas de `80 PLANTILLAS` | Obsidian, Excel |

## Protocolo de orquestación
1. JARVIS entiende la petición y consulta la bóveda (MOC relevante).
2. Divide en subtareas y asigna agentes.
3. Cada agente devuelve resultados **con evidencias** (valores leídos, capturas, IDs de elementos, cita normativa).
4. JARVIS integra, pide confirmación para acciones de escritura ([[JARVIS - Seguridad y gobernanza]]) y registra en la bitácora.

↑ [[MOC JARVIS y MCP]] · [[JARVIS - Flujos de trabajo]]
