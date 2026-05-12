"""
user_dao.py
Data Access Object for the Users table.
Passwords are stored as Werkzeug hashes — never plain text.
Password verification is handled in app.py using check_password_hash.
"""

from database import get_db

# SELECT a user by username — used during login to retrieve the hashed password
def get_user_by_username(username):
    db = get_db()
    try:
        row = db.execute("""
            SELECT user_id, username, password, role
            FROM Users
            WHERE username = ?
        """, (username,)).fetchone()
        return row
    finally:
        db.close()