"""Main chat agent (Hans Strudel) — handles user conversation and tool use."""

from langgraph.checkpoint.memory import MemorySaver

from backend.agents.base import (
    AVAILABLE_MODELS,
    DEFAULT_MODEL,
    build_graph,
    stream_events,
)
from backend.knowledge.compress import OUTPUT_FILE as KNOWLEDGE_FILE
from backend.prompts import render

memory = MemorySaver()


async def agent_respond(
    text: str,
    session_id: str,
    *,
    api_key: str,
    on_event=None,
    model: str = DEFAULT_MODEL,
) -> str:
    """Run the chat agent and stream events via the on_event callback.

    on_event is called with (event_type, data) where event_type is one of:
    - "thinking": agent is processing (no tool calls yet)
    - "tool_call": agent is invoking a tool, data = {"tool": name, "input": args}
    - "tool_result": tool finished, data = {"tool": name, "output": result}
    """
    knowledge = KNOWLEDGE_FILE.read_text() if KNOWLEDGE_FILE.exists() else ""
    system_prompt = render("system.j2", knowledge=knowledge)

    agent = build_graph(
        model=model,
        api_key=api_key,
        system_prompt=system_prompt,
        node_name="chat",
        checkpointer=memory,
    )

    if on_event:
        await on_event("thinking", {})

    return await stream_events(agent, text, session_id, on_event=on_event)
