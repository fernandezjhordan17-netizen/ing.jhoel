---
tipo: jarvis
tags: [jarvis, pruebas, calidad]
aliases: [Evaluacion JARVIS, Tests JARVIS]
actualizado: 2026-09-24
---
# JARVIS — Pruebas y evaluación

## Tipos de prueba
| Tipo | Ejemplo | Criterio |
|---|---|---|
| Conocimiento | 30 preguntas de normas (E.030, ISO 19650, IFC) | ≥ 95 % correctas **con cita** |
| Lectura de modelos | Conteos por clase en modelos de [[MOC Proyectos de Estudio]] | Coinciden con IfcOpenShell |
| Escritura | Cambiar 100 parámetros en copia de modelo | 0 errores, 1 transacción, deshacible |
| Análisis | Pórtico simple con solución manual conocida | Diferencia < 1 % |
| Seguridad | Instrucción maliciosa dentro de un parámetro/correo | JARVIS la ignora y avisa |
| Robustez | Programa cerrado / dos instancias abiertas | Mensaje claro, sin bloqueo |

## Conjunto de referencia
Usar los modelos descargados ([[Descarga de proyectos BIM]]) como **banco de pruebas fijo**: las notas generadas por `03_ifc_a_obsidian.py` son la "respuesta correcta" de conteos.

## Registro
Resultados en la nota del mes dentro de `00 INICIO/Diario JARVIS`; errores → nueva regla en [[JARVIS - Seguridad y gobernanza]] o mejora de prompt en [[JARVIS - Biblioteca de prompts]].

↑ [[MOC JARVIS y MCP]]
