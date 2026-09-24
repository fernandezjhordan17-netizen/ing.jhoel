---
tipo: concepto
tags: [bim/metodologia, dimensiones, 4d, gestion]
aliases: [4D, Simulacion constructiva]
actualizado: 2026-09-24
---
# BIM 4D — Planificación

## Qué es
Vincular elementos del modelo con actividades del cronograma para **simular la secuencia constructiva**.

## Flujo típico
1. Cronograma en MS Project / Primavera P6 ([[Gestion del cronograma]]).
2. Parámetro común en el modelo (p. ej. `Codigo_Actividad`, `Fase`, `Sector_Vaciado`).
3. Vinculación en [[Navisworks]] **TimeLiner** (reglas automáticas por parámetro o sets de búsqueda).
4. Simulación y revisión: logística, grúas, accesos, interferencias temporales.
5. Actualización semanal con avances reales ([[Last Planner System]]).

## Usos
- Revisión de constructibilidad, planificación de sitio ("site utilization"), comunicación con el cliente, control de avance (planificado vs real).

## Normas / referencias
- IFC soporta procesos: `IfcTask`, `IfcWorkSchedule`, `IfcRelSequence` → [[Clases IFC principales]].
- Perú: los [[Usos BIM]] de planificación se establecen en el [[EIR - Requisitos de Intercambio de Informacion]] según la [[Guia Nacional BIM Peru]].

## JARVIS
- Lee el XML de MS Project / XER de P6 y propone reglas de vínculo; ejecuta TimeLiner vía [[MCP Navisworks]].

↑ [[Dimensiones BIM]]
