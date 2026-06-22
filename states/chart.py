from typing import Literal
from pydantic import BaseModel

class ChartSpec(BaseModel):
    chart_type: Literal[
        "bar",
        "line",
        "pie",
        "scatter"
    ]
    x_column: str
    y_column: str
    title: str