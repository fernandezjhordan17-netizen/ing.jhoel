---
tipo: concepto
tags: [bim/metodologia, dimensiones, 7d, fm]
aliases: [7D, Facility Management, FM, O&M]
actualizado: 2026-09-24
---
# BIM 7D — Operación y mantenimiento (FM)

## Qué es
Entregar al propietario un **Modelo de Información del Activo (AIM)** útil para operar: equipos, garantías, manuales, planes de mantenimiento.

## Estándares clave
- [[ISO 19650-3 - Fase operativa]] (AIR → AIM)
- [[COBie]] (entrega estructurada de datos de FM)
- [[IFC - ISO 16739]] (`IfcAsset`, `IfcDistributionElement`, `Pset_ManufacturerTypeInformation`, `Pset_Warranty`)

## Flujo
1. El propietario define [[Requisitos de informacion OIR AIR PIR EIR]] (AIR).
2. El equipo de diseño/obra llena parámetros progresivamente según el [[LOIN - Nivel de Informacion Necesaria]].
3. Entrega "as-built" / registro (código CR) → [[Codigos de estado e idoneidad]].
4. Carga en CAFM/CMMS (Maximo, Archibus, Planon…) o [[Gemelo Digital]].

↑ [[Dimensiones BIM]]
