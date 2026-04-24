from app.services.routing_decision import RoutingDecision

def fallback_rule_based(query: str) -> RoutingDecision:
    q = query.lower().strip()

    trivial_keywords = ["hello", "hi", "who are you", "bonjour", "salut"]
    technical_keywords = ["api", "error", "config", "setup", "bug", "install"]

    if any(k in q for k in trivial_keywords):
        route = "direct_answer"
    elif any(k in q for k in technical_keywords):
        route = "search_docs"
    else:
        route = "search_docs"

    return RoutingDecision(
        route=route,
        question=query.strip()
    )