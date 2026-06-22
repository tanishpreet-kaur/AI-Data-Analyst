from langchain.agents import create_agent
from model.llm import llm
from prompts.visualisation_prompt import VISUALISATION_PROMPT
from states.chart import ChartSpec
from utils.chart_utils import create_plot

visualisation_agent = create_agent(
    model=llm,
    system_prompt=VISUALISATION_PROMPT,
    response_format=ChartSpec
)