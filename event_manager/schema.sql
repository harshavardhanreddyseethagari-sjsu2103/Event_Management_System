CREATE TABLE IF NOT EXISTS Organizers (
    organizer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name         TEXT NOT NULL,
    email        TEXT NOT NULL,
    phone        TEXT NOT NULL,
    organization TEXT NOT NULL
);