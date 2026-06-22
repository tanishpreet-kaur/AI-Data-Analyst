from agents.review_agent import review_agent
from langgraph.graph import END

def review_sql(state):
    review = review_agent.invoke(
                {
                    "messages": [
                        {
                            "role": "user",
                            "content": f"""
                            User Question:
                            {state['question']}

                            Generated SQL:
                            {state['sql_query']}
                            """
                        }
                    ]
                }
            )

    review = review["structured_response"]

    return {
        "approved": review.approved,
        "review_reason": review.reason,
        "sql_query": (
            review.corrected_sql
            if review.corrected_sql
            else state["sql_query"]
        ),
        "retry_count": state.get("retry_count", 0) + 1
    }
    

    
def route_after_review(state):
    if state["approved"]:
        return "execute_and_insight"
    if state["retry_count"] >= 3:
        return END
    return "sql_generator"
