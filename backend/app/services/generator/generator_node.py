from app.llm.generator_chain import generator_chain

def format_context(context: list) -> str:
    if not context:
        return ""

    # gérer dict ou string
    return "\n".join(
        item["content"] if isinstance(item, dict) else item
        for item in context
    )

async def generator_node(state: dict) -> dict:
    question = state.get("question", "")
    context = state.get("context", [])

    if not question.strip():
        return {"answer": ""}

    context_text = format_context(context)

    try:
        response = await generator_chain.ainvoke({
            "context": context_text,
            "question": question,
            "has_context": bool(context)
        })

        return {"answer": response.content.strip()}

    except Exception:
        return {"answer": "An error occurred while generating the answer."}