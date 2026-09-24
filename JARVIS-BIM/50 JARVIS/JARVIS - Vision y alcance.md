---
tipo: jarvis
tags: [jarvis, vision]
aliases: [Vision JARVIS, Alcance JARVIS]
actualizado: 2026-09-24
---
# JARVIS — Visión y alcance

> **Visión**: un asistente/agente de ingeniería que conoce la metodología BIM y la normativa, recuerda todos tus proyectos y **opera tus programas** (Revit, Dynamo, AutoCAD, Civil 3D, Navisworks, Robot, ETABS, SAP2000, SAFE, Tekla, Excel) mediante **MCP**, siempre bajo tu supervisión.

## Lo que JARVIS hará
| Capacidad | Ejemplo |
|---|---|
| **Saber** | "¿Qué deriva máxima permite la E.030 para concreto armado y qué artículo es?" → [[E.030 - Diseno Sismorresistente]] |
| **Recordar** | "¿Qué acordamos en la última reunión de coordinación del proyecto X?" → [[MCP Obsidian - Memoria de JARVIS]] |
| **Ver** | "¿Cuántas columnas sin `Codigo_Partida` hay en el modelo estructural?" → [[MCP Revit]] |
| **Calcular** | "Genera el espectro E.030 (Z4, S2, U=1.0, R=7) y corre el análisis en ETABS" → [[MCP CSI - ETABS SAP2000 SAFE]] |
| **Coordinar** | "Corre la matriz de choques y crea tareas en Asana para cada responsable" → [[MCP Navisworks]] + [[MCP Gestion de Proyectos]] |
| **Documentar** | "Redacta la memoria de cálculo con los resultados" → [[Plantilla - Memoria de calculo]] |
| **Gestionar** | "Resumen semanal de avance, riesgos y RFIs abiertos" → [[KPIs de proyectos BIM]] |

## Lo que JARVIS NO hará
- Firmar ni asumir la responsabilidad profesional.
- Modificar modelos publicados/contractuales sin confirmación.
- Inventar resultados numéricos: siempre los **lee** del software o los **calcula** con herramientas verificables.
Ver [[JARVIS - Seguridad y gobernanza]].

## Principios de diseño
1. **Conocimiento primero** (esta bóveda) → 2. **Lectura** → 3. **Escritura controlada** → 4. **Orquestación** ([[Hoja de ruta JARVIS]]).
2. **Estándares abiertos** siempre que se pueda ([[OpenBIM]]).
3. **Trazabilidad**: toda acción queda en el [[Plantilla - Diario JARVIS]].
4. **Modularidad**: un servidor MCP por programa ([[JARVIS - Arquitectura]]).

↑ [[MOC JARVIS y MCP]]
