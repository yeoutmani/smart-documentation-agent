import pytest
from app.services.generator.generator_node import generator_node


class FakeResponse:
    def __init__(self, content):
        self.content = content


class FakeChain:
    def __init__(self):
        self.last_input = None

    async def ainvoke(self, data):
        self.last_input = data
        return FakeResponse("Mocked answer")


@pytest.mark.asyncio
async def test_generator_with_context(monkeypatch):

    fake_chain = FakeChain()

    # remplacer generator_chain par fake
    monkeypatch.setattr(
        "app.services.generator.generator_node.generator_chain",
        fake_chain
    )

    state = {
        "question": "How to configure API?",
        "context": ["API config doc"]
    }

    result = await generator_node(state)

    # vérifier réponse
    assert result["answer"] == "Mocked answer"

    # vérifier has_context = True
    assert fake_chain.last_input["has_context"] is True

@pytest.mark.asyncio
async def test_generator_without_context(monkeypatch):

    fake_chain = FakeChain()

    monkeypatch.setattr(
        "app.services.generator.generator_node.generator_chain",
        fake_chain
    )

    state = {
        "question": "What is Python?",
        "context": []
    }

    result = await generator_node(state)

    #  réponse OK
    assert result["answer"] == "Mocked answer"

    #  vérifier has_context = False
    assert fake_chain.last_input["has_context"] is False