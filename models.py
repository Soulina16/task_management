import sqlite3
from sqlite3 import Error
from database import create_connection

def add_task(task):
    """ Add a new task to the tasks table """
    conn = create_connection()
    sql = ''' INSERT INTO tasks(title,description,completed)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()
    return cur.lastrowid

def get_tasks():
    """ Query all rows in the tasks table """
    conn = create_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks")
    rows = cur.fetchall()
    return rows

def update_task(task):
    """ Update title, description, and completed status of a task """
    conn = create_connection()
    sql = ''' UPDATE tasks
              SET title = ? ,
                  description = ? ,
                  completed = ?
              WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()

def delete_task(id):
    """ Delete a task by task id """
    conn = create_connection()
    sql = 'DELETE FROM tasks WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()
