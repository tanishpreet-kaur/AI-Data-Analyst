import pandas as pd
from database.create_schema import get_connection
from langchain_core.tools import tool
from langfuse import observe

@observe("execute_query")
@tool
def execute_sql(sql_query: str) -> dict:
    conn = get_connection()

    try:
        df = pd.read_sql_query(sql_query, conn)
        return {
            "success": True,
            "row_count": len(df),
            "columns": df.columns.tolist(),
            "data": df.head(20).to_dict(orient="records")
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

    finally:
        if conn:
            conn.close()