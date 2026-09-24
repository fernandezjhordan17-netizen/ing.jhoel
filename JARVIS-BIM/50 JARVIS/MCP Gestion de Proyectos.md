---
tipo: mcp
tags: [mcp, gestion, integraciones]
aliases: [MCP PM, Integraciones de gestion]
actualizado: 2026-09-24
---
# MCP — Gestión de proyectos

## Conectores disponibles en Claude
Tu cuenta de Claude puede conectar servicios como **Asana, Linear, Google Calendar, Gmail, Google Drive y Slack**. JARVIS los usa para:
| Servicio | Uso |
|---|---|
| Asana / Linear | Tareas por incidencia de coordinación, RFIs, entregables del MIDP |
| Google Calendar | Reuniones de coordinación, hitos, recordatorios de entregas |
| Gmail | Borradores de RFIs, transmittals, actas (siempre como **borrador**, tú envías) |
| Google Drive | Documentos del proyecto, CDE ligero |
| Slack | Avisos al equipo |

## Cronogramas
- **MS Project** (XML/MSPDI) y **Primavera P6** (XER/XML): leer con Python (p. ej. `xerparser`) mediante un servidor MCP propio o scripts → [[Gestion del cronograma]].

## CDE en la nube
ACC/BIM 360 (APS), Trimble Connect → [[Autodesk Platform Services y ACC]], [[CDE - Entorno Comun de Datos]].

## Flujos
- "Lunes de coordinación": Navisworks → BCF → Asana → Calendar → acta en Obsidian ([[JARVIS - Flujos de trabajo]]).
- "Reporte semanal": KPIs + riesgos + RFIs → [[KPIs de proyectos BIM]].

↑ [[MOC JARVIS y MCP]] · [[MOC Gestion de Proyectos]]
