---
tipo: norma
tags: [norma/buildingsmart, ifc, mvd]
aliases: [MVD, Model View Definition, Coordination View, Reference View]
actualizado: 2026-09-24
---
# MVD — Model View Definition

Subconjunto del esquema [[IFC - ISO 16739]] para un propósito de intercambio concreto (lo que el software debe exportar/importar para certificarse).

| Esquema | MVD | Uso |
|---|---|---|
| IFC2x3 | **Coordination View 2.0** | Coordinación multidisciplinaria (la más extendida) |
| IFC2x3 | Structural Analysis View | Intercambio con software de análisis |
| IFC2x3 | Basic FM Handover View | COBie → [[COBie]] |
| IFC4 | **Reference View** | Referencia/coordinación (geometría simplificada, teselada) |
| IFC4 | Design Transfer View | Transferencia editable (geometría paramétrica) |
| IFC4.3 | Reference View / Alignment-based views | Infraestructura |

## Tendencia
buildingSMART está desplazando el uso de MVDs rígidos hacia **[[IDS - Information Delivery Specification]]** para requisitos específicos de proyecto, manteniendo las vistas de certificación del software.

## En Revit
Al exportar IFC eliges la versión/MVD (p. ej. "IFC4 Reference View", "IFC2x3 Coordination View 2.0") → [[Revit]].

↑ [[IFC - ISO 16739]] · [[ISO 29481 - IDM]]
