---
tipo: concepto
tags: [bim/metodologia, loin]
aliases: [LOIN, Level of Information Need, Nivel de informacion necesaria]
actualizado: 2026-09-24
---
# LOIN — Nivel de Información Necesaria

Concepto de ISO 19650-1 desarrollado en **ISO 7817-1:2024** (antes EN 17412-1:2020) → [[ISO 7817 - LOIN]].

## Principio
"**Ni más ni menos** información de la necesaria para el propósito." Evita sobremodelar (costo) y submodelar (riesgo).

## Prerrequisitos (siempre definir primero)
1. **Propósito** (uso: coordinación, metrado, análisis estructural, FM…)
2. **Hito de entrega** de información
3. **Actores** (quién entrega, quién recibe)
4. **Estructura de desglose de objetos** (qué objetos)

## Componentes de la especificación
| Tipo | Aspectos |
|---|---|
| **Información geométrica** | Detalle, dimensionalidad (0D–3D), ubicación, apariencia, comportamiento paramétrico |
| **Información alfanumérica** | Identificación (nombre, código de clasificación) y contenido (propiedades) |
| **Documentación** | Planos, fichas técnicas, certificados, manuales |

## De LOIN a verificación automática
LOIN → plantilla de datos ([[ISO 23386 y 23387 - Plantillas de datos]], [[bSDD - buildingSMART Data Dictionary]]) → reglas **[[IDS - Information Delivery Specification]]** → validación automática del IFC (IfcTester en [[IfcOpenShell y Bonsai]]). JARVIS puede generar el IDS desde la tabla LOIN.

Comparar con [[LOD - Nivel de Desarrollo]].

↑ [[MOC Metodologia BIM]] · [[EIR - Requisitos de Intercambio de Informacion]]
