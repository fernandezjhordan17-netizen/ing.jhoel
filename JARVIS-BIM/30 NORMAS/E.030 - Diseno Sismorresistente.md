---
tipo: norma
tags: [norma/peru, rne, estructural, sismo]
aliases: [E.030, Norma sismorresistente, Diseno sismico Peru]
actualizado: 2026-09-24
---
# E.030 — Diseño Sismorresistente

> [!warning] Versión
> Base de estudio: **E.030-2018** (RM 355-2018-VIVIENDA, sobre la versión 2016). En 2025–2026 el MVCS aprobó modificaciones (se reportan la **RM N.° 279-2025-VIVIENDA** y la **RM N.° 183-2026-VIVIENDA**). **Antes de diseñar, descarga el texto consolidado vigente** y actualiza esta nota; los valores de abajo son los de 2018.

## Filosofía
Evitar pérdidas de vidas, asegurar la continuidad de servicios básicos y minimizar daños a la propiedad. Sismos leves sin daño; moderados con daño reparable; severos sin colapso.

## Parámetros (E.030-2018)
**Zonificación (Z)**: Z4 = 0.45 · Z3 = 0.35 · Z2 = 0.25 · Z1 = 0.10

**Perfiles de suelo**: S0 roca dura · S1 roca o suelos muy rígidos · S2 suelos intermedios · S3 suelos blandos · S4 condiciones excepcionales.

| Factor S | S0 | S1 | S2 | S3 |
|---|---|---|---|---|
| Z4 | 0.80 | 1.00 | 1.05 | 1.10 |
| Z3 | 0.80 | 1.00 | 1.15 | 1.20 |
| Z2 | 0.80 | 1.00 | 1.20 | 1.40 |
| Z1 | 0.80 | 1.00 | 1.60 | 2.00 |

| Periodos | S0 | S1 | S2 | S3 |
|---|---|---|---|---|
| TP (s) | 0.3 | 0.4 | 0.6 | 1.0 |
| TL (s) | 3.0 | 2.5 | 2.0 | 1.6 |

**Factor de amplificación sísmica (C)**
- T < TP → C = 2.5
- TP < T < TL → C = 2.5·(TP/T)
- T > TL → C = 2.5·(TP·TL/T²)

**Uso (U)**: A1 esenciales (hospitales) → aislamiento sísmico en zonas 4 y 3 (ver E.031); A2 = 1.5 · B = 1.3 · C = 1.0

**Coeficiente básico de reducción (R0)** (selección): pórticos de concreto armado 8 · dual 7 · muros estructurales 6 · muros de ductilidad limitada 4 · albañilería armada o confinada 3 · acero SMF 8, IMF 5, OMF 4, SCBF 7, OCBF 4, EBF 8.
**R = R0 · Ia · Ip** (factores de irregularidad en altura y planta).

## Análisis
- **Estático**: V = (Z·U·C·S / R)·P, con C/R ≥ 0.11.
- **Dinámico modal espectral**: Sa = (Z·U·C·S / R)·g; combinación CQC; cortante dinámica ≥ 80 % de la estática (regulares) o 90 % (irregulares); excentricidad accidental 0.05.
- **Peso sísmico P**: categorías A y B → CM + 50 % CV; C → CM + 25 % CV; depósitos 80 % de la carga almacenable; azoteas 25 % CV.

## Control de derivas (Δ/h máximo)
| Material | Límite |
|---|---|
| Concreto armado | 0.007 |
| Acero | 0.010 |
| Albañilería | 0.005 |
| Madera | 0.010 |
| Concreto con muros de ductilidad limitada | 0.005 |

Desplazamientos inelásticos = 0.75·R × elásticos (regulares); 0.85·R (irregulares).

## Implementación en software
- [[ETABS]]: función de espectro de usuario (T vs Sa), casos modales (Ritz o eigen), patrones SX/SY, combinaciones; verificación de derivas con tablas "Story Drifts".
- JARVIS: generar espectro desde Z/U/S/R, crearlo vía OAPI y verificar derivas/cortante automáticamente → [[MCP CSI - ETABS SAP2000 SAFE]], [[JARVIS - Flujos de trabajo]].

↑ [[RNE - Reglamento Nacional de Edificaciones]] · [[MOC Ingenieria Estructural]] · Comparar con [[ASCE 7]]
