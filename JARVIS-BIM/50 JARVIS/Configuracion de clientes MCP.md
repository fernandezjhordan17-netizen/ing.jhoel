---
tipo: jarvis
tags: [mcp, configuracion]
aliases: [claude_desktop_config, Configurar MCP, .mcp.json]
actualizado: 2026-09-24
---
# Configuración de clientes MCP

## Claude Desktop (Windows)
Archivo: `%APPDATA%\Claude\claude_desktop_config.json` (menú *Configuración → Desarrollador → Editar configuración*). Reiniciar Claude Desktop después de editar.

Ejemplo **funcional mínimo** (en el repo: `jarvis/claude_desktop_config.ejemplo.json`):
```json
{
  "mcpServers": {
    "boveda-jarvis": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-filesystem",
               "C:\\Users\\JHORDAN\\Documents\\1.APP CREADOS\\APP PARA BIM\\ing.jhoel\\JARVIS-BIM"]
    },
    "excel": {
      "command": "uvx",
      "args": ["excel-mcp-server", "stdio"]
    }
  }
}
```
Requisitos: Node.js LTS (para `npx`) y `uv` (para `uvx`) → [[JARVIS - Stack tecnologico]].

## Agregar los servidores de software
Comandos tomados de los README de cada servidor (versión completa en `jarvis/claude_desktop_config.completo.ejemplo.json`; `<MCP>` = `C:\Users\JHORDAN\Documents\1.APP CREADOS\APP PARA BIM\04_MCP_SERVERS`):

| Servidor | `command` | `args` / `env` |
|---|---|---|
| Revit (`mcp-servers-for-revit`) | `cmd` | `["/c", "npx", "-y", "mcp-server-for-revit"]` + plugin copiado en `%AppData%\Autodesk\Revit\Addins\<año>` |
| ETABS (`ETABS-mcp`) | `<MCP>\CSI\ETABS-mcp\.venv\Scripts\etabs-mcp.exe` | `[]` (alternativa: `python -m etabs_mcp.server` desde su venv) |
| Robot (`robot-structural-mcp`) | `<MCP>\Robot\robot-structural-mcp\.venv\Scripts\python.exe` | `["-m", "robot_mcp"]`, env `ROBOT_MCP_MAX_ITEMS=200` |
| AutoCAD (`autocad-mcp`) | `<MCP>\AutoCAD\autocad-mcp\.venv\Scripts\python.exe` | `["-m", "autocad_mcp"]`, env `AUTOCAD_MCP_BACKEND=auto` |
| Excel (`excel-mcp-server`) | `uvx` | `["excel-mcp-server", "stdio"]` |
| **JARVIS BIM (propio)** | `...\ing.jhoel\jarvis-mcp\.venv\Scripts\jarvis-bim-mcp.exe` | env `JARVIS_BOVEDA=...\JARVIS-BIM` — lo configura `scripts/07_instalar_jarvis_mcp.ps1` → [[MCP JARVIS BIM - Servidor propio]] |
| Revit 2027 oficial | — | Se configura solo al instalar el complemento |

> [!warning] Antes de activar un servidor: instálalo en su propio entorno virtual (`py -3 -m venv .venv` + `pip install -e .`), lee su README (cambia entre versiones) y pruébalo con una **copia** del modelo. Activa los servidores **de uno en uno**.

## Claude Code
- Por proyecto: archivo `.mcp.json` en la raíz del repo (plantilla: `jarvis/mcp.json.ejemplo`).
- Por comando: `claude mcp add excel -- uvx excel-mcp-server stdio`.
- Verificar: `claude mcp list` y `/mcp` dentro de la sesión.

## Diagnóstico
| Síntoma | Causa típica |
|---|---|
| El servidor no aparece | JSON inválido (comas, `\\` en rutas) o no se reinició Claude |
| "spawn ENOENT" | Comando no está en el PATH → usar ruta absoluta |
| Herramientas fallan con COM | El programa (ETABS/Robot) no está abierto o hay dos instancias |
| Revit no responde | Add-in no cargado o comando no habilitado en la cinta |

↑ [[MOC JARVIS y MCP]] · [[MCP - Fundamentos]]
