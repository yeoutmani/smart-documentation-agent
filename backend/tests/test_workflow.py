import pytest
from app.graph.workflow import build_graph


@pytest.mark.asyncio
async def test_workflow_search_docs():

    async def fake_router(state):
        return {"route": "search_docs", "question": state["question"]}

    async def fake_rag(state):
        return {"context": ["API config doc"]}

    async def fake_generator(state):
        return {"answer": "Generated from context"}

    graph = build_graph(
        router=fake_router,
        rag=fake_rag,
        generator=fake_generator
    )

    result = await graph.ainvoke({
        "question": "How to configure API?"
    })

    assert result["route"] == "search_docs"
    assert result["context"] == ["API config doc"]
    assert result["answer"] == "Generated from context"

@pytest.mark.asyncio
async def test_workflow_direct_answer():

    async def fake_router(state):
        return {"route": "direct_answer", "question": state["question"]}

    async def fake_generator(state):
        return {"answer": "Direct response"}

    async def fake_rag(state):
        raise Exception("RAG should not be called")

    graph = build_graph(
        router=fake_router,
        rag=fake_rag,
        generator=fake_generator
    )

    result = await graph.ainvoke({
        "question": "Hello"
    })

    assert result["answer"] == "Direct response"