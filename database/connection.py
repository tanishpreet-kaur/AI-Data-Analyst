import sqlite3

DB_PATH = "data/Chinook.db"

def get_connection():
    return sqlite3.connect(DB_PATH)