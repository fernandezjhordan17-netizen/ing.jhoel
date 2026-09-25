---
tipo: proyecto
estado: activo
cliente: "Ejemplo JARVIS (datos supuestos)"
codigo_proyecto: "PRY001"
fase: expediente
tipologia: "Vivienda multifamiliar"
ubicacion: "Lima, Lima - verificar zona en el Anexo II de la E.030-2026"
zona_sismica: 4
perfil_suelo: S2
vs30: 420
categoria_uso: C
sistema_estructural: "X: concreto_dual / Y: concreto_muros"
fecha_inicio: 2026-09-25
fecha_entrega: 
cde: ""
ppc:
cpi:
spi:
choques_abiertos:
rfis_abiertos:
tags: [proyecto]
aliases: [PRY001]
actualizado: 2026-09-25
---
# PRY001 Edificio multifamiliar 5 pisos (ejemplo)

## 1. Datos generales
- Cliente / entidad: Ejemplo JARVIS (datos supuestos)
- Ubicación: Lima, Lima - verificar zona en el Anexo II de la E.030-2026 · Tipología: Vivienda multifamiliar
- Tipo de inversión: privada → [[Invierte.pe - Ciclo de inversion]] · ¿BIM obligatorio? → [[Plan BIM Peru]]
- Datos de entrada: `PRY001_ejemplo.json`

## 2. Documentos de información
- [ ] EIR recibido/elaborado → [[Plantilla - EIR]]
- [ ] PEB → [[Plantilla - BEP]]
- [ ] MIDP/TIDP → [[MIDP y TIDP - Planes de entrega]]
- [ ] CDE configurado → [[CDE - Entorno Comun de Datos]]

## 3. Modelos (federación)
| Disciplina | Archivo | Software | Estado | Revisión |
|---|---|---|---|---|
| ARQ | | [[Revit]] | S0 | P01 |
| EST |  | [[Revit]] / [[ETABS]] | S0 | P01 |
| MEP | | [[Revit]] | S0 | P01 |

## 4. Parámetros estructurales
Z = 0,45 · U = 1 · S = 1,065 · TP = 0,53 s · TL = 2,175 s · X: concreto_dual / Y: concreto_muros → [[E.030 - Diseno Sismorresistente]]

Resultado JARVIS: X: R = 7, T = 0,225 s, C = 2,5, V = 1 952,9 kN (17,12 % P) · Y: R = 6, T = 0,225 s, C = 2,5, V = 2 278,4 kN (19,97 % P) → [[PRY001 - Memoria de calculo]] · Excel `90 RECURSOS/Adjuntos/Proyectos/PRY001/PRY001_memoria_E030_E060.xlsx`

## 5. Hitos
| Hito | Fecha | Entregables |
|---|---|---|

## 6. Riesgos principales → [[Gestion de riesgos]]
- (sin alertas normativas)

## 7. Bitácora
- 2026-09-25: creación del proyecto y primera ejecución de JARVIS (E.020 → E.030-2026 → E.060).

↑ [[Indice de proyectos]]
