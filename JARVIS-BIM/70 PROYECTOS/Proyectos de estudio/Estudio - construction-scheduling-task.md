---
tipo: proyecto-estudio
esquema: IFC4X3
disciplina: ARQ
elementos_totales: 5
pisos: 1
espacios: 0
proxies: 0
tamano_mb: 0.0
archivo: "02_PROYECTOS_BIM/buildingSMART_IFC4.3_sample-models/models/construction-scheduling/construction-scheduling-task/construction-scheduling-task.ifc"
software_origen: "redacted - redacted - 3.14159 · redacted"
generado: 2026-09-24
tags: [proyecto, estudio, ifc]
---

# Estudio — construction-scheduling-task

> [!info] Nota generada automáticamente por `scripts/03_ifc_a_obsidian.py`
> Modelo: `02_PROYECTOS_BIM/buildingSMART_IFC4.3_sample-models/models/construction-scheduling/construction-scheduling-task/construction-scheduling-task.ifc` · 0.0 MB · esquema **IFC 4.3 (ISO 16739-1:2024)** → [[IFC - ISO 16739]]

## 1. Ficha del modelo
| Campo | Valor |
|---|---|
| Proyecto (IfcProject) | example project  |
| Software de origen | redacted - redacted - 3.14159 · redacted |
| Autor / organización | redacted / redacted |
| Fecha del archivo | 2010-09-23T23:27:15 |
| Vista (MVD) declarada | ViewDefinition [NotAssigned] → [[MVD - Model View Definition]] |
| Unidad de longitud | inch |
| Disciplina inferida | **ARQ** → [[BIM 3D - Modelado]] |
| Elementos / tipos / espacios | 5 / 0 / 0 |

## 2. Estructura espacial → [[IFC - Estructura del esquema]]
- **Sitio**: Site #1
  - **Edificio**: Building #1
    - Piso: Ground Level (elevación 0.00)

## 3. Clases IFC presentes → [[Clases IFC principales]]
| Clase | Cantidad |
|---|---|
| [[Clases IFC principales#IfcWall|IfcWall]] | 4 |
| [[Clases IFC principales#IfcSlab|IfcSlab]] | 1 |
| [[Clases IFC principales#IfcBuildingStorey|IfcBuildingStorey]] | 1 |
| [[Clases IFC principales#IfcBuilding|IfcBuilding]] | 1 |
| [[Clases IFC principales#IfcSite|IfcSite]] | 1 |

**Mezcla por disciplina**: ARQ 4 · EST 0 · MEP 0 · INFRA 0

## 4. Información (datos) → [[LOIN - Nivel de Informacion Necesaria]]
- Materiales distintos: 2 → Concrete (Nominal), Block (Nominal)
- Conjuntos de cantidades (Qto): 0
- Clasificaciones: ninguna
- Property Sets más frecuentes:

## 5. Diagnóstico de calidad → [[Control de calidad de modelos BIM]]
- ✅ Pocos o ningún proxy: la exportación usa clases IFC específicas → [[Clases IFC principales]].
- ⚠️ Sin `IfcClassification`: los elementos no llevan códigos Uniclass/OmniClass → [[Sistemas de clasificacion]].
- ✅ Todos los elementos revisados están contenidos en la estructura espacial.
- ℹ️ Sin `IfcMapConversion`: el modelo no está georreferenciado → [[BIM y GIS]].
- ℹ️ Sin `IfcElementQuantity` (Qto): los metrados deberán calcularse desde la geometría → [[BIM 5D - Costos y metrados]].

## 6. Preguntas de estudio para JARVIS y para ti
1. ¿Qué [[Usos BIM]] permite este modelo con la información que contiene?
2. Redacta 3 reglas [[IDS - Information Delivery Specification]] que este modelo debería cumplir y verifica si las cumple.
3. ¿Cómo lo federarías con otras disciplinas? → [[Federacion de modelos]]
4. ¿Qué LOD aparente tienen sus elementos principales? → [[LOD - Nivel de Desarrollo]]

↑ [[MOC Proyectos de Estudio]] · [[Resumen de modelos de estudio]] · [[Indice de proyectos]]
