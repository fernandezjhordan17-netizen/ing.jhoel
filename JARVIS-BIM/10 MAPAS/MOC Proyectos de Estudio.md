---
tipo: moc
tags: [moc, proyecto]
aliases: [Mapa Proyectos, Modelos de estudio]
actualizado: 2026-09-24
---
# 🔷 MOC — Proyectos BIM de estudio

Modelos BIM **reales y abiertos** que JARVIS usa para aprender. Cada nota de proyecto se genera automáticamente con `scripts/03_ifc_a_obsidian.py` a partir del archivo IFC y se enlaza con las neuronas de conocimiento ([[Clases IFC principales]], [[IFC - Estructura del esquema]], disciplinas, LOD…).

## Cómo obtenerlos
- [[Descarga de proyectos BIM]] (script PowerShell a `C:\Users\JHORDAN\Documents\1.APP CREADOS\APP PARA BIM`)

## Índice
- [[Resumen de modelos de estudio]] (tabla de los 99 modelos analizados)
- [[Indice de proyectos]]
- Práctica guiada: [[Proyecto integrador - Revit ARQ EST MEP]]

```dataview
TABLE esquema, disciplina, elementos_totales, pisos
FROM "70 PROYECTOS/Proyectos de estudio"
SORT file.name ASC
```

## Qué aprender de cada uno
| Modelo | Lección |
|---|---|
| Duplex (IFC2x3, arquitectura/MEP) | Modelo clásico de buildingSMART/NIBS: disciplinas separadas y [[Federacion de modelos]] |
| Revit ARC/STR/MEP (IFC4) | Exportación IFC4 desde [[Revit]], diferencias entre disciplinas |
| SampleHouse (IFC4) | Estructura espacial mínima y [[Clases IFC principales]] |
| SampleCastle (IFC2x3) | Modelo grande: rendimiento, geometría compleja |
| buildingSMART IFC4.3 | [[BIM para infraestructura]] (alineamientos, puentes, vías) |
