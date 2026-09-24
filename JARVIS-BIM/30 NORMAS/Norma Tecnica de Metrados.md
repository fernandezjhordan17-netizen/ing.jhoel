---
tipo: norma
tags: [norma/peru, costos, metrados, 5d]
aliases: [Norma de metrados, RD 073-2010-VIVIENDA, Metrados para obras de edificacion]
version_vigente: "RD 073-2010-VIVIENDA/VMCS/DNC"
actualizado: 2026-09-24
---
# Norma Técnica de Metrados para Obras de Edificación y Habilitaciones Urbanas

Aprobada por la **RD N.° 073-2010-VIVIENDA/VMCS/DNC**. De uso **obligatorio** en la elaboración de expedientes técnicos de edificaciones y habilitaciones urbanas en todo el país.

## Estructura
Metrados organizados por especialidad y partidas con su **unidad de medida** y **criterio de medición**:
1. Obras provisionales y trabajos preliminares.
2. **Estructuras**: movimiento de tierras, concreto simple, **concreto armado** (concreto en m³, encofrado en m², acero en kg), estructuras metálicas, de madera.
3. **Arquitectura**: muros y tabiques, revoques, pisos, contrazócalos, carpintería, pintura…
4. **Instalaciones sanitarias** y **eléctricas/mecánicas** (puntos, tuberías, aparatos, tableros).
5. Habilitaciones urbanas.

## Integración BIM 5D
- Mapear **cada partida** a categorías/tipos del modelo con un parámetro compartido `Codigo_Partida`.
- Los criterios de medición (qué se descuenta, cómo se mide un encofrado) se programan en Dynamo, en tablas de Revit o en Python → [[BIM 5D - Costos y metrados]].
- Controla diferencias entre el metrado del modelo y el del expediente → [[Gestion de costos y valor ganado]].

> [!todo] Texto oficial: id `Metrados` del catálogo → [[Indice de textos oficiales]]. Con él, JARVIS puede generar la tabla de mapeo partida ↔ categoría de Revit.

↑ [[MOC Gestion de Proyectos]] · [[MOC Normas y Estandares]] · [[Excel]]
