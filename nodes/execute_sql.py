from model.llm import llm
from states.InsightReport import InsightReport

def create_execute_and_generate_insights_node(execution_tools):

    def execute_and_generate_insights(state):

        query_result = execution_tools.invoke(
            state["sql_query"]
        )

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

    return execute_and_generate_insights