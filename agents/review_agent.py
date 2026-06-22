from langchain.agents import create_agent
from model.llm import llm
from prompts.reviewer_prompt import REVIEWER_PROMPT
from states.SQLReview import SQLReview
from utils.sql_utils import validate_query


review_agent = create_agent(
    model=llm,
    system_prompt=REVIEWER_PROMPT,
    response_format=SQLReview,
    tools=[validate_query]
)