from langchain.tools import tool
from langfuse import observe
import sqlite3

DB_PATH = "data/Chinook.db"

def get_connection():
    try:
        return sqlite3.connect(DB_PATH)
    except sqlite3.Error as e:
        raise ConnectionError(
            f"Failed to connect to database: {e}"
        )

@tool
@observe
def get_schema() -> str:
    conn = get_connection()

    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT name
            FROM sqlite_master
            WHERE type='table'
            AND name NOT LIKE 'sqlite_%'
            ORDER BY name
        """)
        tables = cursor.fetchall()
        schema = []

        for (table_name,) in tables:
            schema.append(f"\nTABLE {table_name}")
            cursor.execute(f"PRAGMA table_info('{table_name}')")
            for col in cursor.fetchall():
                schema.append(
                    f"  {col[1]} {col[2]}"
                )
            cursor.execute(
                f"PRAGMA foreign_key_list('{table_name}')"
            )
            foreign_keys = cursor.fetchall()
            
            if foreign_keys:
                schema.append("  FOREIGN KEYS:")
                for fk in foreign_keys:
                    schema.append(
                        f"    {fk[3]} -> {fk[2]}.{fk[4]}"
                    )
        return "\n".join(schema)

    except Exception as e:
        raise RuntimeError(
            f"Failed to load schema: {e}"
        )

    finally:
        conn.close()