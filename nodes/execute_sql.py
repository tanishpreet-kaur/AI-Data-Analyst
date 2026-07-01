from model.llm import llm
from prompts.insight_prompt import INSIGHT_PROMPT
from langchain_core.messages import AIMessage

def create_execute_and_generate_insights_node(execution_tools):
    def execute_and_generate_insights(state):
        query_result = execution_tools.invoke(
            state["sql_query"]
        )

        prompt = f"""
            {INSIGHT_PROMPT}

            User Question:
            {state['question']}

            SQL Query:
            {state['sql_query']}

            Query Results:
            {query_result}
            """
        response = llm.invoke(prompt)

        return {
            "query_result": query_result,
            "answer": response.content,
            "messages": [
            AIMessage(content=response.content)
        ]
        }

    return execute_and_generate_insights