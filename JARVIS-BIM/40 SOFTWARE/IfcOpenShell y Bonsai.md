---
tipo: software
tags: [software/opensource, openbim, ifc, python]
aliases: [IfcOpenShell, Bonsai, BlenderBIM, IfcTester, IfcConvert]
licencia: LGPL-3.0 (IfcOpenShell) / GPL (Bonsai)
actualizado: 2026-09-24
---
# IfcOpenShell y Bonsai

**IfcOpenShell**: librería open source (C++ con API Python) para leer, escribir y analizar [[IFC - ISO 16739]] (IFC2x3, IFC4, IFC4.3). `pip install ifcopenshell`.

## Herramientas incluidas
| Herramienta | Uso |
|---|---|
| `ifcopenshell.api` | Crear/editar modelos IFC por código |
| **IfcConvert** | IFC → OBJ, glTF, DAE, STEP, SVG (planos) |
| **IfcTester** | Validar contra [[IDS - Information Delivery Specification]] |
| **IfcDiff** | Comparar versiones de un modelo |
| **IfcClash** | Detección de interferencias |
| **IfcCSV** | Exportar/importar propiedades a CSV/Excel |
| **IfcPatch** | Recetas de corrección masiva |
| IfcCOBie, ifc4d, ifc5d | COBie, cronogramas, costos |
| BCF | Leer/escribir [[BCF - BIM Collaboration Format]] |

## Ejemplo (lo que usa `scripts/03_ifc_a_obsidian.py`)
```python
import ifcopenshell, ifcopenshell.util.element as ue
m = ifcopenshell.open("modelo.ifc")
print(m.schema)                                   # IFC2X3 / IFC4 / IFC4X3
for piso in m.by_type("IfcBuildingStorey"):
    print(piso.Name, piso.Elevation)
muro = m.by_type("IfcWall")[0]
print(ue.get_psets(muro))                         # {'Pset_WallCommon': {...}}
```

## Bonsai (ex BlenderBIM)
Complemento de **Blender** para crear y editar IFC de forma nativa (modelado, planos, 4D/5D, IDS, BCF). Alternativa gratuita para aprender IFC a fondo.

## Por qué es clave para JARVIS
Permite analizar **cualquier** modelo sin licencias, en Python, y generar conocimiento para esta bóveda → [[MOC Proyectos de Estudio]].

↑ [[MOC Software AEC]] · [[OpenBIM]]
