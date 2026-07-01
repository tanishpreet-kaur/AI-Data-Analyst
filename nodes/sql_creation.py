from langchain_core.messages import HumanMessage

def create_generate_sql_node(sql_agent):

    def generate_sql(state):
        response = sql_agent.invoke(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": state["question"]
                    }
                ]
            }
        )

        return {
            "sql_query": response["messages"][-1].content,
            "messages": [
                HumanMessage(content=state["question"])
            ]
        }

    return generate_sql