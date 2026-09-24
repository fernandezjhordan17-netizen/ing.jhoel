---
tipo: norma
tags: [norma/iso, ifc, esquema]
aliases: [Esquema IFC, Arquitectura IFC, IFC schema]
actualizado: 2026-09-24
---
# IFC — Estructura del esquema

## Cuatro capas conceptuales
| Capa | Contenido | Ejemplos |
|---|---|---|
| **Recursos** | Tipos básicos reutilizables | geometría, materiales, unidades, fechas, costos |
| **Núcleo (Core)** | Kernel + extensiones de producto, proceso y control | `IfcRoot`, `IfcObject`, `IfcProduct`, `IfcProcess` |
| **Interoperabilidad (Shared)** | Elementos comunes a varias disciplinas | `IfcWall`, `IfcBeam`, `IfcColumn`, `IfcSlab` |
| **Dominio** | Específico por disciplina | HVAC, eléctrico, estructural, análisis estructural, construcción |

## Jerarquía de herencia (simplificada)
```
IfcRoot (GlobalId, OwnerHistory, Name, Description)
 ├─ IfcObjectDefinition
 │   ├─ IfcObject
 │   │   ├─ IfcProduct (ObjectPlacement, Representation)
 │   │   │   ├─ IfcElement → IfcBuildingElement (IFC4: IfcBuiltElement) → IfcWall, IfcSlab, IfcBeam…
 │   │   │   └─ IfcSpatialElement → IfcSite, IfcBuilding, IfcBuildingStorey, IfcSpace, IfcFacility…
 │   │   ├─ IfcProcess (IfcTask)
 │   │   ├─ IfcControl (IfcWorkSchedule, IfcCostSchedule)
 │   │   └─ IfcGroup / IfcSystem
 │   ├─ IfcTypeObject → IfcWallType, IfcBeamType…
 │   └─ IfcContext → IfcProject
 ├─ IfcRelationship
 └─ IfcPropertyDefinition → IfcPropertySet, IfcElementQuantity
```

## Estructura espacial obligatoria
`IfcProject → IfcSite → IfcBuilding → IfcBuildingStorey → (IfcSpace)` — en IFC 4.3 también `IfcFacility` (IfcBridge, IfcRoad, IfcRailway…) y `IfcFacilityPart`.

## Relaciones clave (objetivadas)
| Relación | Significado |
|---|---|
| `IfcRelAggregates` | Todo/parte (proyecto → sitio → edificio → pisos) |
| `IfcRelContainedInSpatialStructure` | Elemento contenido en un piso/espacio |
| `IfcRelDefinesByType` | Ocurrencia ↔ tipo |
| `IfcRelDefinesByProperties` | Elemento ↔ Pset/Qto |
| `IfcRelAssociatesMaterial` | Elemento ↔ material/capas |
| `IfcRelAssociatesClassification` | Elemento ↔ código de clasificación |
| `IfcRelVoidsElement` / `IfcRelFillsElement` | Aberturas y puertas/ventanas |
| `IfcRelConnectsPathElements` | Conexión entre muros |
| `IfcRelAssignsToGroup` | Sistemas y grupos |

## GlobalId
GUID de 128 bits comprimido en **22 caracteres** (base64 IFC). Debe ser **estable** entre exportaciones para comparar versiones (IfcDiff) y rastrear BCF.

## Para practicar
Abre un modelo de [[Resumen de modelos de estudio]] y recorre su estructura espacial; compara con la validación de [[IDS - Information Delivery Specification]] y los problemas típicos de [[Control de calidad de modelos BIM]].

Siguiente: [[Clases IFC principales]] · ↑ [[IFC - ISO 16739]] · [[MOC Normas y Estandares]]
