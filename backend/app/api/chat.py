from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from app.graph.workflow import build_graph
import json

router = APIRouter()

graph = build_graph()


@router.post("/chat")
async def chat_endpoint(payload: dict):

    question = payload.get("question", "")

    async def stream():

        async for event in graph.astream_events(
            {"question": question},
            version="v1"
        ):

            # status propre
            if event["event"] == "on_chain_start":

                name = event.get("name")

                if name == "router":
                    yield json.dumps({"type": "status", "content": "classifying"}) + "\n"

                elif name == "rag":
                    yield json.dumps({"type": "status", "content": "searching_docs"}) + "\n"

                elif name == "generator":
                    yield json.dumps({"type": "status", "content": "generating"}) + "\n"

            # tokens
            elif event["event"] == "on_chat_model_stream":

                token = event["data"]["chunk"].content

                if token:  # important
                    yield json.dumps({
                        "type": "token",
                        "content": token
                    }) + "\n"

        yield json.dumps({"type": "end"}) + "\n"

    return StreamingResponse(
        stream(),
        media_type="application/json"
    )