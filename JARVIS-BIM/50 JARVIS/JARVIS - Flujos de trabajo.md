---
tipo: jarvis
tags: [jarvis, flujos, automatizacion]
aliases: [Workflows JARVIS, Recetas JARVIS]
actualizado: 2026-09-24
---
# JARVIS — Flujos de trabajo (recetas)

> Cada receta indica: disparador → pasos → MCP usados → puntos de control humano (🧑) → salida.

## 1. Consulta normativa con cita
"¿Qué dice la norma sobre…?" → buscar en la bóveda ([[MCP Obsidian - Memoria de JARVIS]]) → responder con nota, norma, versión y advertencia de vigencia.

## 2. Auditoría de modelo Revit (semanal)
[[MCP Revit]] → leer parámetros obligatorios del EIR → contar vacíos, duplicados, advertencias → exportar IFC → validar IDS con IfcTester ([[IDS - Information Delivery Specification]]) → reporte en Obsidian + [[Excel]]. 🧑 Revisa antes de enviar al equipo.

## 3. Análisis sísmico E.030 en ETABS
1. Datos del proyecto (Z, S, U, sistema, R0, irregularidades) desde la nota del proyecto.
2. Calcular espectro → [[E.030 - Diseno Sismorresistente]].
3. 🧑 Confirmar parámetros.
4. [[MCP CSI - ETABS SAP2000 SAFE]]: crear función, casos, masa, combinaciones ([[E.060 - Concreto Armado]]) → correr análisis.
5. Leer derivas y cortantes; escalar si corresponde; comparar con límites.
6. Tablas a Excel y borrador de memoria ([[Plantilla - Memoria de calculo]]). 🧑 El ingeniero revisa y firma.

## 4. Cimentación ETABS → SAFE
Exportar F2K → SAFE → balasto del EMS ([[E.050 - Suelos y Cimentaciones]]) → presiones, punzonamiento → reporte.

## 5. Lunes de coordinación
[[MCP Navisworks]]: actualizar NWF → correr matriz de choques → agrupar → BCF → [[Plantilla - Reporte de interferencias]] → tareas en Asana por responsable ([[MCP Gestion de Proyectos]]) → evento en Calendar → acta ([[Plantilla - Reunion de coordinacion]]).

## 6. Metrados 5D
[[MCP Revit]] cantidades por `Codigo_Partida` → [[MCP Excel]] presupuesto/APU → comparación con metrado anterior → alertas de variación > 5 % ([[BIM 5D - Costos y metrados]]).

## 7. Validación de nombres en el CDE
Recorrer carpetas → regex según [[Nomenclatura de archivos y contenedores]] → lista de no conformes → 🧑 aprobar renombrado.

## 8. Civil 3D: eje desde topografía
CSV de puntos → superficie → alineamiento y perfil → reporte de volúmenes → [[MCP AutoCAD y Civil 3D]].

## 9. Tekla: planos de taller por lote
[[MCP Tekla Structures]]: seleccionar ensamblajes por fase → crear planos con plantilla → reporte de pernos a Excel.

## 10. Reporte semanal de gestión
Calendar + Asana + bóveda → [[KPIs de proyectos BIM]] → nota semanal + borrador de correo al cliente (🧑 envía).

## 11. Aprender de un modelo nuevo
Descargar IFC → `scripts/03_ifc_a_obsidian.py` → nota en [[MOC Proyectos de Estudio]] enlazada al conocimiento.

↑ [[MOC JARVIS y MCP]] · [[JARVIS - Agentes especializados]]
