---
tipo: proyecto-estudio
esquema: IFC4
disciplina: MEP
elementos_totales: 15339
pisos: 4
espacios: 163
proxies: 654
tamano_mb: 27.8
archivo: "02_PROYECTOS_BIM/IfcSampleFiles/Ifc4_Revit_MEP.ifc"
software_origen: "21.0.0.383 - Exporter 21.0.0.383 - Alternate UI 21.0.0.383 · The EXPRESS Data Manager Version 5.02.0100.07 : 28 Aug 2013"
generado: 2026-09-24
tags: [proyecto, estudio, ifc]
---

# Estudio — Ifc4_Revit_MEP

> [!info] Nota generada automáticamente por `scripts/03_ifc_a_obsidian.py`
> Modelo: `02_PROYECTOS_BIM/IfcSampleFiles/Ifc4_Revit_MEP.ifc` · 27.8 MB · esquema **IFC4 (ISO 16739-1:2018)** → [[IFC - ISO 16739]]

## 1. Ficha del modelo
| Campo | Valor |
|---|---|
| Proyecto (IfcProject) | Project Number — Project Name |
| Software de origen | 21.0.0.383 - Exporter 21.0.0.383 - Alternate UI 21.0.0.383 · The EXPRESS Data Manager Version 5.02.0100.07 : 28 Aug 2013 |
| Autor / organización | — / — |
| Fecha del archivo | 2021-03-02T23:38:45 |
| Vista (MVD) declarada | ViewDefinition [ReferenceView_V1.2] → [[MVD - Model View Definition]] |
| Unidad de longitud | millimetre |
| Disciplina inferida | **MEP** → [[Coordinacion BIM y deteccion de interferencias]] |
| Elementos / tipos / espacios | 15339 / 1172 / 163 |

## 2. Estructura espacial → [[IFC - Estructura del esquema]]
- **Sitio**: Default (lat 48°7'58", lon 11°34'58")
  - **Edificio**: (sin nombre)
    - Piso: Level 1 (elevación 94.17)
    - Piso: Level 2 (elevación 3800.00)
    - Piso: Level 3 (elevación 7300.00)
    - Piso: Roof Level (elevación 10900.00)

## 3. Clases IFC presentes → [[Clases IFC principales]]
| Clase | Cantidad |
|---|---|
| `IfcDistributionPort` | 8515 |
| [[Clases IFC principales#IfcMember|IfcMember]] | 1450 |
| `IfcDuctFitting` | 935 |
| `IfcDuctSegment` | 837 |
| [[Clases IFC principales#IfcBuildingElementProxy|IfcBuildingElementProxy]] | 654 |
| [[Clases IFC principales#IfcPlate|IfcPlate]] | 629 |
| `IfcPipeFitting` | 535 |
| `IfcPipeSegment` | 491 |
| `IfcLightFixture` | 410 |
| `IfcAirTerminal` | 309 |
| [[Clases IFC principales#IfcSpace|IfcSpace]] | 163 |
| [[Clases IFC principales#IfcColumn|IfcColumn]] | 135 |
| [[Clases IFC principales#IfcWall|IfcWall]] | 133 |
| [[Clases IFC principales#IfcOpeningElement|IfcOpeningElement]] | 131 |
| [[Clases IFC principales#IfcDoor|IfcDoor]] | 124 |
| [[Clases IFC principales#IfcCovering|IfcCovering]] | 43 |
| [[Clases IFC principales#IfcCurtainWall|IfcCurtainWall]] | 33 |
| [[Clases IFC principales#IfcSlab|IfcSlab]] | 25 |
| `IfcCableCarrierSegment` | 20 |
| [[Clases IFC principales#IfcRailing|IfcRailing]] | 14 |
| `IfcCableCarrierFitting` | 14 |
| [[Clases IFC principales#IfcFlowTerminal|IfcFlowTerminal]] | 11 |
| [[Clases IFC principales#IfcStair|IfcStair]] | 8 |
| `IfcStairFlight` | 8 |
| `IfcFireSuppressionTerminal` | 6 |
| [[Clases IFC principales#IfcBuildingStorey|IfcBuildingStorey]] | 4 |
| [[Clases IFC principales#IfcBuilding|IfcBuilding]] | 1 |
| [[Clases IFC principales#IfcSite|IfcSite]] | 1 |

**Mezcla por disciplina**: ARQ 526 · EST 2214 · MEP 12077 · INFRA 0

## 4. Información (datos) → [[LOIN - Nivel de Informacion Necesaria]]
- Materiales distintos: 34 → <Unnamed>, Metal - Paint Finish - Ivory, Glossy, Glass - White, High Luminance, Glass - Clear, Grey, Metal - Chrome, Plastic - Blue, Glass - Frosted, Stahlbeton - Fertigbeton, Stahlbeton - Ortbeton - Rot, Stahlbeton - Ortbeton, Mauerwerk - Ziegel, Tür - Stahl Zarge, Tür - Stahl Griff, Mauerwerk - Lamellen, Fassade - Metallpanel
- Conjuntos de cantidades (Qto): 2208
- Clasificaciones: Uniformat
- Property Sets más frecuentes:
  - `Pset_EnvironmentalImpactIndicators` × 7866
  - `Pset_MemberCommon` × 1704
  - `Pset_DuctFittingTypeCommon` × 1145
  - `Pset_DuctSegmentTypeCommon` × 845
  - `Pset_PlateCommon` × 831
  - `Pset_BuildingElementProxyCommon` × 718
  - `Pset_PipeFittingTypeCommon` × 631
  - `Pset_PipeSegmentTypeCommon` × 493
  - `Pset_PipeSegmentOccurrence` × 491
  - `Pset_LightFixtureTypeCommon` × 415
  - `Pset_AirTerminalBoxTypeCommon` × 359
  - `Pset_AirTerminalTypeCommon` × 359

## 5. Diagnóstico de calidad → [[Control de calidad de modelos BIM]]
- ✅ Pocos o ningún proxy: la exportación usa clases IFC específicas → [[Clases IFC principales]].
- ✅ Clasificación presente (Uniformat) → [[Sistemas de clasificacion]].
- ✅ Todos los elementos revisados están contenidos en la estructura espacial.
- ℹ️ Sin `IfcMapConversion`: el modelo no está georreferenciado → [[BIM y GIS]].
- ✅ 2208 conjuntos de cantidades (Qto) útiles para metrados → [[BIM 5D - Costos y metrados]].

## 6. Preguntas de estudio para JARVIS y para ti
1. ¿Qué [[Usos BIM]] permite este modelo con la información que contiene?
2. Redacta 3 reglas [[IDS - Information Delivery Specification]] que este modelo debería cumplir y verifica si las cumple.
3. ¿Cómo lo federarías con otras disciplinas? → [[Federacion de modelos]]
4. ¿Qué LOD aparente tienen sus elementos principales? → [[LOD - Nivel de Desarrollo]]

↑ [[MOC Proyectos de Estudio]] · [[Resumen de modelos de estudio]] · [[Indice de proyectos]]
