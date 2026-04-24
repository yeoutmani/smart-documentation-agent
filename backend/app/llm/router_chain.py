from langchain_core.prompts import PromptTemplate
from app.llm.ollama import get_llm
from app.prompt.router import ROUTER_PROMPT

prompt = PromptTemplate.from_template(ROUTER_PROMPT)

llm = get_llm()

router_chain = prompt | llm