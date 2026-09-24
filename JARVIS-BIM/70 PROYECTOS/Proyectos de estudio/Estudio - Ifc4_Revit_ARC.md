---
tipo: proyecto-estudio
esquema: IFC4
disciplina: ARQ+EST
elementos_totales: 514
pisos: 6
espacios: 0
proxies: 66
tamano_mb: 13.0
archivo: "02_PROYECTOS_BIM/IfcSampleFiles/Ifc4_Revit_ARC.ifc"
software_origen: "21.0.0.383 - Exporter 21.0.0.383 - Alternate UI 21.0.0.383 · The EXPRESS Data Manager Version 5.02.0100.07 : 28 Aug 2013"
generado: 2026-09-24
tags: [proyecto, estudio, ifc]
---

# Estudio — Ifc4_Revit_ARC

> [!info] Nota generada automáticamente por `scripts/03_ifc_a_obsidian.py`
> Modelo: `02_PROYECTOS_BIM/IfcSampleFiles/Ifc4_Revit_ARC.ifc` · 13.0 MB · esquema **IFC4 (ISO 16739-1:2018)** → [[IFC - ISO 16739]]

## 1. Ficha del modelo
| Campo | Valor |
|---|---|
| Proyecto (IfcProject) | 001-00 — Sample House |
| Software de origen | 21.0.0.383 - Exporter 21.0.0.383 - Alternate UI 21.0.0.383 · The EXPRESS Data Manager Version 5.02.0100.07 : 28 Aug 2013 |
| Autor / organización | — / — |
| Fecha del archivo | 2021-03-02T22:49:04 |
| Vista (MVD) declarada | ViewDefinition [ReferenceView_V1.2] → [[MVD - Model View Definition]] |
| Unidad de longitud | millimetre |
| Disciplina inferida | **ARQ+EST** → [[BIM 3D - Modelado]] · [[MOC Ingenieria Estructural]] |
| Elementos / tipos / espacios | 514 / 215 / 0 |

## 2. Estructura espacial → [[IFC - Estructura del esquema]]
- **Sitio**: Surface:411452 (lat 42°12'46", lon -71°2'0")
- **Sitio**: M_Wind Power Generator:9 Meters High:418977
- **Sitio**: M_Wind Power Generator:9 Meters High:418985
- **Sitio**: M_Wind Power Generator:9 Meters High:554644
  - **Edificio**: Samuel Macalister sample house design
    - Piso: Foundation (elevación -800.00)
    - Piso: Level 1 Living Rm. (elevación -550.00)
    - Piso: Level 1 (elevación 0.00)
    - Piso: Ceiling (elevación 2700.00)
    - Piso: Level 2 (elevación 3000.00)
    - Piso: Roof Line (elevación 6000.00)

## 3. Clases IFC presentes → [[Clases IFC principales]]
| Clase | Cantidad |
|---|---|
| [[Clases IFC principales#IfcMember|IfcMember]] | 144 |
| [[Clases IFC principales#IfcBuildingElementProxy|IfcBuildingElementProxy]] | 66 |
| `IfcDistributionPort` | 60 |
| [[Clases IFC principales#IfcWall|IfcWall]] | 47 |
| [[Clases IFC principales#IfcPlate|IfcPlate]] | 44 |
| [[Clases IFC principales#IfcSlab|IfcSlab]] | 35 |
| [[Clases IFC principales#IfcOpeningElement|IfcOpeningElement]] | 35 |
| `IfcFurniture` | 32 |
| [[Clases IFC principales#IfcWindow|IfcWindow]] | 17 |
| [[Clases IFC principales#IfcDoor|IfcDoor]] | 16 |
| [[Clases IFC principales#IfcRailing|IfcRailing]] | 10 |
| `IfcLightFixture` | 10 |
| [[Clases IFC principales#IfcCurtainWall|IfcCurtainWall]] | 9 |
| [[Clases IFC principales#IfcFlowTerminal|IfcFlowTerminal]] | 9 |
| [[Clases IFC principales#IfcBuildingStorey|IfcBuildingStorey]] | 6 |
| [[Clases IFC principales#IfcSite|IfcSite]] | 4 |
| [[Clases IFC principales#IfcColumn|IfcColumn]] | 3 |
| [[Clases IFC principales#IfcStair|IfcStair]] | 3 |
| `IfcSystemFurnitureElement` | 3 |
| [[Clases IFC principales#IfcCovering|IfcCovering]] | 2 |
| [[Clases IFC principales#IfcRoof|IfcRoof]] | 2 |
| `IfcStairFlight` | 2 |
| [[Clases IFC principales#IfcBuilding|IfcBuilding]] | 1 |

**Mezcla por disciplina**: ARQ 140 · EST 191 · MEP 79 · INFRA 0

## 4. Información (datos) → [[LOIN - Nivel de Informacion Necesaria]]
- Materiales distintos: 107 → SH_resin Floor, Concrete, Sand/Cement Screed, Wood - Stud Layer, Structure - Timber Insulated Panel - OSB, Structure - Timber Insulated Panel - Insulation, Finishes - Interior - Plasterboard, Finishes - Exterior - Timber Cladding, Steel-Kohler-NA-Stainless, Chrome-Kohler-CP-Polished_Chrome, Roofing - Metal Standing Seam, Softwood, Lumber, Wood - Furring, Gypsum Wall Board, Concrete - Cast-in-Place Concrete, SH_Metal - Steel
- Conjuntos de cantidades (Qto): 311
- Clasificaciones: Uniformat
- Property Sets más frecuentes:
  - `Pset_EnvironmentalImpactIndicators` × 689
  - `Pset_MemberCommon` × 207
  - `Pset_BuildingElementProxyCommon` × 96
  - `Pset_ManufacturerTypeInformation` × 86
  - `Pset_ReinforcementBarPitchOfSlab` × 70
  - `Pset_SlabCommon` × 70
  - `Pset_PlateCommon` × 66
  - `Pset_ReinforcementBarPitchOfWall` × 54
  - `Pset_WallCommon` × 54
  - `Pset_FurnitureTypeCommon` × 45
  - `Pset_DoorCommon` × 25
  - `Pset_WindowCommon` × 23

## 5. Diagnóstico de calidad → [[Control de calidad de modelos BIM]]
- ⚠️ 66 `IfcBuildingElementProxy` (13% de los elementos): mapeo de clases IFC deficiente en la exportación → [[Control de calidad de modelos BIM]].
- ⚠️ 4 `IfcSite` en un solo modelo: probablemente familias exportadas con la clase IFC equivocada (revisar el mapeo de exportación) → [[Clases IFC principales]].
- ✅ Clasificación presente (Uniformat) → [[Sistemas de clasificacion]].
- ✅ Todos los elementos revisados están contenidos en la estructura espacial.
- ℹ️ Sin `IfcMapConversion`: el modelo no está georreferenciado → [[BIM y GIS]].
- ✅ 311 conjuntos de cantidades (Qto) útiles para metrados → [[BIM 5D - Costos y metrados]].

## 6. Preguntas de estudio para JARVIS y para ti
1. ¿Qué [[Usos BIM]] permite este modelo con la información que contiene?
2. Redacta 3 reglas [[IDS - Information Delivery Specification]] que este modelo debería cumplir y verifica si las cumple.
3. ¿Cómo lo federarías con otras disciplinas? → [[Federacion de modelos]]
4. ¿Qué LOD aparente tienen sus elementos principales? → [[LOD - Nivel de Desarrollo]]

↑ [[MOC Proyectos de Estudio]] · [[Resumen de modelos de estudio]] · [[Indice de proyectos]]
