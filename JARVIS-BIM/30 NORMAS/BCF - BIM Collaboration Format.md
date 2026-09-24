---
tipo: norma
tags: [norma/buildingsmart, openbim, bcf, coordinacion]
aliases: [BCF, BIM Collaboration Format, bcfzip]
version: "2.1 / 3.0"
actualizado: 2026-09-24
---
# BCF — BIM Collaboration Format

Estándar buildingSMART para **comunicar incidencias** (issues) sobre modelos sin intercambiar el modelo completo.

## Dos variantes
- **BCF-XML**: archivo `.bcf`/`.bcfzip` con carpetas por tema (topic).
- **BCF-API**: servicio REST para sincronizar incidencias entre plataformas (nube).

## Contenido de un tema (topic)
- `markup.bcf`: título, tipo, estado, prioridad, asignado a, fecha límite, **comentarios**, etiquetas.
- `viewpoint.bcfv`: posición de cámara, componentes seleccionados/ocultos/coloreados **por IFC GlobalId**, planos de corte.
- `snapshot.png`: captura.

## Versiones
BCF 2.1 (muy soportada) y **BCF 3.0** (2021: mejoras en extensiones, documentos y API).

## Uso en coordinación
Clash Detective ([[Navisworks]]) / Solibri → BCF → [[Revit]] (BCF Manager, BIMcollab) → corrección → cierre. Ver [[Coordinacion BIM y deteccion de interferencias]].

## JARVIS
Genera BCF desde reportes de choques o fallas IDS (Python: `bcf-client`/IfcOpenShell BCF) y resume estados en [[Plantilla - Reporte de interferencias]].

Repositorio: github.com/buildingSMART/BCF-XML (rama `release_3_0`).

↑ [[MOC Normas y Estandares]] · [[OpenBIM]]
