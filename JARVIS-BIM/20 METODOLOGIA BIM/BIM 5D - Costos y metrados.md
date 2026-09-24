---
tipo: concepto
tags: [bim/metodologia, dimensiones, 5d, costos]
aliases: [5D, Metrados BIM, Quantity takeoff, QTO]
actualizado: 2026-09-24
---
# BIM 5D — Costos y metrados

## Qué es
Extraer **metrados (cantidades)** del modelo y combinarlos con precios unitarios para presupuestos, valorizaciones y control de costos.

## Flujo recomendado (Perú)
1. Estructura de partidas según la norma de metrados vigente (Norma Técnica de Metrados para obras de edificación – referencia MVCS) y códigos del presupuesto (S10 u otro).
2. Parámetro de **código de partida** en cada tipo/elemento del modelo.
3. Extracción: tablas de planificación en [[Revit]], Quantification en [[Navisworks]], `Qto_*BaseQuantities` en [[IFC - ISO 16739]].
4. Exportar a [[Excel]] → cruce con análisis de precios unitarios.
5. Control: metrado modelo vs metrado ejecutado → [[Gestion de costos y valor ganado]].

> [!tip] Precisión
> El metrado del modelo es tan bueno como el modelado: acero de refuerzo, encofrados y desperdicios suelen calcularse con reglas adicionales (Dynamo/Excel).

## Automatización JARVIS
- [[MCP Revit]] → leer cantidades por categoría/partida.
- [[MCP Excel]] → llenar la hoja de presupuesto.
- Flujo "Metrados 5D" en [[JARVIS - Flujos de trabajo]].

↑ [[Dimensiones BIM]] · [[KPIs de proyectos BIM]]
