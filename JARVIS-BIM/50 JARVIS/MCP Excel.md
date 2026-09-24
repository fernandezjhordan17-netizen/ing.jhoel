---
tipo: mcp
tags: [mcp, software/microsoft, excel]
aliases: [Excel MCP]
actualizado: 2026-09-24
---
# MCP — Excel

## Opción recomendada
**`haris-musa/excel-mcp-server`** (MIT, Python ≥ 3.10, basado en openpyxl): crea, lee y modifica libros **sin necesitar Excel instalado** — fórmulas, formato, gráficos, tablas dinámicas, tablas, validación, formato condicional.
- Instalación: `pip install excel-mcp-server` o ejecutar con `uvx excel-mcp-server stdio`.

## Cuándo necesitas Excel "vivo"
Si hay que **recalcular** fórmulas complejas o ejecutar macros, usar un servidor basado en **xlwings/COM** (propio) — openpyxl no calcula fórmulas.

## Primer servidor a conectar
Es el de **menor riesgo** (trabaja sobre archivos). Ideal para la Fase 2 de la [[Hoja de ruta JARVIS]].

## Plantillas
Metrados ([[BIM 5D - Costos y metrados]]), MIDP ([[MIDP y TIDP - Planes de entrega]]), control de RFIs ([[RFI y ordenes de cambio]]), EVM ([[Gestion de costos y valor ganado]]).

↑ [[MOC JARVIS y MCP]] · Software: [[Excel]]
