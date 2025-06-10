import os
import sqlite3
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(__file__), "../data/disaster_relief.db")

def init_db():
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS reports (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT,
        location TEXT,
        image_path TEXT,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)
    con.commit()
    con.close()

def save_report(description, location, image_filename=None):
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.execute(
        "INSERT INTO reports (description, location, image_path) VALUES (?, ?, ?)",
        (description, location, image_filename)
    )
    con.commit()
    report_id = cur.lastrowid
    con.close()
    return report_id

def get_report(report_id):
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    cur.execute("SELECT * FROM reports WHERE id = ?", (report_id,))
    row = cur.fetchone()
    con.close()
    if not row:
        return None
    return {
        "id": row[0],
        "description": row[1],
        "location": row[2],
        "image_path": row[3],
        "created_at": row[4]
    }