from langchain_core.prompts import PromptTemplate
from app.llm.ollama import get_llm

def build_chain(prompt_str: str):
    prompt = PromptTemplate.from_template(prompt_str)
    llm = get_llm()
    return prompt | llm