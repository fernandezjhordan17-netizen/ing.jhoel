---
tipo: norma
tags: [norma/peru, rne, estructural, concreto]
aliases: [E.060, Concreto armado Peru]
anio: 2009
actualizado: 2026-09-24
---
# E.060 — Concreto Armado

Norma basada en **ACI 318** (ediciones de la década de 2000) → comparar con [[ACI 318]].

## Combinaciones de carga (resistencia requerida U)
- U = 1.4 CM + 1.7 CV
- U = 1.25 (CM + CV) ± CS
- U = 0.9 CM ± CS
- Con viento: U = 1.25 (CM + CV ± CVi); U = 0.9 CM ± 1.25 CVi

## Factores de reducción de resistencia (φ)
| Solicitación | φ |
|---|---|
| Flexión sin carga axial | 0.90 |
| Tracción | 0.90 |
| Cortante y torsión | 0.85 |
| Compresión con estribos | 0.70 |
| Compresión con espirales | 0.75 |
| Aplastamiento | 0.70 |

## Otros puntos clave
- Acero de refuerzo grado 60 (fy = 420 MPa).
- Capítulo 21: **disposiciones especiales para diseño sísmico** (pórticos, muros, sistemas duales; confinamiento, nudos, diseño por capacidad en cortante).
- Control de deflexiones, fisuración, recubrimientos mínimos, longitudes de desarrollo y empalmes.

## En software
[[ETABS]] y [[SAFE]] no traen "E.060" como código de diseño nativo: se usa **ACI 318** ajustando combinaciones y factores φ (o hojas de cálculo propias). JARVIS debe **documentar el ajuste** en la memoria ([[Plantilla - Memoria de calculo]]).

↑ [[RNE - Reglamento Nacional de Edificaciones]] · [[MOC Ingenieria Estructural]]
