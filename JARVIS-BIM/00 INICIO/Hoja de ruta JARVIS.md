---
tipo: plan
tags: [inicio, jarvis, roadmap]
aliases: [Roadmap JARVIS, Plan JARVIS]
actualizado: 2026-09-24
---
# Hoja de ruta de JARVIS

> [!info] Principio rector
> Primero **conocimiento** (esta bóveda), luego **lectura** de modelos (MCP en modo solo lectura), luego **escritura controlada** (con confirmación humana y transacciones deshacibles), y al final **orquestación multi-agente**.

## Fase 0 — Cerebro (✅ esta entrega)
- [x] Estudio de metodología BIM y normas → [[MOC Metodologia BIM]], [[MOC Normas y Estandares]]
- [x] Estudio de software, APIs y servidores MCP existentes → [[MOC Software AEC]], [[MOC JARVIS y MCP]]
- [x] Bóveda Obsidian con grafo ("red neuronal") → [[Red neuronal de conocimiento]]
- [x] Scripts de descarga de modelos BIM → [[Descarga de proyectos BIM]]
- [x] Generador IFC → notas de proyecto → [[MOC Proyectos de Estudio]]

## Fase 1 — Memoria conectada (semana 1–2)
- [ ] Instalar plugin Local REST API con MCP y conectar Obsidian a Claude → [[MCP Obsidian - Memoria de JARVIS]]
- [ ] Instalar Smart Connections (embeddings locales)
- [ ] Probar prompts de consulta normativa → [[JARVIS - Biblioteca de prompts]]

## Fase 2 — Ojos (solo lectura) (semana 3–6)
- [ ] Excel MCP (sin riesgo) → [[MCP Excel]]
- [ ] Revit MCP oficial (Technical Preview, Revit 2027) o comunitario → [[MCP Revit]]
- [ ] ETABS/SAP2000 lectura de resultados vía OAPI → [[MCP CSI - ETABS SAP2000 SAFE]]
- [ ] Navisworks: leer reportes de interferencias → [[MCP Navisworks]]
- [ ] Criterio de salida: JARVIS responde preguntas sobre un modelo real sin exportar a mano.

## Fase 3 — Manos (escritura controlada) (semana 7–12)
- [ ] Revit: crear/editar parámetros en lote con transacción única
- [ ] ETABS: generar modelo desde plantilla, asignar cargas E.020/E.030, correr análisis
- [ ] Dynamo: generar grafos desde lenguaje natural → [[MCP Dynamo]]
- [ ] AutoCAD/Civil 3D: planos y alineamientos → [[MCP AutoCAD y Civil 3D]]
- [ ] Tekla: modelado de acero → [[MCP Tekla Structures]]
- [ ] Robot: análisis alternativo → [[MCP Robot Structural Analysis]]
- [ ] Reglas de [[JARVIS - Seguridad y gobernanza]] activas (dry-run, confirmación, bitácora).

## Fase 4 — Cerebro ejecutivo (mes 4+)
- [ ] Agentes especializados → [[JARVIS - Agentes especializados]]
- [ ] Flujos punta a punta → [[JARVIS - Flujos de trabajo]]
- [ ] Integración con gestión (Asana/Linear/Calendar/Gmail) → [[MCP Gestion de Proyectos]]
- [ ] Tablero de KPIs → [[KPIs de proyectos BIM]]
- [ ] Batería de pruebas → [[JARVIS - Pruebas y evaluacion]]

## Riesgos principales
| Riesgo | Mitigación |
|---|---|
| Servidores MCP comunitarios inmaduros | Probar en copia del modelo; preferir oficiales cuando existan |
| APIs COM de un solo hilo (CSI, Robot) | Cola de comandos y una instancia por proceso ([[Patrones de puente MCP para software de escritorio]]) |
| Alucinaciones en cálculos | JARVIS nunca "inventa" resultados: siempre los lee del software y cita la norma ([[JARVIS - Seguridad y gobernanza]]) |
| Licencias/versiones distintas | Matriz de versiones en [[JARVIS - Stack tecnologico]] |

Volver a [[JARVIS BIM - Inicio]].
