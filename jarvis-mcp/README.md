# jarvis-bim-mcp — servidor MCP propio de JARVIS

Herramientas de ingeniería que Claude (Desktop o Code) puede usar directamente:

| Grupo | Herramientas | Qué hace |
|---|---|---|
| **E.030-2026** | `e030_opciones`, `e030_parametros_sitio`, `e030_espectro`, `e030_cortante_basal`, `e030_periodo_aproximado`, `e030_escalamiento_dinamico`, `e030_verificar_derivas`, `e030_restricciones` | Cálculo sísmico según la RM 183-2026-VIVIENDA: S/TP/TL interpolados por Vs30, verificación de Ts, espectro Sa/g (exportable a Excel con gráfico), V = ZUCS/R·P con C/R ≥ 0,11, distribución en altura, escalamiento 80/90 %, derivas, Tablas 9 y 13 |
| **E.060** | `e060_combinaciones`, `e060_flexion_viga`, `e060_cortante_viga`, `e060_columna_axial` | Concreto armado verificado contra el texto oficial (9.2, 9.3.2, 10.3.4, 10.3.6, 10.5.2, 10.9.1, 11.3.1.1, 11.5.5, 11.5.6.2, 11.5.7.9) |
| **Metrados** | `ifc_metrados` | Cantidades Qto por clase/piso con partidas sugeridas, acero en kg, Excel y corrección de unidades mal exportadas |
| **Bóveda** | `boveda_buscar`, `boveda_leer`, `boveda_mapas`, `boveda_estadisticas` | Búsqueda BM25 + proximidad; devuelve la **sección exacta** de los textos oficiales (p. ej. E.060 10.5.2) |
| **ISO 19650** | `iso19650_validar_nombre`, `iso19650_validar_carpeta` | Nomenclatura de contenedores |
| **IFC** | `ifc_resumen`, `ifc_elementos`, `ifc_propiedades` | Lectura de modelos con IfcOpenShell |
| **ETABS / SAP2000** | `csi_estado`, `csi_leer_tabla`, `csi_derivas`, `csi_reacciones_base`, `csi_crear_espectro_e030`, `csi_crear_combinaciones_e060`, `csi_correr_analisis` | CSI OAPI por COM en hilo dedicado; escritura con dry-run y respaldo del .EDB |

Prompts incluidos: `flujo_sismico_e030`, `consulta_normativa`.

## Instalación (Windows)
```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\07_instalar_jarvis_mcp.ps1
```
Crea `jarvis-mcp\.venv`, instala el paquete, ejecuta las pruebas y agrega `jarvis-bim` a `%APPDATA%\Claude\claude_desktop_config.json` (con respaldo). Reinicia Claude Desktop.

Manual:
```powershell
py -3 -m venv jarvis-mcp\.venv
jarvis-mcp\.venv\Scripts\pip install -e "jarvis-mcp[todo,test]"
jarvis-mcp\.venv\Scripts\python -m pytest jarvis-mcp\tests
```

## Seguridad
- Lectura por defecto; escritura en ETABS solo con `dry_run=false` / `confirmar=true`, respaldo previo y registro en `JARVIS-BIM/00 INICIO/Diario JARVIS/`.
- Todo en local (stdio); ningún modelo sale del PC.
- El puente ETABS es **experimental**: pruébalo en una copia del modelo.

## Pendientes normativos
Los resultados incluyen el campo `pendientes` cuando usan valores no confirmados en el PDF 2026 (expresión de C en T > TP, Tabla 14 de derivas y factores 0,75R/0,85R). Cuando descargues el texto oficial, actualiza `src/jarvis_bim/e030.py` y las pruebas.

Requiere Python ≥ 3.10 y el SDK oficial `mcp` 2.x (`MCPServer`).
