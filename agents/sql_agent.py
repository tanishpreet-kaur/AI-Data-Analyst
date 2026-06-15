from prompts.sql_prompt import SQL_PROMPT

class SQLAgent:
    def __init__(self, llm):
        self.llm = llm

    def run(self, question, schema):
        prompt = SQL_PROMPT.format(
            schema=schema,
            question=question
        )
        response = self.llm.invoke(prompt)
        return response.content