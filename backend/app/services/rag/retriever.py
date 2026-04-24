from app.services.rag.store import DOCUMENTS
from app.services.rag.similarity import simple_similarity


def retrieve_documents(query: str, top_k: int = 2):
    scored_docs = []

    for doc in DOCUMENTS:
        score = simple_similarity(query, doc)
        scored_docs.append((doc, score))

    # tri décroissant
    scored_docs.sort(key=lambda x: x[1], reverse=True)

    # filtrer score > 0
    filtered = [doc for doc, score in scored_docs if score > 0]

    return filtered[:top_k]