from database.connection import get_connection
from langfuse import observe

@observe("get_schema")
def get_schema(conn):
    cursor = conn.cursor()

    cursor.execute("""
    SELECT name
    FROM sqlite_master
    WHERE type='table'
    """)

    tables = cursor.fetchall()
    schema = ""

    for table in tables:
        table_name = table[0]
        cursor.execute(
            f"PRAGMA table_info({table_name})"
        )
        columns = cursor.fetchall()
        schema += f"\nTABLE {table_name}\n"

        for col in columns:
            column_name = col[1]
            datatype = col[2]
            schema += (
                f"  {column_name} {datatype}\n"
            )

    return schema