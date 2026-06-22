from pydantic import BaseModel

class InsightReport(BaseModel):
    answer: str
    key_findings: list[str]