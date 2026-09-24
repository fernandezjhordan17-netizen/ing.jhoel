---
tipo: norma
tags: [norma/buildingsmart, openbim, ids, calidad]
aliases: [IDS, Information Delivery Specification]
version: "1.0 (aprobada 2024)"
actualizado: 2026-09-24
---
# IDS — Information Delivery Specification

Estándar **buildingSMART** (IDS 1.0 aprobado en 2024) para definir **requisitos de información legibles por máquina** que un modelo IFC debe cumplir. Convierte el EIR/LOIN en **reglas verificables automáticamente**.

## Estructura de un archivo `.ids` (XML, esquema `ids.xsd`)
```xml
<ids:specification name="Muros portantes con resistencia al fuego" ifcVersion="IFC4">
  <ids:applicability minOccurs="1" maxOccurs="unbounded">
    <ids:entity><ids:name><ids:simpleValue>IFCWALL</ids:simpleValue></ids:name></ids:entity>
  </ids:applicability>
  <ids:requirements>
    <ids:property dataType="IFCLABEL">
      <ids:propertySet><ids:simpleValue>Pset_WallCommon</ids:simpleValue></ids:propertySet>
      <ids:baseName><ids:simpleValue>FireRating</ids:simpleValue></ids:baseName>
    </ids:property>
  </ids:requirements>
</ids:specification>
```

## Las 6 facetas
| Faceta | Verifica |
|---|---|
| **Entity** | Clase IFC y PredefinedType |
| **Attribute** | Atributos directos (Name, Description, Tag…) |
| **Classification** | Código de clasificación (Uniclass, OmniClass…) |
| **Property** | Propiedad dentro de un Pset, tipo de dato y valor |
| **Material** | Material asignado |
| **PartOf** | Relación de pertenencia (contenido en piso, parte de un agregado, grupo/sistema) |

Restricciones: valor simple, enumeración, patrón (regex), rango, longitud. Cardinalidad: requerido / opcional / prohibido.

## Herramientas
- **IfcTester** (IfcOpenShell) → [[IfcOpenShell y Bonsai]] — validación por línea de comandos/Python (ideal para JARVIS).
- Editores/validadores: IDS Editor (buildingSMART), usBIM.IDS, BIMcollab, Solibri, xBIM, IDS-Audit-tool, Revit IDS add-ins.

## Flujo JARVIS
[[LOIN - Nivel de Informacion Necesaria]] (tabla Excel) → JARVIS genera `.ids` → IfcTester valida el IFC exportado de [[Revit]] → reporte HTML + [[BCF - BIM Collaboration Format]] con los elementos que fallan.

Repositorio oficial: github.com/buildingSMART/IDS → [[Descarga de proyectos BIM]]

↑ [[MOC Normas y Estandares]] · [[Control de calidad de modelos BIM]]
