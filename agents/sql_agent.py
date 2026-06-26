from langchain.agents import create_agent
from model.llm import llm
from prompts.sql_prompt import SQL_PROMPT

def create_sql_agent(tools):
    return create_agent(
        llm,
        tools,
        system_prompt=SQL_PROMPT
    )