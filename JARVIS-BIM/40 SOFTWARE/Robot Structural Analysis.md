---
tipo: software
tags: [software/autodesk, estructural, analisis]
aliases: [Robot, RSA, Robot Structural Analysis Professional, RTD]
fabricante: Autodesk
formatos: [RTD, STR]
actualizado: 2026-09-24
---
# Robot Structural Analysis Professional

Software de **análisis y diseño estructural** por elementos finitos de Autodesk (barras, placas, sólidos; análisis lineal, no lineal, modal, espectral, pandeo, tiempo-historia).

## Puntos fuertes
- Enlace bidireccional con el modelo analítico de [[Revit]].
- Amplia base de códigos (Eurocódigos, normas de EE.UU., otros) → [[Eurocodigos]], [[ACI 318]], [[AISC 360 y 341]].
- Mallado automático de losas y muros.

## API
**RobotOM** (COM): `RobotApplication`, `Project.Structure.Nodes/Bars`, `Loads`, `CalcEngine`, `Results`. Se usa desde C#, VBA o Python (`comtypes`/`pywin32`) → [[MCP Robot Structural Analysis]].

## Formatos
`RTD` (modelo nativo), `STR` (texto), intercambio con Revit, IFC limitado.

↑ [[MOC Software AEC]] · [[MOC Ingenieria Estructural]]
