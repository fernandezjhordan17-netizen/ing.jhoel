---
tipo: proyecto-estudio
esquema: IFC4
disciplina: ARQ+EST
elementos_totales: 58
pisos: 1
espacios: 2
proxies: 0
tamano_mb: 2.1
archivo: "02_PROYECTOS_BIM/IfcSampleFiles/Ifc4_SampleHouse_0_GroundFloor.ifc"
software_origen: "Ifc.Toolbox v3.9 - BIM Mars · Xbim File Processor version 4.0.0.0"
generado: 2026-09-24
tags: [proyecto, estudio, ifc]
---

# Estudio — Ifc4_SampleHouse_0_GroundFloor

> [!info] Nota generada automáticamente por `scripts/03_ifc_a_obsidian.py`
> Modelo: `02_PROYECTOS_BIM/IfcSampleFiles/Ifc4_SampleHouse_0_GroundFloor.ifc` · 2.1 MB · esquema **IFC4 (ISO 16739-1:2018)** → [[IFC - ISO 16739]]

## 1. Ficha del modelo
| Campo | Valor |
|---|---|
| Proyecto (IfcProject) | Project Number — Project Name |
| Software de origen | Ifc.Toolbox v3.9 - BIM Mars · Xbim File Processor version 4.0.0.0 |
| Autor / organización | — / — |
| Fecha del archivo | 2016-11-11T10:59:10 |
| Vista (MVD) declarada | — → [[MVD - Model View Definition]] |
| Unidad de longitud | millimetre |
| Disciplina inferida | **ARQ+EST** → [[BIM 3D - Modelado]] · [[MOC Ingenieria Estructural]] |
| Elementos / tipos / espacios | 58 / 20 / 2 |

## 2. Estructura espacial → [[IFC - Estructura del esquema]]
- **Sitio**: Default (lat 51°30'0", lon -0°7'34")
  - **Edificio**: (sin nombre)
    - Piso: Ground Floor (elevación 0.00)

## 3. Clases IFC presentes → [[Clases IFC principales]]
| Clase | Cantidad |
|---|---|
| [[Clases IFC principales#IfcMember|IfcMember]] | 20 |
| `IfcFurniture` | 14 |
| [[Clases IFC principales#IfcOpeningElement|IfcOpeningElement]] | 7 |
| [[Clases IFC principales#IfcPlate|IfcPlate]] | 6 |
| [[Clases IFC principales#IfcWindow|IfcWindow]] | 4 |
| [[Clases IFC principales#IfcCovering|IfcCovering]] | 3 |
| [[Clases IFC principales#IfcDoor|IfcDoor]] | 3 |
| [[Clases IFC principales#IfcWall|IfcWall]] | 3 |
| [[Clases IFC principales#IfcCurtainWall|IfcCurtainWall]] | 2 |
| [[Clases IFC principales#IfcWall|IfcWallStandardCase]] | 2 |
| [[Clases IFC principales#IfcSpace|IfcSpace]] | 2 |
| [[Clases IFC principales#IfcSlab|IfcSlab]] | 1 |
| [[Clases IFC principales#IfcBuilding|IfcBuilding]] | 1 |
| [[Clases IFC principales#IfcBuildingStorey|IfcBuildingStorey]] | 1 |
| [[Clases IFC principales#IfcSite|IfcSite]] | 1 |

**Mezcla por disciplina**: ARQ 33 · EST 26 · MEP 0 · INFRA 0

## 4. Información (datos) → [[LOIN - Nivel de Informacion Necesaria]]
- Materiales distintos: 30 → Brick, Common, Fiberglass Batt, Concrete Masonry Units _Low Density, Plaster, Metal Stud Layer, Door - Handle, Door - Frame/Mullion, Door - Panel, Door - Architrave, Door - Frame/Mullion (1), Window Frame, Glass, Gypsum Wall Board, Concrete, Sand/Cement Screed, Vapor Retarder
- Conjuntos de cantidades (Qto): 22
- Clasificaciones: Uniformat
- Property Sets más frecuentes:
  - `Other` × 82
  - `Dimensions` × 70
  - `Constraints` × 67
  - `Phasing` × 60
  - `Identity Data` × 31
  - `Pset_MemberCommon` × 20
  - `Materials and Finishes` × 14
  - `Construction` × 9
  - `Graphics` × 9
  - `Structural` × 8
  - `Analytical Properties` × 8
  - `Pset_ManufacturerTypeInformation` × 7

## 5. Diagnóstico de calidad → [[Control de calidad de modelos BIM]]
- ✅ Pocos o ningún proxy: la exportación usa clases IFC específicas → [[Clases IFC principales]].
- ✅ Clasificación presente (Uniformat) → [[Sistemas de clasificacion]].
- ✅ Todos los elementos revisados están contenidos en la estructura espacial.
- ℹ️ Sin `IfcMapConversion`: el modelo no está georreferenciado → [[BIM y GIS]].
- ✅ 22 conjuntos de cantidades (Qto) útiles para metrados → [[BIM 5D - Costos y metrados]].

## 6. Preguntas de estudio para JARVIS y para ti
1. ¿Qué [[Usos BIM]] permite este modelo con la información que contiene?
2. Redacta 3 reglas [[IDS - Information Delivery Specification]] que este modelo debería cumplir y verifica si las cumple.
3. ¿Cómo lo federarías con otras disciplinas? → [[Federacion de modelos]]
4. ¿Qué LOD aparente tienen sus elementos principales? → [[LOD - Nivel de Desarrollo]]

↑ [[MOC Proyectos de Estudio]] · [[Resumen de modelos de estudio]] · [[Indice de proyectos]]
