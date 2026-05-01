from flask import Flask, render_template, request, redirect, url_for
import database as DB
from dao import organizer_dao, venue_dao, event_dao, attendee_dao, ticket_dao

app = Flask(__name__)

# create and seed the db on first run if it doesnt exist yet
# @app.before_request
# def setup():
#     DB.init_db()

# home
@app.route('/')
def index():
    return render_template('index.html')

# organizers
@app.route('/organizers')
def list_organizers():
    organizers = organizer_dao.get_all_organizers()
    return render_template('organizers/list.html', organizers=organizers)

@app.route('/organizers/add', methods=['GET', 'POST'])
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
def delete_organizer(organizer_id):
    organizer_dao.delete_organizer(organizer_id)
    return redirect(url_for('list_organizers'))

# venues
@app.route('/venues')
def list_venues():
    venues = venue_dao.get_all_venues()
    return render_template('venues/list.html', venues=venues)

@app.route('/venues/add', methods=['GET', 'POST'])
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
def delete_venue(venue_id):
    venue_dao.delete_venue(venue_id)
    return redirect(url_for('list_venues'))

# events
@app.route('/events')
def list_events():
    events = event_dao.get_all_events()
    return render_template('events/list.html', events=events)

@app.route('/events/add', methods=['GET', 'POST'])
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
    # need these for the dropdowns in the form
    organizers = organizer_dao.get_all_organizers()
    venues = venue_dao.get_all_venues()
    return render_template('events/form.html', event=None, organizers=organizers, venues=venues)

@app.route('/events/edit/<int:event_id>', methods=['GET', 'POST'])
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
def delete_event(event_id):
    event_dao.delete_event(event_id)
    return redirect(url_for('list_events'))


# attendees
@app.route('/attendees')
def list_attendees():
    attendees = attendee_dao.get_all_attendees()
    return render_template('attendees/list.html', attendees=attendees)

@app.route('/attendees/add', methods=['GET', 'POST'])
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
def delete_attendee(attendee_id):
    attendee_dao.delete_attendee(attendee_id)
    return redirect(url_for('list_attendees'))

# tickets
@app.route('/tickets')
def list_tickets():
    tickets = ticket_dao.get_all_tickets()
    return render_template('tickets/list.html', tickets=tickets)

@app.route('/tickets/add', methods=['GET', 'POST'])
def add_ticket():
    if request.method == 'POST':
        ticket_dao.add_ticket(
            request.form['event_id'],
            request.form['attendee_id'],
            request.form['ticket_type'],
            request.form['price']
        )
        return redirect(url_for('list_tickets'))
    # dropdowns for picking event and attendee
    events = event_dao.get_all_events()
    attendees = attendee_dao.get_all_attendees()
    return render_template('tickets/form.html', ticket=None, events=events, attendees=attendees)

@app.route('/tickets/edit/<int:ticket_id>', methods=['GET', 'POST'])
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
def delete_ticket(ticket_id):
    ticket_dao.delete_ticket(ticket_id)
    return redirect(url_for('list_tickets'))

@app.after_request
def no_cache(response):
    response.headers["Cache-Control"] = "no-store"
    return response

if __name__ == '__main__':
    DB.init_db()
    app.run(debug=True)