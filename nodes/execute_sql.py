from database.query_executer import execute_sql
from model.llm import llm
from states.InsightReport import InsightReport
from utils.sql_utils import clean_sql

def execute_and_generate_insights(state):
    sql_query = clean_sql(state["sql_query"])
    query_result = execute_sql(sql_query)
    
    insight_agent = llm.with_structured_output(InsightReport)
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