from app.services.rag.retriever import retrieve_documents


async def rag_node(state: dict) -> dict:
    question = state["question"]

    docs = retrieve_documents(question)

    return {
        "context": docs
    }