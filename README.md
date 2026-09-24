# JARVIS BIM 🧠🏗️

Cerebro de conocimiento (bóveda de **Obsidian**) y herramientas para construir **JARVIS**: un asistente/agente de ingeniería que domina la **metodología BIM** y la normativa, gestiona tus proyectos y se conecta por **MCP (Model Context Protocol)** a Revit, Dynamo, AutoCAD, Civil 3D, Navisworks, Robot, ETABS, SAP2000, SAFE, Tekla y Excel.

## Qué contiene
| Carpeta | Contenido |
|---|---|
| `JARVIS-BIM/` | Bóveda de Obsidian: **259 notas** y **3 200+ enlaces**, organizadas como una red (MOCs → conceptos → normas → software → MCP → gestión → proyectos) |
| `JARVIS-BIM/70 PROYECTOS/Proyectos de estudio/` | **99 modelos IFC reales** (Duplex, Revit ARC/STR/MEP, SampleHouse, puentes/vías/ferrovías IFC 4.3…) analizados automáticamente |
| `scripts/` | Descarga de modelos BIM, clonado de servidores MCP, conversor IFC → Obsidian, verificador del grafo |
| `jarvis/` | Configuraciones de Claude Desktop / Claude Code para los servidores MCP |
| `.claude/agents/` | Agentes especializados: coordinador BIM, estructural, gestor de proyectos, auditor de calidad |
| `CLAUDE.md` | Instrucciones de comportamiento de JARVIS |

## Temas cubiertos
- **Metodología**: BIM 3D–7D, LOD/LOIN, usos y roles BIM, CDE, OIR/AIR/PIR/EIR, PEB, MIDP/TIDP, nomenclatura, coordinación, QA/QC, VDC, Lean, gemelo digital, infraestructura, GIS, Scan-to-BIM.
- **Normas**: ISO 19650-1 a -6, IFC (ISO 16739-1:2024), IDS 1.0, BCF, COBie, ISO 7817 (LOIN), ISO 29481, ISO 12006, ISO 23386/23387, bSDD; **Perú**: Plan BIM Perú, Guía Nacional BIM, NTP-ISO 19650, Ley 32069, RD 0007-2025-EF/63.01 (BIM obligatorio desde 14-08-2026), RNE (E.020, E.030, E.050, E.060, E.070, E.090); ACI 318, ASCE 7, AISC, Eurocódigos.
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

## Mantenimiento
```bash
python scripts/04_salud_red_neuronal.py   # debe terminar en "SANA"
```
