---
tipo: software
tags: [software/csi, estructural, losas, cimentaciones]
aliases: [CSI SAFE, FDB, F2K]
fabricante: Computers and Structures, Inc. (CSI)
formatos: [FDB, F2K]
actualizado: 2026-09-24
---
# SAFE

Software de CSI para **losas, plateas y cimentaciones** (zapatas aisladas, combinadas, cimientos corridos, losas postensadas, vigas de cimentación).

## Flujo típico
1. Importar desde [[ETABS]] (losa de un piso o cargas de la base) o modelar en SAFE.
2. Definir suelo (**coeficiente de balasto** / módulo de reacción) según el EMS → [[E.050 - Suelos y Cimentaciones]].
3. Análisis: presiones en el suelo, deflexiones, punzonamiento, franjas de diseño.
4. Diseño de refuerzo (ACI 318 ajustado a [[E.060 - Concreto Armado]]).

## Formatos
`.FDB` (modelo), `.F2K` (texto; ETABS puede exportar directamente a este formato).

## API
Las versiones modernas (v20+) exponen una OAPI de la misma familia que ETABS/SAP2000. El ProgID y la DLL dependen de la versión instalada: revisar el archivo de ayuda de la API de SAFE en la carpeta de instalación. MCP → [[MCP CSI - ETABS SAP2000 SAFE]].

↑ [[MOC Software AEC]] · [[MOC Ingenieria Estructural]]
