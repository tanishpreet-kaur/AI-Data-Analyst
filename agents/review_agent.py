from langchain.agents import create_agent
from model.llm import llm
from prompts.reviewer_prompt import REVIEWER_PROMPT
from states.SQLReview import SQLReview

review_agent = create_agent(
    model=llm,
    system_prompt=REVIEWER_PROMPT,
    response_format=SQLReview
)