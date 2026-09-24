---
tipo: proyecto-estudio
esquema: IFC2X3
disciplina: EST
elementos_totales: 68
pisos: 0
espacios: 0
proxies: 9
tamano_mb: 0.8
archivo: "02_PROYECTOS_BIM/buildingSMART_Sample-Test-Files/IFC 2.3.0.1 (IFC 2x3 TC1)/Simple-Scene/Infra-Bridge.ifc"
software_origen: "BIM_Tools - Sketchup_IFC_manager - 5.6.0 · Sketchup-IFC-manager 5.6.0 / SketchUp 2026 (26.2.242)"
generado: 2026-09-24
tags: [proyecto, estudio, ifc]
---

# Estudio — Infra-Bridge - IFC 2.3.0.1 (IFC 2x3 TC1) - Simple-Scene

> [!info] Nota generada automáticamente por `scripts/03_ifc_a_obsidian.py`
> Modelo: `02_PROYECTOS_BIM/buildingSMART_Sample-Test-Files/IFC 2.3.0.1 (IFC 2x3 TC1)/Simple-Scene/Infra-Bridge.ifc` · 0.8 MB · esquema **IFC2x3 (ISO/PAS 16739:2005)** → [[IFC - ISO 16739]]

## 1. Ficha del modelo
| Campo | Valor |
|---|---|
| Proyecto (IfcProject) | ifc silly sample scene - project  |
| Software de origen | BIM_Tools - Sketchup_IFC_manager - 5.6.0 · Sketchup-IFC-manager 5.6.0 / SketchUp 2026 (26.2.242) |
| Autor / organización | — / — |
| Fecha del archivo | 2026-06-23T11:53:15 |
| Vista (MVD) declarada | ViewDefinition [CoordinationView_V2.0] → [[MVD - Model View Definition]] |
| Unidad de longitud | millimetre |
| Disciplina inferida | **EST** → [[MOC Ingenieria Estructural]] |
| Elementos / tipos / espacios | 68 / 13 / 0 |

## 2. Estructura espacial → [[IFC - Estructura del esquema]]
- **Sitio**: environment - site
  - **Edificio**: road river bridge
  - **Edificio**: rail bridge
  - **Edificio**: rail bridge

## 3. Clases IFC presentes → [[Clases IFC principales]]
| Clase | Cantidad |
|---|---|
| `IfcElementAssembly` | 20 |
| [[Clases IFC principales#IfcBuildingElementProxy|IfcBuildingElementProxy]] | 9 |
| [[Clases IFC principales#IfcBeam|IfcBeam]] | 8 |
| [[Clases IFC principales#IfcMember|IfcMember]] | 8 |
| [[Clases IFC principales#IfcColumn|IfcColumn]] | 7 |
| [[Clases IFC principales#IfcFooting|IfcFooting]] | 7 |
| [[Clases IFC principales#IfcWall|IfcWall]] | 4 |
| [[Clases IFC principales#IfcSlab|IfcSlab]] | 3 |
| [[Clases IFC principales#IfcBuilding|IfcBuilding]] | 3 |
| [[Clases IFC principales#IfcRailing|IfcRailing]] | 2 |
| [[Clases IFC principales#IfcSite|IfcSite]] | 1 |

**Mezcla por disciplina**: ARQ 6 · EST 30 · MEP 0 · INFRA 0

## 4. Información (datos) → [[LOIN - Nivel de Informacion Necesaria]]
- Materiales distintos: 7 → concrete_reinforced_in-situ, concrete_reinforced_prefab, wood-generic, stone_granite_masonry, metal_copper_generic, bulk-material_soil_generic, virtual_black
- Conjuntos de cantidades (Qto): 15
- Clasificaciones: ninguna
- Property Sets más frecuentes:

## 5. Diagnóstico de calidad → [[Control de calidad de modelos BIM]]
- ⚠️ 9 `IfcBuildingElementProxy` (13% de los elementos): mapeo de clases IFC deficiente en la exportación → [[Control de calidad de modelos BIM]].
- ⚠️ Sin `IfcBuildingStorey`: los elementos no están organizados por niveles (estructura espacial incompleta) → [[IFC - Estructura del esquema]].
- ⚠️ Sin `IfcClassification`: los elementos no llevan códigos Uniclass/OmniClass → [[Sistemas de clasificacion]].
- ✅ Todos los elementos revisados están contenidos en la estructura espacial.
- ℹ️ IFC2x3: sin georreferenciación completa (`IfcMapConversion` llega en IFC4) → [[BIM y GIS]].
- ✅ 15 conjuntos de cantidades (Qto) útiles para metrados → [[BIM 5D - Costos y metrados]].

## 6. Preguntas de estudio para JARVIS y para ti
1. ¿Qué [[Usos BIM]] permite este modelo con la información que contiene?
2. Redacta 3 reglas [[IDS - Information Delivery Specification]] que este modelo debería cumplir y verifica si las cumple.
3. ¿Cómo lo federarías con otras disciplinas? → [[Federacion de modelos]]
4. ¿Qué LOD aparente tienen sus elementos principales? → [[LOD - Nivel de Desarrollo]]

↑ [[MOC Proyectos de Estudio]] · [[Resumen de modelos de estudio]] · [[Indice de proyectos]]
