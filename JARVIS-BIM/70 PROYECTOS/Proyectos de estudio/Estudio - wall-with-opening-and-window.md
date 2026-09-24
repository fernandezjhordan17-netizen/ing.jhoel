---
tipo: proyecto-estudio
esquema: IFC4
disciplina: ARQ
elementos_totales: 2
pisos: 1
espacios: 0
proxies: 0
tamano_mb: 0.0
archivo: "02_PROYECTOS_BIM/buildingSMART_Sample-Test-Files/IFC 4.0.2.1 (IFC 4 ADD2 TC1)/ISO Spec - ReferenceView_V1.2/wall-with-opening-and-window.ifc"
software_origen: "RDF - Test Application - 0.10 · IFC Engine DLL version 1.03 beta"
generado: 2026-09-24
tags: [proyecto, estudio, ifc]
---

# Estudio — wall-with-opening-and-window

> [!info] Nota generada automáticamente por `scripts/03_ifc_a_obsidian.py`
> Modelo: `02_PROYECTOS_BIM/buildingSMART_Sample-Test-Files/IFC 4.0.2.1 (IFC 4 ADD2 TC1)/ISO Spec - ReferenceView_V1.2/wall-with-opening-and-window.ifc` · 0.0 MB · esquema **IFC4 (ISO 16739-1:2018)** → [[IFC - ISO 16739]]

## 1. Ficha del modelo
| Campo | Valor |
|---|---|
| Proyecto (IfcProject) | Default Project  |
| Software de origen | RDF - Test Application - 0.10 · IFC Engine DLL version 1.03 beta |
| Autor / organización | Architect / Test Office |
| Fecha del archivo | 2011-12-12T22:18:35 |
| Vista (MVD) declarada | ViewDefinition [ReferenceView_V1.2] → [[MVD - Model View Definition]] |
| Unidad de longitud | millimetre |
| Disciplina inferida | **ARQ** → [[BIM 3D - Modelado]] |
| Elementos / tipos / espacios | 2 / 1 / 0 |

## 2. Estructura espacial → [[IFC - Estructura del esquema]]
- **Sitio**: Default Site (lat 24°28'0", lon 54°25'0")
  - **Edificio**: Default Building
    - Piso: Default Building Storey (elevación 0.00)

## 3. Clases IFC presentes → [[Clases IFC principales]]
| Clase | Cantidad |
|---|---|
| [[Clases IFC principales#IfcWall|IfcWall]] | 1 |
| [[Clases IFC principales#IfcWindow|IfcWindow]] | 1 |
| [[Clases IFC principales#IfcOpeningElement|IfcOpeningElement]] | 1 |
| [[Clases IFC principales#IfcBuilding|IfcBuilding]] | 1 |
| [[Clases IFC principales#IfcBuildingStorey|IfcBuildingStorey]] | 1 |
| [[Clases IFC principales#IfcSite|IfcSite]] | 1 |

**Mezcla por disciplina**: ARQ 2 · EST 0 · MEP 0 · INFRA 0

## 4. Información (datos) → [[LOIN - Nivel de Informacion Necesaria]]
- Materiales distintos: 3 → Name of the material used for the wall, Glass, Wood
- Conjuntos de cantidades (Qto): 0
- Clasificaciones: ninguna
- Property Sets más frecuentes:
  - `Pset_WallCommon` × 1
  - `Pset_WindowCommon` × 1

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
