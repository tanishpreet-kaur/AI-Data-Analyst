from agents.review_agent import review_agent

def review_sql(state):
    review = review_agent.invoke(
        f"""
        User Question:
        {state['question']}

        Generated SQL:
        {state['sql_query']}
        """
    )

    return {
        "approved": review.approved,
        "review_reason": review.reason,
        "sql_query": (
            review.corrected_sql
            if review.corrected_sql
            else state["sql_query"]
        )
    }
    
def route_after_review(state):
    if state["approved"]:
        return "execute_sql"
    return "sql_generator"