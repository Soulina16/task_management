import sqlite3
from sqlite3 import Error

DATABASE = "tasks.db"

def create_connection():
    """ Create a database connection to the SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(DATABASE)
    except Error as e:
        print(e)
    return conn

def create_table():
    """ Create tasks table if it doesn't exist """
    conn = create_connection()
    with conn:
        sql_create_tasks_table = """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            completed BOOLEAN NOT NULL CHECK (completed IN (0, 1))
        );
        """
        try:
            c = conn.cursor()
            c.execute(sql_create_tasks_table)
        except Error as e:
            print(e)
