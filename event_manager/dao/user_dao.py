from database import get_db

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