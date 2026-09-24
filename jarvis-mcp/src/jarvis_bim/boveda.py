"""Acceso a la bóveda Obsidian JARVIS-BIM: búsqueda BM25, lectura de notas, enlaces y retroenlaces."""
from __future__ import annotations

import math
import os
import re
import unicodedata
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path

RE_ENLACE = re.compile(r"\[\[([^\]\|#]+)(#[^\]\|]*)?(\|[^\]]*)?\]\]")
RE_PALABRA = re.compile(r"[a-z0-9áéíóúñü\.]+")
VACIAS = set("""a al algo como con cual cuando de del desde donde el ella en entre es esta este esto
fue ha la las le lo los mas me mi muy no o para pero por que se sin sobre su sus te tu un una uno y ya
the of and to in is for on with""".split())


def ruta_boveda() -> Path:
    """JARVIS_BOVEDA o la carpeta JARVIS-BIM del repositorio."""
    env = os.environ.get("JARVIS_BOVEDA")
    if env:
        return Path(env).expanduser().resolve()
    return (Path(__file__).resolve().parents[3] / "JARVIS-BIM").resolve()


def _normalizar(texto: str) -> str:
    return unicodedata.normalize("NFC", texto).lower()


def _sin_tildes(texto: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFD", texto) if unicodedata.category(c) != "Mn")


def _tokens(texto: str) -> list[str]:
    salida = []
    for t in RE_PALABRA.findall(_sin_tildes(_normalizar(texto))):
        t = t.strip(".")
        if len(t) > 1 and t not in VACIAS:
            salida.append(t)
    return salida


@dataclass
class Nota:
    nombre: str
    ruta: Path
    texto: str
    tokens: Counter
    largo: int
    enlaces: set[str]


class Boveda:
    def __init__(self, raiz: Path | None = None):
        self.raiz = (raiz or ruta_boveda()).resolve()
        if not self.raiz.exists():
            raise FileNotFoundError(f"No existe la bóveda: {self.raiz}")
        self._cargar()

    def _cargar(self) -> None:
        self.notas: dict[str, Nota] = {}
        for p in sorted(self.raiz.rglob("*.md")):
            if ".obsidian" in p.parts:
                continue
            texto = p.read_text(encoding="utf-8", errors="replace")
            alias = re.search(r"^aliases:\s*\[(.*)\]", texto, re.M)
            titulo = p.stem + " " + (alias.group(1) if alias else "")
            toks = _tokens(" ".join([titulo] * 3) + " " + texto)  # título y alias pesan triple
            enl = {m.group(1).strip() for m in RE_ENLACE.finditer(texto)}
            self.notas[_normalizar(p.stem)] = Nota(p.stem, p, texto, Counter(toks), len(toks), enl)
        self.df = Counter()
        for n in self.notas.values():
            self.df.update(set(n.tokens))
        self.largo_medio = sum(n.largo for n in self.notas.values()) / max(len(self.notas), 1)
        self.retro: dict[str, set[str]] = defaultdict(set)
        for n in self.notas.values():
            for e in n.enlaces:
                self.retro[_normalizar(e)].add(n.nombre)

    def recargar(self) -> int:
        self._cargar()
        return len(self.notas)

    def _rel(self, nota: Nota) -> str:
        return nota.ruta.relative_to(self.raiz).as_posix()

    def buscar(self, consulta: str, limite: int = 8, carpeta: str | None = None) -> list[dict]:
        """BM25 sobre título + contenido; devuelve fragmento con el contexto de la primera coincidencia."""
        q = _tokens(consulta)
        if not q:
            return []
        N, k1, b = len(self.notas), 1.4, 0.6
        puntajes = []
        for n in self.notas.values():
            if carpeta and not self._rel(n).lower().startswith(carpeta.lower()):
                continue
            s = 0.0
            for t in q:
                f = n.tokens.get(t, 0)
                if not f:
                    continue
                idf = math.log(1 + (N - self.df[t] + 0.5) / (self.df[t] + 0.5))
                s += idf * f * (k1 + 1) / (f + k1 * (1 - b + b * n.largo / self.largo_medio))
            if s > 0:
                puntajes.append((s, n))
        puntajes.sort(key=lambda x: -x[0])
        return [{"nota": n.nombre, "ruta": self._rel(n), "puntaje": round(s, 3), "fragmento": self._fragmento(n, q)}
                for s, n in puntajes[:limite]]

    def _fragmento(self, nota: Nota, q: list[str], ancho: int = 240) -> str:
        cuerpo = nota.texto.split("---", 2)[-1] if nota.texto.startswith("---") else nota.texto
        plano = _sin_tildes(cuerpo.lower())
        pos = min([plano.find(t) for t in q if plano.find(t) >= 0], default=0)
        ini = max(0, pos - ancho // 3)
        return " ".join(cuerpo[ini:ini + ancho].split())

    def leer(self, nombre: str, max_caracteres: int = 20000) -> dict:
        n = self.notas.get(_normalizar(nombre))
        if n is None:
            candidatos = [x["nota"] for x in self.buscar(nombre, 5)]
            raise KeyError(f"No existe la nota '{nombre}'. ¿Quisiste decir: {candidatos}?")
        texto = n.texto if len(n.texto) <= max_caracteres else n.texto[:max_caracteres] + "\n…[truncado]"
        return {"nota": n.nombre, "ruta": self._rel(n), "contenido": texto,
                "enlaces": sorted(n.enlaces), "retroenlaces": sorted(self.retro.get(_normalizar(n.nombre), set()))}

    def mapas(self) -> list[dict]:
        return [{"nota": n.nombre, "ruta": self._rel(n), "enlaces": len(n.enlaces)}
                for n in self.notas.values() if n.nombre.startswith("MOC ") or n.nombre.startswith("Indice")]

    def estadisticas(self) -> dict:
        capas = Counter(self._rel(n).split("/")[0] for n in self.notas.values())
        return {"boveda": str(self.raiz), "notas": len(self.notas),
                "enlaces": sum(len(n.enlaces) for n in self.notas.values()), "capas": dict(sorted(capas.items()))}
