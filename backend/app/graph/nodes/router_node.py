
from app.services.query import route_query

async def router_node(state: dict):
    decision = route_query(state["question"])

    return {
        "route": decision.route,
        "question": decision.question
    }