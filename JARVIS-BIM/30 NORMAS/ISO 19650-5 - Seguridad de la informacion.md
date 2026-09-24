---
tipo: norma
tags: [norma/iso, iso19650, seguridad]
aliases: [ISO 19650-5, Security-minded, Seguridad de la informacion BIM]
anio: 2020
actualizado: 2026-09-24
---
# ISO 19650-5:2020 — Enfoque de seguridad para la gestión de la información

Para activos **sensibles** (infraestructura crítica, hospitales, instalaciones de seguridad, datos personales).

## Proceso
1. **Evaluación de sensibilidad** del activo y su información.
2. Si es sensible → **estrategia de seguridad** y **plan de gestión de la seguridad**.
3. Gestión de **incidentes y brechas** de seguridad.
4. Requisitos de seguridad en los EIR/contratos ([[EIR - Requisitos de Intercambio de Informacion]]).
5. Controles: acceso por rol en el [[CDE - Entorno Comun de Datos]], segregación, trazabilidad, borrado seguro, gestión de proveedores.

## Aplicación directa a JARVIS
Un agente con acceso a modelos y correo **es un riesgo de seguridad** si no se controla:
- Principio de **mínimo privilegio** por servidor MCP.
- Servidores MCP locales enlazados a `127.0.0.1`, con token.
- Registro (bitácora) de cada acción de escritura.
- No enviar modelos sensibles a servicios externos sin autorización.
Ver [[JARVIS - Seguridad y gobernanza]].

Adopción Perú: NTP-ISO 19650-5:2024 → [[NTP-ISO 19650 Peru]]

↑ [[ISO 19650 - Serie completa]] · Siguiente: [[ISO 19650-6 - Salud y seguridad]]
