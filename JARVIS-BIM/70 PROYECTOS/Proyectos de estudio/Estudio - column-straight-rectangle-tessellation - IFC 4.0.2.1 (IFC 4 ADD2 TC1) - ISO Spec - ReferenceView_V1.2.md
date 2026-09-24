---
tipo: proyecto-estudio
esquema: IFC4
disciplina: EST
elementos_totales: 1
pisos: 0
espacios: 0
proxies: 0
tamano_mb: 0.0
archivo: "02_PROYECTOS_BIM/buildingSMART_Sample-Test-Files/IFC 4.0.2.1 (IFC 4 ADD2 TC1)/ISO Spec - ReferenceView_V1.2/column-straight-rectangle-tessellation.ifc"
software_origen: "Constructivity - Constructivity - 0.9.8.1 · Constructivity 0.9.8.1"
generado: 2026-09-24
tags: [proyecto, estudio, ifc]
---

# Estudio — column-straight-rectangle-tessellation - IFC 4.0.2.1 (IFC 4 ADD2 TC1) - ISO Spec - ReferenceView_V1.2

> [!info] Nota generada automáticamente por `scripts/03_ifc_a_obsidian.py`
> Modelo: `02_PROYECTOS_BIM/buildingSMART_Sample-Test-Files/IFC 4.0.2.1 (IFC 4 ADD2 TC1)/ISO Spec - ReferenceView_V1.2/column-straight-rectangle-tessellation.ifc` · 0.0 MB · esquema **IFC4 (ISO 16739-1:2018)** → [[IFC - ISO 16739]]

## 1. Ficha del modelo
| Campo | Valor |
|---|---|
| Proyecto (IfcProject) | Project  |
| Software de origen | Constructivity - Constructivity - 0.9.8.1 · Constructivity 0.9.8.1 |
| Autor / organización | Tim Chipman / — |
| Fecha del archivo | 2014-07-08T19:20:14 |
| Vista (MVD) declarada | ViewDefinition [ReferenceView_V1.2] → [[MVD - Model View Definition]] |
| Unidad de longitud | inch |
| Disciplina inferida | **EST** → [[MOC Ingenieria Estructural]] |
| Elementos / tipos / espacios | 1 / 0 / 0 |

## 2. Estructura espacial → [[IFC - Estructura del esquema]]
- **Sitio**: Site #1
  - **Edificio**: (sin IfcBuilding)

## 3. Clases IFC presentes → [[Clases IFC principales]]
| Clase | Cantidad |
|---|---|
| [[Clases IFC principales#IfcColumn|IfcColumn]] | 1 |
| [[Clases IFC principales#IfcSite|IfcSite]] | 1 |

**Mezcla por disciplina**: ARQ 0 · EST 1 · MEP 0 · INFRA 0

## 4. Información (datos) → [[LOIN - Nivel de Informacion Necesaria]]
- Materiales distintos: 0 → —
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
