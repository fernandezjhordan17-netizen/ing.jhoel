---
tipo: mcp
tags: [mcp, obsidian, memoria]
aliases: [Obsidian MCP, Memoria JARVIS]
actualizado: 2026-09-24
---
# MCP — Obsidian (memoria de JARVIS)

Esta bóveda es la **memoria de largo plazo**. Tres formas de conectarla:

| Opción | Cómo | Pros / contras |
|---|---|---|
| **A. Claude Code en el repositorio** | Abrir Claude Code en la carpeta `ing.jhoel`; lee/escribe las notas como archivos y sigue `CLAUDE.md` | Lo más simple y potente; ya funciona hoy |
| **B. Servidor MCP de sistema de archivos** | `@modelcontextprotocol/server-filesystem` apuntando a `JARVIS-BIM` (ver [[Configuracion de clientes MCP]]) | Funciona en Claude Desktop sin plugins; sin búsqueda semántica |
| **C. Plugin Local REST API (con MCP)** | Plugin de Obsidian que desde la v4 (2026) sirve MCP directamente (leer, parchear notas, búsquedas) | Respeta la estructura de Obsidian (encabezados, frontmatter); requiere Obsidian abierto y token |
| **+ Smart Connections MCP** | Búsqueda **semántica** sobre los embeddings locales de Smart Connections (`msdanyg/smart-connections-mcp`) | La "red neuronal" real: encuentra notas por significado |

Configuración completa: [[Activar la red neuronal - Smart Connections]].

## Reglas de escritura de JARVIS en la bóveda
1. Nunca borrar notas; marcar como `estado: obsoleto`.
2. Toda nota nueva con frontmatter y enlace a su MOC ([[Como usar esta boveda]]).
3. Bitácora diaria en `00 INICIO/Diario JARVIS` ([[Plantilla - Diario JARVIS]]).
4. Datos de proyectos reales en `70 PROYECTOS/Proyectos activos` ([[Plantilla - Proyecto]]).
5. Respaldar con git (plugin Obsidian Git) → versión y trazabilidad.

↑ [[MOC JARVIS y MCP]] · [[Red neuronal de conocimiento]]
