import database as DB

def get_all_organizers():
    db = DB.get_db()
    rows = db.execute("SELECT * FROM Organizers ORDER BY name").fetchall()
    db.close()
    return rows

def get_organizer_by_id(organizer_id):
    db = DB.get_db()
    row = db.execute("SELECT * FROM Organizers WHERE organizer_id = ?", (organizer_id,)).fetchone()
    db.close()
    return row

def add_organizer(name, email, phone, organization):
    db = DB.get_db()
    db.execute("""
                INSERT INTO Organizers (name, email, phone, organization) VALUES (?,?,?,?)
            """,(name, email, phone, organization))
    db.commit()
    db.close()

def update_organizer(organizer_id, name, email, phone, organization):
    db = DB.get_db()
    db.execute("""
                UPDATE Organizers 
                SET name = ?, email = ?, phone = ?, organization = ? 
                WHERE organizer_id = ?
                """, (name, email, phone, organization, organizer_id))
    db.commit()
    db.close()

def delete_organizer(organizer_id):
    db = DB.get_db()
    db.execute("DELETE FROM Organizers WHERE organizer_id = ?", (organizer_id,))
    db.commit()
    db.close()


