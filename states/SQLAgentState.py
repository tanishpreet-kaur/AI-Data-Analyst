from typing import TypedDict, Optional, Any

class SQLAgentState(TypedDict):
    question: str
    sql_query: str
    approved: bool
    review_reason: Optional[str]
    retry_count: int
    query_result: list[dict[str, Any]]
    answer: str
    key_findings: str
    chart_json: dict | None
    chart_type: str | None