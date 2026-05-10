import database as DB

def get_all_venues():
    db = None
    try:
        db = DB.get_db()
        return db.execute("SELECT * FROM Venues ORDER BY venue_id").fetchall()
    finally:
        if db: db.close()

def get_venue_by_id(venue_id):
    db = None
    try:
        db = DB.get_db()
        return db.execute("SELECT * FROM Venues WHERE venue_id = ?", (venue_id,)).fetchone()
    finally:
        if db: db.close()

def add_venue(name, address, city, state, capacity):
    db = None
    try:
        db = DB.get_db()
        db.execute("INSERT INTO Venues (name, address, city, state, capacity) VALUES (?, ?, ?, ?, ?)",
                   (name, address, city, state, capacity))
        db.commit()
    except Exception as e:
        if db: db.rollback()
        raise e
    finally:
        if db: db.close()

def update_venue(venue_id, name, address, city, state, capacity):
    db = None
    try:
        db = DB.get_db()
        db.execute("UPDATE Venues SET name=?, address=?, city=?, state=?, capacity=? WHERE venue_id=?",
                   (name, address, city, state, capacity, venue_id))
        db.commit()
    except Exception as e:
        if db: db.rollback()
        raise e
    finally:
        if db: db.close()

def delete_venue(venue_id):
    db = None
    try:
        db = DB.get_db()
        db.execute("DELETE FROM Venues WHERE venue_id = ?", (venue_id,))
        db.commit()
    except Exception as e:
        if db: db.rollback()
        raise e
    finally:
        if db: db.close()