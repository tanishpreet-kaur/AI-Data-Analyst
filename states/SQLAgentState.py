from typing import TypedDict, Optional, Any, Annotated
from langgraph.graph.message import add_messages
from langchain_core.messages import BaseMessage

class SQLAgentState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]
    question: str
    sql_query: str
    approved: bool
    review_reason: Optional[str]
    retry_count: int
    query_result: list[dict[str, Any]]
    answer: str
    chart_json: dict | None
    chart_type: str | None