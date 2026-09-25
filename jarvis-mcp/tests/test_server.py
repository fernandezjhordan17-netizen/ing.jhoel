"""Prueba de extremo a extremo del servidor MCP (en memoria y por stdio)."""
import json
import shutil
import sys

import anyio
import pytest
from mcp import Client, StdioServerParameters

from jarvis_bim.boveda import ruta_boveda


@pytest.fixture(autouse=True)
def boveda_temporal(tmp_path, monkeypatch):
    copia = tmp_path / "JARVIS-BIM"
    shutil.copytree(ruta_boveda(), copia, ignore=shutil.ignore_patterns(".obsidian"))
    monkeypatch.setenv("JARVIS_BOVEDA", str(copia))
    from jarvis_bim import server
    server._boveda.cache_clear()
    return copia


def _datos(resultado):
    if resultado.structured_content is not None:
        sc = resultado.structured_content
        return sc.get("result", sc) if isinstance(sc, dict) else sc
    return json.loads(resultado.content[0].text)


async def _sesion(fn):
    from jarvis_bim.server import servidor
    async with Client(servidor) as c:
        return await fn(c)


def test_lista_herramientas_y_prompts():
    async def fn(c):
        tools = {t.name: t for t in (await c.list_tools()).tools}
        prompts = {p.name for p in (await c.list_prompts()).prompts}
        return tools, prompts
    tools, prompts = anyio.run(_sesion, fn)
    for nombre in ("e030_espectro", "e030_cortante_basal", "boveda_buscar", "iso19650_validar_nombre",
                   "ifc_resumen", "csi_crear_espectro_e030", "csi_derivas", "e060_flexion_viga",
                   "e060_cortante_viga", "ifc_metrados", "csi_crear_combinaciones_e060"):
        assert nombre in tools
    assert tools["boveda_buscar"].annotations.read_only_hint
    assert not tools["csi_crear_espectro_e030"].annotations.read_only_hint
    assert {"flujo_sismico_e030", "consulta_normativa"} <= prompts


def test_espectro_y_excel(tmp_path, boveda_temporal):
    xlsx = tmp_path / "esp.xlsx"
    async def fn(c):
        return await c.call_tool("e030_espectro", {"zona": 4, "categoria": "C", "sistema": "concreto_dual",
                                                    "perfil": "S2", "vs30": 450, "exportar_xlsx": str(xlsx)})
    r = anyio.run(_sesion, fn)
    assert not r.is_error, r.content
    d = _datos(r)
    assert d["parametros"]["S"] == 1.05 and xlsx.exists()
    assert list((boveda_temporal / "00 INICIO" / "Diario JARVIS").glob("20*.md")), "no se registró la bitácora"


def test_error_norma_se_reporta():
    async def fn(c):
        return await c.call_tool("e030_parametros_sitio", {"zona": 4, "perfil": "S4"})
    r = anyio.run(_sesion, fn)
    assert r.is_error and "respuesta de sitio específico" in r.content[0].text


def test_nota_inexistente_mensaje_util():
    async def fn(c):
        return await c.call_tool("boveda_leer", {"nota": "Norma inventada"})
    r = anyio.run(_sesion, fn)
    assert r.is_error and "No existe la nota" in r.content[0].text


def test_boveda_desde_mcp():
    async def fn(c):
        return await c.call_tool("boveda_buscar", {"consulta": "cisterna tanque elevado dotacion", "limite": 3})
    d = _datos(anyio.run(_sesion, fn))
    assert d[0]["nota"] == "IS.010 - Instalaciones Sanitarias"


def test_csi_sin_etabs_error_claro():
    if sys.platform == "win32":
        pytest.skip("en Windows depende de ETABS instalado")
    async def fn(c):
        return await c.call_tool("csi_estado", {})
    r = anyio.run(_sesion, fn)
    assert r.is_error and "solo funciona en Windows" in r.content[0].text


def test_servidor_por_stdio():
    parametros = StdioServerParameters(command=sys.executable, args=["-m", "jarvis_bim.server"])
    async def main():
        async with Client(parametros) as c:
            info = c.server_info
            r = await c.call_tool("iso19650_validar_nombre", {"nombre": "PRJ01-ABC-ZZ-01-M3-S-0001.rvt"})
            return info, r
    info, r = anyio.run(main)
    assert info.name == "jarvis-bim"
    assert _datos(r)["valido"]


def test_flexion_desde_mcp():
    async def fn(c):
        return await c.call_tool("e060_flexion_viga", {"mu_knm": 120, "b_mm": 300, "h_mm": 600})
    d = _datos(anyio.run(_sesion, fn))
    assert d["phi_Mn_kNm"] >= 120 and d["barras"]
