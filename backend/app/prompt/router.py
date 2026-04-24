ROUTER_PROMPT = """
You are a strict classifier.

Return ONLY valid JSON.

Format:
{"route": "direct_answer" or "search_docs", "reason": "short"}

No text outside JSON.

Query: {query}
"""