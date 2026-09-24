---
tipo: concepto
tags: [bim/metodologia, coordinacion, clash]
aliases: [Clash detection, Deteccion de interferencias, Coordinacion 3D]
actualizado: 2026-09-24
---
# Coordinación BIM y detección de interferencias

## Tipos de interferencia
| Tipo | Ejemplo |
|---|---|
| **Dura (hard clash)** | Tubería atravesando una viga |
| **Blanda / holgura (clearance)** | Ducto a menos de 5 cm del cielo raso; espacio de mantenimiento |
| **Duplicados** | Dos columnas idénticas superpuestas |
| **4D (workflow clash)** | Dos actividades usando el mismo espacio al mismo tiempo |

## Proceso (ciclo semanal)
1. Cada disciplina publica su modelo en estado **Compartido** del [[CDE - Entorno Comun de Datos]].
2. [[Federacion de modelos]] en [[Navisworks]] (NWF → NWD).
3. **Matriz de choques** (qué disciplina contra cuál, tolerancias).
4. Ejecutar pruebas en Clash Detective; **agrupar** choques (por nivel, sistema, elemento causante).
5. Asignar responsables y exportar incidencias a **[[BCF - BIM Collaboration Format]]**.
6. Reunión de coordinación ([[Plantilla - Reunion de coordinacion]]).
7. Correcciones en modelos nativos ([[Revit]], [[Tekla Structures]]) y nueva corrida.
8. Registrar KPIs: choques abiertos/cerrados por semana ([[KPIs de proyectos BIM]]).

## Prioridad de disciplinas (regla típica)
Estructura > Drenaje por gravedad > Ductos HVAC grandes > Bandejas eléctricas > Tuberías a presión > Otros.

## JARVIS
- Corre pruebas, agrupa choques con IA y redacta el reporte ([[MCP Navisworks]] → [[Plantilla - Reporte de interferencias]]).
- Flujo en [[JARVIS - Flujos de trabajo]].

## Sin licencia
Revisión y comentarios con [[Visores BIM gratuitos]] (Navisworks Freedom, BIMcollab ZOOM, Dalux, BIMvision, Trimble Connect).

↑ [[MOC Metodologia BIM]]
