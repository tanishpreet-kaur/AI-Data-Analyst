import re
import sqlite3
from database.create_schema import get_connection
from langchain.tools import tool

FORBIDDEN = {
    "DROP",
    "DELETE",
    "UPDATE",
    "INSERT",
    "ALTER",
    "TRUNCATE",
    "CREATE",
    "REPLACE",
}
def clean_sql(sql: str) -> str:
    sql = re.sub(r"```sql", "", sql, flags=re.IGNORECASE)
    sql = re.sub(r"```", "", sql)
    return sql.strip()


def validate_safe_sql(sql: str) -> None:
    sql_upper = sql.upper()
    for keyword in FORBIDDEN:
        if keyword in sql_upper:
            raise ValueError(
                f"Forbidden SQL keyword detected: {keyword}"
            )
    if not sql_upper.startswith(("SELECT", "WITH")):
        raise ValueError(
            "Only SELECT and WITH queries are allowed"
        )


def validate_sqlite_query(sql: str) -> bool:
    """Validate SQL syntax and schema using SQLite."""
    conn = get_connection()
    try:
        conn.execute(
            f"EXPLAIN QUERY PLAN {sql}"
        )
        return True
    except sqlite3.Error as e:
        raise ValueError(
            f"Invalid SQL: {e}"
        )
    finally:
        conn.close()

@tool
def validate_query(sql: str) -> bool:
    """Validate that a SQL query is safe and syntactically correct."""
    sql = clean_sql(sql)
    validate_safe_sql(sql)
    validate_sqlite_query(sql)
    return True