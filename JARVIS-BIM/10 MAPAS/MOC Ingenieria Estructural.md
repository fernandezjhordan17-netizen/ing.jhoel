---
tipo: moc
tags: [moc, estructural]
aliases: [Mapa Estructural]
actualizado: 2026-09-24
---
# 🏗️ MOC — Ingeniería estructural

## Normas peruanas (RNE)
- [[RNE - Reglamento Nacional de Edificaciones]]
- [[E.020 - Cargas]] → [[E.030 - Diseno Sismorresistente]] → [[E.050 - Suelos y Cimentaciones]]
- [[E.060 - Concreto Armado]] · [[E.070 - Albanileria]] · [[E.090 - Estructuras Metalicas]]
- [[E.031 - Aislamiento Sismico]] · [[Otras normas estructurales del RNE]] · Textos completos: [[Indice de textos oficiales]]

## Normas internacionales
- [[ACI 318]] · [[ASCE 7]] · [[AISC 360 y 341]] · [[Eurocodigos]]

## Software
- [[ETABS]] (edificios) · [[SAP2000]] (general) · [[SAFE]] (losas/cimentación) · [[Robot Structural Analysis]] · [[Tekla Structures]] (detallado)
- Puente BIM ↔ análisis: [[Interoperabilidad entre software]] · [[SAF - Structural Analysis Format]]

## Flujo típico (que JARVIS automatizará)
```mermaid
flowchart LR
  A[Revit modelo físico] -->|CSiXRevit / IFC / link| B[ETABS modelo analítico]
  B --> C[Cargas E.020 + espectro E.030]
  C --> D[Análisis modal espectral]
  D --> E[Verificación derivas y cortante basal]
  E --> F[Diseño E.060 / ACI 318]
  F --> G[SAFE: losas y cimentación]
  G --> H[Excel: memoria y metrados]
  H --> I[Revit: actualizar secciones y armado]
```
Detalle en [[JARVIS - Flujos de trabajo]] y plantilla [[Plantilla - Memoria de calculo]].

## MCP estructurales
- [[MCP CSI - ETABS SAP2000 SAFE]] · [[MCP Robot Structural Analysis]] · [[MCP Tekla Structures]]
