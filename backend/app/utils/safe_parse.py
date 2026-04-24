import json

def safe_parse(content: str) -> dict:
    try:
        return json.loads(content)
    except Exception:
        return {}