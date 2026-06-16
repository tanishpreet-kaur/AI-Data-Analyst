from agents.sql_agent import sql_agent

def generate_sql(state):
    response = sql_agent.invoke({
        "messages": [
            {
                "role": "user",
                "content": f"""
                    Schema:
                    {state['schema']}

                    Question:
                    {state['question']}
                    """
            }
        ]
    })
    sql = response["messages"][-1].content
    return {
        "sql_query": sql
    }