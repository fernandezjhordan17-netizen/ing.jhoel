---
tipo: concepto
tags: [ia, machine-learning, aec]
aliases: [IA en construccion, Machine learning AEC, Inteligencia artificial BIM]
actualizado: 2026-09-24
---
# IA y Machine Learning en AEC

| Aplicación | Técnica | Ejemplo |
|---|---|---|
| Agentes que operan software | LLM + herramientas (MCP) | JARVIS, Autodesk Assistant, BIBIM → [[JARVIS - Arquitectura]] |
| Consulta de documentos | RAG / embeddings | Preguntar a la ISO 19650 o a un BEP → [[Red neuronal de conocimiento]] |
| Diseño generativo | Optimización multiobjetivo, algoritmos genéticos | Dynamo Generative Design, distribución de estacionamientos |
| Modelos sustitutos (surrogate) | Redes neuronales entrenadas con resultados FEM | Predicción rápida de derivas/periodos en prediseño |
| Clasificación de elementos | ML sobre propiedades/geometría | Asignar clases IFC o códigos Uniclass automáticamente |
| Coordinación | Clustering/clasificación de choques | Agrupar interferencias relevantes vs ruido |
| Estimación de costos | Regresión / gradient boosting | Costo por m² a partir de parámetros del proyecto |
| Visión por computadora | CNN / segmentación | Avance de obra por fotos, EPP en seguridad, Scan-to-BIM |
| Grafos | GNN sobre el grafo IFC | Detección de errores de modelado, recomendación de conexiones |
| Mantenimiento predictivo | Series de tiempo | Equipos MEP en [[Gemelo Digital]] |

## Riesgos
Datos sesgados o escasos, "cajas negras" en decisiones de seguridad estructural, alucinaciones de LLM → reglas de [[JARVIS - Seguridad y gobernanza]].

## Próximos pasos de aprendizaje
Python para ingenieros → pandas → scikit-learn → PyTorch; datos de entrenamiento: los modelos de [[MOC Proyectos de Estudio]] y tus propios proyectos.

↑ [[MOC JARVIS y MCP]] · [[Herramientas de IA para BIM]]
