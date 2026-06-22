from langgraph.graph import StateGraph, START, END
from states.SQLAgentState import SQLAgentState
from nodes.sql_creation import generate_sql
from nodes.review_node import review_sql, route_after_review
from nodes.execute_sql import execute_and_generate_insights

graph = StateGraph(SQLAgentState)

graph.add_node("sql_generator", generate_sql)
graph.add_node("sql_reviewer", review_sql)
graph.add_node("execute_and_insight", execute_and_generate_insights)

graph.add_edge(START, "sql_generator")
graph.add_edge("sql_generator", "sql_reviewer")
graph.add_conditional_edges(
    "sql_reviewer",
    route_after_review,
    {
        "sql_generator": "sql_generator",
        "execute_and_insight": "execute_and_insight",
    }
)
graph.add_edge("execute_and_insight", END)

analyst_bot = graph.compile()

