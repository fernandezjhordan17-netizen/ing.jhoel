---
tipo: norma
tags: [norma/peru, rne, estructural, cargas]
aliases: [E.020, Norma de cargas]
actualizado: 2026-09-24
---
# E.020 — Cargas

Define **cargas muertas, vivas, de viento y nieve** mínimas.

## Valores de referencia frecuentes (verificar tabla vigente)
| Uso (carga viva repartida) | kPa | kgf/m² |
|---|---|---|
| Vivienda | 2.0 | 200 |
| Oficinas (ambientes) | 2.5 | 250 |
| Aulas (centros educativos) | 2.5 | 250 |
| Corredores y escaleras de centros educativos | 4.0 | 400 |
| Tiendas | 5.0 | 500 |
| Estacionamientos (vehículos de pasajeros) | 2.5 | 250 |
| Azoteas planas | 1.0 | 100 |

| Peso unitario | kN/m³ | kgf/m³ |
|---|---|---|
| Concreto armado | 24 | 2400 |
| Albañilería de unidades sólidas | 18 | 1800 |
| Acero | 78.5 | 7850 |

> [!warning] Usa siempre la tabla oficial de la norma vigente; estos valores son orientativos para aprendizaje.

## En software
- Patrones de carga en [[ETABS]]/[[SAP2000]]/[[SAFE]]: `CM` (muerta), `CV` (viva), `CVT` (viva de techo), `SX`, `SY` (sismo).
- Combinaciones según [[E.060 - Concreto Armado]].
- Masa sísmica según [[E.030 - Diseno Sismorresistente]].

↑ [[RNE - Reglamento Nacional de Edificaciones]] · [[MOC Ingenieria Estructural]]
