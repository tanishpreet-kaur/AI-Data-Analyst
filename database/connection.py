import sqlite3

DB_PATH = "data/Chinook.db"

def get_connection():
    try:
        return sqlite3.connect(DB_PATH)

    except sqlite3.Error as e:
        raise ConnectionError(
            f"Failed to connect to database: {e}"
        )