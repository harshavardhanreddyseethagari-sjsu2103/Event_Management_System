import database as DB

def get_all_venues():
    db = DB.get_db()
    venues = db.execute("SELECT * FROM Venues ORDER BY name").fetchall()
    db.close()
    return venues

def get_venue_by_id(venue_id):
    db = DB.get_db()
    venue = db.execute("SELECT * FROM Venues WHERE venue_id = ?", (venue_id,)).fetchone()
    db.close()
    return venue

def add_venue(name, address, city, state, capacity):
    db = DB.get_db()
    db.execute(
        "INSERT INTO Venues (name, address, city, state, capacity) VALUES (?, ?, ?, ?, ?)",
        (name, address, city, state, capacity)
    )
    db.commit()
    db.close()

def update_venue(venue_id, name, address, city, state, capacity):
    db = DB.get_db()
    db.execute(
        "UPDATE Venues SET name=?, address=?, city=?, state=?, capacity=? WHERE venue_id=?",
        (name, address, city, state, capacity, venue_id)
    )
    db.commit()
    db.close()

def delete_venue(venue_id):
    db = DB.get_db()
    db.execute("DELETE FROM Venues WHERE venue_id = ?", (venue_id,))
    db.commit()
    db.close()