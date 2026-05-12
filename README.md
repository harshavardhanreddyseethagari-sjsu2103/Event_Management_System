# Event Management System

> A three-tier web application for CS-157A (Database Management Systems) at San José State University

---

## What it does

A browser-based system for managing events, attendees, venues, organizers, and ticket purchases — with full create, read, update, and delete operations backed by a relational database.

---

## Tech Stack

| Layer | Technology | Role |
|-------|-----------|------|
| Presentation | Flask + Jinja2 + Bootstrap 5 | Web pages the user sees |
| Application | Python — DAO functions | Business logic, SQL execution |
| Data | SQLite3 (Python DB-API 2.0) | Relational database storage |

---

## Database Schema

6 tables, all normalized to BCNF.

```
Organizers ──< Events >── Venues
                 │
              Tickets
              /     \
         Events   Attendees

Users (authentication only)
```

| Table | Primary Key | Foreign Keys |
|-------|------------|--------------|
| Organizers | organizer_id | — |
| Venues | venue_id | — |
| Events | event_id | organizer_id, venue_id |
| Attendees | attendee_id | — |
| Tickets | ticket_id | event_id, attendee_id |
| Users | user_id | — |

---

## Project Structure

```
event_manager/
├── app.py                  # All Flask routes and auth decorators
├── database.py             # DB connection helper
├── create_schema.sql       # CREATE TABLE statements
├── initialize_data.sql     # Sample data (15+ rows per table)
├── generate_passwords.py   # Run once to generate hashed passwords
├── .env                    # Secret key (not committed to GitHub)
├── dao/
│   ├── organizer_dao.py
│   ├── venue_dao.py
│   ├── event_dao.py
│   ├── attendee_dao.py
│   ├── ticket_dao.py
│   └── user_dao.py
└── templates/
    ├── base.html
    ├── index.html
    ├── query.html
    ├── auth/
    │   ├── login.html
    │   └── unauthorized.html
    ├── events/
    ├── attendees/
    ├── tickets/
    ├── organizers/
    └── venues/
```

---

## How to Run

```bash
# Install dependencies
pip3 install flask python-dotenv werkzeug

# Run password generator once to set up seed data
python3 generate_passwords.py
# Copy the output into initialize_data.sql

# Start the app
cd event_manager
python3 app.py
```

Open `http://127.0.0.1:5000` in your browser.

The database (`events.db`) is created and seeded automatically on first run.

---

## Demo Accounts

| Username | Password | Role |
|----------|----------|------|
| admin | admin123 | Full CRUD access + Query Console |
| viewer | viewer123 | Read-only access |

---

## CRUD Coverage

Every table supports all four SQL operations through the web UI.

| Operation | SQL | Where |
|-----------|-----|-------|
| Read | SELECT | All list pages |
| Create | INSERT | Every "Add New" form (admin only) |
| Update | UPDATE | Every "Edit" form (admin only) |
| Delete | DELETE | Every "Delete" button (admin only) |

---

## Key Features

- Role-based authentication (admin / viewer)
- Admin SQL Query Console — run any SQL query from the browser
- ON DELETE CASCADE — deleting a parent record removes all linked child records
- Input validation enforced at both the HTML form level and the database CHECK constraint level
- Parameterized queries throughout — no SQL injection risk

---

## Project Progress Check

- [x] Project proposal
- [x] Schema design (6 tables, BCNF)
- [x] create_schema.sql + initialize_data.sql
- [x] database.py
- [x] All 5 entity DAOs + user_dao.py
- [x] Flask routes (app.py)
- [x] Role-based authentication
- [x] HTML templates
- [x] Query Console
- [x] Final report
- [x] Presentation

---

## Team

| Name |
|------|
| Victor Tung |
| Harshavardhan Seethagari |

---

*CS-157A · Spring 2026 · San José State University*
