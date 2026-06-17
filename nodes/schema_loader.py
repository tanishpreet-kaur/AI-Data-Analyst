from database.connection import get_connection
from database.create_schema import get_schema

def schema_loader(state):
    conn = None
    try:
        conn = get_connection()
        schema = get_schema(conn)
        return {
            "schema": schema
        }
        
    finally:
        if conn:
            conn.close()