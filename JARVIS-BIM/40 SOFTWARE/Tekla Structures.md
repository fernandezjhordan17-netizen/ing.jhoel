---
tipo: software
tags: [software/trimble, estructural, detallado, fabricacion]
aliases: [Tekla, Tekla Structures, DB1]
fabricante: Trimble
formatos: [DB1, IFC, NC-DSTV, TSEP]
actualizado: 2026-09-24
---
# Tekla Structures

Software BIM de Trimble para **detallado constructivo** (LOD 400) de acero, concreto armado/prefabricado y madera: conexiones, armaduras, planos de taller, listas de materiales, archivos CNC (DSTV) para fabricación.

## Conceptos
Modelo (carpeta con `.db1`), entornos/roles, catálogos de perfiles y materiales, **componentes** (conexiones y detalles paramétricos), fases y lotes (4D), organizador, planos (GA, ensamble, pieza, vaciado), Tekla Model Sharing, **Trimble Connect** (CDE).

## API — Tekla Open API (.NET)
- Ensamblados: `Tekla.Structures.Model`, `Tekla.Structures.Drawing`, `Tekla.Structures.Dialog`, `Tekla.Structures.Catalogs`, `Tekla.Structures.Plugins` (paquetes NuGet por versión).
- Conexión: `var model = new Model(); model.GetConnectionStatus();` requiere Tekla abierto y **misma versión** de los ensamblados.
- Macros C# en la carpeta de macros; plugins; Tekla Warehouse para descargar extensiones y **modelos de ejemplo**.
- MCP → [[MCP Tekla Structures]].

## Interoperabilidad
IFC (importar referencia de [[Revit]], exportar para [[Navisworks]]), enlaces de análisis (Tekla Structural Designer y otros), [[Speckle]].

↑ [[MOC Software AEC]] · [[MOC Ingenieria Estructural]] · [[LOD - Nivel de Desarrollo]]
