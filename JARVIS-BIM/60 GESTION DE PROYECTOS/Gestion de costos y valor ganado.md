---
tipo: gestion
tags: [gestion, costos, evm]
aliases: [EVM, Valor ganado, Earned Value, Gestion de costos]
actualizado: 2026-09-24
---
# Gestión de costos y valor ganado (EVM)

## Variables
| Sigla | Nombre | Definición |
|---|---|---|
| **BAC** | Presupuesto a la conclusión | Presupuesto total |
| **PV** | Valor planificado | Costo presupuestado del trabajo programado a la fecha |
| **EV** | Valor ganado | Costo presupuestado del trabajo **realizado** |
| **AC** | Costo real | Costo real incurrido |

## Indicadores
- CV = EV − AC · SV = EV − PV
- **CPI = EV / AC** · **SPI = EV / PV** (< 1 → sobrecosto / retraso)
- EAC = BAC / CPI (si el desempeño se mantiene) · ETC = EAC − AC · VAC = BAC − EAC
- TCPI = (BAC − EV) / (BAC − AC)

## Integración BIM 5D
Metrado del modelo × precios → PV por actividad ([[BIM 5D - Costos y metrados]]); avance real por elementos construidos (estado en el modelo) → EV; costos reales del ERP → AC. JARVIS calcula todo en [[Excel]] y alerta desviaciones.

## Perú
Valorizaciones mensuales, adicionales y deductivos → [[RFI y ordenes de cambio]].

↑ [[MOC Gestion de Proyectos]] · [[KPIs de proyectos BIM]]
