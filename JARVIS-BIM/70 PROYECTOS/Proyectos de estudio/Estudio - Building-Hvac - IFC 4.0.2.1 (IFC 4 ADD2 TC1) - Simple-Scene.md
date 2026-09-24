---
tipo: proyecto-estudio
esquema: IFC4
disciplina: MEP
elementos_totales: 6
pisos: 1
espacios: 0
proxies: 2
tamano_mb: 0.1
archivo: "02_PROYECTOS_BIM/buildingSMART_Sample-Test-Files/IFC 4.0.2.1 (IFC 4 ADD2 TC1)/Simple-Scene/Building-Hvac.ifc"
software_origen: "BIM_Tools - Sketchup_IFC_manager - 5.6.0 · Sketchup-IFC-manager 5.6.0 / SketchUp 2026 (26.2.242)"
generado: 2026-09-24
tags: [proyecto, estudio, ifc]
---

# Estudio — Building-Hvac - IFC 4.0.2.1 (IFC 4 ADD2 TC1) - Simple-Scene

> [!info] Nota generada automáticamente por `scripts/03_ifc_a_obsidian.py`
> Modelo: `02_PROYECTOS_BIM/buildingSMART_Sample-Test-Files/IFC 4.0.2.1 (IFC 4 ADD2 TC1)/Simple-Scene/Building-Hvac.ifc` · 0.1 MB · esquema **IFC4 (ISO 16739-1:2018)** → [[IFC - ISO 16739]]

## 1. Ficha del modelo
| Campo | Valor |
|---|---|
| Proyecto (IfcProject) | ifc silly sample scene - project  |
| Software de origen | BIM_Tools - Sketchup_IFC_manager - 5.6.0 · Sketchup-IFC-manager 5.6.0 / SketchUp 2026 (26.2.242) |
| Autor / organización | — / — |
| Fecha del archivo | 2026-06-23T11:53:44 |
| Vista (MVD) declarada | ViewDefinition [ReferenceView_V1.2] → [[MVD - Model View Definition]] |
| Unidad de longitud | millimetre |
| Disciplina inferida | **MEP** → [[Coordinacion BIM y deteccion de interferencias]] |
| Elementos / tipos / espacios | 6 / 6 / 0 |

## 2. Estructura espacial → [[IFC - Estructura del esquema]]
- **Sitio**: environment - site
- **Sitio**: house - site
  - **Edificio**: Single-family house
    - Piso: 00 groundfloor (elevación 0.00)

## 3. Clases IFC presentes → [[Clases IFC principales]]
| Clase | Cantidad |
|---|---|
| [[Clases IFC principales#IfcBuildingElementProxy|IfcBuildingElementProxy]] | 2 |
| `IfcAirTerminal` | 2 |
| [[Clases IFC principales#IfcSite|IfcSite]] | 2 |
| `IfcChimney` | 1 |
| `IfcDuctSegment` | 1 |
| [[Clases IFC principales#IfcBuilding|IfcBuilding]] | 1 |
| [[Clases IFC principales#IfcBuildingStorey|IfcBuildingStorey]] | 1 |

**Mezcla por disciplina**: ARQ 0 · EST 0 · MEP 3 · INFRA 0

## 4. Información (datos) → [[LOIN - Nivel de Informacion Necesaria]]
- Materiales distintos: 6 → stone_sand-lime, metal_steel_generic_coated-anthracitegrey, metal_steel-galvanized, concrete_reinforced_prefab, virtual_white, virtual_black
- Conjuntos de cantidades (Qto): 0
- Clasificaciones: CCI Construction
- Property Sets más frecuentes:

## 5. Diagnóstico de calidad → [[Control de calidad de modelos BIM]]
- ⚠️ 2 `IfcBuildingElementProxy` (33% de los elementos): mapeo de clases IFC deficiente en la exportación → [[Control de calidad de modelos BIM]].
- ⚠️ 2 `IfcSite` en un solo modelo: probablemente familias exportadas con la clase IFC equivocada (revisar el mapeo de exportación) → [[Clases IFC principales]].
- ✅ Clasificación presente (CCI Construction) → [[Sistemas de clasificacion]].
- ✅ Todos los elementos revisados están contenidos en la estructura espacial.
- ℹ️ Sin `IfcElementQuantity` (Qto): los metrados deberán calcularse desde la geometría → [[BIM 5D - Costos y metrados]].

## 6. Preguntas de estudio para JARVIS y para ti
1. ¿Qué [[Usos BIM]] permite este modelo con la información que contiene?
2. Redacta 3 reglas [[IDS - Information Delivery Specification]] que este modelo debería cumplir y verifica si las cumple.
3. ¿Cómo lo federarías con otras disciplinas? → [[Federacion de modelos]]
4. ¿Qué LOD aparente tienen sus elementos principales? → [[LOD - Nivel de Desarrollo]]

↑ [[MOC Proyectos de Estudio]] · [[Resumen de modelos de estudio]] · [[Indice de proyectos]]
