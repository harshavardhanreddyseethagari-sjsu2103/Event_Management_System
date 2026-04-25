import database as DB
# join in organizer and venue names so we dont have to do it in the template
def get_all_events():
    db = DB.get_db()
    events = db.execute("""
        SELECT e.*, o.name AS organizer_name, v.name AS venue_name
        FROM Events e
        JOIN Organizers o ON e.organizer_id = o.organizer_id
        JOIN Venues v ON e.venue_id = v.venue_id
        ORDER BY e.event_date
    """).fetchall()
    db.close()
    return events

def get_event_by_id(event_id):
    db = DB.get_db()
    event = db.execute("""
        SELECT e.*, o.name AS organizer_name, v.name AS venue_name
        FROM Events e
        JOIN Organizers o ON e.organizer_id = o.organizer_id
        JOIN Venues v ON e.venue_id = v.venue_id
        WHERE e.event_id = ?
    """, (event_id,)).fetchone()
    db.close()
    return event

def add_event(title, description, event_date, organizer_id, venue_id):
    db = DB.get_db()
    db.execute(
        "INSERT INTO Events (title, description, event_date, organizer_id, venue_id) VALUES (?, ?, ?, ?, ?)",
        (title, description, event_date, organizer_id, venue_id)
    )
    db.commit()
    db.close()

def update_event(event_id, title, description, event_date, organizer_id, venue_id):
    db = DB.get_db()
    db.execute("""
        UPDATE Events
        SET title=?, description=?, event_date=?, organizer_id=?, venue_id=?
        WHERE event_id=?
    """, (title, description, event_date, organizer_id, venue_id, event_id))
    db.commit()
    db.close()

def delete_event(event_id):
    db = DB.get_db()
    db.execute("DELETE FROM Events WHERE event_id = ?", (event_id,))
    db.commit()
    db.close()