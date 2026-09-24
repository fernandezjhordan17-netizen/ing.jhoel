---
tipo: proyecto-estudio
esquema: IFC4X3
disciplina: EST
elementos_totales: 111
pisos: 0
espacios: 0
proxies: 5
tamano_mb: 2.2
archivo: "02_PROYECTOS_BIM/buildingSMART_Sample-Test-Files/IFC 4.3.2.0 (IFC 4.3 ADD2)/Simple-Scene/Infra-Landscaping.ifc"
software_origen: "BIM_Tools - Sketchup_IFC_manager - 5.6.0 · Sketchup-IFC-manager 5.6.0 / SketchUp 2026 (26.2.242)"
generado: 2026-09-24
tags: [proyecto, estudio, ifc]
---

# Estudio — Infra-Landscaping - IFC 4.3.2.0 (IFC 4.3 ADD2) - Simple-Scene

> [!info] Nota generada automáticamente por `scripts/03_ifc_a_obsidian.py`
> Modelo: `02_PROYECTOS_BIM/buildingSMART_Sample-Test-Files/IFC 4.3.2.0 (IFC 4.3 ADD2)/Simple-Scene/Infra-Landscaping.ifc` · 2.2 MB · esquema **IFC 4.3 (ISO 16739-1:2024)** → [[IFC - ISO 16739]]

## 1. Ficha del modelo
| Campo | Valor |
|---|---|
| Proyecto (IfcProject) | ifc silly sample scene - project  |
| Software de origen | BIM_Tools - Sketchup_IFC_manager - 5.6.0 · Sketchup-IFC-manager 5.6.0 / SketchUp 2026 (26.2.242) |
| Autor / organización | — / — |
| Fecha del archivo | 2026-06-23T11:54:07 |
| Vista (MVD) declarada | ViewDefinition [ReferenceView] → [[MVD - Model View Definition]] |
| Unidad de longitud | millimetre |
| Disciplina inferida | **EST** → [[MOC Ingenieria Estructural]] |
| Elementos / tipos / espacios | 111 / 24 / 0 |

## 2. Estructura espacial → [[IFC - Estructura del esquema]]
- **Sitio**: environment - site
- **Sitio**: park - site
- **Sitio**: road parking - site
- **Sitio**: road river bridge - site
- **Sitio**: rail river bridge - site
- **Sitio**: road rail bridge - site
- **Sitio**: meadow - site
- **Sitio**: road - site
  - **Edificio**: (sin IfcBuilding)

## 3. Clases IFC presentes → [[Clases IFC principales]]
| Clase | Cantidad |
|---|---|
| `IfcGeographicElement` | 76 |
| [[Clases IFC principales#IfcMember|IfcMember]] | 10 |
| `IfcElementAssembly` | 10 |
| `IfcSign` | 10 |
| [[Clases IFC principales#IfcSite|IfcSite]] | 8 |
| [[Clases IFC principales#IfcBuildingElementProxy|IfcBuildingElementProxy]] | 5 |

**Mezcla por disciplina**: ARQ 0 · EST 10 · MEP 0 · INFRA 0

## 4. Información (datos) → [[LOIN - Nivel de Informacion Necesaria]]
- Materiales distintos: 11 → bulk-material_soil_generic, vegetation_grass, vegetation_generic, vegetation_apple, bulk-material_topsoil_generic, Default, metal_steel-galvanized, metal_aluminum_sheet_coated-green, bulk-material_water_surfacewater, bulk-material_sand_generic, virtual_black
- Conjuntos de cantidades (Qto): 0
- Clasificaciones: CCI Construction, Fruit and vegetables
- Property Sets más frecuentes:
  - `SizeSet` × 1

## 5. Diagnóstico de calidad → [[Control de calidad de modelos BIM]]
- ✅ Pocos o ningún proxy: la exportación usa clases IFC específicas → [[Clases IFC principales]].
- ⚠️ 8 `IfcSite` en un solo modelo: probablemente familias exportadas con la clase IFC equivocada (revisar el mapeo de exportación) → [[Clases IFC principales]].
- ⚠️ Sin `IfcBuildingStorey`: los elementos no están organizados por niveles (estructura espacial incompleta) → [[IFC - Estructura del esquema]].
- ✅ Clasificación presente (CCI Construction, Fruit and vegetables) → [[Sistemas de clasificacion]].
- ✅ Todos los elementos revisados están contenidos en la estructura espacial.
- ℹ️ Sin `IfcElementQuantity` (Qto): los metrados deberán calcularse desde la geometría → [[BIM 5D - Costos y metrados]].

## 6. Preguntas de estudio para JARVIS y para ti
1. ¿Qué [[Usos BIM]] permite este modelo con la información que contiene?
2. Redacta 3 reglas [[IDS - Information Delivery Specification]] que este modelo debería cumplir y verifica si las cumple.
3. ¿Cómo lo federarías con otras disciplinas? → [[Federacion de modelos]]
4. ¿Qué LOD aparente tienen sus elementos principales? → [[LOD - Nivel de Desarrollo]]

↑ [[MOC Proyectos de Estudio]] · [[Resumen de modelos de estudio]] · [[Indice de proyectos]]
