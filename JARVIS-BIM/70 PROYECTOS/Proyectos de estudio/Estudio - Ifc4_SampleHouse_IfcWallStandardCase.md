---
tipo: proyecto-estudio
esquema: IFC4
disciplina: ARQ
elementos_totales: 2
pisos: 1
espacios: 0
proxies: 0
tamano_mb: 0.0
archivo: "02_PROYECTOS_BIM/IfcSampleFiles/Ifc4_SampleHouse_IfcWallStandardCase.ifc"
software_origen: "Ifc.Toolbox v3.9 - BIM Mars · Xbim File Processor version 4.0.0.0"
generado: 2026-09-24
tags: [proyecto, estudio, ifc]
---

# Estudio — Ifc4_SampleHouse_IfcWallStandardCase

> [!info] Nota generada automáticamente por `scripts/03_ifc_a_obsidian.py`
> Modelo: `02_PROYECTOS_BIM/IfcSampleFiles/Ifc4_SampleHouse_IfcWallStandardCase.ifc` · 0.0 MB · esquema **IFC4 (ISO 16739-1:2018)** → [[IFC - ISO 16739]]

## 1. Ficha del modelo
| Campo | Valor |
|---|---|
| Proyecto (IfcProject) | Project Number — Project Name |
| Software de origen | Ifc.Toolbox v3.9 - BIM Mars · Xbim File Processor version 4.0.0.0 |
| Autor / organización | — / — |
| Fecha del archivo | 2016-11-11T10:59:10 |
| Vista (MVD) declarada | — → [[MVD - Model View Definition]] |
| Unidad de longitud | millimetre |
| Disciplina inferida | **ARQ** → [[BIM 3D - Modelado]] |
| Elementos / tipos / espacios | 2 / 1 / 0 |

## 2. Estructura espacial → [[IFC - Estructura del esquema]]
- **Sitio**: Default (lat 51°30'0", lon -0°7'34")
  - **Edificio**: (sin nombre)
    - Piso: Ground Floor (elevación 0.00)

## 3. Clases IFC presentes → [[Clases IFC principales]]
| Clase | Cantidad |
|---|---|
| [[Clases IFC principales#IfcWall|IfcWallStandardCase]] | 2 |
| [[Clases IFC principales#IfcOpeningElement|IfcOpeningElement]] | 2 |
| [[Clases IFC principales#IfcBuilding|IfcBuilding]] | 1 |
| [[Clases IFC principales#IfcBuildingStorey|IfcBuildingStorey]] | 1 |
| [[Clases IFC principales#IfcSite|IfcSite]] | 1 |

**Mezcla por disciplina**: ARQ 2 · EST 0 · MEP 0 · INFRA 0

## 4. Información (datos) → [[LOIN - Nivel de Informacion Necesaria]]
- Materiales distintos: 2 → Plaster, Metal Stud Layer
- Conjuntos de cantidades (Qto): 4
- Clasificaciones: ninguna
- Property Sets más frecuentes:
  - `Other` × 7
  - `Identity Data` × 5
  - `Constraints` × 4
  - `Dimensions` × 3
  - `Phasing` × 2
  - `Structural` × 2
  - `Pset_WallCommon` × 2
  - `Graphics` × 2
  - `Pset_BuildingStoreyCommon` × 1
  - `Pset_BuildingCommon` × 1
  - `Analytical Properties` × 1
  - `Construction` × 1

## 5. Diagnóstico de calidad → [[Control de calidad de modelos BIM]]
- ✅ Pocos o ningún proxy: la exportación usa clases IFC específicas → [[Clases IFC principales]].
- ⚠️ Sin `IfcClassification`: los elementos no llevan códigos Uniclass/OmniClass → [[Sistemas de clasificacion]].
- ✅ Todos los elementos revisados están contenidos en la estructura espacial.
- ℹ️ Sin `IfcMapConversion`: el modelo no está georreferenciado → [[BIM y GIS]].
- ✅ 4 conjuntos de cantidades (Qto) útiles para metrados → [[BIM 5D - Costos y metrados]].

## 6. Preguntas de estudio para JARVIS y para ti
1. ¿Qué [[Usos BIM]] permite este modelo con la información que contiene?
2. Redacta 3 reglas [[IDS - Information Delivery Specification]] que este modelo debería cumplir y verifica si las cumple.
3. ¿Cómo lo federarías con otras disciplinas? → [[Federacion de modelos]]
4. ¿Qué LOD aparente tienen sus elementos principales? → [[LOD - Nivel de Desarrollo]]

↑ [[MOC Proyectos de Estudio]] · [[Resumen de modelos de estudio]] · [[Indice de proyectos]]
