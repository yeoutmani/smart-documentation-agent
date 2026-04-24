def simple_similarity(query: str, doc: str) -> float:
    query_words = set(query.lower().split())
    doc_words = set(doc.lower().split())

    if not query_words:
        return 0.0

    # intersection ratio
    common = query_words.intersection(doc_words)

    return len(common) / len(query_words)