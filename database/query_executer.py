import sqlite3
from database.create_schema import get_connection
from langchain_core.tools import tool
from langfuse import observe

@observe()
def execute_sql(sql_query: str) -> list[dict]:
    """Execute SQL and return rows."""

    conn = get_connection()

    try:
        conn.row_factory = sqlite3.Row

        cursor = conn.cursor()
        cursor.execute(sql_query)

        return [
            dict(row)
            for row in cursor.fetchall()
        ]

    finally:
        conn.close()