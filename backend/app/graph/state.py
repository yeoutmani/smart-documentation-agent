from typing import TypedDict, List


class AgentState(TypedDict):
    question: str
    route: str
    context: List[str]
    answer: str