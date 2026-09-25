---
tipo: norma
tags: [norma/peru, rne, estructural, sismo]
aliases: [E.030, Norma sismorresistente, Diseno sismico Peru, E.030 2026]
version_vigente: "RM 183-2026-VIVIENDA (El Peruano, separata especial 03-05-2026)"
actualizado: 2026-09-24
---
# E.030 — Diseño Sismorresistente (edición vigente 2026)

## 1. Estado normativo
| Año | Dispositivo | Nota |
|---|---|---|
| 2003 | NTE E.030-2003 | Histórica |
| 2016 | DS N.° 003-2016-VIVIENDA | Reformula la norma (espectro con TP/TL, irregularidades) |
| 2018 | RM N.° 355-2018-VIVIENDA | Modificación → texto histórico: [[Texto oficial - E030_2018_historica]] |
| 2019 | RM N.° 043-2019-VIVIENDA | Edición usada hasta abril de 2026 |
| 2025 | RM N.° 279-2025-VIVIENDA (30-10-2025) | **Solo publicó el proyecto** de modificación para comentarios → [[Texto oficial - E030_RM279_2025_proyecto]] |
| **2026** | **RM N.° 183-2026-VIVIENDA** (firmada 28-04-2026, publicada 03-05-2026) | **Vigente.** Reemplaza el texto completo: 74 artículos y 4 anexos (antes 53 y 2) |
| 2026 | RM N.° 217-2026-VIVIENDA (jun-2026) | Modifica la Única Disposición Complementaria Transitoria de la RM 183-2026 (régimen de transición) |

> [!warning] Fuente y verificación
> Los cambios de esta nota se contrastaron con una transcripción del texto oficial de la RM 183-2026-VIVIENDA. **Descarga el PDF oficial** con `scripts/05_descargar_normas_oficiales.ps1` (texto completo en [[Indice de textos oficiales]]) y revisa la **RM 217-2026** para saber desde cuándo es exigible en tu proyecto. Pendiente de confirmar en el PDF 2026: tabla de derivas (ahora Tabla N.° 14) y factores de desplazamiento inelástico.

## 2. Qué cambió en 2026 (resumen para el ingeniero)
| Tema | Antes (2019) | Ahora (2026) |
|---|---|---|
| Perfil **S0** (roca) | Vs30 > 1500 m/s | **Vs30 ≥ 800 m/s** |
| Perfil **S5** | No existía | **Suelos excepcionales** (licuables, colapsables, orgánicos, turba, muy flexibles…): no se construye salvo estudio de sitio con mejoramiento |
| Clasificación de suelo | Vs, N60, Su | Vs30, N60 o Su en los 30 m bajo el fondo de cimentación; el más desfavorable si es heterogéneo |
| **Periodo del suelo Ts** | — | **Obligatorio** para categorías A y B en **Zona 4** (S1–S4): medir H/V (método SESAME, ≥3 registros de 30 min); si Ts > 0,65·TP se pasa al perfil siguiente más desfavorable o se hace estudio de sitio |
| S, TP, TL para S2 y S3 | Valores fijos | **Rangos interpolados según Vs30** |
| R0 muros de ductilidad limitada (EMDL) | 4,0 | **3,5** |
| Altura máxima EMDL | 8 pisos | **5 pisos** (densidad de muros > 2,5 % por piso, espesor ≥ 10 cm) |
| Tierra (E.080) | Prohibida en S4 | Prohibida en **S4 y S5** |
| Microzonificación | — | Nuevo **Anexo III** con contenido mínimo |
| Disipación de energía | — | Permitida cumpliendo además el Cap. 18 de **ASCE/SEI 7-22** (o equivalente) y supervisión especializada |

**No cambiaron**: factores Z, factores U, R0 del resto de sistemas, V = ZUCS/R·P, C/R ≥ 0,11, CT = 35/45/60, excentricidad 0,05, sismo vertical 2/3·ZUS y cortante mínima 80 %/90 %.

## 3. Peligro sísmico (Cap. II, arts. 10–18)
**Zonas y factor Z (art. 11, Tabla 1)**: Z4 = 0,45 · Z3 = 0,35 · Z2 = 0,25 · Z1 = 0,10. El **Anexo II** asigna la zona por provincia y distrito.

**Perfiles de suelo (art. 14, Tablas 2 y 3)**
| Perfil | Vs30 (m/s) | N60 (granulares) | Su (cohesivos) |
|---|---|---|---|
| S0 Roca | ≥ 800 | — | — |
| S1 Muy rígido | 550–800 | > 50 | > 100 kPa |
| S2 Rígido | 350–550 | 30–50 | 80–100 kPa |
| S3 Intermedio | 200–350 | 15–30 | 50–80 kPa |
| S4 Blando | < 200 | < 15 | < 50 kPa |
| S5 Excepcional | Estudio específico | | |

**Factor de suelo S (art. 17, Tabla 4)**
| Zona | S0 | S1 | S2 | S3 | S4 |
|---|---|---|---|---|---|
| Z4 | 0,80 | 1,00 | 1,00–1,10 | 1,10–1,20 | Estudio de sitio |
| Z3 | 0,80 | 1,00 | 1,00–1,15 | 1,15–1,20 | 1,30 |
| Z2 | 0,80 | 1,00 | 1,00–1,30 | 1,30–1,40 | 1,70 |
| Z1 | 0,80 | 1,00 | 1,00–1,30 | 1,30–1,60 | 2,40 |

**Periodos TP y TL (art. 17, Tabla 5)**
| | S0 | S1 | S2 | S3 | S4 |
|---|---|---|---|---|---|
| TP (s) | 0,3 | 0,4 | 0,4–0,6 | 0,6–0,9 | 1,2 |
| TL (s) | 3,0 | 2,5 | 2,5–2,0 | 2,0–1,6 | 1,6 |

Interpolación lineal según el Vs30 medido dentro del rango del perfil (interpretación: el extremo de mayor Vs30 da el menor S y TP y el mayor TL). **Sin Vs30 medido**: tomar el mayor S del rango y TP = 0,6 s / TL = 2,0 s (S2) o TP = 0,9 s / TL = 1,6 s (S3).

**Factor C (art. 18, Tabla 6)**: C = 2,5 para T ≤ TP; decrece con TP/T entre TP y TL, y con TP·TL/T² para T > TL (misma forma que ediciones previas — confirmar expresión en el PDF).

## 4. Categoría, sistema y regularidad (Cap. III, arts. 19–27)
- **U (Tabla 7)**: A1 y A2 = 1,5 · B = 1,3 · C = 1,0. Nuevas A1 (salud de 2.° y 3.° nivel) en zonas 3 y 4 → **aislamiento sísmico obligatorio** ([[E.031 - Aislamiento Sismico]]), U = 1.
- **Sistemas (Tabla 8)**: pórticos (≥ 80 % del cortante en columnas), muros estructurales (≥ 70 % en muros), dual (20–70 % en muros), EMDL (máx. 5 pisos).
- **Sistema permitido por categoría y zona (Tabla 9)**: A1 en Z3–Z4 solo con aislamiento; A2 y B limitados a sistemas dúctiles en zonas altas; C cualquier sistema.
- **R0 (Tabla 10)**: acero SMF 8, IMF 5, OMF 4, SCBF 7, OCBF 4, EBF 8 · concreto pórticos 8, dual 7, muros 6, **EMDL 3,5** · albañilería 3 · madera 7 · péndulo invertido 2,5. Con dos sistemas en una dirección se usa el menor R0.
- **Irregularidades en altura (Tabla 11, Ia)**: piso blando o débil 0,75 · extrema 0,50 · masa 0,90 · geométrica vertical 0,90 · discontinuidad 0,80 · discontinuidad extrema 0,60.
- **Irregularidades en planta (Tabla 12, Ip)**: torsional 0,75 · torsional extrema 0,60 · esquinas entrantes 0,90 · discontinuidad de diafragma 0,85 · sistemas no paralelos 0,90.
- **Restricciones (Tabla 13)**: A1 y A2 sin irregularidades en Z2–Z4; B y C sin irregularidades extremas en zonas altas. En Z2–Z4 no se permiten transferencias de más del 25 % de la carga en un nivel.
- **R = R0 · Ia · Ip** (art. 26).

## 5. Análisis estructural (Cap. IV, arts. 28–49)
- 100 % en una dirección + 30 % en la perpendicular (art. 28); fuerzas × 0,8 para esfuerzos admisibles (art. 29).
- Modelo: secciones brutas, diafragma rígido si corresponde, tabiquería no aislada con y sin ella, interacción de muros en H, T, L (art. 30).
- **Peso P (art. 31)**: A y B → CM + 50 % CV · C → CM + 25 % CV · depósitos 80 % · azoteas 25 % · tanques y silos 100 %.
- **Estático (arts. 33–38)**: todas las estructuras en Z1; en otras zonas solo regulares ≤ 30 m o muros portantes ≤ 15 m. **V = (Z·U·C·S / R)·P**, C/R ≥ 0,11. Distribución en altura con k = 1 (T ≤ 0,5 s) o 0,75 + 0,5T ≤ 2. **T = hn/CT** con CT = 35 (pórticos), 45 (pórticos con muros en cajas de ascensor o escalera, acero arriostrado), 60 (albañilería, duales, muros, EMDL); Rayleigh como alternativa (× 0,85 si no se modela la tabiquería). Excentricidad accidental 0,05·B. Sismo vertical 2/3·Z·U·S.
- **Modal espectral (arts. 39–45)**: modos hasta ≥ 90 % de masa (mínimo 3 por dirección); **Sa = (Z·U·C·S / R)·g** (vertical 2/3); combinación **CQC** con 5 % de amortiguamiento (SRSS como alternativa); cortante mínima **80 % (regular) / 90 % (irregular)** de la estática, escalando todo menos los desplazamientos.
- **Tiempo-historia (arts. 46–49)**: complementario (no sustituye); ≥ 7 pares de registros escalados entre 0,2T y 1,5T; distorsiones ≤ 1,25 × Tabla 14; resistencias verificadas con R = 2.

## 6. Derivas (control de distorsión)
Valores de la edición 2019 (en 2026 la tabla pasa a ser la N.° 14 — **confirmar valores en el PDF**):
| Material | Δ/h máx. |
|---|---|
| Concreto armado | 0,007 |
| Acero | 0,010 |
| Albañilería | 0,005 |
| Madera | 0,010 |
| Concreto con muros de ductilidad limitada | 0,005 |

En 2019 los desplazamientos inelásticos eran 0,75·R × elásticos (regulares) y 0,85·R (irregulares) → confirmar en 2026.

## 7. Implementación en software y JARVIS
- [[ETABS]]: espectro de usuario Sa(T) con S, TP y TL interpolados según el Vs30 del EMS ([[E.050 - Suelos y Cimentaciones]]); casos modal + SX/SY; masa según el art. 31; derivas (tabla *Story Drifts*); escalamiento del cortante dinámico.
- JARVIS: herramienta `espectro_e030_2026(zona, perfil, Vs30, U, R)` que interpola, muestra la tabla y pide confirmación antes de crearla vía OAPI → [[MCP CSI - ETABS SAP2000 SAFE]], [[JARVIS - Flujos de trabajo]].
- Si el proyecto se diseñó con la edición 2019, revisa la **disposición transitoria** (RM 217-2026) antes de rehacer el análisis.

Texto completo: [[Indice de textos oficiales]] · Comparar con [[ASCE 7]] · ↑ [[RNE - Reglamento Nacional de Edificaciones]] · [[MOC Ingenieria Estructural]]
