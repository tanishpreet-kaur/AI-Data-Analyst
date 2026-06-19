from langgraph.graph import StateGraph, START, END
from states.SQLAgentState import SQLAgentState
from nodes.sql_creation import generate_sql
from nodes.review_node import review_sql, route_after_review

graph = StateGraph(SQLAgentState)

graph.add_node("sql_generator", generate_sql)
graph.add_node("sql_reviewer", review_sql)

graph.add_edge(START, "sql_generator")
graph.add_edge("sql_generator", "sql_reviewer")

analyst_bot = graph.compile()

