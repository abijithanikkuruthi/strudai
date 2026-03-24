"""Performer agent — executes set plan sections by writing Strudel code."""

from langgraph.checkpoint.memory import MemorySaver

from backend.agents.base import build_graph, stream_events
from backend.prompts import render

memory = MemorySaver()

PERFORMER_TOOLS = {
    "strudel_read_code",
    "strudel_edit_code",
    "strudel_rewrite_code",
    "strudel_read_console",
    "strudel_docs_search",
    "sample_search",
}


async def performer_respond(
    instruction: str,
    session_id: str,
    *,
    api_key: str,
    on_event=None,
    model: str,
    prompt_vars: dict,
) -> str:
    """Run the performer agent on a single section instruction."""
    system_prompt = render("performer.j2", **prompt_vars)

    agent = build_graph(
        model=model,
        api_key=api_key,
        system_prompt=system_prompt,
        node_name="act",
        tool_names=PERFORMER_TOOLS,
        checkpointer=memory,
    )

    return await stream_events(agent, instruction, session_id, on_event=on_event)
