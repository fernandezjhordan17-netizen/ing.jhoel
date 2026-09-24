---
tipo: proyecto-estudio
esquema: IFC4X3
disciplina: MIXTO
elementos_totales: 6
pisos: 0
espacios: 0
proxies: 2
tamano_mb: 1.0
archivo: "02_PROYECTOS_BIM/buildingSMART_Sample-Test-Files/IFC 4.3.2.0 (IFC 4.3 ADD2)/Simple-Scene/Building-Landscaping.ifc"
software_origen: "BIM_Tools - Sketchup_IFC_manager - 5.6.0 · Sketchup-IFC-manager 5.6.0 / SketchUp 2026 (26.2.242)"
generado: 2026-09-24
tags: [proyecto, estudio, ifc]
---

# Estudio — Building-Landscaping - IFC 4.3.2.0 (IFC 4.3 ADD2) - Simple-Scene

> [!info] Nota generada automáticamente por `scripts/03_ifc_a_obsidian.py`
> Modelo: `02_PROYECTOS_BIM/buildingSMART_Sample-Test-Files/IFC 4.3.2.0 (IFC 4.3 ADD2)/Simple-Scene/Building-Landscaping.ifc` · 1.0 MB · esquema **IFC 4.3 (ISO 16739-1:2024)** → [[IFC - ISO 16739]]

## 1. Ficha del modelo
| Campo | Valor |
|---|---|
| Proyecto (IfcProject) | ifc silly sample scene - project  |
| Software de origen | BIM_Tools - Sketchup_IFC_manager - 5.6.0 · Sketchup-IFC-manager 5.6.0 / SketchUp 2026 (26.2.242) |
| Autor / organización | — / — |
| Fecha del archivo | 2026-06-23T11:54:06 |
| Vista (MVD) declarada | ViewDefinition [ReferenceView] → [[MVD - Model View Definition]] |
| Unidad de longitud | millimetre |
| Disciplina inferida | **MIXTO** → [[Federacion de modelos]] |
| Elementos / tipos / espacios | 6 / 6 / 0 |

## 2. Estructura espacial → [[IFC - Estructura del esquema]]
- **Sitio**: environment - site
- **Sitio**: house - site
  - **Edificio**: (sin IfcBuilding)

## 3. Clases IFC presentes → [[Clases IFC principales]]
| Clase | Cantidad |
|---|---|
| `IfcGeographicElement` | 4 |
| [[Clases IFC principales#IfcBuildingElementProxy|IfcBuildingElementProxy]] | 2 |
| [[Clases IFC principales#IfcSite|IfcSite]] | 2 |

**Mezcla por disciplina**: ARQ 0 · EST 0 · MEP 0 · INFRA 0

## 4. Información (datos) → [[LOIN - Nivel de Informacion Necesaria]]
- Materiales distintos: 6 → vegetation_grass, bulk-material_topsoil_generic, bulk-material_soil_generic, virtual_white, vegetation_generic, virtual_black
- Conjuntos de cantidades (Qto): 0
- Clasificaciones: CCI Construction
- Property Sets más frecuentes:

## 5. Diagnóstico de calidad → [[Control de calidad de modelos BIM]]
- ⚠️ 2 `IfcBuildingElementProxy` (33% de los elementos): mapeo de clases IFC deficiente en la exportación → [[Control de calidad de modelos BIM]].
- ⚠️ 2 `IfcSite` en un solo modelo: probablemente familias exportadas con la clase IFC equivocada (revisar el mapeo de exportación) → [[Clases IFC principales]].
- ⚠️ Sin `IfcBuildingStorey`: los elementos no están organizados por niveles (estructura espacial incompleta) → [[IFC - Estructura del esquema]].
- ✅ Clasificación presente (CCI Construction) → [[Sistemas de clasificacion]].
- ✅ Todos los elementos revisados están contenidos en la estructura espacial.
- ℹ️ Sin `IfcElementQuantity` (Qto): los metrados deberán calcularse desde la geometría → [[BIM 5D - Costos y metrados]].

## 6. Preguntas de estudio para JARVIS y para ti
1. ¿Qué [[Usos BIM]] permite este modelo con la información que contiene?
2. Redacta 3 reglas [[IDS - Information Delivery Specification]] que este modelo debería cumplir y verifica si las cumple.
3. ¿Cómo lo federarías con otras disciplinas? → [[Federacion de modelos]]
4. ¿Qué LOD aparente tienen sus elementos principales? → [[LOD - Nivel de Desarrollo]]

↑ [[MOC Proyectos de Estudio]] · [[Resumen de modelos de estudio]] · [[Indice de proyectos]]
