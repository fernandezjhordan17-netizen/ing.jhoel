---
tipo: guia
tags: [proyecto, guia]
aliases: [Registrar proyecto]
actualizado: 2026-09-25
---
# Cómo registrar un proyecto real

1. En esta carpeta: *Nueva nota* → *Insertar plantilla* → [[Plantilla - Proyecto]].
2. Nombre de la nota = código del proyecto + nombre corto (p. ej. `PRJ01 Colegio Chiclayo`).
3. Llena el frontmatter (estado, fase, zona sísmica, suelo…): alimenta el [[Indice de proyectos]] y los [[KPIs de proyectos BIM]].
4. Guarda los modelos **fuera de git** en `03_PROYECTOS_REALES` (ver [[JARVIS - Arquitectura]]) y enlázalos por ruta.
5. Pide a JARVIS: "Lee la nota del proyecto PRJ01 y prepara el EIR/PEB".

## Con JARVIS (recomendado)
1. Copia `jarvis/proyectos/PRY001_ejemplo.json` como `PRY002_<nombre>.json` y reemplaza los datos: zona (Anexo II), perfil y Vs30 del EMS ([[E.050 - Suelos y Cimentaciones]]), categoría, sistema e irregularidades por dirección, niveles (altura y área), cargas ([[E.020 - Cargas]]), vigas y columnas a verificar, `modelo_ifc` (opcional, para metrados).
2. Dry-run: `python scripts/08_ejecutar_proyecto.py jarvis/proyectos/PRY002_<nombre>.json` (o pide a Claude *"ejecuta el proyecto PRY002"* → `proyecto_ejecutar`).
3. Revisa alertas y pendientes; luego `--confirmar` → se crean la nota del proyecto, la memoria ([[Plantilla - Memoria de calculo]]) y el Excel en `90 RECURSOS/Adjuntos/Proyectos/`.
4. Tras correr ETABS, copia la cortante dinámica y las derivas elásticas en `resultados_etabs` y vuelve a ejecutar: se agregan el escalamiento (art. 44) y la verificación de derivas.

Ejemplo terminado: [[PRY001 Edificio multifamiliar 5 pisos (ejemplo)]].
