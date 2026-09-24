# Configuración de clientes MCP para JARVIS

| Archivo | Uso |
|---|---|
| `claude_desktop_config.ejemplo.json` | **Empieza aquí.** Conecta Claude Desktop a la bóveda de Obsidian (lectura/escritura de notas) y a Excel. Solo requiere Node.js LTS y `uv`. |
| `claude_desktop_config.completo.ejemplo.json` | Agrega Revit, ETABS, Robot y AutoCAD con los comandos que indican los README de cada servidor. **Actívalos uno por uno**, solo después de instalar y probar cada servidor (ver `scripts/02_clonar_servidores_mcp.ps1`). |
| `mcp.json.ejemplo` | Para Claude Code: cópialo como `.mcp.json` en la raíz del repositorio. |

Ubicación en Windows: `%APPDATA%\Claude\claude_desktop_config.json` (Claude Desktop → Configuración → Desarrollador → Editar configuración). Reinicia Claude Desktop después de guardar.

Revit 2027 con el **MCP oficial de Autodesk** (Technical Preview) no necesita entrada manual: su instalador configura Claude Desktop.

Instalación de los servidores Python clonados (ejemplo ETABS):
```powershell
cd "C:\Users\JHORDAN\Documents\1.APP CREADOS\APP PARA BIM\04_MCP_SERVERS\CSI\ETABS-mcp"
py -3 -m venv .venv
.\.venv\Scripts\pip install -e .
.\.venv\Scripts\etabs-mcp --help
```

Detalles y diagnóstico: `JARVIS-BIM/50 JARVIS/Configuracion de clientes MCP.md`.
