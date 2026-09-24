---
tipo: jarvis
tags: [jarvis, obsidian, grafo, ia]
aliases: [Red neuronal, Grafo de conocimiento, Knowledge graph]
actualizado: 2026-09-24
---
# Red neuronal de conocimiento

## La metáfora (y por qué funciona)
| Red neuronal | Esta bóveda |
|---|---|
| Neurona | Nota atómica (un concepto, una norma, un software) |
| Sinapsis | `[[enlace]]` entre notas |
| Peso de la conexión | Cantidad de enlaces/menciones (tamaño del nodo en el grafo) |
| Capas | Carpetas: inicio → metodología → normas → software → JARVIS → gestión → proyectos |
| Neuronas "hub" | MOCs ([[MOC Metodologia BIM]], [[MOC Normas y Estandares]]…) |
| Activación | Consulta: JARVIS entra por un MOC y recorre enlaces |
| Entrenamiento | Cada proyecto nuevo agrega notas y enlaces ([[MOC Proyectos de Estudio]]) |

## La red neuronal "real": embeddings
El plugin **Smart Connections** calcula **embeddings** (vectores generados por un modelo de lenguaje local) de cada nota y bloque. Así encuentra relaciones **por significado** aunque no exista un enlace escrito. Con su servidor MCP, JARVIS hace búsqueda semántica → [[MCP Obsidian - Memoria de JARVIS]]. Esto es, en la práctica, **RAG** (Retrieval-Augmented Generation): recuperar las notas relevantes y dárselas al modelo como contexto.

## Ver la red
- `Ctrl+G` → vista de grafo. Colores por capa (configurados en `.obsidian/graph.json`): dorado hubs, azul metodología, rojo normas, verde software, morado JARVIS, naranja gestión, cian proyectos.
- Grafo local de una nota: clic derecho → *Abrir grafo local* (muestra sus "sinapsis" a 2–3 saltos).

## Mantenerla sana
`python scripts/04_salud_red_neuronal.py` reporta: número de neuronas y sinapsis, enlaces rotos, notas huérfanas, hubs más conectados y densidad por capa.

## Reglas de crecimiento
1. Una idea = una nota.
2. Cada nota nueva ≥ 3 enlaces (MOC + 2 hermanas).
3. Revisar huérfanas cada semana.
4. Preferir enlazar a crear duplicados (usar `aliases`).

Relacionado: [[IA y Machine Learning en AEC]] · [[Como usar esta boveda]]

↑ [[MOC JARVIS y MCP]]
