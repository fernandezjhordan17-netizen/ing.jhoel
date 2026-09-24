#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
04_salud_red_neuronal.py - Diagnostico de la "red neuronal" (grafo) de la boveda JARVIS-BIM.

Reporta neuronas (notas), sinapsis (enlaces), enlaces rotos, encabezados inexistentes,
notas huerfanas, notas con pocas conexiones y los hubs mas conectados.

Uso:
    python scripts/04_salud_red_neuronal.py                 # boveda por defecto (../JARVIS-BIM)
    python scripts/04_salud_red_neuronal.py --boveda RUTA --estricto
Codigo de salida 1 si hay enlaces rotos (util para automatizar).
"""
from __future__ import annotations

import argparse
import collections
import re
import sys
import unicodedata
from pathlib import Path

ENLACE = re.compile(r"(!?)\[\[([^\]\|#]*)(#[^\]\|]*)?(\|[^\]]*)?\]\]")
BLOQUE_CODIGO = re.compile(r"```.*?```", re.S)
CODIGO_LINEA = re.compile(r"`[^`\n]*`")
ENCABEZADO = re.compile(r"^#{1,6}\s+(.+?)\s*$", re.M)
CARPETAS_PLANTILLA = ("80 PLANTILLAS",)


def normalizar(texto: str) -> str:
    return unicodedata.normalize("NFC", texto).strip().lower()


def limpiar(texto: str) -> str:
    texto = BLOQUE_CODIGO.sub("", texto)
    return CODIGO_LINEA.sub("", texto)


def main() -> int:
    ap = argparse.ArgumentParser(description="Salud de la red neuronal de la boveda")
    ap.add_argument("--boveda", default=str(Path(__file__).resolve().parent.parent / "JARVIS-BIM"))
    ap.add_argument("--min-enlaces", type=int, default=3, help="Umbral de conexiones salientes")
    ap.add_argument("--estricto", action="store_true", help="Tambien falla con encabezados inexistentes")
    args = ap.parse_args()

    boveda = Path(args.boveda).resolve()
    notas = sorted(p for p in boveda.rglob("*.md") if ".obsidian" not in p.parts)
    if not notas:
        print(f"No hay notas en {boveda}")
        return 2

    por_nombre: dict[str, Path] = {}
    por_ruta: dict[str, Path] = {}
    encabezados: dict[Path, set[str]] = {}
    for n in notas:
        por_nombre.setdefault(normalizar(n.stem), n)
        por_ruta[normalizar(n.relative_to(boveda).with_suffix("").as_posix())] = n
        encabezados[n] = {normalizar(h) for h in ENCABEZADO.findall(limpiar(n.read_text(encoding="utf-8")))}

    salientes: dict[Path, set[Path]] = collections.defaultdict(set)
    entrantes: dict[Path, set[Path]] = collections.defaultdict(set)
    rotos, anclas_rotas = [], []
    for n in notas:
        for m in ENLACE.finditer(limpiar(n.read_text(encoding="utf-8"))):
            destino, ancla = m.group(2).strip(), (m.group(3) or "")[1:]
            if not destino:  # enlace a un encabezado de la misma nota
                continue
            clave = normalizar(destino)
            objetivo = por_ruta.get(clave) or por_nombre.get(clave)
            if objetivo is None:
                if not (boveda / destino).exists():
                    rotos.append((n, destino))
                continue
            if objetivo != n:
                salientes[n].add(objetivo)
                entrantes[objetivo].add(n)
            if ancla and normalizar(ancla) not in encabezados[objetivo]:
                anclas_rotas.append((n, destino, ancla))

    sinapsis = sum(len(v) for v in salientes.values())
    huerfanas = [n for n in notas if not salientes[n] and not entrantes[n]]
    debiles = [n for n in notas if len(salientes[n]) < args.min_enlaces
               and not n.relative_to(boveda).parts[0].startswith(CARPETAS_PLANTILLA)]
    grado = collections.Counter({n: len(salientes[n]) + len(entrantes[n]) for n in notas})
    capas = collections.Counter(n.relative_to(boveda).parts[0] if len(n.relative_to(boveda).parts) > 1 else "(raiz)"
                                for n in notas)

    print("=" * 64)
    print(" SALUD DE LA RED NEURONAL - JARVIS BIM")
    print("=" * 64)
    print(f" Neuronas (notas):        {len(notas)}")
    print(f" Sinapsis (enlaces unicos): {sinapsis}")
    print(f" Densidad media:          {sinapsis / len(notas):.1f} enlaces por nota")
    print(f" Enlaces rotos:           {len(rotos)}")
    print(f" Encabezados inexistentes: {len(anclas_rotas)}")
    print(f" Notas huerfanas:         {len(huerfanas)}")
    print(f" Notas con < {args.min_enlaces} enlaces:   {len(debiles)}")
    print("\n Capas:")
    for capa, n in sorted(capas.items()):
        print(f"   {capa:<28} {n:>4} notas")
    print("\n Hubs mas conectados:")
    for n, g in grado.most_common(10):
        print(f"   {g:>4}  {n.stem}")
    if rotos:
        print("\n ENLACES ROTOS:")
        for n, d in rotos:
            print(f"   {n.relative_to(boveda)}  ->  [[{d}]]")
    if anclas_rotas:
        print("\n ENCABEZADOS INEXISTENTES:")
        for n, d, a in anclas_rotas:
            print(f"   {n.relative_to(boveda)}  ->  [[{d}#{a}]]")
    if huerfanas:
        print("\n HUERFANAS:")
        for n in huerfanas:
            print(f"   {n.relative_to(boveda)}")
    if debiles:
        print(f"\n CON POCAS CONEXIONES (< {args.min_enlaces}):")
        for n in debiles:
            print(f"   {len(salientes[n])}  {n.relative_to(boveda)}")
    falla = bool(rotos) or (args.estricto and bool(anclas_rotas))
    print("\n Estado:", "REVISAR" if falla else "SANA")
    return 1 if falla else 0


if __name__ == "__main__":
    sys.exit(main())
