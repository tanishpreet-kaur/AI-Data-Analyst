from agents.review_agent import review_agent

def review_sql(state):
    response = review_agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": f"""
                        Question:
                        {state['question']}

                        Schema:
                        {state['schema']}

                        SQL:
                        {state['sql_query']}
                        """
                }
            ]
        }
    )

    review = response["structured_response"]

    if review.approved:
        return {
            "approved": True,
            "review_reason": review.reason
        }

    return {
        "approved": False,
        "review_reason": review.reason,
        "sql_query": review.corrected_sql
    }
    

def review_router(state):
    if state["approved"]:
        return "execute_query"
    return "execute_query"