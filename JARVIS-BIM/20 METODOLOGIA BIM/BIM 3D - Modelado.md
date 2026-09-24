---
tipo: concepto
tags: [bim/metodologia, dimensiones, modelado]
aliases: [3D, Modelado BIM]
actualizado: 2026-09-24
---
# BIM 3D — Modelado

## Qué es
Creación de modelos paramétricos por disciplina (arquitectura, estructuras, MEP, civil) con objetos que llevan geometría **y** datos.

## Buenas prácticas
1. **Plantilla corporativa** (niveles, rejillas, parámetros compartidos, códigos de clasificación → [[Sistemas de clasificacion]]).
2. **Punto base y coordenadas compartidas** idénticos en todos los modelos (clave para [[Federacion de modelos]] y [[BIM y GIS]]).
3. Modelar **como se construye** (muros por niveles, losas por paños de vaciado).
4. Nivel de detalle según el [[LOIN - Nivel de Informacion Necesaria]] / [[LOD - Nivel de Desarrollo]], ni más ni menos.
5. Separar modelos por disciplina y volumen; nombrarlos según [[Nomenclatura de archivos y contenedores]].
6. Verificar con [[Control de calidad de modelos BIM]] antes de compartir en el [[CDE - Entorno Comun de Datos]].

## Herramientas
[[Revit]] · [[Tekla Structures]] · [[Civil 3D]] · [[AutoCAD]] (2D de apoyo) · [[IfcOpenShell y Bonsai]] (abierto)

## Automatización con JARVIS
- Creación de niveles/ejes desde Excel ([[MCP Revit]] + [[MCP Excel]]).
- Auditoría de parámetros vacíos ([[JARVIS - Flujos de trabajo]]).

↑ [[Dimensiones BIM]]
