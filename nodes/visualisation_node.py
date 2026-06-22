from agents.visualisation_agent import visualisation_agent
from utils.chart_utils import create_plot
import plotly.io as pio

def visualisation_node(state):
    response = visualisation_agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": f"""
                    Question:
                    {state['question']}

                    Query Result:
                    {state['query_result']}
                    """
                }
            ]
        }
    )

    chart_spec = response["structured_response"]
    chart_json = create_plot(
        data=state["query_result"],
        chart_type=chart_spec.chart_type,
        x_column=chart_spec.x_column,
        y_column=chart_spec.y_column,
        title=chart_spec.title
    )
    
    fig = pio.from_json(chart_json)
    fig.show()

    return {
        "chart_type": chart_spec.chart_type,
        "chart_spec": chart_spec.model_dump(),
        "chart_json": chart_json
    }