# Event Management System

> A three-tier web application 
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

5 tables, all normalized to BCNF.

```
Organizers ──< Events >── Venues
                 │
              Tickets
                 │
            Attendees
```

| Table | Primary Key | Foreign Keys |
|-------|------------|--------------|
| Organizers | organizer_id | — |
| Venues | venue_id | — |
| Events | event_id | organizer_id, venue_id |
| Attendees | attendee_id | — |
| Tickets | ticket_id | event_id, attendee_id |

---

## Project Structure

```
event_manager/
├── app.py              # All Flask routes
├── database.py         # DB connection helper
├── schema.sql          # CREATE TABLE statements
├── seed.sql            # Sample data (15+ rows per table)
├── dao/
│   ├── organizer_dao.py
│   ├── venue_dao.py
│   ├── event_dao.py
│   ├── attendee_dao.py
│   └── ticket_dao.py
└── templates/
    ├── base.html
    ├── index.html
    ├── events/
    ├── attendees/
    ├── tickets/
    ├── organizers/
    └── venues/
```

---

## How to Run

```bash
# Install Flask
pip install flask

# Start the app
cd event_manager
python app.py
```

Open `http://127.0.0.1:5000` in your browser.

The database (`events.db`) is created and seeded automatically on first run.

---

## CRUD Coverage

Every table supports all four SQL operations through the web UI.

| Operation | SQL | Where |
|-----------|-----|-------|
| Read | SELECT | All list pages |
| Create | INSERT | Every "Add New" form |
| Update | UPDATE | Every "Edit" form |
| Delete | DELETE | Every "Delete" button |

---

## Current Progress

- [x] Project proposal
- [x] Schema design (5 tables, BCNF)
- [x] schema.sql + seed.sql
- [x] database.py
- [x] organizer_dao.py
- [x] venue_dao.py
- [x] event_dao.py
- [x] attendee_dao.py
- [x] ticket_dao.py
- [x] Flask routes (app.py)
- [x] HTML templates
- [x] Final report
- [x] Presentation

---


*CS-157A · Spring 2026 · San José State University*
