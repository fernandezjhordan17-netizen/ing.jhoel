---
tipo: software
tags: [software/autodesk, nube, api, cde]
aliases: [APS, Autodesk Forge, ACC, Autodesk Construction Cloud, BIM 360, Autodesk Docs]
fabricante: Autodesk
actualizado: 2026-09-24
---
# Autodesk Platform Services (APS) y Autodesk Construction Cloud (ACC)

## ACC (CDE en la nube)
Autodesk Docs (gestión documental con flujos de aprobación), Build (obra: incidencias, RFIs, submittals, checklists), Model Coordination (interferencias en la nube), Cost, Takeoff. Es un [[CDE - Entorno Comun de Datos]] ampliamente usado.

## APS (antes Forge) — APIs
| API | Uso |
|---|---|
| Authentication (OAuth 2, PKCE) | Tokens de 2 y 3 patas |
| Data Management | Hubs, proyectos, carpetas, versiones |
| Model Derivative + Viewer | Traducir RVT/DWG/IFC/NWD y visualizar en web |
| **AEC Data Model** (GraphQL) | Datos granulares de modelos Revit publicados en ACC |
| **Design Automation** | Ejecutar Revit/AutoCAD/Inventor/3ds Max sin interfaz en la nube |
| ACC APIs | Issues, RFIs, Submittals, Cost, Model Coordination, Checklists |
| Webhooks | Eventos (nueva versión, nueva incidencia) |

## MCP en la nube
Autodesk publica ejemplos oficiales de servidores MCP sobre APS (p. ej. `aps-aecdm-mcp-dotnet` con AEC Data Model + Viewer) y la comunidad ofrece servidores para ACC (proyectos, archivos, incidencias, RFIs) → [[MCP Revit]], [[MCP Gestion de Proyectos]].

↑ [[MOC Software AEC]]
