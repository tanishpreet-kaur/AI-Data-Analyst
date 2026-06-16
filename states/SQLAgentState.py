from typing import TypedDict, Optional
import pandas as pd

class SQLAgentState(TypedDict):
    question: str
    schema: str
    sql_query: Optional[str]
    query_result: Optional[list]
    error: Optional[str]