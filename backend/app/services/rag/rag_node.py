from app.services.rag.retriever import retrieve_documents


async def rag_node(state: dict) -> dict:
    question = state.get("question", "")

    if not question.strip():
        return {"context": []}

    docs = retrieve_documents(question)

    # enrichissement du contexte avec un score de similarité (mocké ici à 1.0 pour simplifier)
    context = [
        {"content": doc, "score": 1.0}  # mock score
        for doc in docs
    ]

    return {"context": context}