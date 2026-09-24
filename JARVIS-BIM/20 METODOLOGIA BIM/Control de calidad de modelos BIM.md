---
tipo: concepto
tags: [bim/metodologia, calidad, qa-qc]
aliases: [QA QC BIM, Auditoria de modelos, Model checking]
actualizado: 2026-09-24
---
# Control de calidad de modelos BIM (QA/QC)

## Tres niveles de verificación
| Nivel | Qué se revisa | Herramientas |
|---|---|---|
| **Técnico / estándar** | Nomenclatura, unidades, coordenadas, niveles, worksets, tamaño, advertencias de Revit | Revit (Model Checker, pyRevit), scripts [[Dynamo]] |
| **Información** | Parámetros obligatorios llenos, clasificación, LOIN, IFC válido | [[IDS - Information Delivery Specification]] (IfcTester), Solibri, BIMcollab Zoom |
| **Diseño / coordinación** | Interferencias, holguras, normativa (accesibilidad A.120, evacuación A.130) | [[Navisworks]], Solibri, reglas propias |

## Checklist mínimo antes de compartir (S1)
- [ ] Nombre conforme a [[Nomenclatura de archivos y contenedores]]
- [ ] Coordenadas compartidas correctas
- [ ] Sin elementos duplicados / advertencias críticas
- [ ] Parámetros obligatorios del [[EIR - Requisitos de Intercambio de Informacion]] completos
- [ ] Vistas de trabajo depuradas; modelo purgado
- [ ] Exportación IFC probada con el mapeo acordado ([[Clases IFC principales]])
- [ ] Validación IDS sin errores

## Validación del archivo IFC
buildingSMART ofrece el **Validation Service** (validate.buildingsmart.org) para esquema, reglas normativas y normativas de implementación.

## JARVIS
Auditoría automática semanal y reporte en Obsidian ([[JARVIS - Flujos de trabajo]]).

↑ [[MOC Metodologia BIM]] · [[Gestion de la calidad]]
