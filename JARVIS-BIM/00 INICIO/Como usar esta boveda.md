---
tipo: guia
tags: [inicio, obsidian, guia]
aliases: [Manual de la boveda, Guia Obsidian]
actualizado: 2026-09-24
---
# Cómo usar esta bóveda (Obsidian)

## 1. Abrir la bóveda
1. Instala Obsidian (obsidian.md).
2. `Abrir carpeta como bóveda` → selecciona la carpeta `JARVIS-BIM` dentro de
   `C:\Users\JHORDAN\Documents\1.APP CREADOS\APP PARA BIM\ing.jhoel\JARVIS-BIM`.
3. La configuración (`.obsidian/`) ya trae: colores del grafo por área, carpeta de plantillas y notas diarias.

## 2. Plugins comunitarios recomendados
| Plugin | Para qué lo usa JARVIS |
|---|---|
| **Dataview** | Tablas dinámicas de proyectos, normas y tareas (ver [[Indice de proyectos]]) |
| **Templater** | Plantillas avanzadas (las de la carpeta `80 PLANTILLAS` (p. ej. [[Plantilla - Proyecto]]) funcionan también con el núcleo) |
| **Smart Connections** | Embeddings locales → conexiones semánticas automáticas ([[Red neuronal de conocimiento]]) |
| **Local REST API** (con MCP) | Permite que JARVIS lea/escriba notas vía MCP ([[MCP Obsidian - Memoria de JARVIS]]) |
| **Excalidraw** | Croquis, diagramas de flujo BIM |
| **Obsidian Git** | Sincroniza la bóveda con GitHub (respaldo y versión) |
| **Tasks** | Tareas con fechas dentro de notas de proyecto |
| **Kanban** | Tableros de seguimiento (entregables, RFIs) |

Actívalos en *Configuración → Complementos de la comunidad*.

## 3. Estructura de carpetas (capas de la red)
| Carpeta | Capa | Color en grafo |
|---|---|---|
| `00 INICIO` / `10 MAPAS` | Hubs / entrada | Dorado |
| `20 METODOLOGIA BIM` | Conceptos | Azul |
| `30 NORMAS` | Normativa | Rojo |
| `40 SOFTWARE` | Herramientas | Verde |
| `50 JARVIS` | Agente + MCP | Morado |
| `60 GESTION DE PROYECTOS` | Gestión | Naranja |
| `70 PROYECTOS` | Datos reales | Cian |
| `80 PLANTILLAS` | Plantillas | Gris |
| `90 RECURSOS` | Fuentes | Rosa |

## 4. Convenciones
- **Nombres de archivo** sin tildes ni `:` `/` (compatibilidad Windows/Git); el título visible puede llevar tildes.
- **Frontmatter** obligatorio: `tipo`, `tags`, `aliases`, `actualizado`.
- Toda nota nueva debe enlazar **al menos a un MOC** y a 2–3 notas hermanas (sin neuronas huérfanas).
- Etiquetas jerárquicas: `#bim/…`, `#norma/iso`, `#norma/peru`, `#software/…`, `#mcp`, `#jarvis`, `#gestion`, `#estructural`.
- Callouts: `> [!warning]` para riesgos, `> [!tip]` para buenas prácticas, `> [!todo]` para pendientes de verificación.

## 5. Mantener la red sana
Ejecuta `python scripts/04_salud_red_neuronal.py` para detectar enlaces rotos y notas huérfanas. Ver [[Red neuronal de conocimiento]].

## 6. Relación con JARVIS
JARVIS (Claude + MCP) lee esta bóveda como contexto. Instrucciones de comportamiento en `CLAUDE.md` (raíz del repositorio) y en [[JARVIS - Biblioteca de prompts]].

Volver a [[JARVIS BIM - Inicio]].
