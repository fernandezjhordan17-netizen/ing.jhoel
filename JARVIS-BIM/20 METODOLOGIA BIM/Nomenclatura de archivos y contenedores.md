---
tipo: concepto
tags: [bim/metodologia, iso19650, nomenclatura]
aliases: [Naming convention, Codificacion de archivos, Convencion de nombres]
actualizado: 2026-09-24
---
# Nomenclatura de archivos y contenedores

ISO 19650-2 exige identificadores únicos basados en campos acordados. La estructura más usada viene del **Anexo Nacional del Reino Unido** (BS EN ISO 19650-2 NA) y la adoptan muchas guías nacionales:

```
PROYECTO - ORIGINADOR - VOLUMEN/SISTEMA - NIVEL/UBICACION - TIPO - ROL - NUMERO
  PRJ01  -    ABC     -       ZZ        -        01        -  M3  -  S  - 0001
```
| Campo | Ejemplos |
|---|---|
| Proyecto | Código corto del proyecto (2–6 caracteres) |
| Originador | Código de la empresa autora |
| Volumen/Sistema | ZZ (todos), XX (ninguno), T1 (torre 1) |
| Nivel/Ubicación | 00, 01, B1 (sótano), RF (techo), ZZ, XX |
| Tipo | **M3** modelo 3D, **M2** modelo 2D, **DR** plano, **SP** especificación, **SH** planilla, **RP** reporte, **CA** cálculo, **MI** minuta, **VS** visualización |
| Rol | **A** arquitectura, **S** estructuras, **M** mecánica, **E** eléctrica, **P** sanitarias, **C** civil, **B** BIM/gestión de información, **K** cliente |
| Número | 0001–9999 secuencial |

Metadatos (no en el nombre): estado → [[Codigos de estado e idoneidad]], revisión, clasificación → [[Sistemas de clasificacion]].

> [!tip] Perú
> La [[Guia Nacional BIM Peru]] propone su propia estructura de codificación; si el cliente es público, **usa la de la Guía/EIR**.

## JARVIS
Script de validación por expresión regular sobre carpetas del CDE y renombrado masivo con confirmación ([[JARVIS - Flujos de trabajo]]).

↑ [[CDE - Entorno Comun de Datos]] · [[ISO 19650-2 - Fase de desarrollo]]
