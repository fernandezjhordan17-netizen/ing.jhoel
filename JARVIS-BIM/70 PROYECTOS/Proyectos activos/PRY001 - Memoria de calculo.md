---
tipo: documento
documento: memoria-calculo
proyecto: "PRY001 Edificio multifamiliar 5 pisos (ejemplo)"
fecha: 2026-09-25
software: JARVIS (jarvis-bim) + ETABS
tags: [estructural, memoria, proyecto]
aliases: [PRY001 memoria]
actualizado: 2026-09-25
---
# Memoria de cálculo — PRY001 Edificio multifamiliar 5 pisos (ejemplo)

> [!warning] Borrador generado por JARVIS
> Se regenera con `proyecto_ejecutar` (no edites a mano). Debe ser revisado y firmado por el ingeniero responsable.
> Los datos marcados *supuesto* deben reemplazarse por los del proyecto o del modelo ETABS.
> Excel: `90 RECURSOS/Adjuntos/Proyectos/PRY001/PRY001_memoria_E030_E060.xlsx`

Proyecto: [[PRY001 Edificio multifamiliar 5 pisos (ejemplo)]] · Plantilla: [[Plantilla - Memoria de calculo]]

## 1. Descripción
- Cliente: Ejemplo JARVIS (datos supuestos) · Ubicación: Lima, Lima - verificar zona en el Anexo II de la E.030-2026 · Tipología: Vivienda multifamiliar
- 5 niveles · hn = 13,50 m · f'c = 21 MPa · fy = 420 MPa

## 2. Normas
[[E.020 - Cargas]] · [[E.030 - Diseno Sismorresistente]] (E.030-2026 (RM 183-2026-VIVIENDA)) · [[E.060 - Concreto Armado]] (E.060-2009 (DS 010-2009-VIVIENDA))

## 3. Pesos por nivel (E.020 + E.030 art. 31)
P = CM + 25 % CV (categoría C); azotea 25 % CV (E.030 art. 31).

| Nivel | h (m) | Área (m²) | CM (kPa) | CV (kPa) | CM (kN) | CV (kN) | %CV | P (kN) |
|---|---|---|---|---|---|---|---|---|
| Piso 1 | 2,70 | 280 | 8 | 2 | 2 240,0 | 560,0 | 25 % | 2 380,0 |
| Piso 2 | 5,40 | 280 | 8 | 2 | 2 240,0 | 560,0 | 25 % | 2 380,0 |
| Piso 3 | 8,10 | 280 | 8 | 2 | 2 240,0 | 560,0 | 25 % | 2 380,0 |
| Piso 4 | 10,80 | 280 | 8 | 2 | 2 240,0 | 560,0 | 25 % | 2 380,0 |
| Azotea | 13,50 | 280 | 6,5 | 1 | 1 820,0 | 280,0 | 25 % | 1 890,0 |

**P total = 11 410,0 kN**

Fuentes: CV: E.020, art. 6.1, Tabla 1 (vivienda); CV: E.020, art. 7.1 a); acabados: supuesto del proyecto (revisar); aligerado: E.020, Anexo 1 (losas aligeradas en una dirección); estructura: supuesto del proyecto (revisar); tabiqueria: supuesto del proyecto (revisar).

## 4. Parámetros sísmicos (E.030-2026)
Z = 0,45 · U = 1 · perfil S2 (Vs30 = 420 m/s) · S = 1,065 · TP = 0,53 s · TL = 2,175 s · categoría C

| Dir. | Sistema | R0 | Ia | Ip | R | T (s) | C | C/R | V (kN) | V/P | V mín. din. (kN) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| X | Concreto armado – dual | 7 | 1 | 1 | 7 | 0,225 | 2,5 | 0,3571 | 1 952,9 | 17,12 % | 1 562,4 |
| Y | Concreto armado – muros estructurales | 6 | 1 | 1 | 6 | 0,225 | 2,5 | 0,4167 | 2 278,4 | 19,97 % | 1 822,8 |

Fórmula: V = Z·U·C·S/R·P con C/R ≥ 0,11 (arts. 34–35); T = hn/CT (art. 36); cortante dinámica mínima 80 % (regular) / 90 % (irregular) de la estática (art. 44).

### Dirección X: fuerzas por nivel (k = 1)
| Nivel | h (m) | P (kN) | α | F (kN) |
|---|---|---|---|---|
| Piso 1 | 2,7 | 2 380,0 | 0,07158 | 139,8 |
| Piso 2 | 5,4 | 2 380,0 | 0,14316 | 279,6 |
| Piso 3 | 8,1 | 2 380,0 | 0,21474 | 419,4 |
| Piso 4 | 10,8 | 2 380,0 | 0,28632 | 559,2 |
| Azotea | 13,5 | 1 890,0 | 0,28421 | 555,0 |

- T = hn/CT = 13.5/60 (art. 36) · método estático aplicable (art. 33)

### Dirección Y: fuerzas por nivel (k = 1)
| Nivel | h (m) | P (kN) | α | F (kN) |
|---|---|---|---|---|
| Piso 1 | 2,7 | 2 380,0 | 0,07158 | 163,1 |
| Piso 2 | 5,4 | 2 380,0 | 0,14316 | 326,2 |
| Piso 3 | 8,1 | 2 380,0 | 0,21474 | 489,3 |
| Piso 4 | 10,8 | 2 380,0 | 0,28632 | 652,4 |
| Azotea | 13,5 | 1 890,0 | 0,28421 | 647,6 |

- T = hn/CT = 13.5/60 (art. 36) · método estático aplicable (art. 33)

## 5. Combinaciones de carga (E.060 art. 9.2)
| Nombre | Tipo | Casos |
|---|---|---|
| U1 | suma lineal | Dead×1.4, SCP×1.4, Live×1.7, LiveTecho×1.7 |
| U2_SX | suma lineal | Dead×1.25, SCP×1.25, Live×1.25, LiveTecho×1.25, SX×1 |
| U3_SX | suma lineal | Dead×0.9, SCP×0.9, SX×1 |
| U2_SY | suma lineal | Dead×1.25, SCP×1.25, Live×1.25, LiveTecho×1.25, SY×1 |
| U3_SY | suma lineal | Dead×0.9, SCP×0.9, SY×1 |
| ENV_E060 | envolvente | U1, U2_SX, U3_SX, U2_SY, U3_SY |

## 6. Vigas (E.060 arts. 10 y 11)
| Viga | b×h | Mu (kN·m) | As diseño (mm²) | Barras | φMn | Vu (kN) | Estribos | Obs. |
|---|---|---|---|---|---|---|---|---|
| V-101 (eje A, tramo 1-2) | 250×500 | 95 | 607,1 | 4 Ø 5/8 | 95 | 110 | Ø 3/8 (2 ramas) @ 200 mm |  |
| V-102 (eje B, tramo 2-3) | 300×600 | 180 | 941,8 | 5 Ø 5/8 | 180 | 160 | Ø 3/8 (2 ramas) @ 250 mm |  |
| VCH-01 (chata) | 200×200 | 6 | 117 | 2 Ø 12mm | 6 | 12 | no requiere por cálculo (11.5.6.1); estribos de montaje a criterio |  |

As mín = 0,22·√f'c/fy·b·d (10.5.2); As máx = 0,75·Asb (10.3.4); Vc = 0,17·√f'c·b·d (11.3.1.1). Confinamiento y diseño por capacidad del cap. 21 aparte.

## 7. Columnas — carga axial máxima (E.060 10.3.6 y 10.9.1)
| Columna | b×h | Refuerzo | Cuantía | Pu (kN) | φPn máx (kN) | Uso | Cumple |
|---|---|---|---|---|---|---|---|
| C-1 (esquina) | 400×400 | 8 Ø 3/4 | 0,0142 | 1400 | 2111 | 66,3 % | sí |
| C-2 (central) | 300×600 | 10 Ø 5/8 | 0,0111 | 1800 | 2247,4 | 80,1 % | sí |

Solo axial: con flexión verifica con el diagrama de interacción en ETABS.

## 8. Alertas
- Ninguna.

## 9. Pendientes normativos
- [!todo] Expresión de C para T > TP tomada de ediciones previas (2,5·TP/T y 2,5·TP·TL/T²); confirmar en Tabla N.° 6 del PDF 2026.
- [!todo] Factores 0,75·R (regular) y 0,85·R (irregular) de la edición 2019; confirmar en el PDF 2026.
- [!todo] Límites de distorsión de la edición 2019 (en 2026 es la Tabla N.° 14); confirmar valores en el PDF 2026.

## 10. Siguientes pasos en ETABS
1. `csi_crear_espectro_e030` (dry-run → confirmar) con los parámetros de la sección 4, una función por dirección.
2. `csi_crear_combinaciones_e060` con los casos del modelo (sección 5).
3. `csi_correr_analisis(confirmar=True)` → `csi_reacciones_base` para V dinámica y `csi_derivas` para distorsiones.
4. Copia V dinámica y derivas en `resultados_etabs` del JSON del proyecto y vuelve a ejecutar.

↑ [[PRY001 Edificio multifamiliar 5 pisos (ejemplo)]] · [[Indice de proyectos]] · [[JARVIS - Flujos de trabajo]]
