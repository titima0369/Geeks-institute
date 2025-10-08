-- Drop existing (dev only)
DROP TABLE IF EXISTS tickets CASCADE;
DROP TABLE IF EXISTS comments CASCADE;
DROP TABLE IF EXISTS events CASCADE;
DROP TABLE IF EXISTS organizers CASCADE;
DROP TABLE IF EXISTS attendees CASCADE;
DROP TABLE IF EXISTS users CASCADE;

-- Users (for auth)
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  username VARCHAR(50) UNIQUE NOT NULL,
  email VARCHAR(120) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Organizers
CREATE TABLE organizers (
  id SERIAL PRIMARY KEY,
  name VARCHAR(120) NOT NULL,
  contact_info TEXT
);

-- Events
CREATE TABLE events (
  id SERIAL PRIMARY KEY,
  name VARCHAR(180) NOT NULL,
  date DATE NOT NULL,
  location VARCHAR(180) NOT NULL,
  description TEXT,
  organizer_id INT NOT NULL REFERENCES organizers(id) ON DELETE CASCADE
);
CREATE INDEX idx_events_name ON events (name);
CREATE INDEX idx_events_date ON events (date);

-- Attendees
CREATE TABLE attendees (
  id SERIAL PRIMARY KEY,
  name VARCHAR(120) NOT NULL,
  email VARCHAR(180) UNIQUE NOT NULL,
  phone VARCHAR(40)
);

-- Tickets (registrations) many-to-many
CREATE TABLE tickets (
  id SERIAL PRIMARY KEY,
  event_id INT NOT NULL REFERENCES events(id) ON DELETE CASCADE,
  attendee_id INT NOT NULL REFERENCES attendees(id) ON DELETE CASCADE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UNIQUE(event_id, attendee_id)
);

-- (Optional) Comments - handy for future bonus
CREATE TABLE comments (
  id SERIAL PRIMARY KEY,
  event_id INT NOT NULL REFERENCES events(id) ON DELETE CASCADE,
  attendee_id INT NOT NULL REFERENCES attendees(id) ON DELETE CASCADE,
  content TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Seed organizers
INSERT INTO organizers (name, contact_info) VALUES
('Alpha Events', 'alpha@example.com'),
('Beta Productions', 'beta@example.com'),
('Gamma Group', 'gamma@example.com'),
('Delta Org', 'delta@example.com'),
('Epsilon Entertainment', 'epsi@example.com'),
('Zeta House', 'zeta@example.com'),
('Eta Events', 'eta@example.com'),
('Theta Team', 'theta@example.com'),
('Iota Innovations', 'iota@example.com'),
('Kappa Krew', 'kappa@example.com');

-- Seed events (10+)
INSERT INTO events (name, date, location, description, organizer_id) VALUES
('Tech Meetup', '2025-09-10', 'Marrakech', 'Monthly tech community meetup.', 1),
('Data Conference', '2025-10-01', 'Casablanca', 'Data & AI conference.', 2),
('Startup Pitch', '2025-09-20', 'Rabat', 'Startup pitch night.', 3),
('Music Fest', '2025-11-05', 'Agadir', 'Outdoor music festival.', 4),
('Design Workshop', '2025-09-15', 'Fes', 'UI/UX best practices.', 5),
('Cybersec Day', '2025-10-12', 'Tangier', 'Security talks.', 6),
('Cloud Summit', '2025-12-01', 'Casablanca', 'Cloud & DevOps.', 7),
('Hackathon', '2025-09-25', 'Marrakech', '48h hackathon.', 8),
('Marketing Expo', '2025-10-18', 'Rabat', 'Marketing trends.', 9),
('Gaming Con', '2025-11-12', 'Casablanca', 'Gaming convention.', 10);

-- Seed attendees (15+)
INSERT INTO attendees (name, email, phone) VALUES
('Amina', 'amina@example.com', '0611111111'),
('Youssef', 'youssef@example.com', '0622222222'),
('Sara', 'sara@example.com', '0633333333'),
('Omar', 'omar@example.com', '0644444444'),
('Salma', 'salma@example.com', '0655555555'),
('Hajar', 'hajar@example.com', '0666666666'),
('Hamza', 'hamza@example.com', '0677777777'),
('Ikram', 'ikram@example.com', '0688888888'),
('Rachid', 'rachid@example.com', '0699999999'),
('Khadija', 'khadija@example.com', '0610101010'),
('Nadia', 'nadia@example.com', '0610202020'),
('Zineb', 'zineb@example.com', '0610303030'),
('Ismail', 'ismail@example.com', '0610404040'),
('Anas', 'anas@example.com', '0610505050'),
('Marwa', 'marwa@example.com', '0610606060');

-- Seed tickets
INSERT INTO tickets (event_id, attendee_id) VALUES
(1,1),(1,2),(1,3),(1,4),
(2,1),(2,5),(2,6),
(3,2),(3,7),
(4,8),(4,9),(4,10),
(5,11),(5,12),
(6,13),
(7,14),(7,15),
(8,1),(8,3),
(9,4),(9,5),
(10,6),(10,7),(10,8);

-- Sample users (password: password)
INSERT INTO users (username, email, password_hash) VALUES
('admin', 'admin@example.com', '$pbkdf2-sha256$600000$gH2Xxq2gqOk9vL3n1m6F3Q$Go8Hc9gH6qZP1Yw7x5oFDv2wMZQx9h5m3p5cYQzRkqY'), -- placeholder, will be overwritten on first run
('user', 'user@example.com', '$pbkdf2-sha256$600000$gH2Xxq2gqOk9vL3n1m6F3Q$Go8Hc9gH6qZP1Yw7x5oFDv2wMZQx9h5m3p5cYQzRkqY');


CREATE TABLE api_keys (
    id SERIAL PRIMARY KEY,
    key_value TEXT NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT NOW()
);

INSERT INTO api_keys (key_value) VALUES ('123456');  


SELECT * FROM events;
