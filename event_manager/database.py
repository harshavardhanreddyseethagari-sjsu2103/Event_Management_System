import sqlite3
import os

DATABASE = 'events.db'

def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def init_db():
    if os.path.exists(DATABASE):
        return

    conn = get_db()

    with open('schema.sql', 'r') as f:
        conn.executescript(f.read())

    with open('seed.sql', 'r') as f:
        conn.executescript(f.read())

    conn.commit()
    conn.close()
    print("Database created and seeded!")