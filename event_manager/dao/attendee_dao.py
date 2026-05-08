import database as DB

def get_all_attendees():
    db = DB.get_db()
    attendees = db.execute("SELECT * FROM Attendees ORDER BY attendee_id").fetchall()
    db.close()
    return attendees

def get_attendee_by_id(attendee_id):
    db = DB.get_db()
    attendee = db.execute("SELECT * FROM Attendees WHERE attendee_id = ?", (attendee_id,)).fetchone()
    db.close()
    return attendee

def add_attendee(name, email, phone):
    db = DB.get_db()
    db.execute(
        "INSERT INTO Attendees (name, email, phone) VALUES (?, ?, ?)",
        (name, email, phone)
    )
    db.commit()
    db.close()

def update_attendee(attendee_id, name, email, phone):
    db = DB.get_db()
    db.execute(
        "UPDATE Attendees SET name=?, email=?, phone=? WHERE attendee_id=?",
        (name, email, phone, attendee_id)
    )
    db.commit()
    db.close()

def delete_attendee(attendee_id):
    db = DB.get_db()
    try:
        db.execute("DELETE FROM Attendees WHERE attendee_id = ?", (attendee_id,))
        db.commit()
    finally:
        db.close()  