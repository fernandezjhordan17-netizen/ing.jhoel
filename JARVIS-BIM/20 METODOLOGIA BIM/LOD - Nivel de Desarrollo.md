---
tipo: concepto
tags: [bim/metodologia, lod]
aliases: [LOD, Level of Development, Nivel de desarrollo]
actualizado: 2026-09-24
---
# LOD — Level of Development

Definido por la **[[BIMForum LOD Specification]]** (EE.UU., basado en AIA E202/G202). Indica el **grado de confiabilidad** de la geometría e información de un elemento en una etapa.

| LOD | Significado | Ejemplo (columna de concreto) |
|---|---|---|
| **100** | Símbolo/masa genérica; información aproximada | Masa conceptual del edificio |
| **200** | Objeto genérico con tamaño, forma y ubicación aproximados | Columna genérica 40×40 aproximada |
| **300** | Objeto específico: tamaño, forma, ubicación y orientación precisos y medibles | Columna 40×60 f'c 280 en eje A-1 |
| **350** | LOD 300 + interfaces con otros sistemas (conexiones, soportes) | Columna con planchas, anclajes, pases |
| **400** | Listo para fabricación/instalación (detalle, armado) | Columna con refuerzo detallado, [[Tekla Structures]] |
| **500** | Verificado en campo ("as-built"); no es progresión geométrica | Columna según levantamiento |

> [!note] LOD vs LOG vs LOI
> - **LOG** (Level of Geometry) = detalle geométrico.
> - **LOI** (Level of Information) = datos no gráficos.
> - Europa/ISO reemplaza estos conceptos por el **[[LOIN - Nivel de Informacion Necesaria]]** (ISO 7817-1), que es más preciso: define la información **necesaria para un propósito**, no un "nivel" genérico.

## Uso práctico
- Tabla de LOD por elemento y etapa dentro del [[BEP - Plan de Ejecucion BIM]] o del [[EIR - Requisitos de Intercambio de Informacion]].
- El [[Control de calidad de modelos BIM]] verifica el cumplimiento (se puede automatizar con [[IDS - Information Delivery Specification]]).

↑ [[MOC Metodologia BIM]]
