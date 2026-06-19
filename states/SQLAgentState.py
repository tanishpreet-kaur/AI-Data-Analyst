from typing import TypedDict, Optional
import pandas as pd

class SQLAgentState(TypedDict):
    question: str
    sql_query: Optional[str]
    approved: Optional[bool]
    review_reason: Optional[str]
    query_result: Optional[list]