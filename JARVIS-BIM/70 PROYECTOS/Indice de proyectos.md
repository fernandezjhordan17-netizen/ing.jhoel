---
tipo: moc
tags: [proyecto, moc]
aliases: [Proyectos, Lista de proyectos]
actualizado: 2026-09-24
---
# Índice de proyectos

## Proyectos activos (reales)
Crea cada proyecto en `70 PROYECTOS/Proyectos activos` con [[Plantilla - Proyecto]].
```dataview
TABLE estado, cliente, fase, fecha_entrega, ppc, cpi, spi
FROM "70 PROYECTOS/Proyectos activos"
SORT fecha_entrega ASC
```

## Proyectos de estudio (modelos abiertos descargados)
Generados por `scripts/03_ifc_a_obsidian.py` → [[MOC Proyectos de Estudio]].
```dataview
TABLE esquema, disciplina, elementos_totales, pisos
FROM "70 PROYECTOS/Proyectos de estudio"
```

## Práctica guiada
- [[Proyecto integrador - Revit ARQ EST MEP]]

↑ [[JARVIS BIM - Inicio]] · [[MOC Gestion de Proyectos]]
