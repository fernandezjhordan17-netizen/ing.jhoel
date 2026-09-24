---
tipo: proyecto-estudio
esquema: IFC4
disciplina: MEP
elementos_totales: 1
pisos: 0
espacios: 0
proxies: 0
tamano_mb: 0.0
archivo: "02_PROYECTOS_BIM/IfcSampleFiles/Ifc4_BasinFacetedBrep.ifc"
software_origen: "ggIFC - Exporter by Geometry Gym Pty Ltd"
generado: 2026-09-24
tags: [proyecto, estudio, ifc]
---

# Estudio — Ifc4_BasinFacetedBrep

> [!info] Nota generada automáticamente por `scripts/03_ifc_a_obsidian.py`
> Modelo: `02_PROYECTOS_BIM/IfcSampleFiles/Ifc4_BasinFacetedBrep.ifc` · 0.0 MB · esquema **IFC4 (ISO 16739-1:2018)** → [[IFC - ISO 16739]]

## 1. Ficha del modelo
| Campo | Valor |
|---|---|
| Proyecto (IfcProject) | IfcProject — IfcProject |
| Software de origen | ggIFC - Exporter by Geometry Gym Pty Ltd |
| Autor / organización | Jon / Unknown |
| Fecha del archivo | 2014-12-09T00:27:55 |
| Vista (MVD) declarada | ViewDefinition [notYetAssigned] → [[MVD - Model View Definition]] |
| Unidad de longitud | millimetre |
| Disciplina inferida | **MEP** → [[Coordinacion BIM y deteccion de interferencias]] |
| Elementos / tipos / espacios | 1 / 1 / 0 |

## 2. Estructura espacial → [[IFC - Estructura del esquema]]
- **Sitio**: (sin IfcSite)
  - **Edificio**: IfcBuilding

## 3. Clases IFC presentes → [[Clases IFC principales]]
| Clase | Cantidad |
|---|---|
| `IfcSanitaryTerminal` | 1 |
| [[Clases IFC principales#IfcBuilding|IfcBuilding]] | 1 |

**Mezcla por disciplina**: ARQ 0 · EST 0 · MEP 1 · INFRA 0

## 4. Información (datos) → [[LOIN - Nivel de Informacion Necesaria]]
- Materiales distintos: 1 → Ceramic
- Conjuntos de cantidades (Qto): 0
- Clasificaciones: ninguna
- Property Sets más frecuentes:

## 5. Diagnóstico de calidad → [[Control de calidad de modelos BIM]]
- ✅ Pocos o ningún proxy: la exportación usa clases IFC específicas → [[Clases IFC principales]].
- ⚠️ Sin `IfcBuildingStorey`: los elementos no están organizados por niveles (estructura espacial incompleta) → [[IFC - Estructura del esquema]].
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
