from app.services.query import route_query


def test_trivial_queries():
    queries = ["hello", "who are you", "bonjour"]

    for q in queries:
        result = route_query(q)
        print(f"\n[TEST] Query: {q}")
        print(f"[TEST] Route: {result.route}")
        assert result.route == "direct_answer"


def test_technical_queries():
    queries = [
        "how to configure API",
        "I have an error in my setup"
    ]

    for q in queries:
        result = route_query(q)
        print(f"\n[TEST] Query: {q}")
        print(f"[TEST] Route: {result.route}")
        assert result.route == "search_docs"


def test_empty_query():
    result = route_query("")
    print(f"\n[TEST] test_empty_query")
    print(f"[TEST] Route: {result.route}")
    assert result.route == "direct_answer"


def test_weird_query():
    result = route_query("???")
    print(f"\n[TEST] test_weird_query")
    print(f"[TEST] Route: {result.route}")
    assert result.route in ["direct_answer", "search_docs"]