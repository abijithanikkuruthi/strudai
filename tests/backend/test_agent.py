import json

import pytest
from pydantic import BaseModel

from backend.tools.registry import ToolRegistry


class EchoParams(BaseModel):
    text: str


class TestToLangchainTools:
    """Test that to_langchain_tools() produces working LangChain tools."""

    def _make_registry(self):
        reg = ToolRegistry()

        @reg.tool(name="ping", description="A ping tool")
        async def ping():
            return {"pong": True}

        @reg.tool(name="echo", description="Echo back text", params_model=EchoParams)
        async def echo(params: EchoParams):
            return {"echoed": params.text}

        return reg

    def test_returns_correct_count(self):
        reg = self._make_registry()
        tools = reg.to_langchain_tools()
        assert len(tools) == 2

    def test_tool_names(self):
        reg = self._make_registry()
        tools = reg.to_langchain_tools()
        names = {t.name for t in tools}
        assert names == {"ping", "echo"}

    def test_tool_descriptions(self):
        reg = self._make_registry()
        tools = reg.to_langchain_tools()
        by_name = {t.name: t for t in tools}
        assert by_name["ping"].description == "A ping tool"
        assert by_name["echo"].description == "Echo back text"

    @pytest.mark.asyncio
    async def test_invoke_no_params(self):
        reg = self._make_registry()
        tools = reg.to_langchain_tools()
        by_name = {t.name: t for t in tools}
        result = await by_name["ping"].ainvoke({})
        assert json.loads(result) == {"pong": True}

    @pytest.mark.asyncio
    async def test_invoke_with_params(self):
        reg = self._make_registry()
        tools = reg.to_langchain_tools()
        by_name = {t.name: t for t in tools}
        result = await by_name["echo"].ainvoke({"text": "hello"})
        assert json.loads(result) == {"echoed": "hello"}
