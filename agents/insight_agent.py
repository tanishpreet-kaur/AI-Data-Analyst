from model.llm import llm
from states.InsightReport import InsightReport

insight_agent = llm.with_structured_output(
    InsightReport
)