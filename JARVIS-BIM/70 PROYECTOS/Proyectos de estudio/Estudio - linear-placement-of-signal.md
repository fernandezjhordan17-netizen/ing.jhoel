---
tipo: proyecto-estudio
esquema: IFC4X3
disciplina: INFRA
elementos_totales: 2
pisos: 0
espacios: 0
proxies: 0
tamano_mb: 0.2
archivo: "02_PROYECTOS_BIM/buildingSMART_IFC4.3_sample-models/models/alignment-geometries-and-linear-positioning/linear-placement-of-signal/linear-placement-of-signal.ifc"
software_origen: "redacted - redacted - 3.14159 · redacted"
generado: 2026-09-24
tags: [proyecto, estudio, ifc]
---

# Estudio — linear-placement-of-signal

> [!info] Nota generada automáticamente por `scripts/03_ifc_a_obsidian.py`
> Modelo: `02_PROYECTOS_BIM/buildingSMART_IFC4.3_sample-models/models/alignment-geometries-and-linear-positioning/linear-placement-of-signal/linear-placement-of-signal.ifc` · 0.2 MB · esquema **IFC 4.3 (ISO 16739-1:2024)** → [[IFC - ISO 16739]]

## 1. Ficha del modelo
| Campo | Valor |
|---|---|
| Proyecto (IfcProject) | Stationing  |
| Software de origen | redacted - redacted - 3.14159 · redacted |
| Autor / organización | redacted / redacted |
| Fecha del archivo | 2023-07-11T10:16:10 |
| Vista (MVD) declarada | ViewDefinition [Alignment-basedView] → [[MVD - Model View Definition]] |
| Unidad de longitud | metre |
| Disciplina inferida | **INFRA** → [[BIM para infraestructura]] |
| Elementos / tipos / espacios | 2 / 1 / 0 |

## 2. Estructura espacial → [[IFC - Estructura del esquema]]
- **Sitio**: Default Site Name
  - **Edificio**: (sin IfcBuilding)

## 3. Clases IFC presentes → [[Clases IFC principales]]
| Clase | Cantidad |
|---|---|
| `IfcAlignmentSegment` | 26 |
| `IfcReferent` | 23 |
| `IfcSignal` | 2 |
| `IfcAlignmentCant` | 1 |
| `IfcAlignmentHorizontal` | 1 |
| `IfcAlignmentVertical` | 1 |
| [[Clases IFC principales#IfcAlignment|IfcAlignment]] | 1 |
| [[Clases IFC principales#IfcRailway|IfcRailway]] | 1 |
| [[Clases IFC principales#IfcSite|IfcSite]] | 1 |

**Mezcla por disciplina**: ARQ 0 · EST 0 · MEP 0 · INFRA 2

## 4. Información (datos) → [[LOIN - Nivel de Informacion Necesaria]]
- Materiales distintos: 0 → —
- Conjuntos de cantidades (Qto): 0
- Clasificaciones: ninguna
- Property Sets más frecuentes:
  - `Pset_Stationing` × 23

## 5. Diagnóstico de calidad → [[Control de calidad de modelos BIM]]
- ✅ Pocos o ningún proxy: la exportación usa clases IFC específicas → [[Clases IFC principales]].
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
