---
tipo: concepto
tags: [bim/metodologia, clasificacion]
aliases: [Uniclass, OmniClass, MasterFormat, UniFormat, Clasificacion]
actualizado: 2026-09-24
---
# Sistemas de clasificación

Marco normativo: [[ISO 12006 - Clasificacion]] (ISO 12006-2).

| Sistema | Origen | Uso típico |
|---|---|---|
| **Uniclass 2015** | Reino Unido (NBS) | Tablas: Co (complejos), En (entidades), SL (espacios), EF (elementos/funciones), Ss (sistemas), Pr (productos), TE, PM (gestión), Ac (actividades), FI, Ro (roles), Zz |
| **OmniClass** | EE.UU./Canadá (CSI) | 15 tablas; p. ej. Tabla 21 Elementos, 22 Resultados de obra, 23 Productos. Revit trae OmniClass por defecto |
| **MasterFormat** | CSI (EE.UU.) | Especificaciones por divisiones (03 Concreto, 05 Metales…) |
| **UniFormat II** | ASTM E1557 | Estimación por elementos (A Subestructura, B Envolvente…) |
| **CoClass** | Suecia | Basado en ISO 81346 |
| **ISO 81346** | Internacional | Designación de referencia de sistemas |

## En la práctica peruana
- Presupuestos: estructura de partidas del expediente técnico (S10, Norma de Metrados).
- Recomendación: mapear **partida ↔ Uniclass/OmniClass** en un parámetro compartido para enlazar [[BIM 5D - Costos y metrados]] con clasificación internacional.

## Herramienta práctica
**Classification Manager** (Autodesk BIM Interoperability Tools, gratis) asigna Uniclass u OmniClass en Revit → [[Add-ins recomendados para Revit]].

## En IFC
`IfcClassification` + `IfcClassificationReference` asociados mediante `IfcRelAssociatesClassification` → [[Clases IFC principales]]; verificable con la faceta *Classification* de [[IDS - Information Delivery Specification]]; diccionarios en [[bSDD - buildingSMART Data Dictionary]].

↑ [[MOC Metodologia BIM]]
