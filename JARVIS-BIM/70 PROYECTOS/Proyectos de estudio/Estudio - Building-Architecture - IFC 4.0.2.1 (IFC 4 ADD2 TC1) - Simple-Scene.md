---
tipo: proyecto-estudio
esquema: IFC4
disciplina: ARQ
elementos_totales: 14
pisos: 1
espacios: 2
proxies: 3
tamano_mb: 0.1
archivo: "02_PROYECTOS_BIM/buildingSMART_Sample-Test-Files/IFC 4.0.2.1 (IFC 4 ADD2 TC1)/Simple-Scene/Building-Architecture.ifc"
software_origen: "BIM_Tools - Sketchup_IFC_manager - 5.6.0 · Sketchup-IFC-manager 5.6.0 / SketchUp 2026 (26.2.242)"
generado: 2026-09-24
tags: [proyecto, estudio, ifc]
---

# Estudio — Building-Architecture - IFC 4.0.2.1 (IFC 4 ADD2 TC1) - Simple-Scene

> [!info] Nota generada automáticamente por `scripts/03_ifc_a_obsidian.py`
> Modelo: `02_PROYECTOS_BIM/buildingSMART_Sample-Test-Files/IFC 4.0.2.1 (IFC 4 ADD2 TC1)/Simple-Scene/Building-Architecture.ifc` · 0.1 MB · esquema **IFC4 (ISO 16739-1:2018)** → [[IFC - ISO 16739]]

## 1. Ficha del modelo
| Campo | Valor |
|---|---|
| Proyecto (IfcProject) | ifc silly sample scene - project  |
| Software de origen | BIM_Tools - Sketchup_IFC_manager - 5.6.0 · Sketchup-IFC-manager 5.6.0 / SketchUp 2026 (26.2.242) |
| Autor / organización | — / — |
| Fecha del archivo | 2026-06-23T11:53:44 |
| Vista (MVD) declarada | ViewDefinition [ReferenceView_V1.2] → [[MVD - Model View Definition]] |
| Unidad de longitud | millimetre |
| Disciplina inferida | **ARQ** → [[BIM 3D - Modelado]] |
| Elementos / tipos / espacios | 14 / 16 / 2 |

## 2. Estructura espacial → [[IFC - Estructura del esquema]]
- **Sitio**: environment - site
- **Sitio**: house - site
  - **Edificio**: Single-family house
    - Piso: 00 groundfloor (elevación 0.00)

## 3. Clases IFC presentes → [[Clases IFC principales]]
| Clase | Cantidad |
|---|---|
| [[Clases IFC principales#IfcWall|IfcWall]] | 4 |
| [[Clases IFC principales#IfcBuildingElementProxy|IfcBuildingElementProxy]] | 3 |
| [[Clases IFC principales#IfcSlab|IfcSlab]] | 3 |
| [[Clases IFC principales#IfcSite|IfcSite]] | 2 |
| [[Clases IFC principales#IfcSpace|IfcSpace]] | 2 |
| `IfcChimney` | 1 |
| [[Clases IFC principales#IfcRoof|IfcRoof]] | 1 |
| `IfcFurniture` | 1 |
| [[Clases IFC principales#IfcBuilding|IfcBuilding]] | 1 |
| [[Clases IFC principales#IfcBuildingStorey|IfcBuildingStorey]] | 1 |
| `IfcSpatialZone` | 1 |

**Mezcla por disciplina**: ARQ 8 · EST 0 · MEP 0 · INFRA 0

## 4. Información (datos) → [[LOIN - Nivel de Informacion Necesaria]]
- Materiales distintos: 8 → concrete_reinforced_in-situ, wood_mdf_plate, stone_sand-lime, gypsum_fiber-board_panel, composite_element_roof, bulk-material_sand-coarse_generic, virtual_white, virtual_black
- Conjuntos de cantidades (Qto): 7
- Clasificaciones: CCI Construction
- Property Sets más frecuentes:
  - `Pset_SlabCommon` × 2

## 5. Diagnóstico de calidad → [[Control de calidad de modelos BIM]]
- ⚠️ 3 `IfcBuildingElementProxy` (21% de los elementos): mapeo de clases IFC deficiente en la exportación → [[Control de calidad de modelos BIM]].
- ⚠️ 2 `IfcSite` en un solo modelo: probablemente familias exportadas con la clase IFC equivocada (revisar el mapeo de exportación) → [[Clases IFC principales]].
- ✅ Clasificación presente (CCI Construction) → [[Sistemas de clasificacion]].
- ✅ Todos los elementos revisados están contenidos en la estructura espacial.
- ✅ 7 conjuntos de cantidades (Qto) útiles para metrados → [[BIM 5D - Costos y metrados]].

## 6. Preguntas de estudio para JARVIS y para ti
1. ¿Qué [[Usos BIM]] permite este modelo con la información que contiene?
2. Redacta 3 reglas [[IDS - Information Delivery Specification]] que este modelo debería cumplir y verifica si las cumple.
3. ¿Cómo lo federarías con otras disciplinas? → [[Federacion de modelos]]
4. ¿Qué LOD aparente tienen sus elementos principales? → [[LOD - Nivel de Desarrollo]]

↑ [[MOC Proyectos de Estudio]] · [[Resumen de modelos de estudio]] · [[Indice de proyectos]]
