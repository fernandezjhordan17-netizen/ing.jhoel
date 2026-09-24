---
tipo: norma
tags: [norma/iso, openbim, ifc]
aliases: [IFC, Industry Foundation Classes, ISO 16739]
organismo: buildingSMART International / ISO
actualizado: 2026-09-24
---
# IFC — Industry Foundation Classes (ISO 16739)

Esquema de datos **abierto y neutral** para describir edificios e infraestructura (objetos, relaciones, propiedades, geometría, procesos, costos).

## Versiones
| Versión | Estatus ISO | Notas |
|---|---|---|
| IFC2x3 TC1 | ISO/PAS 16739:2005 | Aún muy usada; MVD "Coordination View 2.0" |
| IFC4 ADD2 TC1 | ISO 16739-1:2018 | Mejor geometría (NURBS, teselación), Reference View / Design Transfer View |
| **IFC 4.3 ADD2** | **ISO 16739-1:2024** | Infraestructura: vías, ferrovías, puentes, puertos → [[BIM para infraestructura]] |
| IFC5 | En desarrollo (buildingSMART) | Enfoque modular, serialización JSON, composición por capas |

## Formatos de archivo
- `.ifc` → STEP Physical File (ISO 10303-21), texto plano.
- `.ifcXML` → XML; `.ifcZIP` → comprimido.
- Serializaciones experimentales: JSON, bases de datos (hdf5, sql).

## Qué contiene
- Estructura espacial, elementos, tipos, materiales, propiedades (Psets), cantidades (Qto), relaciones, clasificación, procesos (4D), costos (5D), análisis estructural.
- Detalle en [[IFC - Estructura del esquema]] y [[Clases IFC principales]].

## Subconjuntos y validación
- [[MVD - Model View Definition]] (qué parte del esquema usar en un intercambio).
- [[IDS - Information Delivery Specification]] (qué información debe tener el modelo).
- buildingSMART Validation Service.

## Herramientas para leerlo por código
[[IfcOpenShell y Bonsai]] (Python/C++), xBIM (.NET), web-ifc / That Open (JS), IFC.js.

## En esta bóveda
Los modelos de [[MOC Proyectos de Estudio]] se analizan automáticamente con IfcOpenShell.

↑ [[MOC Normas y Estandares]] · [[OpenBIM]]
