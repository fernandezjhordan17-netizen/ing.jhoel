"""Bitácora de acciones de JARVIS en el Diario de la bóveda (trazabilidad, ISO 19650-5)."""
from __future__ import annotations

import datetime as dt
from pathlib import Path

from .boveda import ruta_boveda

CARPETA = Path("00 INICIO") / "Diario JARVIS"
CABECERA = """---
tipo: diario
fecha: {fecha}
tags: [diario, jarvis]
---
# Diario JARVIS — {fecha}

## Acciones ejecutadas
| Hora | Herramienta MCP | Acción | Lectura/Escritura | Confirmado por | Resultado |
|---|---|---|---|---|---|
"""


def registrar(herramienta: str, accion: str, modo: str = "lectura", confirmado_por: str = "—",
              resultado: str = "ok", boveda: Path | None = None) -> Path:
    raiz = boveda or ruta_boveda()
    ahora = dt.datetime.now()
    nota = raiz / CARPETA / f"{ahora:%Y-%m-%d}.md"
    nota.parent.mkdir(parents=True, exist_ok=True)
    if not nota.exists():
        nota.write_text(CABECERA.format(fecha=f"{ahora:%Y-%m-%d}") +
                        "\n↑ [[Indice del Diario JARVIS]] · [[JARVIS - Seguridad y gobernanza]]\n", encoding="utf-8")
    fila = "| {} | {} | {} | {} | {} | {} |".format(
        f"{ahora:%H:%M:%S}", herramienta, accion.replace("|", "/")[:200], modo, confirmado_por,
        str(resultado).replace("|", "/").replace("\n", " ")[:200])
    contenido = nota.read_text(encoding="utf-8")
    marcador = "\n↑ [[Indice del Diario JARVIS]]"
    if marcador in contenido:
        contenido = contenido.replace(marcador, f"{fila}\n{marcador}", 1)
    else:
        contenido += f"\n{fila}\n"
    nota.write_text(contenido, encoding="utf-8")
    return nota
