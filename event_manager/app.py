from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import check_password_hash
from functools import wraps
import database as DB
from dao import organizer_dao, venue_dao, event_dao, attendee_dao, ticket_dao, user_dao
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)

app.secret_key = os.getenv('SECRET_KEY')

# ── Auth decorators ──────────────────────────────────────────
# login_required: redirects unauthenticated users to /login
# admin_required: blocks non-admin users with a 403 page

def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated

def admin_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('login'))
        if session.get('role') != 'admin':
            return render_template('auth/unauthorized.html'), 403
        return f(*args, **kwargs)
    return decorated

# ── Login / Logout ───────────────────────────────────────────
# GET  /login → show login form
# POST /login → verify credentials against Users table, store session
@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect(url_for('index'))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = user_dao.get_user_by_username(username)
        if user and check_password_hash(user['password'], password):
            session['username'] = user['username']
            session['role']     = user['role']
            return redirect(url_for('index'))
        else:
            return render_template('auth/login.html', error="Invalid username or password")
    return render_template('auth/login.html', error=None)


# Clear session and redirect to login page
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/')
@login_required
def index():
    return render_template('index.html')

# organizers
@app.route('/organizers')
@login_required
def list_organizers():
    organizers = organizer_dao.get_all_organizers()
    return render_template('organizers/list.html', organizers=organizers)

@app.route('/organizers/add', methods=['GET', 'POST'])
@admin_required
def add_organizer():
    if request.method == 'POST':
        organizer_dao.add_organizer(
            request.form['name'],
            request.form['email'],
            request.form['phone'],
            request.form['organization']
        )
        return redirect(url_for('list_organizers'))
    return render_template('organizers/form.html', organizer=None)

@app.route('/organizers/edit/<int:organizer_id>', methods=['GET', 'POST'])
@admin_required
def edit_organizer(organizer_id):
    organizer = organizer_dao.get_organizer_by_id(organizer_id)
    if request.method == 'POST':
        organizer_dao.update_organizer(
            organizer_id,
            request.form['name'],
            request.form['email'],
            request.form['phone'],
            request.form['organization']
        )
        return redirect(url_for('list_organizers'))
    return render_template('organizers/form.html', organizer=organizer)

@app.route('/organizers/delete/<int:organizer_id>', methods=['POST'])
@admin_required
def delete_organizer(organizer_id):
    organizer_dao.delete_organizer(organizer_id)
    return redirect(url_for('list_organizers'))

# venues
@app.route('/venues')
@login_required
def list_venues():
    venues = venue_dao.get_all_venues()
    return render_template('venues/list.html', venues=venues)

@app.route('/venues/add', methods=['GET', 'POST'])
@admin_required
def add_venue():
    if request.method == 'POST':
        venue_dao.add_venue(
            request.form['name'],
            request.form['address'],
            request.form['city'],
            request.form['state'],
            request.form['capacity']
        )
        return redirect(url_for('list_venues'))
    return render_template('venues/form.html', venue=None)

@app.route('/venues/edit/<int:venue_id>', methods=['GET', 'POST'])
@admin_required
def edit_venue(venue_id):
    venue = venue_dao.get_venue_by_id(venue_id)
    if request.method == 'POST':
        venue_dao.update_venue(
            venue_id,
            request.form['name'],
            request.form['address'],
            request.form['city'],
            request.form['state'],
            request.form['capacity']
        )
        return redirect(url_for('list_venues'))
    return render_template('venues/form.html', venue=venue)

@app.route('/venues/delete/<int:venue_id>', methods=['POST'])
@admin_required
def delete_venue(venue_id):
    venue_dao.delete_venue(venue_id)
    return redirect(url_for('list_venues'))

# events
@app.route('/events')
@login_required
def list_events():
    events = event_dao.get_all_events()
    return render_template('events/list.html', events=events)

@app.route('/events/add', methods=['GET', 'POST'])
@admin_required
def add_event():
    if request.method == 'POST':
        event_dao.add_event(
            request.form['title'],
            request.form['description'],
            request.form['event_date'],
            request.form['organizer_id'],
            request.form['venue_id']
        )
        return redirect(url_for('list_events'))
    organizers = organizer_dao.get_all_organizers()
    venues = venue_dao.get_all_venues()
    return render_template('events/form.html', event=None, organizers=organizers, venues=venues)

@app.route('/events/edit/<int:event_id>', methods=['GET', 'POST'])
@admin_required
def edit_event(event_id):
    event = event_dao.get_event_by_id(event_id)
    if request.method == 'POST':
        event_dao.update_event(
            event_id,
            request.form['title'],
            request.form['description'],
            request.form['event_date'],
            request.form['organizer_id'],
            request.form['venue_id']
        )
        return redirect(url_for('list_events'))
    organizers = organizer_dao.get_all_organizers()
    venues = venue_dao.get_all_venues()
    return render_template('events/form.html', event=event, organizers=organizers, venues=venues)

@app.route('/events/delete/<int:event_id>', methods=['POST'])
@admin_required
def delete_event(event_id):
    event_dao.delete_event(event_id)
    return redirect(url_for('list_events'))

# attendees
@app.route('/attendees')
@login_required
def list_attendees():
    attendees = attendee_dao.get_all_attendees()
    return render_template('attendees/list.html', attendees=attendees)

@app.route('/attendees/add', methods=['GET', 'POST'])
@admin_required
def add_attendee():
    if request.method == 'POST':
        attendee_dao.add_attendee(
            request.form['name'],
            request.form['email'],
            request.form['phone']
        )
        return redirect(url_for('list_attendees'))
    return render_template('attendees/form.html', attendee=None)

@app.route('/attendees/edit/<int:attendee_id>', methods=['GET', 'POST'])
@admin_required
def edit_attendee(attendee_id):
    attendee = attendee_dao.get_attendee_by_id(attendee_id)
    if request.method == 'POST':
        attendee_dao.update_attendee(
            attendee_id,
            request.form['name'],
            request.form['email'],
            request.form['phone']
        )
        return redirect(url_for('list_attendees'))
    return render_template('attendees/form.html', attendee=attendee)

@app.route('/attendees/delete/<int:attendee_id>', methods=['POST'])
@admin_required
def delete_attendee(attendee_id):
    attendee_dao.delete_attendee(attendee_id)
    return redirect(url_for('list_attendees'))

# tickets
@app.route('/tickets')
@login_required
def list_tickets():
    tickets = ticket_dao.get_all_tickets()
    return render_template('tickets/list.html', tickets=tickets)

@app.route('/tickets/add', methods=['GET', 'POST'])
@admin_required
def add_ticket():
    if request.method == 'POST':
        ticket_dao.add_ticket(
            request.form['event_id'],
            request.form['attendee_id'],
            request.form['ticket_type'],
            request.form['price']
        )
        return redirect(url_for('list_tickets'))
    events = event_dao.get_all_events()
    attendees = attendee_dao.get_all_attendees()
    return render_template('tickets/form.html', ticket=None, events=events, attendees=attendees)

@app.route('/tickets/edit/<int:ticket_id>', methods=['GET', 'POST'])
@admin_required
def edit_ticket(ticket_id):
    ticket = ticket_dao.get_ticket_by_id(ticket_id)
    if request.method == 'POST':
        ticket_dao.update_ticket(
            ticket_id,
            request.form['event_id'],
            request.form['attendee_id'],
            request.form['ticket_type'],
            request.form['price']
        )
        return redirect(url_for('list_tickets'))
    events = event_dao.get_all_events()
    attendees = attendee_dao.get_all_attendees()
    return render_template('tickets/form.html', ticket=ticket, events=events, attendees=attendees)

@app.route('/tickets/delete/<int:ticket_id>', methods=['POST'])
@admin_required
def delete_ticket(ticket_id):
    ticket_dao.delete_ticket(ticket_id)
    return redirect(url_for('list_tickets'))

# Prevent browser from caching pages so data is always fresh
@app.after_request
def no_cache(response):
    response.headers["Cache-Control"] = "no-store"
    return response

@app.route('/query', methods=['GET', 'POST'])
@admin_required
def query_console():
    results = None
    columns = []
    error   = None
    query   = ''

    if request.method == 'POST':
        query = request.form['query'].strip()
        try:
            db = DB.get_db()
            cursor = db.execute(query)
            results = cursor.fetchall()
            columns = [description[0] for description in cursor.description]
            db.close()
        except Exception as e:
            error = str(e)

    return render_template('query.html',
                           results=results,
                           columns=columns,
                           error=error,
                           query=query)

if __name__ == '__main__':
    DB.init_db()
    app.run(debug=True)