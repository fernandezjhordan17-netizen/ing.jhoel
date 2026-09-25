# JARVIS BIM 🧠🏗️

Cerebro de conocimiento (bóveda de **Obsidian**) y herramientas para construir **JARVIS**: un asistente/agente de ingeniería que domina la **metodología BIM** y la normativa, gestiona tus proyectos y se conecta por **MCP (Model Context Protocol)** a Revit, Dynamo, AutoCAD, Civil 3D, Navisworks, Robot, ETABS, SAP2000, SAFE, Tekla y Excel.

## Qué contiene
| Carpeta | Contenido |
|---|---|
| `JARVIS-BIM/` | Bóveda de Obsidian: **289 notas** y **3 480+ enlaces**, con **13 textos oficiales del RNE** completos (E.010–E.100, EM.110), organizadas como una red (MOCs → conceptos → normas → software → MCP → gestión → proyectos) |
| `JARVIS-BIM/70 PROYECTOS/Proyectos de estudio/` | **99 modelos IFC reales** (Duplex, Revit ARC/STR/MEP, SampleHouse, puentes/vías/ferrovías IFC 4.3…) analizados automáticamente |
| `scripts/` | Descarga de modelos BIM, clonado de servidores MCP, conversor IFC → Obsidian, verificador del grafo, **descarga de 29 normas y guías oficiales** (`catalogo_normas.csv`) y conversor PDF → notas por artículo |
| `jarvis-mcp/` | **Servidor MCP propio `jarvis-bim`**: 29 herramientas (E.030-2026, E.060, metrados IFC, bóveda, ISO 19650, ETABS/SAP2000) y 70 pruebas |
| `jarvis/` | Configuraciones de Claude Desktop / Claude Code para los servidores MCP |
| `.claude/agents/` | Agentes especializados: coordinador BIM, estructural, gestor de proyectos, auditor de calidad |
| `CLAUDE.md` | Instrucciones de comportamiento de JARVIS |

## Temas cubiertos
- **Metodología**: BIM 3D–7D, LOD/LOIN, usos y roles BIM, CDE, OIR/AIR/PIR/EIR, PEB, MIDP/TIDP, nomenclatura, coordinación, QA/QC, VDC, Lean, gemelo digital, infraestructura, GIS, Scan-to-BIM.
- **Normas**: E.030 **edición 2026** (RM 183-2026-VIVIENDA), A.010, A.120, A.130, IS.010, EM.010, E.031, G.050, OS, DG-2018, Norma de Metrados; ISO 19650-1 a -6, IFC (ISO 16739-1:2024), IDS 1.0, BCF, COBie, ISO 7817 (LOIN), ISO 29481, ISO 12006, ISO 23386/23387, bSDD; **Perú**: Plan BIM Perú, Guía Nacional BIM, NTP-ISO 19650, Ley 32069, RD 0007-2025-EF/63.01 (BIM obligatorio desde 14-08-2026), RNE (E.020, E.030, E.050, E.060, E.070, E.090); ACI 318, ASCE 7, AISC, Eurocódigos.
- **Software y APIs**: Revit API, Dynamo, AutoCAD/Civil 3D .NET y AutoLISP, Navisworks API, CSI OAPI, RobotOM, Tekla Open API, openpyxl/xlwings, IfcOpenShell, APS, Speckle.
- **JARVIS/MCP**: arquitectura, patrones de puente (COM, add-in + IPC, nube), servidores MCP existentes por programa (oficiales y comunitarios, sep. 2026), seguridad, agentes, flujos, prompts, pruebas.
- **Gestión**: PMBOK, ISO 21502, Invierte.pe, Last Planner, EVM, riesgos, calidad, NEC/FIDIC, RFIs, KPIs, SST.

## Inicio rápido (Windows)
```powershell
cd "C:\Users\JHORDAN\Documents\1.APP CREADOS\APP PARA BIM"
git clone https://github.com/fernandezjhordan17-netizen/ing.jhoel.git
cd ing.jhoel
powershell -ExecutionPolicy Bypass -File .\scripts\INSTALAR_JARVIS_BIM.ps1
```
Conectar JARVIS a Claude Desktop (servidor propio):
```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\07_instalar_jarvis_mcp.ps1
```

Luego: Obsidian → *Abrir carpeta como bóveda* → `ing.jhoel\JARVIS-BIM` → nota **"JARVIS BIM - Inicio"** → `Ctrl+G` para ver la red.

Estructura final en tu PC:
```
APP PARA BIM\
├─ ing.jhoel\            (este repositorio)
├─ 02_PROYECTOS_BIM\     (modelos descargados + ejemplos de tu software + MANIFIESTO.csv)
├─ 03_PROYECTOS_REALES\  (tus proyectos, fuera de git)
├─ 04_MCP_SERVERS\       (servidores MCP clonados para revisar)
└─ 05_RESPALDOS\
```

## Normas oficiales completas (red neuronal)
```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\05_descargar_normas_oficiales.ps1
```
Descarga los PDF oficiales a `JARVIS-BIM\90 RECURSOS\Adjuntos\Normas` (fuera de git) y los convierte en notas con un encabezado por artículo para que Smart Connections y JARVIS los absorban. Guía: `JARVIS-BIM/50 JARVIS/Activar la red neuronal - Smart Connections.md`.

## Mantenimiento
```bash
python scripts/04_salud_red_neuronal.py   # debe terminar en "SANA"
```
