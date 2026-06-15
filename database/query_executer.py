import pandas as pd
from .connection import get_connection

def execute_query(sql):
    conn = get_connection()
    df = pd.read_sql_query(
        sql,
        conn
    )
    conn.close()
    return df