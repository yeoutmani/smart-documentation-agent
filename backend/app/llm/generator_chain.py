from app.llm.base_chain import build_chain
from app.prompt.generator import GENERATOR_PROMPT

generator_chain = build_chain(GENERATOR_PROMPT)
