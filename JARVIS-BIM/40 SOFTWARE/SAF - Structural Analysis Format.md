---
tipo: norma
tags: [software, estructural, formato-abierto]
aliases: [SAF, Structural Analysis Format]
actualizado: 2026-09-24
---
# SAF — Structural Analysis Format

Formato abierto basado en **Excel (.xlsx)** para intercambiar **modelos analíticos** estructurales (nudos, barras, superficies, apoyos, materiales, secciones, cargas, combinaciones). Impulsado inicialmente por SCIA/Nemetschek y adoptado por varios programas (SCIA Engineer, Dlubal RFEM/RSTAB, FEM-Design y plugins para Revit, entre otros). Especificación en saf.guide.

## Por qué es interesante
- Legible por humanos y por Python (pandas) → fácil de generar desde JARVIS.
- Complementa a IFC (`IfcStructuralAnalysisModel`, poco implementado) → [[Clases IFC principales]].

## Limitación
[[ETABS]]/[[SAP2000]] no lo usan de forma nativa; con ellos JARVIS usa la OAPI o las tablas de base de datos.

↑ [[Interoperabilidad entre software]] · [[MOC Ingenieria Estructural]]
