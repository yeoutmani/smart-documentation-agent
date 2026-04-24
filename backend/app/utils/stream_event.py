import json

def stream_event(type_: str, content: str = "", meta: dict = None):
    return json.dumps({
        "type": type_,
        "content": content,
        "meta": meta or {}
    }) + "\n"