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

## ✅ Verificado contra el texto oficial ([[Texto oficial - E060]])
| Tema | Sección |
|---|---|
| Combinaciones U (9-1 a 9-7); no combinar sismo y viento | 9.2.1–9.2.5 |
| Factores φ | 9.3.2.1–9.3.2.5 |
| β1 = 0,85 (17–28 MPa) → 0,65 (≥ 56 MPa) | 10.2.7.3 |
| As ≤ 0,75·Asb | 10.3.4 |
| φPn máx = 0,80·φ·Po (estribos) / 0,85·φ·Po (espiral) | 10.3.6.1–10.3.6.2 |
| As mín = 0,22·√f'c/fy·bw·d (MPa) | 10.5.2 (ec. 10-3) |
| Cuantía de columnas 1 %–6 % | 10.9.1 |
| Vc = 0,17·√f'c·bw·d | 11.3.1.1 |
| s ≤ d/2 ≤ 600 mm; mitad si Vs > 0,33·√f'c·bw·d | 11.5.5.1, 11.5.5.3 |
| Av mín = 0,062·√f'c·bw·s/fyt ≥ 0,35·bw·s/fyt | 11.5.6.2 |
| Vs ≤ 0,66·√f'c·bw·d | 11.5.7.9 |

Herramientas que lo aplican: `e060_*` en [[MCP JARVIS BIM - Servidor propio]].

## En software
[[ETABS]] y [[SAFE]] no traen "E.060" como código de diseño nativo: se usa **ACI 318** ajustando combinaciones y factores φ (o hojas de cálculo propias). JARVIS debe **documentar el ajuste** en la memoria ([[Plantilla - Memoria de calculo]]).

↑ [[RNE - Reglamento Nacional de Edificaciones]] · [[MOC Ingenieria Estructural]]
