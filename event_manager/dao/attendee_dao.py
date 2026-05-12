"""
attendee_dao.py
Data Access Object for the Attendees table.
Contains all SQL operations: SELECT, INSERT, UPDATE, DELETE.
All queries use parameterized statements (?) to prevent SQL injection.
"""

import database as DB

# SELECT all attendees ordered by ID
def get_all_attendees():
    db = None
    try:
        db = DB.get_db()
        return db.execute("SELECT * FROM Attendees ORDER BY attendee_id").fetchall()
    finally:
        if db: db.close()

# SELECT a single attendee by primary key — used to pre-fill the edit form
def get_attendee_by_id(attendee_id):
    db = None
    try:
        db = DB.get_db()
        return db.execute("SELECT * FROM Attendees WHERE attendee_id = ?", (attendee_id,)).fetchone()
    finally:
        if db: db.close()

# INSERT a new attendee row into the Attendees table
def add_attendee(name, email, phone):
    db = None
    try:
        db = DB.get_db()
        db.execute("INSERT INTO Attendees (name, email, phone) VALUES (?, ?, ?)",
                   (name, email, phone))
        db.commit()
    except Exception as e:
        if db: db.rollback()
        raise e
    finally:
        if db: db.close()

# UPDATE an existing attendee row identified by attendee_id
def update_attendee(attendee_id, name, email, phone):
    db = None
    try:
        db = DB.get_db()
        db.execute("UPDATE Attendees SET name=?, email=?, phone=? WHERE attendee_id=?",
                   (name, email, phone, attendee_id))
        db.commit()
    except Exception as e:
        if db: db.rollback()
        raise e
    finally:
        if db: db.close()

# DELETE an attendee — ON DELETE CASCADE removes their linked Tickets automatically
def delete_attendee(attendee_id):
    db = None
    try:
        db = DB.get_db()
        db.execute("DELETE FROM Attendees WHERE attendee_id = ?", (attendee_id,))
        db.commit()
    except Exception as e:
        if db: db.rollback()
        raise e
    finally:
        if db: db.close()