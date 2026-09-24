---
tipo: proyecto-estudio
esquema: IFC4
disciplina: ARQ
elementos_totales: 2
pisos: 1
espacios: 0
proxies: 0
tamano_mb: 0.1
archivo: "02_PROYECTOS_BIM/IfcSampleFiles/Ifc4_SampleHouse_1_Roof.ifc"
software_origen: "Ifc.Toolbox v3.9 - BIM Mars · Xbim File Processor version 4.0.0.0"
generado: 2026-09-24
tags: [proyecto, estudio, ifc]
---

# Estudio — Ifc4_SampleHouse_1_Roof

> [!info] Nota generada automáticamente por `scripts/03_ifc_a_obsidian.py`
> Modelo: `02_PROYECTOS_BIM/IfcSampleFiles/Ifc4_SampleHouse_1_Roof.ifc` · 0.1 MB · esquema **IFC4 (ISO 16739-1:2018)** → [[IFC - ISO 16739]]

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
| Elementos / tipos / espacios | 2 / 0 / 0 |

## 2. Estructura espacial → [[IFC - Estructura del esquema]]
- **Sitio**: Default (lat 51°30'0", lon -0°7'34")
  - **Edificio**: (sin nombre)
    - Piso: Roof (elevación 2500.00)

## 3. Clases IFC presentes → [[Clases IFC principales]]
| Clase | Cantidad |
|---|---|
| [[Clases IFC principales#IfcRoof|IfcRoof]] | 1 |
| [[Clases IFC principales#IfcSlab|IfcSlab]] | 1 |
| [[Clases IFC principales#IfcBuilding|IfcBuilding]] | 1 |
| [[Clases IFC principales#IfcBuildingStorey|IfcBuildingStorey]] | 1 |
| [[Clases IFC principales#IfcSite|IfcSite]] | 1 |

**Mezcla por disciplina**: ARQ 1 · EST 0 · MEP 0 · INFRA 0

## 4. Información (datos) → [[LOIN - Nivel de Informacion Necesaria]]
- Materiales distintos: 2 → Concrete, Sand/Cement Screed, Concrete Masonry, Floor Block
- Conjuntos de cantidades (Qto): 1
- Clasificaciones: ninguna
- Property Sets más frecuentes:
  - `Other` × 8
  - `Identity Data` × 6
  - `Constraints` × 4
  - `Construction` × 3
  - `Dimensions` × 3
  - `Graphics` × 3
  - `Phasing` × 2
  - `Analytical Properties` × 2
  - `Pset_RoofCommon` × 1
  - `Pset_SlabCommon` × 1
  - `Structural` × 1
  - `Materials and Finishes` × 1

## 5. Diagnóstico de calidad → [[Control de calidad de modelos BIM]]
- ✅ Pocos o ningún proxy: la exportación usa clases IFC específicas → [[Clases IFC principales]].
- ⚠️ Sin `IfcClassification`: los elementos no llevan códigos Uniclass/OmniClass → [[Sistemas de clasificacion]].
- ✅ Todos los elementos revisados están contenidos en la estructura espacial.
- ℹ️ Sin `IfcMapConversion`: el modelo no está georreferenciado → [[BIM y GIS]].
- ✅ 1 conjuntos de cantidades (Qto) útiles para metrados → [[BIM 5D - Costos y metrados]].

## 6. Preguntas de estudio para JARVIS y para ti
1. ¿Qué [[Usos BIM]] permite este modelo con la información que contiene?
2. Redacta 3 reglas [[IDS - Information Delivery Specification]] que este modelo debería cumplir y verifica si las cumple.
3. ¿Cómo lo federarías con otras disciplinas? → [[Federacion de modelos]]
4. ¿Qué LOD aparente tienen sus elementos principales? → [[LOD - Nivel de Desarrollo]]

↑ [[MOC Proyectos de Estudio]] · [[Resumen de modelos de estudio]] · [[Indice de proyectos]]
