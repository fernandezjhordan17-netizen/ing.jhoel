#!/usr/bin/env python3
"""
Ejecuta un proyecto con JARVIS de punta a punta desde su JSON:
E.020 (pesos) -> E.030-2026 (espectro y cortante por direccion) -> E.060 (combinaciones, vigas, columnas)
-> metrado IFC opcional -> memoria Excel + notas del proyecto en la boveda + Diario JARVIS.

Uso:
    python scripts/08_ejecutar_proyecto.py jarvis/proyectos/PRY001_ejemplo.json            (dry-run)
    python scripts/08_ejecutar_proyecto.py jarvis/proyectos/PRY001_ejemplo.json --confirmar
Opciones: --boveda RUTA (por defecto JARVIS-BIM o JARVIS_BOVEDA), --salida CARPETA (Excel), --ifc MODELO.ifc
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "jarvis-mcp" / "src"))

from jarvis_bim import proyecto  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("config", help="JSON del proyecto")
    ap.add_argument("--confirmar", action="store_true", help="escribe Excel y notas (sin esto es dry-run)")
    ap.add_argument("--boveda", type=Path)
    ap.add_argument("--salida", type=Path)
    ap.add_argument("--ifc", help="modelo IFC para el metrado (reemplaza modelo_ifc del JSON)")
    args = ap.parse_args()

    cfg = proyecto.cargar(args.config)
    if args.ifc:
        cfg["modelo_ifc"] = str(Path(args.ifc).resolve())
    try:
        r = proyecto.ejecutar(cfg, confirmar=args.confirmar, boveda=args.boveda, salida=args.salida)
    except (proyecto.ErrorProyecto, ValueError, FileNotFoundError) as exc:
        print(f"ERROR: {exc}")
        return 1
    res = r["resumen"]
    print(f"\n== {r['proyecto']} ==")
    print(f" P total = {res['P_total_kN']:,.1f} kN   hn = {res['hn_m']} m")
    print(" " + "  ".join(f"{k}={v}" for k, v in res["parametros"].items()))
    for linea in res["direcciones"]:
        print(f"  {linea}")
    for v in r["concreto"]["vigas"]:
        fl, co = v.get("flexion", {}), v.get("cortante", {})
        barras = fl["barras"][0]["barras"] if fl.get("barras") else "-"
        print(f"  Viga {v['id']}: As = {fl.get('As_diseno_mm2')} mm2 -> {barras}; {co.get('estribos', '')} {v.get('error', '')}")
    for c in r["concreto"]["columnas"]:
        ax = c.get("axial", {})
        print(f"  Columna {c['id']}: phiPn max = {ax.get('phi_Pn_max_kN')} kN, uso {ax.get('uso_%')} %")
    print("\n Alertas:" if r["alertas"] else "\n Alertas: ninguna")
    for a in r["alertas"]:
        print(f"  - {a}")
    print(" Pendientes normativos:")
    for p in r["pendientes"]:
        print(f"  - {p}")
    print(f"\n {r['mensaje']}")
    for k, v in r["archivos"].items():
        print(f"  {k}: {v}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
