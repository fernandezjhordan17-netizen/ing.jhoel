---
tipo: referencia
tags: [norma/iso, ifc, clases]
aliases: [Entidades IFC, Clases IFC, IfcWall, IfcBeam, IfcColumn, IfcSlab]
actualizado: 2026-09-24
---
# Clases IFC principales (referencia rápida)

> Los modelos de [[MOC Proyectos de Estudio]] enlazan aquí con el conteo real de cada clase.

## Estructura espacial
### IfcProject
Contexto global: unidades, sistema de coordenadas, contexto de representación.
### IfcSite
Terreno; lat/long/elevación; en IFC4 georreferenciación con `IfcMapConversion` → [[BIM y GIS]].
### IfcBuilding
Edificio. En IFC 4.3 hereda de `IfcFacility`.
### IfcBuildingStorey
Nivel/piso; `Elevation`.
### IfcSpace
Espacio/ambiente; áreas y volúmenes; base para FM ([[BIM 7D - Operacion y mantenimiento]]).

## Elementos constructivos (estructura y arquitectura)
### IfcWall
Muro (IFC2x3 usa `IfcWallStandardCase` para muros de sección constante). Pset: `Pset_WallCommon` (IsExternal, LoadBearing, FireRating, ThermalTransmittance, AcousticRating). Qto: `Qto_WallBaseQuantities`.
### IfcSlab
Losa/piso/techo; `PredefinedType`: FLOOR, ROOF, LANDING, BASESLAB.
### IfcBeam
Viga; `Pset_BeamCommon` (LoadBearing, Span, Slope).
### IfcColumn
Columna; `Pset_ColumnCommon`.
### IfcFooting
Zapata/cimentación; `PredefinedType`: PAD_FOOTING, STRIP_FOOTING, PILE_CAP, FOOTING_BEAM.
### IfcPile
Pilote.
### IfcMember
Elemento lineal secundario (arriostres, correas, montantes de muro cortina).
### IfcPlate
Placa (paneles de muro cortina, planchas de acero).
### IfcReinforcingBar
Barra de refuerzo (acero corrugado); también `IfcReinforcingMesh`, `IfcTendon`.
### IfcStair
Escalera (con `IfcStairFlight`).
### IfcRailing
Baranda.
### IfcRoof
Techo (contenedor de losas de techo).
### IfcCovering
Revestimientos: cielo raso (CEILING), pisos (FLOORING), enchapes.
### IfcCurtainWall
Muro cortina.
### IfcDoor
Puerta (llena una abertura: `IfcRelFillsElement`).
### IfcWindow
Ventana.
### IfcOpeningElement
Vano/abertura (`IfcRelVoidsElement`).
### IfcBuildingElementProxy
Elemento sin clase específica. **Señal de alerta**: exceso de proxies = mala exportación IFC ([[Control de calidad de modelos BIM]]).

## Instalaciones (MEP)
### IfcFlowSegment
Tuberías/ductos (IFC4: `IfcPipeSegment`, `IfcDuctSegment`, `IfcCableCarrierSegment`).
### IfcFlowFitting
Accesorios (IFC4: `IfcPipeFitting`, `IfcDuctFitting`).
### IfcFlowTerminal
Terminales (IFC4: `IfcSanitaryTerminal`, `IfcAirTerminal`, `IfcLightFixture`, `IfcOutlet`).
### IfcDistributionElement
Base de todos los elementos de distribución; sistemas con `IfcDistributionSystem`.
### IfcFurnishingElement
Mobiliario (IFC4: `IfcFurniture`).

## Infraestructura (IFC 4.3)
### IfcAlignment
Eje de vía/ferrovía; horizontal/vertical/peralte → [[BIM para infraestructura]].
### IfcRoad
### IfcBridge
### IfcRailway
### IfcEarthworksCut
### IfcGeotechnicalStratum

## Análisis estructural
### IfcStructuralAnalysisModel
Modelo analítico; `IfcStructuralCurveMember` (barras), `IfcStructuralSurfaceMember` (placas), `IfcStructuralPointConnection` (nudos), `IfcStructuralLoadGroup` (casos/combos). Ver [[SAF - Structural Analysis Format]] como alternativa práctica.

## Procesos y costos
### IfcTask
Actividad del cronograma ([[BIM 4D - Planificacion]]); `IfcWorkSchedule`, `IfcRelSequence`.
### IfcCostItem
Partida de costo ([[BIM 5D - Costos y metrados]]); `IfcCostSchedule`.

↑ [[IFC - Estructura del esquema]] · [[IFC - ISO 16739]]
