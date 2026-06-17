from pydantic import BaseModel

class SQLReview(BaseModel):
    approved: bool
    reason: str
    corrected_sql: str | None