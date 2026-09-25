---
tipo: moc
tags: [proyecto, moc]
aliases: [Proyectos, Lista de proyectos]
actualizado: 2026-09-25
---
# Índice de proyectos

## Proyectos activos (reales)
Crea cada proyecto en `70 PROYECTOS/Proyectos activos` con [[Plantilla - Proyecto]] o, más rápido, con un JSON en `jarvis/proyectos/` y `proyecto_ejecutar` ([[Como registrar un proyecto]]).

Proyecto de ejemplo ejecutado por JARVIS (datos supuestos): [[PRY001 Edificio multifamiliar 5 pisos (ejemplo)]] → [[PRY001 - Memoria de calculo]].
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
