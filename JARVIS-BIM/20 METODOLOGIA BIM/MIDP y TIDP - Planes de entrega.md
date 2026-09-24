---
tipo: concepto
tags: [bim/metodologia, iso19650, midp, tidp]
aliases: [MIDP, TIDP, PEIM, PEIT, Plan de entrega de informacion]
actualizado: 2026-09-24
---
# MIDP y TIDP — Planes de entrega de información

| Plan | Quién | Qué contiene |
|---|---|---|
| **TIDP** (Task Information Delivery Plan) – *PEIT* | Cada equipo de tarea | Lista de contenedores que producirá: nombre, descripción, [[LOIN - Nivel de Informacion Necesaria]], fecha, autor, dependencias |
| **MIDP** (Master Information Delivery Plan) – *PEIM* | Parte designada principal | Consolidación de todos los TIDP alineada a hitos del proyecto |

## Campos típicos (tabla en Excel)
`Código de contenedor | Título | Disciplina | Tipo (M3, DR, SP…) | Hito | Fecha planificada | Responsable | Estado | Revisión | LOIN | Predecesores`

## Por qué importa
- Es la base del control de avance de la producción de información (planificado vs entregado) → [[KPIs de proyectos BIM]].
- Se vincula con el cronograma general → [[Gestion del cronograma]].

## JARVIS
- Genera el TIDP desde la lista de planos/modelos de [[Revit]] y [[AutoCAD]].
- Compara el MIDP con el contenido real del [[CDE - Entorno Comun de Datos]] y alerta retrasos ([[MCP Excel]]).

↑ [[BEP - Plan de Ejecucion BIM]] · [[ISO 19650-2 - Fase de desarrollo]]
