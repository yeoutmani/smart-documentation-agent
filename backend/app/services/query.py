import json
from app.services.routing_decision import RoutingDecision
from app.services.fallback import fallback_rule_based
from app.llm.router_chain import router_chain
from app.utils import safe_parse

def route_query(query: str) -> RoutingDecision:
    query = (query or "").strip()

    if not query:
        return RoutingDecision(
            route="direct_answer",
            question="empty_query",
            reason="empty input fallback"
        )

    try:
        response = router_chain.invoke({"query": query})

        content = response.content

        data = safe_parse(content)

        if data.get("route") not in ["direct_answer", "search_docs"]:
            return fallback_rule_based(query)
        
        data.setdefault("reason", "LLM classification")
        data["question"] = query

        return RoutingDecision(**data)

    except Exception:
        return fallback_rule_based(query)