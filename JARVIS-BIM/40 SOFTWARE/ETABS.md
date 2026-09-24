---
tipo: software
tags: [software/csi, estructural, analisis]
aliases: [CSI ETABS, EDB, E2K]
fabricante: Computers and Structures, Inc. (CSI)
formatos: [EDB, "$ET", E2K]
actualizado: 2026-09-24
---
# ETABS

Software de CSI especializado en **edificios**: modelado por pisos, análisis lineal/no lineal, modal espectral, P-Delta, tiempo-historia, diseño de concreto, acero, muros y compuestos.

## Formatos
`.EDB` (modelo binario), `.$ET` (respaldo de texto), `.E2K` (exportación de texto editable). Exporta a [[SAFE]] (`.F2K`) losas y cimentaciones, y a Revit (CSiXRevit).

## Flujo con normas peruanas
1. Materiales (f'c, fy) y secciones.
2. Cargas por patrón (CM, CV, CVT) según [[E.020 - Cargas]].
3. **Masa sísmica** (source) según [[E.030 - Diseno Sismorresistente]].
4. **Espectro de usuario** Sa(T) y casos modal + espectral SX/SY.
5. Verificación de **derivas** (tabla Story Drifts) y **cortante basal** (escalamiento dinámico/estático).
6. Combinaciones según [[E.060 - Concreto Armado]] y diseño (código ACI 318 ajustado).
7. Exportar losas/cimentación a SAFE.

## API — CSI OAPI
- Librería `ETABSv1.dll` (COM y .NET). En Python con `comtypes`:
```python
import comtypes.client
helper = comtypes.client.CreateObject("ETABSv1.Helper")
helper = helper.QueryInterface(comtypes.gen.ETABSv1.cHelper)
etabs = helper.GetObject("CSI.ETABS.API.ETABSObject")   # adjuntarse a ETABS abierto
SapModel = etabs.SapModel
SapModel.SetPresentUnits(6)                               # 6 = kN_m_C (12 = Ton_m_C)
ret = SapModel.Analyze.RunAnalysis()                      # 0 = éxito
```
- Objetos: `SapModel.File`, `FrameObj`, `AreaObj`, `PointObj`, `PropMaterial`, `PropFrame`, `LoadPatterns`, `LoadCases`, `RespCombo`, `Func.FuncRS`, `Analyze`, `Results`, **`DatabaseTables`** (lectura/escritura de cualquier tabla interactiva, ideal para JARVIS).
- Ayuda de la API instalada con el programa (archivo CHM "CSI API ETABS v1") y documentación en docs.csiamerica.com.
- MCP → [[MCP CSI - ETABS SAP2000 SAFE]].

↑ [[MOC Software AEC]] · [[MOC Ingenieria Estructural]] · Hermanos: [[SAP2000]] · [[SAFE]]
