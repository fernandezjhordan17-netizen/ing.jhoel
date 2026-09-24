---
tipo: jarvis
tags: [jarvis, stack, instalacion]
aliases: [Stack JARVIS, Requisitos JARVIS, Matriz de versiones]
actualizado: 2026-09-24
---
# JARVIS — Stack tecnológico

## Estación de trabajo
Windows 10/11 64 bits (todo el software AEC y COM lo exige), 32 GB RAM recomendados, GPU dedicada.

## Software base
| Componente | Para qué | Nota |
|---|---|---|
| **Obsidian** | Memoria / bóveda | [[Como usar esta boveda]] |
| **Claude Desktop** y **Claude Code** | Interfaz y cerebro | [[Configuracion de clientes MCP]] |
| **Git** (+ Git LFS) | Versionar bóveda y clonar servidores/modelos | |
| **Python 3.11/3.12** + **uv** | Servidores MCP Python, scripts | `pip install uv` |
| **Node.js LTS** | Servidores MCP en TypeScript (`npx`) | |
| **.NET 8 SDK** + Visual Studio 2022 | Add-ins de Revit 2025–2027, Navisworks, Tekla, AutoCAD | .NET Framework 4.8 para Revit ≤ 2024 |

## Librerías
| Python | C# |
|---|---|
| `mcp` (FastMCP), `comtypes`, `pywin32`, `pythonnet`, `ifcopenshell`, `openpyxl`, `pandas`, `xlwings`, `ezdxf` | `ModelContextProtocol` (SDK oficial), Revit API, Navisworks API, Tekla Open API (NuGet por versión), AutoCAD/Civil 3D .NET |

## Matriz de versiones (llenar con lo instalado)
| Programa | Versión instalada | API/MCP elegido | Probado |
|---|---|---|---|
| Revit |  | [[MCP Revit]] | ☐ |
| Dynamo |  | [[MCP Dynamo]] | ☐ |
| AutoCAD / Civil 3D |  | [[MCP AutoCAD y Civil 3D]] | ☐ |
| Navisworks Manage |  | [[MCP Navisworks]] | ☐ |
| ETABS / SAP2000 / SAFE |  | [[MCP CSI - ETABS SAP2000 SAFE]] | ☐ |
| Robot |  | [[MCP Robot Structural Analysis]] | ☐ |
| Tekla Structures |  | [[MCP Tekla Structures]] | ☐ |
| Excel |  | [[MCP Excel]] | ☐ |

↑ [[MOC JARVIS y MCP]] · [[JARVIS - Arquitectura]]
