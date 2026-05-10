import database as DB

def get_all_attendees():
    db = None
    try:
        db = DB.get_db()
        return db.execute("SELECT * FROM Attendees ORDER BY attendee_id").fetchall()
    finally:
        if db: db.close()

def get_attendee_by_id(attendee_id):
    db = None
    try:
        db = DB.get_db()
        return db.execute("SELECT * FROM Attendees WHERE attendee_id = ?", (attendee_id,)).fetchone()
    finally:
        if db: db.close()

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