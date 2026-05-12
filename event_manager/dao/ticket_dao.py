"""
ticket_dao.py
Data Access Object for the Tickets table.
Tickets is a junction table linking Events and Attendees (many-to-many).
The get_all_tickets query JOINs Events and Attendees to show
readable titles and names instead of raw IDs.
"""

import database as DB

def get_all_tickets():
    db = None
    try:
        db = DB.get_db()
        return db.execute("""
            SELECT t.*, e.title AS event_title, a.name AS attendee_name
            FROM Tickets t
            JOIN Events e ON t.event_id = e.event_id
            JOIN Attendees a ON t.attendee_id = a.attendee_id
            ORDER BY t.purchase_date DESC
        """).fetchall()
    finally:
        if db: db.close()

def get_ticket_by_id(ticket_id):
    db = None
    try:
        db = DB.get_db()
        return db.execute("SELECT * FROM Tickets WHERE ticket_id = ?", (ticket_id,)).fetchone()
    finally:
        if db: db.close()

def add_ticket(event_id, attendee_id, ticket_type, price, purchase_date):
    db = None
    try:
        db = DB.get_db()
        db.execute("""
            INSERT INTO Tickets (event_id, attendee_id, ticket_type, price, purchase_date)
            VALUES (?, ?, ?, ?, ?)
        """, (event_id, attendee_id, ticket_type, price, purchase_date))
        db.commit()
    except Exception as e:
        if db: db.rollback()
        raise e
    finally:
        if db: db.close()

def update_ticket(ticket_id, event_id, attendee_id, ticket_type, price, purchase_date):
    db = None
    try:
        db = DB.get_db()
        db.execute("""
            UPDATE Tickets
            SET event_id=?, attendee_id=?, ticket_type=?, price=?, purchase_date=?
            WHERE ticket_id=?
        """, (event_id, attendee_id, ticket_type, price, purchase_date, ticket_id))
        db.commit()
    except Exception as e:
        if db: db.rollback()
        raise e
    finally:
        if db: db.close()

def delete_ticket(ticket_id):
    db = None
    try:
        db = DB.get_db()
        db.execute("DELETE FROM Tickets WHERE ticket_id = ?", (ticket_id,))
        db.commit()
    except Exception as e:
        if db: db.rollback()
        raise e
    finally:
        if db: db.close()