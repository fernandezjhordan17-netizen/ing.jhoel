---
tipo: concepto
tags: [bim/metodologia, nube-de-puntos, as-built]
aliases: [Nube de puntos, Escaneo laser, Scan-to-BIM]
actualizado: 2026-09-24
---
# Scan to BIM

Modelado de condiciones existentes a partir de **nubes de puntos** (escáner láser terrestre, LiDAR móvil, fotogrametría con drones).

## Flujo
1. Captura (Leica, Faro, Trimble, Matterport; drones con fotogrametría).
2. Registro y limpieza (ReCap Pro, Cyclone, CloudCompare) → formatos RCP/RCS, E57, LAS/LAZ.
3. Vinculación a [[Revit]] / [[Civil 3D]] / [[Navisworks]].
4. Modelado según LOD/LOIN requerido y tolerancias (p. ej. USIBD LOA – Level of Accuracy).
5. Control: desviaciones modelo vs nube (heatmaps).

## Usos
Rehabilitaciones, levantamientos de infraestructura, control de obra (planificado vs construido), [[BIM 7D - Operacion y mantenimiento]].

Ejemplo: el proyecto de muestra "Snowdon Towers" de Revit incluye una nube de puntos (Brownsville.rcp) → [[Descarga de proyectos BIM]].

↑ [[Usos BIM]] · [[MOC Metodologia BIM]]
