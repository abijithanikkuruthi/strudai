from langchain_anthropic import ChatAnthropic
from langchain_core.messages import SystemMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import END, MessagesState, StateGraph
from langgraph.prebuilt import ToolNode

from backend.prompts import render
from backend.tools.registry import registry

memory = MemorySaver()

PERFORMER_TOOLS = {
    "strudel_read_code",
    "strudel_edit_code",
    "strudel_rewrite_code",
    "strudel_read_console",
    "strudel_docs_search",
    "sample_search",
}


def _should_continue(state: MessagesState) -> str:
    last = state["messages"][-1]
    if hasattr(last, "tool_calls") and last.tool_calls:
        return "tools"
    return END


def _build_performer(model: str, api_key: str, *, prompt_vars: dict):
    tools = registry.to_langchain_tools(include=PERFORMER_TOOLS)

    llm = ChatAnthropic(
        model=model,
        api_key=api_key,
    ).bind_tools(tools)

    system_prompt = render("performer.j2", **prompt_vars)

    async def act(state: MessagesState) -> MessagesState:
        messages = [SystemMessage(content=system_prompt), *state["messages"]]
        response = await llm.ainvoke(messages)
        return {"messages": [response]}

    tool_node = ToolNode(tools)

    graph = StateGraph(MessagesState)
    graph.add_node("act", act)
    graph.add_node("tools", tool_node)
    graph.set_entry_point("act")
    graph.add_conditional_edges("act", _should_continue, {"tools": "tools", END: END})
    graph.add_edge("tools", "act")
    return graph.compile(checkpointer=memory)


async def performer_respond(
    instruction: str,
    session_id: str,
    *,
    api_key: str,
    on_event=None,
    model: str,
    prompt_vars: dict,
) -> str:
    """Run the performer agent on a single section instruction.

    on_event is called with (event_type, data) where event_type is one of:
    - "tool_call": performer is invoking a tool
    - "tool_result": tool finished
    """
    agent = _build_performer(model, api_key, prompt_vars=prompt_vars)
    config = {"configurable": {"thread_id": session_id}}

    final_content = ""
    async for event in agent.astream_events(
        {"messages": [("human", instruction)]}, config=config, version="v2"
    ):
        kind = event["event"]

        if kind == "on_chat_model_end":
            msg = event["data"]["output"]
            if hasattr(msg, "tool_calls") and msg.tool_calls and on_event:
                for tc in msg.tool_calls:
                    await on_event("tool_call", {
                        "tool": tc["name"],
                        "input": tc["args"],
                    })

        elif kind == "on_tool_end" and on_event:
            data = event["data"]
            tool_msg = data.get("output", data) if isinstance(data, dict) else data
            output = getattr(tool_msg, "content", None) or str(tool_msg)
            await on_event("tool_result", {
                "tool": event["name"],
                "output": output,
            })

        elif kind == "on_chain_end" and event["name"] == "LangGraph":
            messages = event["data"]["output"].get("messages", [])
            if messages:
                content = messages[-1].content
                if isinstance(content, list):
                    final_content = "".join(
                        block.get("text", "") if isinstance(block, dict) else str(block)
                        for block in content
                    )
                else:
                    final_content = content

    return final_content
