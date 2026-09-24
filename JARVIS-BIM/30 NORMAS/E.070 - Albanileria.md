---
tipo: norma
tags: [norma/peru, rne, estructural, albanileria]
aliases: [E.070, Albanileria confinada]
actualizado: 2026-09-24
---
# E.070 — Albañilería

Diseño de **albañilería confinada** (la más usada en vivienda peruana) y **armada**.

## Criterios clave
- Unidades de albañilería (clases), morteros, resistencia f'm y v'm.
- **Densidad mínima de muros** por dirección: Σ(L·t)/Ap ≥ Z·U·S·N / 56 (N = número de pisos).
- Esfuerzo axial máximo en muros; control de fisuración ante sismo moderado; diseño de columnas y vigas de confinamiento ante sismo severo.
- Coeficiente R0 = 3 y deriva máxima 0.005 → [[E.030 - Diseno Sismorresistente]].

## BIM
Muros portantes con parámetro `LoadBearing = TRUE` (`Pset_WallCommon`) para distinguirlos de tabiques → [[Clases IFC principales]]. JARVIS puede calcular la densidad de muros desde el modelo de [[Revit]].

↑ [[RNE - Reglamento Nacional de Edificaciones]] · [[MOC Ingenieria Estructural]]
