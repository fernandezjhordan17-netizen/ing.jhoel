---
tipo: proyecto-estudio
esquema: IFC2X3
disciplina: ARQ
elementos_totales: 218
pisos: 4
espacios: 21
proxies: 0
tamano_mb: 2.3
archivo: "02_PROYECTOS_BIM/IfcSampleFiles/Ifc2x3_Duplex_Architecture.ifc"
software_origen: "20100326_1700 · Autodesk Revit Architecture 2011 - 1.0"
generado: 2026-09-24
tags: [proyecto, estudio, ifc]
---

# Estudio — Ifc2x3_Duplex_Architecture

> [!info] Nota generada automáticamente por `scripts/03_ifc_a_obsidian.py`
> Modelo: `02_PROYECTOS_BIM/IfcSampleFiles/Ifc2x3_Duplex_Architecture.ifc` · 2.3 MB · esquema **IFC2x3 (ISO/PAS 16739:2005)** → [[IFC - ISO 16739]]

## 1. Ficha del modelo
| Campo | Valor |
|---|---|
| Proyecto (IfcProject) | 0001 — Duplex Apartment |
| Software de origen | 20100326_1700 · Autodesk Revit Architecture 2011 - 1.0 |
| Autor / organización | — / — |
| Fecha del archivo | 2011-09-07T12:28:29 |
| Vista (MVD) declarada | ViewDefinition [CoordinationView] → [[MVD - Model View Definition]] |
| Unidad de longitud | metre |
| Disciplina inferida | **ARQ** → [[BIM 3D - Modelado]] |
| Elementos / tipos / espacios | 218 / 37 / 21 |

## 2. Estructura espacial → [[IFC - Estructura del esquema]]
- **Sitio**: Default (lat 41°52'27", lon -87°38'21")
  - **Edificio**: (sin nombre)
    - Piso: T/FDN (elevación -1.25)
    - Piso: Level 1 (elevación 0.00)
    - Piso: Level 2 (elevación 3.10)
    - Piso: Roof (elevación 6.00)

## 3. Clases IFC presentes → [[Clases IFC principales]]
| Clase | Cantidad |
|---|---|
| [[Clases IFC principales#IfcFurnishingElement|IfcFurnishingElement]] | 61 |
| [[Clases IFC principales#IfcWall|IfcWallStandardCase]] | 56 |
| [[Clases IFC principales#IfcOpeningElement|IfcOpeningElement]] | 50 |
| [[Clases IFC principales#IfcWindow|IfcWindow]] | 24 |
| [[Clases IFC principales#IfcSlab|IfcSlab]] | 21 |
| [[Clases IFC principales#IfcSpace|IfcSpace]] | 21 |
| [[Clases IFC principales#IfcDoor|IfcDoor]] | 14 |
| [[Clases IFC principales#IfcCovering|IfcCovering]] | 13 |
| [[Clases IFC principales#IfcBeam|IfcBeam]] | 8 |
| [[Clases IFC principales#IfcFooting|IfcFooting]] | 7 |
| [[Clases IFC principales#IfcMember|IfcMember]] | 4 |
| [[Clases IFC principales#IfcRailing|IfcRailing]] | 4 |
| [[Clases IFC principales#IfcBuildingStorey|IfcBuildingStorey]] | 4 |
| [[Clases IFC principales#IfcStair|IfcStair]] | 2 |
| `IfcStairFlight` | 2 |
| [[Clases IFC principales#IfcRoof|IfcRoof]] | 1 |
| [[Clases IFC principales#IfcWall|IfcWall]] | 1 |
| [[Clases IFC principales#IfcBuilding|IfcBuilding]] | 1 |
| [[Clases IFC principales#IfcSite|IfcSite]] | 1 |

**Mezcla por disciplina**: ARQ 199 · EST 19 · MEP 0 · INFRA 0

## 4. Información (datos) → [[LOIN - Nivel de Informacion Necesaria]]
- Materiales distintos: 18 → Masonry - Brick, Misc. Air Layers - Air Space, Insulation / Thermal Barriers - Rigid insulation, Masonry - Concrete Block, Metal - Stud Layer, Plasterboard, Concrete - Cast In Situ, Concrete, Wood - Sheathing - plywood, Wood - Dimensional Lumber, Wood - Flooring, Insulation / Thermal Barriers - Semi-rigid insulation, Ceramic Tile, Masonry - Grout, Site - Grass
- Conjuntos de cantidades (Qto): 21
- Clasificaciones: ninguna
- Property Sets más frecuentes:
  - `PSet_Revit_Other` × 237
  - `PSet_Revit_Constraints` × 236
  - `PSet_Revit_Phasing` × 232
  - `PSet_Revit_Dimensions` × 139
  - `PSet_Revit_Structural` × 92
  - `PSet_Revit_Identity Data` × 63
  - `Pset_WallCommon` × 57
  - `PSet_Revit_Type_Identity Data` × 44
  - `PSet_Revit_Type_Other` × 44
  - `PSet_Revit_Type_Construction` × 36
  - `PSet_Revit_Analytical Model` × 35
  - `PSet_Revit_Structural Analysis` × 35

## 5. Diagnóstico de calidad → [[Control de calidad de modelos BIM]]
- ✅ Pocos o ningún proxy: la exportación usa clases IFC específicas → [[Clases IFC principales]].
- ⚠️ Sin `IfcClassification`: los elementos no llevan códigos Uniclass/OmniClass → [[Sistemas de clasificacion]].
- ✅ Todos los elementos revisados están contenidos en la estructura espacial.
- ℹ️ IFC2x3: sin georreferenciación completa (`IfcMapConversion` llega en IFC4) → [[BIM y GIS]].
- ✅ 21 conjuntos de cantidades (Qto) útiles para metrados → [[BIM 5D - Costos y metrados]].

## 6. Preguntas de estudio para JARVIS y para ti
1. ¿Qué [[Usos BIM]] permite este modelo con la información que contiene?
2. Redacta 3 reglas [[IDS - Information Delivery Specification]] que este modelo debería cumplir y verifica si las cumple.
3. ¿Cómo lo federarías con otras disciplinas? → [[Federacion de modelos]]
4. ¿Qué LOD aparente tienen sus elementos principales? → [[LOD - Nivel de Desarrollo]]

↑ [[MOC Proyectos de Estudio]] · [[Resumen de modelos de estudio]] · [[Indice de proyectos]]
