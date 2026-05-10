import database as DB

def get_all_organizers():
    db = None
    try:
        db = DB.get_db()
        rows = db.execute("SELECT * FROM Organizers ORDER BY organizer_id").fetchall()
        return rows
    finally:
        if db: db.close()

def get_organizer_by_id(organizer_id):
    db = None
    try:
        db = DB.get_db()
        return db.execute("SELECT * FROM Organizers WHERE organizer_id = ?", (organizer_id,)).fetchone()
    finally:
        if db: db.close()

def add_organizer(name, email, phone, organization):
    db = None
    try:
        db = DB.get_db()
        db.execute("INSERT INTO Organizers (name, email, phone, organization) VALUES (?, ?, ?, ?)",
                   (name, email, phone, organization))
        db.commit()
    except Exception as e:
        if db: db.rollback()
        raise e
    finally:
        if db: db.close()

def update_organizer(organizer_id, name, email, phone, organization):
    db = None
    try:
        db = DB.get_db()
        db.execute("UPDATE Organizers SET name=?, email=?, phone=?, organization=? WHERE organizer_id=?",
                   (name, email, phone, organization, organizer_id))
        db.commit()
    except Exception as e:
        if db: db.rollback()
        raise e
    finally:
        if db: db.close()

def delete_organizer(organizer_id):
    db = None
    try:
        db = DB.get_db()
        db.execute("DELETE FROM Organizers WHERE organizer_id = ?", (organizer_id,))
        db.commit()
    except Exception as e:
        if db: db.rollback()
        raise e
    finally:
        if db: db.close()