---
tipo: concepto
tags: [bim/metodologia, gis, georreferenciacion]
aliases: [GIS, Georreferenciacion BIM, BIM GIS]
actualizado: 2026-09-24
---
# BIM y GIS

## Por qué integrarlos
BIM = detalle del activo; GIS = contexto territorial (catastro, riesgos, redes). La integración es esencial para infraestructura y ciudades.

## Georreferenciación correcta
- Definir **sistema de referencia** (en Perú, típicamente **WGS 84 / UTM zona 17S, 18S o 19S**, EPSG 32717/32718/32719) y la elevación (nivel medio del mar).
- En [[Revit]]: punto de reconocimiento (survey point), punto base del proyecto, coordenadas compartidas, "Adquirir coordenadas" desde el modelo topográfico de [[Civil 3D]].
- En IFC4+: `IfcMapConversion` + `IfcProjectedCRS` (en IFC2x3 solo lat/long en `IfcSite`).
- buildingSMART publicó una guía de georreferenciación de IFC ("User Guide for Geo-referencing in IFC").

## Estándares
OGC (CityGML, GeoPackage), ISO 19100 (información geográfica), LandXML (civil), [[IFC - ISO 16739]].

## Herramientas
ArcGIS (ArcGIS GeoBIM, ArcGIS for Autodesk), QGIS, FME, [[Civil 3D]], InfraWorks.

↑ [[BIM para infraestructura]] · [[Federacion de modelos]]
