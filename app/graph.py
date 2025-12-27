from typing import TypedDict, List
from langchain_core.messages import BaseMessage

from langchain_core.messages import AIMessage
from app.llm import get_llm
from langgraph.graph import StateGraph, END

llm = get_llm()

class ChatState(TypedDict):
    messages: List[BaseMessage]

def chat_node(state: ChatState):
    response = llm.invoke(state["messages"])
    return {
        "messages": state["messages"] + [response]
    }

def build_graph():
    graph = StateGraph(ChatState)

    graph.add_node("chat", chat_node)
    graph.set_entry_point("chat")
    graph.add_edge("chat", END)

    return graph.compile()