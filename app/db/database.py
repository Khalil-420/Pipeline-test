import sqlite3
import os

DATABASE = "tasks.db"

def initialize_database():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    with open('db/schema.sql') as f:
        cursor.executescript(f.read())
    conn.commit()
    conn.close()

def add_task(device_id,remote_path, label, local_path, device_name,):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tasks (device_id, remote_path, label, local_path, device_name) VALUES (?, ?, ?, ?, ?)",
        (device_id, remote_path, label, local_path, device_name)
    )
    conn.commit()
    conn.close()

def get_all_tasks():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT device_id, folder_id, label, local_path, device_name,remote_path FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    return tasks
