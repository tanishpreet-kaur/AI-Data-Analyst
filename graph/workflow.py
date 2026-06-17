from langgraph.graph import StateGraph, START, END
from states.SQLAgentState import SQLAgentState
from nodes.schema_loader import schema_loader
from nodes.sql_creation import generate_sql

graph = StateGraph(SQLAgentState)

graph.add_node("schema_loader", schema_loader)
graph.add_node("sql_generator", generate_sql)

graph.add_edge(START, "schema_loader")
graph.add_edge("schema_loader", "sql_generator")

analyst_bot = graph.compile()

