---
tipo: proyecto-estudio
esquema: IFC4X3
disciplina: MEP
elementos_totales: 29
pisos: 0
espacios: 0
proxies: 1
tamano_mb: 0.3
archivo: "02_PROYECTOS_BIM/buildingSMART_Sample-Test-Files/IFC 4.3.2.0 (IFC 4.3 ADD2)/Simple-Scene/Infra-Plumbing.ifc"
software_origen: "BIM_Tools - Sketchup_IFC_manager - 5.6.0 · Sketchup-IFC-manager 5.6.0 / SketchUp 2026 (26.2.242)"
generado: 2026-09-24
tags: [proyecto, estudio, ifc]
---

# Estudio — Infra-Plumbing - IFC 4.3.2.0 (IFC 4.3 ADD2) - Simple-Scene

> [!info] Nota generada automáticamente por `scripts/03_ifc_a_obsidian.py`
> Modelo: `02_PROYECTOS_BIM/buildingSMART_Sample-Test-Files/IFC 4.3.2.0 (IFC 4.3 ADD2)/Simple-Scene/Infra-Plumbing.ifc` · 0.3 MB · esquema **IFC 4.3 (ISO 16739-1:2024)** → [[IFC - ISO 16739]]

## 1. Ficha del modelo
| Campo | Valor |
|---|---|
| Proyecto (IfcProject) | ifc silly sample scene - project  |
| Software de origen | BIM_Tools - Sketchup_IFC_manager - 5.6.0 · Sketchup-IFC-manager 5.6.0 / SketchUp 2026 (26.2.242) |
| Autor / organización | — / — |
| Fecha del archivo | 2026-06-23T11:54:08 |
| Vista (MVD) declarada | ViewDefinition [ReferenceView] → [[MVD - Model View Definition]] |
| Unidad de longitud | millimetre |
| Disciplina inferida | **MEP** → [[Coordinacion BIM y deteccion de interferencias]] |
| Elementos / tipos / espacios | 29 / 4 / 0 |

## 2. Estructura espacial → [[IFC - Estructura del esquema]]
- **Sitio**: environment - site
- **Sitio**: road parking - site
- **Sitio**: road river bridge - site
- **Sitio**: rail river bridge - site
- **Sitio**: road rail bridge - site
- **Sitio**: road - site
  - **Edificio**: (sin IfcBuilding)

## 3. Clases IFC presentes → [[Clases IFC principales]]
| Clase | Cantidad |
|---|---|
| `IfcPipeSegment` | 24 |
| [[Clases IFC principales#IfcSite|IfcSite]] | 6 |
| [[Clases IFC principales#IfcBridge|IfcBridge]] | 3 |
| `IfcDistributionChamberElement` | 2 |
| `IfcElementAssembly` | 2 |
| [[Clases IFC principales#IfcBuildingElementProxy|IfcBuildingElementProxy]] | 1 |

**Mezcla por disciplina**: ARQ 0 · EST 0 · MEP 26 · INFRA 3

## 4. Información (datos) → [[LOIN - Nivel de Informacion Necesaria]]
- Materiales distintos: 3 → concrete_reinforced_prefab, Default, virtual_black
- Conjuntos de cantidades (Qto): 0
- Clasificaciones: ninguna
- Property Sets más frecuentes:

## 5. Diagnóstico de calidad → [[Control de calidad de modelos BIM]]
- ✅ Pocos o ningún proxy: la exportación usa clases IFC específicas → [[Clases IFC principales]].
- ⚠️ 6 `IfcSite` en un solo modelo: probablemente familias exportadas con la clase IFC equivocada (revisar el mapeo de exportación) → [[Clases IFC principales]].
- ⚠️ Sin `IfcBuildingStorey`: los elementos no están organizados por niveles (estructura espacial incompleta) → [[IFC - Estructura del esquema]].
- ⚠️ Sin `IfcClassification`: los elementos no llevan códigos Uniclass/OmniClass → [[Sistemas de clasificacion]].
- ✅ Todos los elementos revisados están contenidos en la estructura espacial.
- ℹ️ Sin `IfcElementQuantity` (Qto): los metrados deberán calcularse desde la geometría → [[BIM 5D - Costos y metrados]].

## 6. Preguntas de estudio para JARVIS y para ti
1. ¿Qué [[Usos BIM]] permite este modelo con la información que contiene?
2. Redacta 3 reglas [[IDS - Information Delivery Specification]] que este modelo debería cumplir y verifica si las cumple.
3. ¿Cómo lo federarías con otras disciplinas? → [[Federacion de modelos]]
4. ¿Qué LOD aparente tienen sus elementos principales? → [[LOD - Nivel de Desarrollo]]

↑ [[MOC Proyectos de Estudio]] · [[Resumen de modelos de estudio]] · [[Indice de proyectos]]
