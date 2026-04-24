from app.services.rag.rag_node import rag_node as rag_service

async def rag_node(state: dict):
    return await rag_service(state)