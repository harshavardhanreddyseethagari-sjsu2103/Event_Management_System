INSERT INTO Organizers (name, email, phone, organization) VALUES
('Jackie Chan', 'jackie@gmail.com', '123456789', 'Kung-Fu Panda'),
('Bruce Lee', 'bruce@gmail.com', '987654321', 'Dragon Studio'),
('John Doe', 'john@gmail.com', '111222333', 'Doe Events');

-- venues
INSERT INTO Venues (name, address, city, state, capacity) VALUES
('The Grand Hall', '100 Market St', 'San Jose', 'CA', 1000),
('Sunset Pavilion', '200 Ocean Ave', 'Santa Cruz', 'CA', 500),
('Downtown Arena', '300 Main St', 'San Francisco', 'CA', 3000),
('Riverside Park', '400 River Rd', 'Sacramento', 'CA', 800),
('The Rooftop', '500 Sky Blvd', 'Oakland', 'CA', 250);

-- events (organizer_id and venue_id match the rows above)
INSERT INTO Events (title, description, event_date, organizer_id, venue_id) VALUES
('Kung-Fu Night', 'A night of martial arts demos and performances', '2026-06-10', 1, 1),
('Dragon Gala', 'Annual gala hosted by Dragon Studio', '2026-06-15', 2, 3),
('Summer Mixer', 'Casual networking event by the water', '2026-06-20', 3, 2),
('Fight Night', 'Exhibition matches and live music', '2026-07-04', 2, 4),
('Rooftop Social', 'Evening social with food and drinks', '2026-07-12', 1, 5),
('Doe Conference', 'Professional development conference', '2026-07-18', 3, 1);

-- attendees
INSERT INTO Attendees (name, email, phone) VALUES
('Alice Wang', 'alice@gmail.com', '408-111-2222'),
('Bob Smith', 'bob@gmail.com', '408-333-4444'),
('Carlos Rivera', 'carlos@gmail.com', '415-555-6666'),
('Diana Lee', 'diana@gmail.com', '510-777-8888'),
('Ethan Park', 'ethan@gmail.com', '650-999-0000'),
('Fiona Chen', 'fiona@gmail.com', '408-121-3434'),
('George Kim', 'george@gmail.com', '415-565-7878'),
('Hannah Tran', 'hannah@gmail.com', '510-909-1212');

-- tickets (event_id and attendee_id match rows above)
INSERT INTO Tickets (event_id, attendee_id, ticket_type, price) VALUES
(1, 1, 'General', 30.00),
(1, 2, 'VIP', 75.00),
(2, 3, 'General', 50.00),
(2, 4, 'VIP', 120.00),
(3, 5, 'General', 25.00),
(3, 6, 'General', 25.00),
(4, 7, 'VIP', 90.00),
(4, 8, 'General', 40.00),
(5, 1, 'General', 20.00),
(5, 3, 'VIP', 60.00),
(6, 2, 'General', 35.00),
(6, 5, 'VIP', 80.00);