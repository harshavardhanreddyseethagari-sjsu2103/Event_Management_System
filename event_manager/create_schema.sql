CREATE TABLE IF NOT EXISTS Organizers (
    organizer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name         TEXT    NOT NULL CHECK(length(name) >= 2),
    email        TEXT    NOT NULL CHECK(email LIKE '%@gmail.com' OR email LIKE '%@sjsu.edu'),
    phone        TEXT    NOT NULL CHECK(length(phone) == 10 AND phone GLOB '[0-9]*'),
    organization TEXT    NOT NULL CHECK(length(organization) >= 2)
);

CREATE TABLE IF NOT EXISTS Venues (
    venue_id  INTEGER PRIMARY KEY AUTOINCREMENT,
    name      TEXT    NOT NULL CHECK(length(name) >= 2),
    address   TEXT    NOT NULL CHECK(length(address) >= 5),
    city      TEXT    NOT NULL CHECK(length(city) >= 2),
    state     TEXT    NOT NULL CHECK(length(state) == 2),
    capacity  INTEGER NOT NULL CHECK(capacity > 0)
);

CREATE TABLE IF NOT EXISTS Events (
    event_id     INTEGER PRIMARY KEY AUTOINCREMENT,
    title        TEXT    NOT NULL CHECK(length(title) >= 2),
    description  TEXT,
    event_date   TEXT    NOT NULL,
    max_capacity INTEGER NOT NULL CHECK(max_capacity > 0),
    organizer_id INTEGER NOT NULL,
    venue_id     INTEGER NOT NULL,
    FOREIGN KEY (organizer_id) REFERENCES Organizers(organizer_id) ON DELETE CASCADE,
    FOREIGN KEY (venue_id)     REFERENCES Venues(venue_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Attendees (
    attendee_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name        TEXT NOT NULL CHECK(length(name) >= 2),
    email       TEXT NOT NULL CHECK(email LIKE '%@gmail.com' OR email LIKE '%@sjsu.edu'),
    phone       TEXT NOT NULL CHECK(length(phone) == 10 AND phone GLOB '[0-9]*')
);

CREATE TABLE IF NOT EXISTS Tickets (
    ticket_id     INTEGER PRIMARY KEY AUTOINCREMENT,
    event_id      INTEGER NOT NULL,
    attendee_id   INTEGER NOT NULL,
    ticket_type   TEXT    NOT NULL CHECK(ticket_type IN ('General', 'VIP', 'Standard', 'Premium', 'Free', 'Workshop')),
    price         REAL    NOT NULL CHECK(price >= 0),
    purchase_date TEXT    NOT NULL,
    FOREIGN KEY (event_id)    REFERENCES Events(event_id)    ON DELETE CASCADE,
    FOREIGN KEY (attendee_id) REFERENCES Attendees(attendee_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Users (
    user_id  INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    role     TEXT NOT NULL
);