from app.services.rag.rag_node import rag_node
from app.services.rag import store
import pytest

@pytest.mark.asyncio
async def test_rag_node_with_mock(monkeypatch):

    mock_docs = [
        "API config example",
        "Random text"
    ]

    monkeypatch.setattr(store, "DOCUMENTS", mock_docs)

    state = {"question": "API"}

    result = await rag_node(state)
    print(f"\n[TEST] RAG Node Result: {result}")

    assert len(result["context"]) > 0

@pytest.mark.asyncio
async def test_rag_node_empty_question():
    state = {
        "question": "   "
    }

    result = await rag_node(state)

    # doit retourner une liste vide
    assert "context" in result
    assert result["context"] == []