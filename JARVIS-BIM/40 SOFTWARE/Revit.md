---
tipo: software
tags: [software/autodesk, modelado, bim]
aliases: [Autodesk Revit, RVT]
fabricante: Autodesk
formatos: [RVT, RFA, RTE, RFT, IFC, NWC, DWG]
actualizado: 2026-09-24
---
# Revit

Software BIM de Autodesk para **arquitectura, estructuras y MEP** (modelado paramétrico, documentación, tablas, coordinación).

## Conceptos clave
Categorías → familias (sistema, cargables `.rfa`, in situ) → tipos → ejemplares; parámetros (de proyecto, compartidos, globales); vistas y planos; worksets y modelo central (colaboración); vínculos RVT/IFC/DWG/nube de puntos; fases y opciones de diseño; modelo analítico estructural.

## Formatos
`RVT` (proyecto), `RFA` (familia), `RTE` (plantilla), exportación [[IFC - ISO 16739]] (IFC2x3/IFC4/IFC4.3 vía exportador open source de Autodesk), `NWC` para [[Navisworks]], `DWG`.

## Automatización / API
| Vía | Detalle |
|---|---|
| **Revit API (.NET)** | C# con `IExternalCommand` / `IExternalApplication`; manifiesto `.addin` en `%AppData%\Autodesk\Revit\Addins\<año>`; cambios dentro de `Transaction`; eventos externos (`IExternalEventHandler`) para llamadas desde otros hilos. Revit 2025+ usa **.NET 8** (antes .NET Framework 4.8) |
| **[[Dynamo]]** | Programación visual + Python |
| **pyRevit** | Framework de herramientas en Python (IronPython/CPython) |
| **Design Automation API** | Revit "headless" en la nube → [[Autodesk Platform Services y ACC]] |
| **MCP** | Oficial (Revit 2027, Technical Preview) y comunitarios → [[MCP Revit]] |

## Proyectos de muestra
Revit instala/ofrece muestras (arquitectura, estructura, MEP; desde 2024 el proyecto multidisciplinario **Snowdon Towers** con nube de puntos) → [[Descarga de proyectos BIM]].

## Buenas prácticas
[[BIM 3D - Modelado]] · [[Control de calidad de modelos BIM]] · exportar IFC con mapeo de clases revisado ([[Clases IFC principales]]).

## Integraciones estructurales
Revit ↔ [[ETABS]] (CSiXRevit), Revit ↔ [[Robot Structural Analysis]] (Structural Analysis Toolkit), Revit ↔ [[Tekla Structures]] (IFC / Tekla Link) → [[Interoperabilidad entre software]].

## Complementos y recursos
[[Add-ins recomendados para Revit]] · [[Bibliotecas de familias BIM]] · [[Herramientas de IA para BIM]] · Práctica: [[Proyecto integrador - Revit ARQ EST MEP]]

↑ [[MOC Software AEC]]
