# EventMS (Flask + PostgreSQL with psycopg2)

Complete Event Management System with authentication, CRUD, pagination, search, and analytics dashboard.

## Quick start

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Create DB (PostgreSQL)
createdb eventms

# Load schema + seed data
psql $DATABASE_URL -f database/seed/index.sql
# or: psql -d eventms -U postgres -h localhost -f database/seed/index.sql

# Configure env
cp .env.example .env
# edit DATABASE_URL if needed

# Run
python index.py  # app at http://127.0.0.1:5000
# Login: username=admin, password=password
```

## Project structure
```
.
├── index.py
├── auth/
│   └── routes.py
├── events/
│   └── routes.py
├── organizers/
│   └── routes.py
├── attendees/
│   └── routes.py
├── tickets/
│   └── routes.py
├── stats_routes.py
├── helpers.py
├── database/
│   ├── index.py
│   └── seed/
│       └── index.sql
├── templates/
│   ├── base.html
│   ├── stats.html
│   ├── auth/...
│   ├── events/...
│   ├── organizers/...
│   └── attendees/...
├── static/
├── requirements.txt
└── .env.example
```

## Database schema (tables)

- **users**: app users for authentication  
  - `id`, `username` (unique), `email` (unique), `password_hash`, `created_at`
- **organizers**: event organizers  
  - `id`, `name`, `contact_info`
- **events**: events managed by the platform  
  - `id`, `name`, `date`, `location`, `description`, `organizer_id → organizers.id (CASCADE)`
- **attendees**: people who can register to events  
  - `id`, `name`, `email` (unique), `phone`
- **tickets**: registrations linking attendees to events (many-to-many)  
  - `id`, `event_id → events.id (CASCADE)`, `attendee_id → attendees.id (CASCADE)`, `created_at`, `UNIQUE(event_id, attendee_id)`
- **comments** (optional): attendees comments on events  
  - `id`, `event_id`, `attendee_id`, `content`, `created_at`

## Features

- Auth: register, login, logout (Flask-Login + psycopg2)
- CRUD for events, organizers, attendees
- Registrations via tickets (create/delete)
- Pagination (6 per page) and search (events by name)
- Flash messages and validation checks
- TailwindCSS for responsive UI
- Chart.js dashboard with 3 analytics

## Notes

- All DB access uses parameterized **psycopg2** queries.
- Adjust `DATABASE_URL` in `.env` if your Postgres differs.
- Seed creates demo data and default login: `admin/password`.
