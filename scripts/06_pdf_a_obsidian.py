#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
06_pdf_a_obsidian.py - Convierte PDF de normas y guias en notas Markdown de Obsidian.

Obsidian (y el plugin Smart Connections) solo "absorben" texto Markdown: un PDF adjunto no entra
en la red de embeddings. Este script extrae el texto de cada PDF, limpia encabezados/pies de pagina
repetidos, une lineas cortadas y detecta la estructura (Titulos, Capitulos, Articulos, Anexos) para
crear una nota por documento con un encabezado por articulo (ideal para busqueda semantica por bloque).

Uso:
    python scripts/06_pdf_a_obsidian.py --entrada "JARVIS-BIM/90 RECURSOS/Adjuntos/Normas" --boveda JARVIS-BIM

Requisitos: pip install pymupdf   (alternativa: pip install pypdf)
"""
from __future__ import annotations

import argparse
import collections
import csv
import datetime as dt
import re
import sys
from pathlib import Path

CARPETA_SALIDA = Path("30 NORMAS") / "Textos oficiales"
NOTA_INDICE = "Indice de textos oficiales"

RE_TITULO = re.compile(r"^\s*(T[ÍI]TULO)\s+([IVXLC\d]+)\b(.*)$", re.I)
RE_CAPITULO = re.compile(r"^\s*(CAP[ÍI]TULO)\s+([IVXLC\d]+)\b(.*)$", re.I)
RE_SUBCAP = re.compile(r"^\s*(SUBCAP[ÍI]TULO|SECCI[ÓO]N)\s+([IVXLC\d]+)\b(.*)$", re.I)
RE_ARTICULO = re.compile(r"^\s*(Art[íi]culo|ART[ÍI]CULO|Art\.)\s*(\d+[A-Za-z]?(?:\.\d+)*)\s*[\.\-–—°º:]*\s*(.*)$")
RE_ANEXO = re.compile(r"^\s*(ANEXO|Anexo)\s+([IVXLC\d]+|[A-Z])\b(.*)$")
RE_NUM_PAGINA = re.compile(r"^\s*(p[áa]g\.?\s*)?\d{1,6}\s*$", re.I)


def extraer_paginas(ruta: Path) -> list[str]:
    try:
        try:
            import pymupdf as fitz  # PyMuPDF >= 1.24
        except ImportError:
            import fitz  # PyMuPDF (nombre antiguo)
        with fitz.open(str(ruta)) as doc:
            return [p.get_text("text") for p in doc]
    except ImportError:
        pass
    try:
        from pypdf import PdfReader
    except ImportError:
        sys.exit("Instala una libreria PDF:  pip install pymupdf   (o  pip install pypdf)")
    return [p.extract_text() or "" for p in PdfReader(str(ruta)).pages]


def clave_repeticion(linea: str) -> str:
    return re.sub(r"\d+", "#", linea.strip().lower())


def limpiar(paginas: list[str]) -> list[str]:
    """Quita encabezados/pies repetidos y numeros de pagina; devuelve lineas."""
    frecuencia = collections.Counter()
    for texto in paginas:
        frecuencia.update({clave_repeticion(l) for l in texto.splitlines() if l.strip()})
    umbral = max(3, int(len(paginas) * 0.3))
    repetidas = {k for k, n in frecuencia.items() if n >= umbral and len(k) < 90}
    lineas = []
    for texto in paginas:
        for l in texto.splitlines():
            s = l.strip()
            if not s or RE_NUM_PAGINA.match(s) or clave_repeticion(s) in repetidas:
                continue
            lineas.append(s)
        lineas.append("")  # separador de pagina = posible fin de parrafo
    return lineas


def estructurar(lineas: list[str]) -> tuple[list[str], dict]:
    """Une lineas en parrafos y convierte Titulo/Capitulo/Articulo/Anexo en encabezados Markdown."""
    salida: list[str] = []
    parrafo: list[str] = []
    stats = collections.Counter()

    def cerrar():
        if parrafo:
            texto = " ".join(parrafo)
            texto = re.sub(r"(\w)- (\w)", r"\1\2", texto)  # guiones de fin de linea
            salida.append(texto)
            salida.append("")
            parrafo.clear()

    esperando_nombre = False  # el nombre de un capitulo suele venir en la linea siguiente
    for l in lineas:
        if not l:
            cerrar()
            continue
        if esperando_nombre:
            esperando_nombre = False
            if l.isupper() and len(l) < 100 and not RE_ARTICULO.match(l):
                salida[-2] += f" - {l.title() if len(l) > 3 else l}"
                continue
        for regex, nivel, tipo in ((RE_TITULO, "##", "titulos"), (RE_CAPITULO, "##", "capitulos"),
                                   (RE_ANEXO, "##", "anexos"), (RE_SUBCAP, "###", "subcapitulos")):
            m = regex.match(l)
            if m and len(l) < 120:
                cerrar()
                resto = m.group(3).strip(" .-–—:")
                salida.append(f"{nivel} {m.group(1).capitalize()} {m.group(2)}{(' - ' + resto) if resto else ''}")
                salida.append("")
                stats[tipo] += 1
                esperando_nombre = not resto
                break
        else:
            m = RE_ARTICULO.match(l)
            if m:
                cerrar()
                resto = m.group(3).strip()
                titulo_art, _, cuerpo = resto.partition(". ")
                if not cuerpo and len(resto) <= 90:
                    titulo_art, cuerpo = resto.rstrip("."), ""
                elif len(titulo_art) > 90 or not cuerpo:
                    titulo_art, cuerpo = "", resto
                salida.append(f"### Artículo {m.group(2)}{(' - ' + titulo_art.strip()) if titulo_art else ''}")
                salida.append("")
                stats["articulos"] += 1
                if cuerpo:
                    parrafo.append(cuerpo)
                continue
            if len(l) < 60 and re.search(r"\d[,\.]\d", l):  # fila de tabla: se conserva como linea
                cerrar()
                if len(salida) >= 2 and salida[-1] == "" and salida[-2].startswith("- "):
                    salida.pop()  # filas consecutivas = una sola lista
                salida.append(f"- {l}")
                salida.append("")
                continue
            if parrafo and re.search(r"[\.:;]$", parrafo[-1]) and re.match(r"^([a-z]\)|\d+(\.\d+)*[\.\)]|[-•·])\s", l):
                cerrar()
            parrafo.append(l)
    cerrar()
    return salida, dict(stats)


def leer_catalogo(ruta: Path | None) -> dict[str, dict]:
    if not ruta or not ruta.exists():
        return {}
    with open(ruta, encoding="utf-8") as f:
        return {r["id"]: r for r in csv.DictReader(f)}


def escribir_nota(pdf: Path, boveda: Path, meta: dict) -> tuple[Path, dict]:
    paginas = extraer_paginas(pdf)
    lineas = limpiar(paginas)
    cuerpo, stats = estructurar(lineas)
    caracteres = sum(len(x) for x in cuerpo)
    escaneado = len(paginas) > 0 and caracteres / len(paginas) < 200
    ident = pdf.stem
    codigo = meta.get("codigo", ident)
    titulo = meta.get("titulo", ident.replace("_", " "))
    resumen = meta.get("nota_resumen", "")
    rel_pdf = pdf.relative_to(boveda).as_posix() if pdf.is_relative_to(boveda) else str(pdf)
    nota = boveda / CARPETA_SALIDA / f"Texto oficial - {ident}.md"
    nota.parent.mkdir(parents=True, exist_ok=True)

    L = ["---", "tipo: texto-oficial", f'codigo: "{codigo}"', f'titulo: "{titulo}"',
         f'version: "{meta.get("version", "")}"', f'fuente_pdf: "{rel_pdf}"', f"paginas: {len(paginas)}",
         f"articulos: {stats.get('articulos', 0)}", f"requiere_ocr: {str(escaneado).lower()}",
         f"extraido: {dt.date.today().isoformat()}", "tags: [norma/texto-oficial]",
         f'aliases: ["{codigo} texto", "{titulo}"]', "---", "",
         f"# {codigo} — {titulo} (texto oficial)", "",
         "> [!warning] Texto extraído automáticamente del PDF",
         f"> Fuente: [[{rel_pdf}]] · {len(paginas)} páginas · {stats.get('articulos', 0)} artículos detectados.",
         "> Tablas y fórmulas pueden perder formato: **para citar valores, verifica siempre en el PDF**.", ""]
    if escaneado:
        L += ["> [!danger] Poco texto extraíble: el PDF parece escaneado. Aplica OCR (p. ej. `ocrmypdf`) y vuelve a ejecutar.", ""]
    enlaces = [f"[[{resumen}]]"] if resumen else []
    L += ["Resumen y contexto: " + " · ".join(enlaces + [f"[[{NOTA_INDICE}]]", "[[MOC Normas y Estandares]]"]), "", "---", ""]
    L += cuerpo
    nota.write_text("\n".join(L), encoding="utf-8")
    return nota, {"paginas": len(paginas), "articulos": stats.get("articulos", 0), "ocr": escaneado}


def escribir_indice(boveda: Path, catalogo: dict[str, dict], resultados: dict[str, dict]) -> Path:
    carpeta = boveda / CARPETA_SALIDA
    carpeta.mkdir(parents=True, exist_ok=True)
    existentes = {p.stem.replace("Texto oficial - ", ""): p.stem for p in carpeta.glob("Texto oficial - *.md")}
    L = ["---", "tipo: moc", "tags: [norma, moc, norma/texto-oficial]", "aliases: [Textos oficiales, Normas completas]",
         f"actualizado: {dt.date.today().isoformat()}", "---", "", "# Índice de textos oficiales", "",
         "Textos completos de normas y guías convertidos a Markdown para que Obsidian (Smart Connections) y JARVIS",
         "los *absorban*. Se generan en tu PC con `scripts/05_descargar_normas_oficiales.ps1` → `scripts/06_pdf_a_obsidian.py`.",
         "Los PDF quedan en `90 RECURSOS/Adjuntos/Normas/` (fuera de git).", "",
         "| Documento | Versión | Estado | Resumen |", "|---|---|---|---|"]
    ids = list(catalogo) + [i for i in existentes if i not in catalogo]
    for i in ids:
        meta = catalogo.get(i, {})
        nombre = f"{meta.get('codigo', i)} — {meta.get('titulo', i)}"
        estado = f"[[{existentes[i]}|✅ texto]]" if i in existentes else "⏳ pendiente de descargar"
        if i in resultados and resultados[i].get("ocr"):
            estado += " ⚠️ requiere OCR"
        resumen = f"[[{meta['nota_resumen']}]]" if meta.get("nota_resumen") else ""
        L.append(f"| {nombre} | {meta.get('version', '')} | {estado} | {resumen} |")
    L += ["", "> [!note] Normas ISO (19650, 16739, 7817…) no se incluyen: son documentos de pago protegidos por derechos de autor.",
          "> La bóveda contiene resúmenes propios en [[MOC Normas y Estandares]].", "",
          "↑ [[MOC Normas y Estandares]] · [[Red neuronal de conocimiento]]", ""]
    ruta = carpeta / f"{NOTA_INDICE}.md"
    ruta.write_text("\n".join(L), encoding="utf-8")
    return ruta


def main() -> int:
    raiz = Path(__file__).resolve().parent.parent
    ap = argparse.ArgumentParser(description="PDF de normas -> notas de Obsidian (JARVIS BIM)")
    ap.add_argument("--entrada", default=str(raiz / "JARVIS-BIM" / "90 RECURSOS" / "Adjuntos" / "Normas"))
    ap.add_argument("--boveda", default=str(raiz / "JARVIS-BIM"))
    ap.add_argument("--catalogo", default=str(raiz / "scripts" / "catalogo_normas.csv"))
    ap.add_argument("--solo-indice", action="store_true", help="Solo regenera el indice")
    args = ap.parse_args()

    boveda = Path(args.boveda).resolve()
    entrada = Path(args.entrada).resolve()
    catalogo = leer_catalogo(Path(args.catalogo))
    resultados: dict[str, dict] = {}
    pdfs = sorted(entrada.rglob("*.pdf")) if entrada.exists() and not args.solo_indice else []
    for pdf in pdfs:
        try:
            nota, r = escribir_nota(pdf, boveda, catalogo.get(pdf.stem, {}))
            resultados[pdf.stem] = r
            aviso = "  ⚠️ requiere OCR" if r["ocr"] else ""
            print(f"[ok] {pdf.name}: {r['paginas']} pág., {r['articulos']} artículos -> {nota.relative_to(boveda)}{aviso}")
        except Exception as exc:
            print(f"[error] {pdf.name}: {exc}")
    indice = escribir_indice(boveda, catalogo, resultados)
    print(f"\nPDF procesados: {len(resultados)} · índice: {indice.relative_to(boveda)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
