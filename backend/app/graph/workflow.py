# app/graph/workflow.py

from langgraph.graph import StateGraph, END
from app.graph.state import AgentState

from app.graph.nodes.router_node import router_node
from app.graph.nodes.rag_node import rag_node
from app.graph.nodes.generator_node import generator_node


def build_graph(
    router=router_node,
    rag=rag_node,
    generator=generator_node
):

    workflow = StateGraph(AgentState)

    workflow.add_node("router", router)
    workflow.add_node("rag", rag)
    workflow.add_node("generator", generator)

    workflow.set_entry_point("router")

    def route_condition(state):
        return state["route"]

    workflow.add_conditional_edges(
        "router",
        route_condition,
        {
            "search_docs": "rag",
            "direct_answer": "generator"
        }
    )

    workflow.add_edge("rag", "generator")
    workflow.add_edge("generator", END)

    return workflow.compile()