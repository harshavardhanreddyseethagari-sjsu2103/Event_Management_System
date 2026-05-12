"""
database.py
Handles the SQLite database connection and first-run initialization.

get_db()   — opens and returns a connection to events.db
init_db()  — runs create_schema.sql and initialize_data.sql on first launch
"""
import sqlite3
import os

# Path to the SQLite database file — created automatically on first run
DATABASE = 'events.db'

"""
    Opens a connection to the SQLite database and returns it.
    row_factory = sqlite3.Row allows columns to be accessed by name
    e.g. row['title'] instead of row[0]
    PRAGMA foreign_keys = ON enforces FK constraints — SQLite disables
    them by default, so this line is required for ON DELETE CASCADE to work.
"""
def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

"""
    Initializes the database on first run.
    Checks if events.db already exists — if it does, skips setup
    so existing data is never wiped on restart.
    Runs create_schema.sql to create all tables, then
    initialize_data.sql to insert the sample data.
"""
def init_db():
    if os.path.exists(DATABASE):
        return

    conn = get_db()

    # Create all tables from schema file
    with open('schema.sql', 'r') as f:
        conn.executescript(f.read())

    # Populate tables with sample data (15+ rows per table)
    with open('seed.sql', 'r') as f:
        conn.executescript(f.read())

    conn.commit()
    conn.close()
    print("Database created and seeded!")
