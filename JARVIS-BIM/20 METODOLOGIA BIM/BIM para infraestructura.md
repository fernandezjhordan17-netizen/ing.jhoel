---
tipo: concepto
tags: [bim/metodologia, infraestructura, ifc43]
aliases: [BIM civil, BIM vial, Infrastructure BIM]
actualizado: 2026-09-24
---
# BIM para infraestructura

## IFC 4.3 (ISO 16739-1:2024)
Amplió IFC para **carreteras, ferrovías, puentes, puertos y vías navegables**:
- Nuevas estructuras espaciales: `IfcFacility` → `IfcRoad`, `IfcRailway`, `IfcBridge`, `IfcMarineFacility`; `IfcFacilityPart`.
- **Alineamientos**: `IfcAlignment` (horizontal, vertical, peralte) y **referencia lineal** (`IfcLinearPlacement`, `IfcReferent`) — kilometrajes/progresivas.
- Geotecnia: `IfcGeotechnicalStratum`, `IfcBorehole`; movimiento de tierras: `IfcEarthworksCut`, `IfcEarthworksFill`.
- Georreferenciación: `IfcMapConversion`, `IfcProjectedCRS` → [[BIM y GIS]].

## Herramientas
[[Civil 3D]] (alineamientos, perfiles, corredores, superficies, redes de tuberías), Revit para estructuras de puentes, InfraWorks, OpenRoads (Bentley), [[Tekla Structures]] para puentes de acero/concreto, [[SAP2000]]/CSiBridge para análisis.

## Perú
Muchas de las tipologías obligatorias de la RD 0007-2025-EF/63.01 son de infraestructura (carreteras, riego, defensas ribereñas) → [[Plan BIM Peru]].

Ejemplos de modelos: repositorio buildingSMART IFC4.3.x-sample-models → [[Descarga de proyectos BIM]].

↑ [[MOC Metodologia BIM]] · [[IFC - ISO 16739]]
