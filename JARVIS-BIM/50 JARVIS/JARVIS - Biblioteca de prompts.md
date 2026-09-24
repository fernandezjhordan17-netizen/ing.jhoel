---
tipo: jarvis
tags: [jarvis, prompts]
aliases: [Prompts JARVIS, System prompt JARVIS]
actualizado: 2026-09-24
---
# JARVIS — Biblioteca de prompts

## Prompt de sistema (resumen; versión completa en `CLAUDE.md`)
> Eres **JARVIS**, asistente de ingeniería BIM del Ing. Jhordan. Respondes en español técnico. Antes de responder, consulta la bóveda `JARVIS-BIM` empezando por el MOC pertinente. Cita siempre norma, versión y artículo y advierte si la nota indica "verificar". Nunca inventes resultados numéricos: léelos del software vía MCP o calcúlalos mostrando la fórmula. Para cualquier escritura en modelos, correos o CDE, muestra primero un *dry-run* y pide confirmación. Registra cada acción en el Diario JARVIS.

## Plantillas de petición
| Objetivo | Prompt |
|---|---|
| Estudio | "Explícame [[LOIN - Nivel de Informacion Necesaria]] con un ejemplo de columna para metrados y para FM; crea una nota de repaso con 5 preguntas." |
| EIR | "Redacta un EIR para [proyecto] (hospital, Z4, S2) usando [[Plantilla - EIR]] y la [[Guia Nacional BIM Peru]]." |
| BEP | "Responde el EIR de [ruta] con un PEB usando [[Plantilla - BEP]]; marca supuestos." |
| Revit | "En el modelo abierto, lista muros portantes sin `FireRating` por nivel. No modifiques nada." |
| ETABS | "Con Z=0.45, U=1.0, S=1.05, TP=0.6, TL=2.0, R=7, genera el espectro y muéstrame la tabla antes de crearlo en ETABS." |
| Coordinación | "Resume los choques abiertos del NWF por disciplina y propone responsables." |
| Gestión | "Prepara el reporte semanal del proyecto X con KPIs y riesgos; deja borrador de correo." |
| Aprendizaje | "Compara el modelo Duplex con SampleHouse: ¿cuál tiene mejor estructura IFC y por qué?" |

## Buenas prácticas de prompting
Contexto (proyecto, fase, norma) → tarea concreta → formato de salida → restricciones (solo lectura, unidades) → criterio de éxito.

↑ [[MOC JARVIS y MCP]]
