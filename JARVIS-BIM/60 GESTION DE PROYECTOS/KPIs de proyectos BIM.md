---
tipo: gestion
tags: [gestion, kpi, bim]
aliases: [KPIs BIM, Indicadores BIM, Metricas]
actualizado: 2026-09-24
---
# KPIs de proyectos BIM

| Área | KPI | Fórmula / fuente |
|---|---|---|
| Información | % entregables a tiempo | Entregados a tiempo / planificados en el MIDP → [[MIDP y TIDP - Planes de entrega]] |
| Información | % cumplimiento IDS | Elementos que pasan / aplicables → [[IDS - Information Delivery Specification]] |
| Coordinación | Choques abiertos / cerrados por semana | [[Navisworks]] / BCF |
| Coordinación | Tiempo medio de resolución de choques | Fecha cierre − fecha apertura |
| Gestión | RFIs por semana y por causa | [[RFI y ordenes de cambio]] |
| Producción | PPC | [[Last Planner System]] |
| Costo | CPI | [[Gestion de costos y valor ganado]] |
| Plazo | SPI | [[Gestion de costos y valor ganado]] |
| Calidad | No conformidades abiertas | [[Gestion de la calidad]] |
| Seguridad | Índices de frecuencia/gravedad | [[Seguridad y salud en obra]] |
| JARVIS | Horas ahorradas por automatización | Bitácora [[Plantilla - Diario JARVIS]] |

## Tablero
```dataview
TABLE ppc, cpi, spi, choques_abiertos, rfis_abiertos
FROM "70 PROYECTOS/Proyectos activos"
```

↑ [[MOC Gestion de Proyectos]] · [[VDC - Diseno y Construccion Virtual]]
