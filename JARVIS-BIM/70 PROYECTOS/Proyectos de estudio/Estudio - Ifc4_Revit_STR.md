---
tipo: proyecto-estudio
esquema: IFC4
disciplina: EST
elementos_totales: 4150
pisos: 0
espacios: 1
proxies: 0
tamano_mb: 10.8
archivo: "02_PROYECTOS_BIM/IfcSampleFiles/Ifc4_Revit_STR.ifc"
software_origen: "21.0.0.383 - Exporter 21.0.0.383 - Alternate UI 21.0.0.383 · The EXPRESS Data Manager Version 5.02.0100.07 : 28 Aug 2013"
generado: 2026-09-24
tags: [proyecto, estudio, ifc]
---

# Estudio — Ifc4_Revit_STR

> [!info] Nota generada automáticamente por `scripts/03_ifc_a_obsidian.py`
> Modelo: `02_PROYECTOS_BIM/IfcSampleFiles/Ifc4_Revit_STR.ifc` · 10.8 MB · esquema **IFC4 (ISO 16739-1:2018)** → [[IFC - ISO 16739]]

## 1. Ficha del modelo
| Campo | Valor |
|---|---|
| Proyecto (IfcProject) | 001-00 — Sample House |
| Software de origen | 21.0.0.383 - Exporter 21.0.0.383 - Alternate UI 21.0.0.383 · The EXPRESS Data Manager Version 5.02.0100.07 : 28 Aug 2013 |
| Autor / organización | — / — |
| Fecha del archivo | 2021-03-02T22:55:40 |
| Vista (MVD) declarada | ViewDefinition [ReferenceView_V1.2] → [[MVD - Model View Definition]] |
| Unidad de longitud | millimetre |
| Disciplina inferida | **EST** → [[MOC Ingenieria Estructural]] |
| Elementos / tipos / espacios | 4150 / 114 / 1 |

## 2. Estructura espacial → [[IFC - Estructura del esquema]]
- **Sitio**: Default (lat 42°23'13", lon -71°14'31")
  - **Edificio**: (sin IfcBuilding)

## 3. Clases IFC presentes → [[Clases IFC principales]]
| Clase | Cantidad |
|---|---|
| [[Clases IFC principales#IfcReinforcingBar|IfcReinforcingBar]] | 3680 |
| [[Clases IFC principales#IfcBeam|IfcBeam]] | 370 |
| [[Clases IFC principales#IfcSlab|IfcSlab]] | 37 |
| [[Clases IFC principales#IfcColumn|IfcColumn]] | 30 |
| `IfcElementAssembly` | 16 |
| [[Clases IFC principales#IfcWall|IfcWall]] | 9 |
| [[Clases IFC principales#IfcFooting|IfcFooting]] | 4 |
| [[Clases IFC principales#IfcMember|IfcMember]] | 2 |
| [[Clases IFC principales#IfcStair|IfcStair]] | 1 |
| `IfcStairFlight` | 1 |
| [[Clases IFC principales#IfcSite|IfcSite]] | 1 |
| [[Clases IFC principales#IfcSpace|IfcSpace]] | 1 |

**Mezcla por disciplina**: ARQ 12 · EST 4086 · MEP 0 · INFRA 0

## 4. Información (datos) → [[LOIN - Nivel de Informacion Necesaria]]
- Materiales distintos: 15 → CL Concrete_ panels, Concrete - Cast-in-Place Concrete, Concrete - Rough, Rigid insulation, Damp-proofing, Rubble, Metal - Steel - 345 MPa, Metal Stud Layer, Aluminum, Metal - Steel - 250 MPa, Concrete, Cast-in-Place gray, Softwood, Lumber, Concrete - Cast-in-Place Concrete - 35 MPa, Plywood, Sheathing, Steel, 45-345
- Conjuntos de cantidades (Qto): 450
- Clasificaciones: Uniformat
- Property Sets más frecuentes:
  - `Pset_EnvironmentalImpactIndicators` × 4342
  - `Pset_ElementComponentCommon` × 3760
  - `Pset_ReinforcingBarCommon` × 3760
  - `Pset_BeamCommon` × 431
  - `Pset_ReinforcementBarPitchOfBeam` × 431
  - `Pset_ReinforcementBarPitchOfSlab` × 74
  - `Pset_SlabCommon` × 74
  - `Pset_ColumnCommon` × 37
  - `Pset_ReinforcementBarPitchOfColumn` × 37
  - `Pset_ElementAssemblyCommon` × 16
  - `Pset_ReinforcementBarPitchOfWall` × 10
  - `Pset_WallCommon` × 10

## 5. Diagnóstico de calidad → [[Control de calidad de modelos BIM]]
- ✅ Pocos o ningún proxy: la exportación usa clases IFC específicas → [[Clases IFC principales]].
- ⚠️ Sin `IfcBuildingStorey`: los elementos no están organizados por niveles (estructura espacial incompleta) → [[IFC - Estructura del esquema]].
- ✅ Clasificación presente (Uniformat) → [[Sistemas de clasificacion]].
- ✅ Todos los elementos revisados están contenidos en la estructura espacial.
- ℹ️ Sin `IfcMapConversion`: el modelo no está georreferenciado → [[BIM y GIS]].
- ✅ 450 conjuntos de cantidades (Qto) útiles para metrados → [[BIM 5D - Costos y metrados]].

## 6. Preguntas de estudio para JARVIS y para ti
1. ¿Qué [[Usos BIM]] permite este modelo con la información que contiene?
2. Redacta 3 reglas [[IDS - Information Delivery Specification]] que este modelo debería cumplir y verifica si las cumple.
3. ¿Cómo lo federarías con otras disciplinas? → [[Federacion de modelos]]
4. ¿Qué LOD aparente tienen sus elementos principales? → [[LOD - Nivel de Desarrollo]]

↑ [[MOC Proyectos de Estudio]] · [[Resumen de modelos de estudio]] · [[Indice de proyectos]]
