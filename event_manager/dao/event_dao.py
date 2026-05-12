"""
event_dao.py
Data Access Object for the Events table.
The get_all_events query uses JOIN across Organizers and Venues
to return readable names instead of raw foreign key IDs.
"""

import database as DB

# SELECT all events with organizer name and venue name via JOIN
def get_all_events():
    db = None
    try:
        db = DB.get_db()
        return db.execute("""
            SELECT e.*, o.name AS organizer_name, v.name AS venue_name
            FROM Events e
            JOIN Organizers o ON e.organizer_id = o.organizer_id
            JOIN Venues v ON e.venue_id = v.venue_id
            ORDER BY e.event_date
        """).fetchall()
    finally:
        if db: db.close()

# SELECT a single event by primary key — used to pre-fill the edit form
def get_event_by_id(event_id):
    db = None
    try:
        db = DB.get_db()
        return db.execute("SELECT * FROM Events WHERE event_id = ?", (event_id,)).fetchone()
    finally:
        if db: db.close()

# INSERT a new event — organizer_id and venue_id are foreign keys
def add_event(title, description, event_date, max_capacity, organizer_id, venue_id):
    db = None
    try:
        db = DB.get_db()
        db.execute("""
            INSERT INTO Events (title, description, event_date, max_capacity, organizer_id, venue_id)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (title, description, event_date, max_capacity, organizer_id, venue_id))
        db.commit()
    except Exception as e:
        if db: db.rollback()
        raise e
    finally:
        if db: db.close()

# UPDATE an existing event row
def update_event(event_id, title, description, event_date, max_capacity, organizer_id, venue_id):
    db = None
    try:
        db = DB.get_db()
        db.execute("""
            UPDATE Events
            SET title=?, description=?, event_date=?, max_capacity=?, organizer_id=?, venue_id=?
            WHERE event_id=?
        """, (title, description, event_date, max_capacity, organizer_id, venue_id, event_id))
        db.commit()
    except Exception as e:
        if db: db.rollback()
        raise e
    finally:
        if db: db.close()

# DELETE an event — ON DELETE CASCADE removes linked Tickets automatically
def delete_event(event_id):
    db = None
    try:
        db = DB.get_db()
        db.execute("DELETE FROM Events WHERE event_id = ?", (event_id,))
        db.commit()
    except Exception as e:
        if db: db.rollback()
        raise e
    finally:
        if db: db.close()