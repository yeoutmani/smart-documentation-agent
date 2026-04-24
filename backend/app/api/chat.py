from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from app.graph.workflow import build_graph
from app.utils.stream_event import stream_event
import time

router = APIRouter()

graph = build_graph()


@router.post("/chat")
async def chat_endpoint(payload: dict):

    question = payload.get("question", "")

    async def stream():

        try:

            async for event in graph.astream_events(
                {"question": question},
                version="v1"
            ):

                if event["event"] == "on_chain_start":

                    name = event.get("name")

                    meta = {
                        "node": name,
                        "timestamp": time.time()
                    }

                    if name == "router":
                        yield stream_event("status", "classifying", meta)

                    elif name == "rag":
                        yield stream_event("status", "searching_docs", meta)

                    elif name == "generator":
                        yield stream_event("status", "generating", meta)

                elif event["event"] == "on_chat_model_stream":

                    token = event["data"]["chunk"].content

                    if token:
                        yield stream_event(
                            "token",
                            token,
                            {"node": "generator", "timestamp": time.time()}
                        )

            yield stream_event("end", meta={"timestamp": time.time()})

        except Exception as e:
            yield stream_event("error", str(e))

    return StreamingResponse(
        stream(),
        media_type="application/json"
    )