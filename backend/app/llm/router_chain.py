from app.llm.base_chain import build_chain
from app.prompt.router import ROUTER_PROMPT

router_chain = build_chain(ROUTER_PROMPT)
