---
tipo: software
tags: [software/microsoft, datos, calculo]
aliases: [Microsoft Excel, XLSX, Hojas de calculo]
fabricante: Microsoft
formatos: [XLSX, XLSM, CSV]
actualizado: 2026-09-24
---
# Excel

La herramienta universal de ingeniería: metrados, presupuestos (APU), cronogramas simples, memorias de cálculo, TIDP/MIDP, COBie, control de RFIs.

## Automatización
| Vía | Cuándo |
|---|---|
| **openpyxl / pandas** (Python) | Leer/escribir archivos sin Excel abierto (servidor, rápido, seguro) |
| **xlwings / pywin32 (COM)** | Controlar el Excel abierto (recalcular fórmulas, macros) |
| **VBA** | Macros dentro del libro (`.xlsm`) |
| **Power Query** | Limpieza/unión de datos (reportes de ETABS, Revit) |
| **Office Scripts / Microsoft Graph** | Excel en la web / OneDrive |
| **MCP** | → [[MCP Excel]] |

## Plantillas que JARVIS debe manejar
Metrados → [[BIM 5D - Costos y metrados]] · MIDP/TIDP → [[MIDP y TIDP - Planes de entrega]] · Memoria de cálculo → [[Plantilla - Memoria de calculo]] · COBie → [[COBie]] · EVM → [[Gestion de costos y valor ganado]].

> [!tip] Tablas de ETABS
> ETABS permite exportar/importar tablas a Excel (edición interactiva de base de datos) — puente muy potente con [[ETABS]].

↑ [[MOC Software AEC]]
