import database as DB

# pull in event title and attendee name so the ticket list is readable
def get_all_tickets():
    db = DB.get_db()
    tickets = db.execute("""
        SELECT t.*, e.title AS event_title, a.name AS attendee_name
        FROM Tickets t
        JOIN Events e ON t.event_id = e.event_id
        JOIN Attendees a ON t.attendee_id = a.attendee_id
        ORDER BY t.ticket_id
    """).fetchall()
    db.close()
    return tickets

def get_ticket_by_id(ticket_id):
    db = DB.get_db()
    ticket = db.execute("""
        SELECT t.*, e.title AS event_title, a.name AS attendee_name
        FROM Tickets t
        JOIN Events e ON t.event_id = e.event_id
        JOIN Attendees a ON t.attendee_id = a.attendee_id
        WHERE t.ticket_id = ?
    """, (ticket_id,)).fetchone()
    db.close()
    return ticket

def add_ticket(event_id, attendee_id, ticket_type, price):
    db = DB.get_db()
    db.execute(
        "INSERT INTO Tickets (event_id, attendee_id, ticket_type, price) VALUES (?, ?, ?, ?)",
        (event_id, attendee_id, ticket_type, price)
    )
    db.commit()
    db.close()

def update_ticket(ticket_id, event_id, attendee_id, ticket_type, price):
    db = DB.get_db()
    db.execute(
        "UPDATE Tickets SET event_id=?, attendee_id=?, ticket_type=?, price=? WHERE ticket_id=?",
        (event_id, attendee_id, ticket_type, price, ticket_id)
    )
    db.commit()
    db.close()


def delete_ticket(ticket_id):
    db = DB.get_db()
    try:
        db.execute("DELETE FROM Events WHERE event_id = ?", (ticket_id,))
        db.commit()
    finally:
        db.close()