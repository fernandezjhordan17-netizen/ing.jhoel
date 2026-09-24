---
tipo: moc
tags: [moc, software]
aliases: [Mapa Software, MOC Software]
actualizado: 2026-09-24
---
# 🟢 MOC — Software AEC

## Modelado y documentación (Autodesk)
- [[Revit]] (arquitectura, estructura, MEP) · [[Dynamo]] (programación visual)
- [[AutoCAD]] (2D/3D CAD) · [[Civil 3D]] (infraestructura, topografía, vías)
- [[Navisworks]] (federación, interferencias, 4D/5D)

## Análisis y diseño estructural
- CSI: [[ETABS]] (edificios) · [[SAP2000]] (estructuras generales, puentes) · [[SAFE]] (losas y cimentaciones)
- Autodesk: [[Robot Structural Analysis]]
- Trimble: [[Tekla Structures]] (acero/concreto detallado para fabricación)

## Datos y cálculo
- [[Excel]] (metrados, presupuestos, hojas de cálculo)

## Ecosistema abierto y nube
- [[IfcOpenShell y Bonsai]] · [[Speckle]] · [[Autodesk Platform Services y ACC]]

## Caja de herramientas (gratis/freemium)
[[Caja de herramientas BIM]] → [[Bibliotecas de familias BIM]] · [[Visores BIM gratuitos]] · [[Add-ins recomendados para Revit]] · [[Herramientas de IA para BIM]]

## Interoperabilidad
- [[Formatos de archivo AEC]] · [[Interoperabilidad entre software]] · [[SAF - Structural Analysis Format]]

## Cómo se conecta cada uno a JARVIS
| Software | API principal | Nota MCP |
|---|---|---|
| Revit | .NET (C#), Revit API | [[MCP Revit]] |
| Dynamo | Nodos + Python, DynamoMCP | [[MCP Dynamo]] |
| AutoCAD / Civil 3D | .NET, AutoLISP, COM | [[MCP AutoCAD y Civil 3D]] |
| Navisworks | .NET API, COM, Automation | [[MCP Navisworks]] |
| ETABS / SAP2000 / SAFE | CSI OAPI (COM/.NET) | [[MCP CSI - ETABS SAP2000 SAFE]] |
| Robot | RobotOM (COM) | [[MCP Robot Structural Analysis]] |
| Tekla | Tekla Open API (.NET) | [[MCP Tekla Structures]] |
| Excel | archivo (openpyxl) o COM (xlwings) | [[MCP Excel]] |

Ver también [[MOC JARVIS y MCP]].
