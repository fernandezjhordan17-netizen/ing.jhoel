---
tipo: jarvis
tags: [mcp, protocolo]
aliases: [MCP, Model Context Protocol]
actualizado: 2026-09-24
---
# MCP — Model Context Protocol (fundamentos)

Estándar abierto (presentado por Anthropic en noviembre de 2024) para conectar aplicaciones de IA con herramientas y datos. "El USB-C de la IA": un cliente habla con **cualquier** servidor que implemente el protocolo.

## Roles
| Rol | Ejemplo en JARVIS |
|---|---|
| **Host** | Claude Desktop / Claude Code |
| **Cliente** | Conexión 1:1 que el host abre con cada servidor |
| **Servidor** | "Revit MCP", "ETABS MCP", "Excel MCP"… |

## Primitivas
- Del servidor: **Tools** (acciones invocables: `crear_muro`, `correr_analisis`), **Resources** (datos legibles: tabla de derivas, nota de Obsidian), **Prompts** (plantillas reutilizables).
- Del cliente: **Sampling** (el servidor pide al modelo que razone), **Roots** (carpetas permitidas), **Elicitation** (pedir datos/confirmación al usuario).

## Transporte
- **stdio**: el host lanza el servidor como proceso local (lo más seguro para software de escritorio).
- **Streamable HTTP**: servidor local o remoto por HTTP.
- Mensajes **JSON-RPC 2.0**; ciclo de vida: `initialize` → negociación de capacidades → llamadas.

## Versión de la especificación
La especificación **2026-07-28** (publicada el 28 de julio de 2026) introduce un núcleo **sin estado** (se eliminan las sesiones de protocolo y `Mcp-Session-Id`), encabezados `Mcp-Method`/`Mcp-Name` para enrutar, resultados de listas cacheables (`ttlMs`), endurecimiento de autorización y un marco formal de extensiones. Revisa la compatibilidad de cada servidor con la versión que use tu cliente.

## SDK
Python (`mcp`, incluye FastMCP), TypeScript, **C#** (`ModelContextProtocol`, ideal para add-ins .NET de Revit/Navisworks/Tekla), Java, Kotlin, Go, Rust, entre otros.

## Servidor mínimo en Python
```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("jarvis-normas")

DERIVAS_E030 = {"concreto armado": 0.007, "acero": 0.010, "albanileria": 0.005,
                "madera": 0.010, "muros de ductilidad limitada": 0.005}

@mcp.tool()
def deriva_maxima(material: str) -> float:
    """Deriva máxima de entrepiso según E.030 (versión 2018; verificar la vigente)."""
    return DERIVAS_E030[material.lower()]

if __name__ == "__main__":
    mcp.run()  # transporte stdio
```

Siguiente: [[Patrones de puente MCP para software de escritorio]] · [[Configuracion de clientes MCP]]

↑ [[MOC JARVIS y MCP]]
