"""Shared utilities for all LangGraph agents."""

from langchain_anthropic import ChatAnthropic
from langchain_core.messages import SystemMessage
from langgraph.graph import END, MessagesState, StateGraph
from langgraph.prebuilt import ToolNode

from backend.tools.registry import registry

AVAILABLE_MODELS = [
    "claude-haiku-4-5-20251001",
    "claude-sonnet-4-6",
    "claude-opus-4-6",
]

DEFAULT_MODEL = "claude-haiku-4-5-20251001"


def should_continue(state: MessagesState) -> str:
    """Route to tools if the last message has tool calls, otherwise end."""
    last = state["messages"][-1]
    if hasattr(last, "tool_calls") and last.tool_calls:
        return "tools"
    return END


def build_graph(
    *,
    model: str,
    api_key: str,
    system_prompt: str,
    node_name: str = "agent",
    tool_names: set[str] | None = None,
    checkpointer=None,
):
    """Build a standard LangGraph agent with an LLM node and a tool node.

    Args:
        model: Claude model identifier.
        api_key: Anthropic API key.
        system_prompt: System prompt text.
        node_name: Name for the LLM node in the graph.
        tool_names: If given, only include these tools. None = all tools.
        checkpointer: LangGraph checkpointer for session memory.
    """
    tools = registry.to_langchain_tools(include=tool_names)

    llm = ChatAnthropic(
        model=model,
        api_key=api_key,
    ).bind_tools(tools)

    async def invoke(state: MessagesState) -> MessagesState:
        messages = [SystemMessage(content=system_prompt), *state["messages"]]
        response = await llm.ainvoke(messages)
        return {"messages": [response]}

    tool_node = ToolNode(tools)

    graph = StateGraph(MessagesState)
    graph.add_node(node_name, invoke)
    graph.add_node("tools", tool_node)
    graph.set_entry_point(node_name)
    graph.add_conditional_edges(node_name, should_continue, {"tools": "tools", END: END})
    graph.add_edge("tools", node_name)
    return graph.compile(checkpointer=checkpointer)


async def stream_events(agent, text: str, session_id: str, *, on_event=None) -> str:
    """Run an agent and stream tool_call/tool_result events via on_event callback.

    Returns the final text content from the agent.
    """
    config = {"configurable": {"thread_id": session_id}}

    final_content = ""
    async for event in agent.astream_events(
        {"messages": [("human", text)]}, config=config, version="v2"
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
