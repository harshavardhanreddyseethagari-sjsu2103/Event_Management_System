CREATE TABLE IF NOT EXISTS Organizers (
    organizer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name         TEXT NOT NULL,
    email        TEXT NOT NULL,
    phone        TEXT NOT NULL,
    organization TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS Venues (
    venue_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name     TEXT NOT NULL,
    address  TEXT NOT NULL,
    city     TEXT NOT NULL,
    state    TEXT NOT NULL,
    capacity INTEGER NOT NULL
);
 
-- events need both an organizer and a venue to exist first
CREATE TABLE IF NOT EXISTS Events (
    event_id     INTEGER PRIMARY KEY AUTOINCREMENT,
    title        TEXT NOT NULL,
    description  TEXT,
    event_date   TEXT NOT NULL,
    organizer_id INTEGER NOT NULL,
    venue_id     INTEGER NOT NULL,
    FOREIGN KEY (organizer_id) REFERENCES Organizers(organizer_id),
    FOREIGN KEY (venue_id)     REFERENCES Venues(venue_id)
);
 
CREATE TABLE IF NOT EXISTS Attendees (
    attendee_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name        TEXT NOT NULL,
    email       TEXT NOT NULL,
    phone       TEXT NOT NULL
);
 
-- a ticket ties one attendee to one event
CREATE TABLE IF NOT EXISTS Tickets (
    ticket_id   INTEGER PRIMARY KEY AUTOINCREMENT,
    event_id    INTEGER NOT NULL,
    attendee_id INTEGER NOT NULL,
    ticket_type TEXT NOT NULL,
    price       REAL NOT NULL,
    FOREIGN KEY (event_id)    REFERENCES Events(event_id),
    FOREIGN KEY (attendee_id) REFERENCES Attendees(attendee_id)
);
