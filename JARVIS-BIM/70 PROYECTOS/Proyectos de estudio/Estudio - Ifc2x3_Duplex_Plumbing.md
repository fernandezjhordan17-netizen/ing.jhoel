---
tipo: proyecto-estudio
esquema: IFC2X3
disciplina: MEP
elementos_totales: 1468
pisos: 3
espacios: 1
proxies: 0
tamano_mb: 30.1
archivo: "02_PROYECTOS_BIM/IfcSampleFiles/Ifc2x3_Duplex_Plumbing.ifc"
software_origen: "20121003_2115(x64) · Autodesk Revit 2013"
generado: 2026-09-24
tags: [proyecto, estudio, ifc]
---

# Estudio — Ifc2x3_Duplex_Plumbing

> [!info] Nota generada automáticamente por `scripts/03_ifc_a_obsidian.py`
> Modelo: `02_PROYECTOS_BIM/IfcSampleFiles/Ifc2x3_Duplex_Plumbing.ifc` · 30.1 MB · esquema **IFC2x3 (ISO/PAS 16739:2005)** → [[IFC - ISO 16739]]

## 1. Ficha del modelo
| Campo | Valor |
|---|---|
| Proyecto (IfcProject) | 0001 — Duplex Apartment |
| Software de origen | 20121003_2115(x64) · Autodesk Revit 2013 |
| Autor / organización | — / — |
| Fecha del archivo | 2012-12-18T09:56:57 |
| Vista (MVD) declarada | ViewDefinition [CoordinationView] → [[MVD - Model View Definition]] |
| Unidad de longitud | millimetre |
| Disciplina inferida | **MEP** → [[Coordinacion BIM y deteccion de interferencias]] |
| Elementos / tipos / espacios | 1468 / 73 / 1 |

## 2. Estructura espacial → [[IFC - Estructura del esquema]]
- **Sitio**: Default (lat 41°52'27", lon -87°38'21")
  - **Edificio**: XYZ
    - Piso: Level 1 (elevación 0.00)
    - Piso: Level 2 (elevación 3100.00)
    - Piso: Roof (elevación 6000.00)

## 3. Clases IFC presentes → [[Clases IFC principales]]
| Clase | Cantidad |
|---|---|
| `IfcDistributionPort` | 970 |
| [[Clases IFC principales#IfcFlowSegment|IfcFlowSegment]] | 231 |
| [[Clases IFC principales#IfcFlowFitting|IfcFlowFitting]] | 227 |
| `IfcFlowController` | 20 |
| [[Clases IFC principales#IfcFlowTerminal|IfcFlowTerminal]] | 16 |
| [[Clases IFC principales#IfcBuildingStorey|IfcBuildingStorey]] | 3 |
| `IfcEnergyConversionDevice` | 2 |
| `IfcFlowMovingDevice` | 2 |
| [[Clases IFC principales#IfcBuilding|IfcBuilding]] | 1 |
| [[Clases IFC principales#IfcSite|IfcSite]] | 1 |
| [[Clases IFC principales#IfcSpace|IfcSpace]] | 1 |

**Mezcla por disciplina**: ARQ 1 · EST 0 · MEP 1468 · INFRA 0

## 4. Información (datos) → [[LOIN - Nivel de Informacion Necesaria]]
- Materiales distintos: 3 → Chrome - DELTA - Polished, Metal - Delta - Aged Pewter - PT, Metal-Copper Piping
- Conjuntos de cantidades (Qto): 1
- Clasificaciones: UniFormat
- Property Sets más frecuentes:
  - `Other` × 526
  - `Identity Data` × 526
  - `Mechanical` × 511
  - `Constraints` × 509
  - `Phasing` × 499
  - `Text` × 486
  - `Dimensions` × 485
  - `Insulation` × 464
  - `Graphics` × 234
  - `Mechanical - Flow` × 231
  - `Plumbing` × 18
  - `Electrical - Loads` × 6

## 5. Diagnóstico de calidad → [[Control de calidad de modelos BIM]]
- ✅ Pocos o ningún proxy: la exportación usa clases IFC específicas → [[Clases IFC principales]].
- ✅ Clasificación presente (UniFormat) → [[Sistemas de clasificacion]].
- ✅ Todos los elementos revisados están contenidos en la estructura espacial.
- ℹ️ IFC2x3: sin georreferenciación completa (`IfcMapConversion` llega en IFC4) → [[BIM y GIS]].
- ✅ 1 conjuntos de cantidades (Qto) útiles para metrados → [[BIM 5D - Costos y metrados]].

## 6. Preguntas de estudio para JARVIS y para ti
1. ¿Qué [[Usos BIM]] permite este modelo con la información que contiene?
2. Redacta 3 reglas [[IDS - Information Delivery Specification]] que este modelo debería cumplir y verifica si las cumple.
3. ¿Cómo lo federarías con otras disciplinas? → [[Federacion de modelos]]
4. ¿Qué LOD aparente tienen sus elementos principales? → [[LOD - Nivel de Desarrollo]]

↑ [[MOC Proyectos de Estudio]] · [[Resumen de modelos de estudio]] · [[Indice de proyectos]]
