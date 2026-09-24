---
tipo: mcp
tags: [mcp, jarvis, e030, python]
aliases: [jarvis-bim, Servidor MCP propio, jarvis-bim-mcp]
version: 0.1.0
actualizado: 2026-09-24
---
# MCP JARVIS BIM — servidor propio (`jarvis-bim`)

Primer servidor MCP construido para JARVIS (carpeta `jarvis-mcp/` del repositorio). SDK oficial de Python **mcp 2.x** (`MCPServer`), transporte stdio, 23 herramientas y 2 prompts. **52 pruebas automáticas** (cálculo, bóveda, IFC, puente ETABS simulado, servidor en memoria y por stdio).

## Herramientas
| Grupo | Herramientas | Base de conocimiento |
|---|---|---|
| Norma sísmica | `e030_parametros_sitio`, `e030_espectro` (+ Excel con gráfico), `e030_cortante_basal`, `e030_periodo_aproximado`, `e030_escalamiento_dinamico`, `e030_verificar_derivas`, `e030_restricciones`, `e030_opciones` | [[E.030 - Diseno Sismorresistente]] (ed. 2026) |
| Memoria | `boveda_buscar`, `boveda_leer`, `boveda_mapas`, `boveda_estadisticas` | [[Red neuronal de conocimiento]] |
| Gestión de información | `iso19650_validar_nombre`, `iso19650_validar_carpeta` | [[Nomenclatura de archivos y contenedores]] |
| Modelos | `ifc_resumen`, `ifc_elementos`, `ifc_propiedades` | [[IFC - ISO 16739]], [[Clases IFC principales]] |
| Estructuras | `csi_estado`, `csi_leer_tabla`, `csi_derivas`, `csi_reacciones_base`, `csi_crear_espectro_e030`, `csi_correr_analisis` | [[MCP CSI - ETABS SAP2000 SAFE]] |

Prompts: `flujo_sismico_e030` (receta completa del análisis) y `consulta_normativa` (respuesta con cita).

## Ejemplo verificado a mano
Zona 4, S2 con Vs30 = 420 m/s, categoría C, dual regular (R = 7), T = 0,62 s, P = 12 000 kN:
S = 1,065 · TP = 0,53 s · TL = 2,175 s · C = 2,5·0,53/0,62 = 2,137 · **V = 0,45·1,0·2,137·1,065/7 · 12 000 = 1 755,8 kN** · k = 1,06.

## Seguridad incorporada ([[JARVIS - Seguridad y gobernanza]])
- Herramientas marcadas como **solo lectura** o **escritura** (anotaciones MCP).
- ETABS: hilo COM único, se adjunta al programa abierto, **dry-run por defecto**, **respaldo** del `.EDB` antes de escribir, rechaza modelos bloqueados (no borra resultados).
- Toda escritura queda en el **Diario JARVIS** (`00 INICIO/Diario JARVIS/AAAA-MM-DD.md`).
- Si la norma lo impide (A1 sin aislamiento en Z3–Z4, EMDL > 5 pisos, S5, Z4-S4), el cálculo se **bloquea** con el artículo correspondiente.
- Los resultados que usan valores sin confirmar en el PDF 2026 traen el campo `pendientes`.

## Instalación
```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\07_instalar_jarvis_mcp.ps1
```
Luego reinicia Claude Desktop y prueba: *"JARVIS, verifica si un hospital A1 en Zona 4 con sistema dual cumple la E.030"*.

## Próximas versiones
1. Actualizar `e030.py` con el PDF oficial 2026 (Tabla 6 de C, Tabla 14 de derivas).
2. `e060_*`: combinaciones de carga y diseño de secciones → [[E.060 - Concreto Armado]].
3. `metrados_*`: mapeo partida ↔ categoría desde IFC/Revit → [[Norma Tecnica de Metrados]].
4. Herramientas de Revit y Navisworks mediante los servidores de [[MCP Revit]] y [[MCP Navisworks]].

↑ [[MOC JARVIS y MCP]] · [[JARVIS - Arquitectura]] · [[Hoja de ruta JARVIS]]
