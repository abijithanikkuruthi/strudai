import json
from collections.abc import Callable, Coroutine
from typing import Any

from pydantic import BaseModel


class ToolDef:
    def __init__(
        self,
        name: str,
        description: str,
        params_model: type[BaseModel] | None,
        handler: Callable[..., Coroutine[Any, Any, Any]],
    ) -> None:
        self.name = name
        self.description = description
        self.params_model = params_model
        self.handler = handler


class ToolRegistry:
    def __init__(self) -> None:
        self._tools: dict[str, ToolDef] = {}

    def tool(
        self,
        name: str,
        description: str,
        params_model: type[BaseModel] | None = None,
    ) -> Callable:
        def decorator(fn: Callable[..., Coroutine[Any, Any, Any]]) -> Callable:
            self._tools[name] = ToolDef(name, description, params_model, fn)
            return fn
        return decorator

    async def execute(self, name: str, params: dict | None = None) -> Any:
        tool_def = self._tools.get(name)
        if tool_def is None:
            raise KeyError(f"Unknown tool: {name}")
        if tool_def.params_model is not None and params is not None:
            validated = tool_def.params_model(**params)
            return await tool_def.handler(validated)
        return await tool_def.handler()

    def to_langchain_tools(self, include: set[str] | None = None) -> list:
        """Convert registered tools to LangChain StructuredTools.

        If *include* is given, only tools whose names are in the set are returned.
        """
        from langchain_core.tools import StructuredTool

        tools = []
        for t in self._tools.values():
            if include is not None and t.name not in include:
                continue

            async def _handler(t=t, **kwargs):
                if t.params_model and kwargs:
                    result = await t.handler(t.params_model(**kwargs))
                else:
                    result = await t.handler()
                return json.dumps(result)

            tools.append(
                StructuredTool.from_function(
                    coroutine=_handler,
                    name=t.name,
                    description=t.description,
                    args_schema=t.params_model,
                )
            )
        return tools

    def to_schemas(self) -> list[dict]:
        schemas = []
        for t in self._tools.values():
            schema: dict[str, Any] = {
                "name": t.name,
                "description": t.description,
            }
            if t.params_model:
                schema["parameters"] = t.params_model.model_json_schema()
            else:
                schema["parameters"] = {"type": "object", "properties": {}}
            schemas.append(schema)
        return schemas


registry = ToolRegistry()
