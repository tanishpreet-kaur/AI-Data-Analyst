from agents.insight_agent import insight_agent
from database.query_executer import execute_sql

def execute_and_generate_insights(state):
    query_result = execute_sql(state["sql_query"])
    
    report = insight_agent.invoke(
        f"""
        User Question:
        {state['question']}

        SQL Query:
        {state['sql_query']}

        Query Results:
        {query_result}
        """
    )

    return {
        "query_result": query_result,
        "answer": report.answer,
        "key_findings": report.key_findings
    }