from langchain.agents import create_agent
from model.llm import llm 
from prompts.sql_prompt import SQL_PROMPT

sql_agent = create_agent(
    model=llm,
    system_prompt = SQL_PROMPT)