---
tipo: guia
tags: [recurso, descarga, proyectos, scripts]
aliases: [Descargar modelos BIM, Modelos de ejemplo, Datasets BIM]
actualizado: 2026-09-24
---
# Descarga de proyectos BIM (modelos reales para entrenar a JARVIS)

Todo se descarga en **`C:\Users\JHORDAN\Documents\1.APP CREADOS\APP PARA BIM\02_PROYECTOS_BIM`**.

## Paso a paso (Windows)
1. Instala **Git para Windows** y **Python 3.11+** (marca *Add to PATH*).
2. Clona este repositorio dentro de la carpeta base:
   ```powershell
   cd "C:\Users\JHORDAN\Documents\1.APP CREADOS\APP PARA BIM"
   git clone https://github.com/fernandezjhordan17-netizen/ing.jhoel.git
   cd ing.jhoel
   ```
3. Ejecuta el instalador completo:
   ```powershell
   powershell -ExecutionPolicy Bypass -File .\scripts\INSTALAR_JARVIS_BIM.ps1
   ```
   Opciones: `-IncluirPesados` (Community Sample Files con Git LFS + Dynamo Primer), `-SinServidoresMCP`, `-SinArchivosLocales`.
4. Abre la bóveda en Obsidian: las notas nuevas aparecen en [[Resumen de modelos de estudio]].

## Qué descarga (fuentes verificadas)
| Carpeta | Fuente | Contenido |
|---|---|---|
| `IfcSampleFiles\` | github.com/youshengCode/IfcSampleFiles | 18 IFC: Duplex (ARQ, MEP, eléctrico, mecánico, sanitario), Revit ARC/STR/MEP en IFC4, SampleHouse, SampleCastle, ejemplos de geometría |
| `buildingSMART_Sample-Test-Files\` | github.com/buildingSMART/Sample-Test-Files | Conjuntos de certificación: *Simple-Scene* (edificio y obras de infraestructura) en IFC2x3, IFC4 e IFC 4.3 |
| `buildingSMART_IFC4.3_sample-models\` | github.com/buildingSMART/IFC4.3.x-sample-models | Ejemplos por tema: alineamientos, estructuras, programación de obra, geometría → [[BIM para infraestructura]] |
| `_ESTANDARES\IDS\` | github.com/buildingSMART/IDS | Esquema, manual y casos de prueba de [[IDS - Information Delivery Specification]] |
| `_ESTANDARES\BCF-XML\` | github.com/buildingSMART/BCF-XML | Especificación y ejemplos de [[BCF - BIM Collaboration Format]] 3.0 |
| `buildingSMART_Community-Sample-Test-Files\` *(opcional)* | github.com/buildingsmart-community | Modelos aportados por la comunidad (requiere Git LFS) |
| `_APRENDIZAJE\DynamoPrimer\` *(opcional)* | github.com/DynamoDS/DynamoPrimerNew | Manual de [[Dynamo]] |
| `LOCAL_<Programa>\` | **Tu propio PC** | Ejemplos instalados con Revit, Dynamo, Navisworks, Robot, ETABS, SAP2000, SAFE, AutoCAD/Civil 3D (carpetas *Samples/Examples/Tutorials*); los modelos de Tekla se registran en el manifiesto |
| `MANIFIESTO.csv` | Script | Inventario de todo lo obtenido |

## Descargas manuales (requieren cuenta o licencia)
| Recurso | Dónde |
|---|---|
| Proyectos de muestra de Revit (incluye **Snowdon Towers**: arquitectura, estructura, MEP, fachadas, sitio y nube de puntos) | Ayuda de Revit → "Revit Sample Project Files" (help.autodesk.com) |
| Modelos y extensiones de Tekla | Tekla Warehouse (warehouse.tekla.com) |
| Ejemplos y manuales de verificación de ETABS/SAP2000/SAFE | Instalación de CSI y csiamerica.com |
| Familias y objetos | [[Bibliotecas de familias BIM]] |

## Convertir modelos en conocimiento
```powershell
python scripts\03_ifc_a_obsidian.py --entrada "C:\Users\JHORDAN\Documents\1.APP CREADOS\APP PARA BIM\02_PROYECTOS_BIM" --boveda JARVIS-BIM --raiz-mostrada 02_PROYECTOS_BIM
```
Cada IFC genera una nota con ficha, estructura espacial, clases IFC enlazadas a [[Clases IFC principales]], datos (materiales, Psets, clasificación), diagnóstico de calidad y preguntas de estudio. Los casos de prueba de IDS/BCF se excluyen automáticamente.

> [!note] Ya incluidas
> La bóveda trae **99 notas de estudio** generadas con estas mismas fuentes. Al ejecutar el script en tu PC se regeneran (mismos nombres) y se agregan tus modelos locales.

## Proyectos completos para practicar
[[Proyecto integrador - Revit ARQ EST MEP]] · [[MOC Proyectos de Estudio]]

↑ [[Caja de herramientas BIM]] · [[JARVIS BIM - Inicio]]
