---
tipo: proyecto-estudio
esquema: IFC2X3
disciplina: MEP
elementos_totales: 926
pisos: 3
espacios: 42
proxies: 0
tamano_mb: 17.0
archivo: "02_PROYECTOS_BIM/IfcSampleFiles/Ifc2x3_Duplex_MEP.ifc"
software_origen: "20100326_1700 · Autodesk Revit MEP 2011 - 1.0"
generado: 2026-09-24
tags: [proyecto, estudio, ifc]
---

# Estudio — Ifc2x3_Duplex_MEP

> [!info] Nota generada automáticamente por `scripts/03_ifc_a_obsidian.py`
> Modelo: `02_PROYECTOS_BIM/IfcSampleFiles/Ifc2x3_Duplex_MEP.ifc` · 17.0 MB · esquema **IFC2x3 (ISO/PAS 16739:2005)** → [[IFC - ISO 16739]]

## 1. Ficha del modelo
| Campo | Valor |
|---|---|
| Proyecto (IfcProject) | 0001 — Duplex Apartment |
| Software de origen | 20100326_1700 · Autodesk Revit MEP 2011 - 1.0 |
| Autor / organización | — / — |
| Fecha del archivo | 2011-09-07T12:40:02 |
| Vista (MVD) declarada | ViewDefinition [CoordinationView] → [[MVD - Model View Definition]] |
| Unidad de longitud | metre |
| Disciplina inferida | **MEP** → [[Coordinacion BIM y deteccion de interferencias]] |
| Elementos / tipos / espacios | 926 / 513 / 42 |

## 2. Estructura espacial → [[IFC - Estructura del esquema]]
- **Sitio**: Default (lat 41°52'27", lon -87°38'21")
  - **Edificio**: (sin nombre)
    - Piso: Level 1 (elevación 0.00)
    - Piso: Level 2 (elevación 3.10)
    - Piso: Roof (elevación 6.00)

## 3. Clases IFC presentes → [[Clases IFC principales]]
| Clase | Cantidad |
|---|---|
| [[Clases IFC principales#IfcFlowSegment|IfcFlowSegment]] | 427 |
| [[Clases IFC principales#IfcFlowFitting|IfcFlowFitting]] | 358 |
| [[Clases IFC principales#IfcFlowTerminal|IfcFlowTerminal]] | 105 |
| [[Clases IFC principales#IfcSpace|IfcSpace]] | 42 |
| `IfcEnergyConversionDevice` | 16 |
| `IfcFlowController` | 14 |
| `IfcFlowMovingDevice` | 4 |
| [[Clases IFC principales#IfcBuildingStorey|IfcBuildingStorey]] | 3 |
| `IfcDistributionControlElement` | 2 |
| [[Clases IFC principales#IfcBuilding|IfcBuilding]] | 1 |
| [[Clases IFC principales#IfcSite|IfcSite]] | 1 |

**Mezcla por disciplina**: ARQ 42 · EST 0 · MEP 926 · INFRA 0

## 4. Información (datos) → [[LOIN - Nivel de Informacion Necesaria]]
- Materiales distintos: 0 → —
- Conjuntos de cantidades (Qto): 42
- Clasificaciones: ninguna
- Property Sets más frecuentes:
  - `PSet_Revit_Other` × 972
  - `PSet_Revit_Constraints` × 971
  - `PSet_Revit_Phasing` × 968
  - `PSet_Revit_Identity Data` × 947
  - `PSet_Revit_Dimensions` × 849
  - `PSet_Revit_Mechanical` × 811
  - `PSet_Revit_Graphics` × 372
  - `PSet_Revit_Electrical - Loads` × 122
  - `PSet_Revit_Electrical - Circuiting` × 79
  - `Pset_SpaceCommon` × 42
  - `PSet_Revit_Type_Other` × 39
  - `PSet_Revit_Type_Identity Data` × 39

## 5. Diagnóstico de calidad → [[Control de calidad de modelos BIM]]
- ✅ Pocos o ningún proxy: la exportación usa clases IFC específicas → [[Clases IFC principales]].
- ⚠️ Sin `IfcClassification`: los elementos no llevan códigos Uniclass/OmniClass → [[Sistemas de clasificacion]].
- ✅ Todos los elementos revisados están contenidos en la estructura espacial.
- ℹ️ IFC2x3: sin georreferenciación completa (`IfcMapConversion` llega en IFC4) → [[BIM y GIS]].
- ✅ 42 conjuntos de cantidades (Qto) útiles para metrados → [[BIM 5D - Costos y metrados]].

## 6. Preguntas de estudio para JARVIS y para ti
1. ¿Qué [[Usos BIM]] permite este modelo con la información que contiene?
2. Redacta 3 reglas [[IDS - Information Delivery Specification]] que este modelo debería cumplir y verifica si las cumple.
3. ¿Cómo lo federarías con otras disciplinas? → [[Federacion de modelos]]
4. ¿Qué LOD aparente tienen sus elementos principales? → [[LOD - Nivel de Desarrollo]]

↑ [[MOC Proyectos de Estudio]] · [[Resumen de modelos de estudio]] · [[Indice de proyectos]]
