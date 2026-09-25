---
tipo: norma
tags: [norma/peru, rne, sostenibilidad, instalaciones, 6d]
aliases: [EM.110, Confort termico y luminico, Eficiencia energetica RNE]
actualizado: 2026-09-25
---
# EM.110 — Confort Térmico y Lumínico con Eficiencia Energética

Norma del RNE (Título III.4). Resumen verificado contra el texto oficial → [[Texto oficial - EM110]].

## Aplicación (numeral 3)
Se aplica **de forma optativa** a edificaciones nuevas y a ampliaciones, remodelaciones o acondicionamientos incluidos en las modalidades B, C y D de la Ley 29090. Un EIR, un municipio o una certificación pueden volverla exigible.

## Zonificación bioclimática (numeral 6, Tabla 1)
Nueve zonas: **1 Desértico costero · 2 Desértico · 3 Interandino bajo · 4 Mesoandino · 5 Altoandino · 6 Nevado · 7 Ceja de montaña · 8 Subtropical húmedo · 9 Tropical húmedo**. La zona del proyecto sale del Anexo 1(A) por provincia; se puede cambiar solo sustentándolo con información oficial del SENAMHI (Anexo 1(B)).

## Requisitos
| Numeral | Requisito |
|---|---|
| 7.1 | **Transmitancia térmica máxima U** (W/m²·K) de muro, techo y piso por zona bioclimática (**Tabla 2**) |
| 7.2 | Control de **condensaciones** (metodología del Anexo 4) |
| 7.3 | **Permeabilidad al aire** de carpinterías de ventanas por zona (Tabla 3, Anexo 5) |
| 8 | **Confort lumínico** (factor de luz diurna, metodología del Anexo 6) |
| Anexos 2–3 | Cálculo de confort térmico y propiedades higrotérmicas de materiales |
| Anexo 7 | Control solar (informativo) |

> [!warning] Toma los valores U de la **Tabla 2** directamente del texto oficial: al extraerlos del PDF, las columnas de la tabla se desordenan.

## En BIM
- Propiedades térmicas de materiales y capas en [[Revit]] → U de muros y techos calculado por el modelo.
- Zona bioclimática como parámetro del proyecto; verificación automática de U ≤ U máx por elemento (futura herramienta de JARVIS).
- Contexto: [[BIM 6D - Sostenibilidad]] · [[Codigo Tecnico de Construccion Sostenible]] · [[EM.010 - Instalaciones Electricas Interiores]]

↑ [[RNE - Reglamento Nacional de Edificaciones]] · [[MOC Normas y Estandares]]
