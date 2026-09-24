---
tipo: proyecto-estudio
esquema: IFC2X3
disciplina: MEP
elementos_totales: 487
pisos: 3
espacios: 37
proxies: 0
tamano_mb: 8.4
archivo: "02_PROYECTOS_BIM/IfcSampleFiles/Ifc2x3_Duplex_Mechanical.ifc"
software_origen: "20100903_2115(x64) · Autodesk Revit MEP 2011 - 1.0"
generado: 2026-09-24
tags: [proyecto, estudio, ifc]
---

# Estudio — Ifc2x3_Duplex_Mechanical

> [!info] Nota generada automáticamente por `scripts/03_ifc_a_obsidian.py`
> Modelo: `02_PROYECTOS_BIM/IfcSampleFiles/Ifc2x3_Duplex_Mechanical.ifc` · 8.4 MB · esquema **IFC2x3 (ISO/PAS 16739:2005)** → [[IFC - ISO 16739]]

## 1. Ficha del modelo
| Campo | Valor |
|---|---|
| Proyecto (IfcProject) | 0001 — Duplex Apartment |
| Software de origen | 20100903_2115(x64) · Autodesk Revit MEP 2011 - 1.0 |
| Autor / organización | — / — |
| Fecha del archivo | 2011-10-24T08:49:50 |
| Vista (MVD) declarada | ViewDefinition [CoordinationView] → [[MVD - Model View Definition]] |
| Unidad de longitud | metre |
| Disciplina inferida | **MEP** → [[Coordinacion BIM y deteccion de interferencias]] |
| Elementos / tipos / espacios | 487 / 55 / 37 |

## 2. Estructura espacial → [[IFC - Estructura del esquema]]
- **Sitio**: Default (lat 41°52'41", lon -87°37'47")
  - **Edificio**: (sin nombre)
    - Piso: Level 1 (elevación 0.00)
    - Piso: Level 2 (elevación 3.10)
    - Piso: Roof (elevación 6.00)

## 3. Clases IFC presentes → [[Clases IFC principales]]
| Clase | Cantidad |
|---|---|
| [[Clases IFC principales#IfcFlowSegment|IfcFlowSegment]] | 246 |
| [[Clases IFC principales#IfcFlowFitting|IfcFlowFitting]] | 207 |
| [[Clases IFC principales#IfcSpace|IfcSpace]] | 37 |
| `IfcEnergyConversionDevice` | 22 |
| `IfcFlowController` | 8 |
| `IfcFlowMovingDevice` | 4 |
| [[Clases IFC principales#IfcBuildingStorey|IfcBuildingStorey]] | 3 |
| [[Clases IFC principales#IfcBuilding|IfcBuilding]] | 1 |
| [[Clases IFC principales#IfcSite|IfcSite]] | 1 |

**Mezcla por disciplina**: ARQ 37 · EST 0 · MEP 487 · INFRA 0

## 4. Información (datos) → [[LOIN - Nivel de Informacion Necesaria]]
- Materiales distintos: 0 → —
- Conjuntos de cantidades (Qto): 37
- Clasificaciones: ninguna
- Property Sets más frecuentes:
  - `PSet_Revit_Identity Data` × 527
  - `PSet_Revit_Constraints` × 527
  - `PSet_Revit_Phasing` × 524
  - `PSet_Revit_Dimensions` × 518
  - `PSet_Revit_Mechanical` × 487
  - `PSet_Revit_Other` × 426
  - `PSet_Revit_Graphics` × 215
  - `Pset_SpaceCommon` × 37
  - `PSet_Revit_Electrical - Loads` × 24
  - `PSet_Revit_Mechanical - Airflow` × 22
  - `PSet_Revit_Mechanical - Loads` × 20
  - `PSet_Revit_Energy Analysis` × 18

## 5. Diagnóstico de calidad → [[Control de calidad de modelos BIM]]
- ✅ Pocos o ningún proxy: la exportación usa clases IFC específicas → [[Clases IFC principales]].
- ⚠️ Sin `IfcClassification`: los elementos no llevan códigos Uniclass/OmniClass → [[Sistemas de clasificacion]].
- ✅ Todos los elementos revisados están contenidos en la estructura espacial.
- ℹ️ IFC2x3: sin georreferenciación completa (`IfcMapConversion` llega en IFC4) → [[BIM y GIS]].
- ✅ 37 conjuntos de cantidades (Qto) útiles para metrados → [[BIM 5D - Costos y metrados]].

## 6. Preguntas de estudio para JARVIS y para ti
1. ¿Qué [[Usos BIM]] permite este modelo con la información que contiene?
2. Redacta 3 reglas [[IDS - Information Delivery Specification]] que este modelo debería cumplir y verifica si las cumple.
3. ¿Cómo lo federarías con otras disciplinas? → [[Federacion de modelos]]
4. ¿Qué LOD aparente tienen sus elementos principales? → [[LOD - Nivel de Desarrollo]]

↑ [[MOC Proyectos de Estudio]] · [[Resumen de modelos de estudio]] · [[Indice de proyectos]]
