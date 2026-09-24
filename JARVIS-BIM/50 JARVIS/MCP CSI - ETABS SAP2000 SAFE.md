---
tipo: mcp
tags: [mcp, software/csi, estructural]
aliases: [ETABS MCP, SAP2000 MCP, SAFE MCP, CSI MCP]
actualizado: 2026-09-24
---
# MCP — CSI: ETABS, SAP2000 y SAFE

## Opciones
| Repositorio | Programa | Notas |
|---|---|---|
| `mdvaleed7/ETABS-mcp` | ETABS v19–v22 | Python 3.10+, FastMCP + `comtypes` (ETABSv1 COM); se adjunta a ETABS abierto o lanza uno nuevo; **69 herramientas en 13 categorías** (modelo, geometría, propiedades, cargas, análisis, diseño, sísmico, tablas); MIT. Sus flujos sísmicos usan la norma india IS 1893 → **adaptar a [[E.030 - Diseno Sismorresistente]]** |
| `Aaradhya-Dev-Tamrakar/sap2000-mcp` | SAP2000 | Puente universal vía OAPI COM |
| `PriyankGodhat/etabs-mcp-server-local-embeddings` | Documentación ETABS | Búsqueda semántica local en manuales (ChromaDB) |
| SAFE | — | No se encontró un servidor MCP público maduro → **construir** con el mismo patrón (OAPI) |

## Herramientas JARVIS a construir/adaptar (E.030/E.060)
| Herramienta | Qué hace |
|---|---|
| `crear_espectro_e030(Z, U, S, TP, TL, R)` | Crea función de espectro de usuario |
| `asignar_masa_sismica(categoria)` | CM + % CV según categoría |
| `correr_analisis()` | Ejecuta y reporta advertencias |
| `derivas(caso, limite)` | Lee Story Drifts, multiplica por 0.75R/0.85R, compara con el límite |
| `cortante_basal()` | Compara dinámico vs estático y propone factor de escala |
| `tabla(nombre)` | Lee cualquier tabla (`DatabaseTables`) → [[Excel]] |
| `exportar_safe(piso)` | Exporta losa/cimentación a [[SAFE]] |

> [!warning] Hilo único
> La OAPI es COM: usa un hilo trabajador dedicado ([[Patrones de puente MCP para software de escritorio]]). Nunca ejecutes dos análisis en paralelo sobre la misma instancia.

## Prueba de aceptación
Modelo de 5 pisos generado por JARVIS desde una tabla de Excel, analizado, con derivas y cortante verificados y exportados a una memoria ([[Plantilla - Memoria de calculo]]).

↑ [[MOC JARVIS y MCP]] · Software: [[ETABS]] · [[SAP2000]] · [[SAFE]]
