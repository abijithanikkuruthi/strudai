from unittest.mock import AsyncMock, patch

import pytest

class TestStrudelReadCode:
    @pytest.mark.asyncio
    async def test_read_code_calls_frontend(self):
        with patch("backend.tools.strudel_read_code.manager") as mock_mgr:
            mock_mgr.request_from_frontend = AsyncMock(
                return_value={"code": "s('bd sd')"}
            )
            # Import fresh to use the patched manager
            from backend.tools.strudel_read_code import strudel_read_code

            result = await strudel_read_code()
            mock_mgr.request_from_frontend.assert_awaited_once_with("read_code")
            assert result == {"code": "s('bd sd')"}


class TestStrudelReadConsole:
    @pytest.mark.asyncio
    async def test_read_console_calls_frontend(self):
        with patch("backend.tools.strudel_read_console.manager") as mock_mgr:
            mock_mgr.request_from_frontend = AsyncMock(
                return_value={"logs": ["hello"]}
            )
            from backend.tools.strudel_read_console import strudel_read_console

            result = await strudel_read_console()
            mock_mgr.request_from_frontend.assert_awaited_once_with("read_console")
            assert result == {"logs": ["hello"]}


class TestStrudelRewriteCode:
    @pytest.mark.asyncio
    async def test_rewrite_code_calls_frontend(self):
        with patch("backend.tools.strudel_rewrite_code.manager") as mock_mgr:
            mock_mgr.request_from_frontend = AsyncMock(
                return_value={"ok": True}
            )
            from backend.tools.strudel_rewrite_code import (
                RewriteCodeParams,
                strudel_rewrite_code,
            )

            params = RewriteCodeParams(code="s('bd sd')")
            result = await strudel_rewrite_code(params)
            mock_mgr.request_from_frontend.assert_awaited_once_with(
                "rewrite_code", {"code": "s('bd sd')"}
            )
            assert result == {"ok": True}


class TestStrudelEditCode:
    @pytest.mark.asyncio
    async def test_edit_code_calls_frontend(self):
        with patch("backend.tools.strudel_edit_code.manager") as mock_mgr:
            mock_mgr.request_from_frontend = AsyncMock(
                return_value={"ok": True, "logs": []}
            )
            from backend.tools.strudel_edit_code import (
                EditCodeParams,
                strudel_edit_code,
            )

            params = EditCodeParams(old_string="bd", new_string="sd")
            result = await strudel_edit_code(params)
            mock_mgr.request_from_frontend.assert_awaited_once_with(
                "edit_code", {"old_string": "bd", "new_string": "sd"}
            )
            assert result == {"ok": True, "logs": []}


class TestToolsRegisteredInRegistry:
    def test_all_tools_registered(self):
        from backend.tools import registry

        names = set(registry._tools.keys())
        assert "strudel_read_code" in names
        assert "strudel_rewrite_code" in names
        assert "strudel_edit_code" in names
        assert "strudel_read_console" in names
        assert "web_search" in names
        assert "sample_search" in names

    def test_schemas_exported(self):
        from backend.tools import registry

        schemas = registry.to_schemas()
        assert len(schemas) >= 6
        schema_names = {s["name"] for s in schemas}
        assert "strudel_read_code" in schema_names
        assert "strudel_rewrite_code" in schema_names
        assert "strudel_edit_code" in schema_names
        assert "strudel_read_console" in schema_names
        assert "web_search" in schema_names
        assert "sample_search" in schema_names


FAKE_INDEX = [
    {
        "name": "strudel.cc/drums",
        "url": "https://strudel.cc/drums.json",
        "samples": ["bd", "sd", "hh", "cp"],
        "builtin": True,
    },
    {
        "name": "user/synth-pack",
        "url": "https://example.com/synth.json",
        "samples": ["pad", "lead", "bass_synth"],
    },
    {
        "name": "user/percussion",
        "url": "https://example.com/perc.json",
        "samples": ["conga", "bongo", "bd_heavy"],
    },
]


class TestSampleSearch:
    @pytest.mark.asyncio
    async def test_search_by_pack_name(self):
        with patch(
            "backend.tools.sample_search._fetch_index", return_value=FAKE_INDEX
        ):
            from backend.tools.sample_search import SampleSearchParams, sample_search

            result = await sample_search(SampleSearchParams(query="drums"))
            assert len(result["results"]) == 1
            assert result["results"][0]["pack"] == "strudel.cc/drums"
            assert result["results"][0]["sounds"] == ["bd", "sd", "hh", "cp"]
            assert result["results"][0]["builtin"] is True

    @pytest.mark.asyncio
    async def test_search_by_sound_name(self):
        with patch(
            "backend.tools.sample_search._fetch_index", return_value=FAKE_INDEX
        ):
            from backend.tools.sample_search import SampleSearchParams, sample_search

            result = await sample_search(SampleSearchParams(query="bd"))
            packs = {r["pack"] for r in result["results"]}
            assert "strudel.cc/drums" in packs
            assert "user/percussion" in packs

    @pytest.mark.asyncio
    async def test_search_case_insensitive(self):
        with patch(
            "backend.tools.sample_search._fetch_index", return_value=FAKE_INDEX
        ):
            from backend.tools.sample_search import SampleSearchParams, sample_search

            result = await sample_search(SampleSearchParams(query="SYNTH"))
            assert len(result["results"]) == 1
            assert result["results"][0]["pack"] == "user/synth-pack"

    @pytest.mark.asyncio
    async def test_search_no_results(self):
        with patch(
            "backend.tools.sample_search._fetch_index", return_value=FAKE_INDEX
        ):
            from backend.tools.sample_search import SampleSearchParams, sample_search

            result = await sample_search(SampleSearchParams(query="zzzznotfound"))
            assert result["results"] == []
