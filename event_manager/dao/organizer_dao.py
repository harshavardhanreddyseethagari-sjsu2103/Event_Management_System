"""
organizer_dao.py
Data Access Object for the Organizers table.
Contains all SQL operations: SELECT, INSERT, UPDATE, DELETE.
All queries use parameterized statements (?) to prevent SQL injection.
"""
import database as DB

# SELECT all organizers ordered by ID
def get_all_organizers():
    db = None
    try:
        db = DB.get_db()
        rows = db.execute("SELECT * FROM Organizers ORDER BY organizer_id").fetchall()
        return rows
    finally:
        if db: db.close()

# SELECT a single organizer by primary key — used to pre-fill the edit form
def get_organizer_by_id(organizer_id):
    db = None
    try:
        db = DB.get_db()
        return db.execute("SELECT * FROM Organizers WHERE organizer_id = ?", (organizer_id,)).fetchone()
    finally:
        if db: db.close()

# INSERT a new organizer row into the Organizers table
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

# UPDATE an existing organizer row identified by organizer_id
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
        
# DELETE an organizer row by primary key
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