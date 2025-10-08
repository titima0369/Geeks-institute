# 🍽️ Restaurant Management System (Flask + Neon PostgreSQL + Jinja2 + Tailwind + Chart.js)

A clean starter to manage **menu items, chefs, categories, and orders** with CRUD, pagination, search, and a stats dashboard.

## ▶️ Quick Start

1) **Clone / unzip** this project.

2) Create a virtual env and install deps:
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
```

3) Copy `.env.example` to `.env` and set:
```env
SECRET_KEY=change-me
DATABASE_URL=postgresql+psycopg://<user>:<password>@<neon-host>/<db>?sslmode=require
```
> In Neon console, copy the **SQLAlchemy** connection string (Python) and make sure **`sslmode=require`** is present.

4) Initialize DB schema (Flask-Migrate will auto-detect models):
```bash
export FLASK_APP=run.py  # Windows PowerShell: $env:FLASK_APP="run.py"
flask db init
flask db migrate -m "init"
flask db upgrade
```

5) (Optional) Seed sample data (drops & recreates tables):
```bash
flask seed
```

6) Run:
```bash
flask run
```
Visit: http://127.0.0.1:5000

## Features implemented
- ✅ CRUD for Items, Chefs, Categories, Orders
- ✅ Form validation (Flask-WTF + CSRF)
- ✅ Search (by title/name) + Pagination (6 per page)
- ✅ Delete confirmation
- ✅ Many-to-many: `menu_items` ↔ `chefs`
- ✅ Orders with order lines & quantity
- ✅ Dashboard with Chart.js (counts, items per category, top items)
- ✅ TailwindCSS (Play CDN) + responsive UI

## Notes
- Cascade deletes are set at the DB level using `ondelete="CASCADE"` and on relationships using `cascade="all, delete-orphan"`. For PostgreSQL this is enforced by the DB.
- For local dev without Neon, remove `DATABASE_URL` to use the SQLite fallback.

## Project structure
```text
app/
  blueprints/     # routes
  forms/          # Flask-WTF forms
  templates/      # Jinja2 templates
  static/         # JS/CSS (Tailwind via CDN)
  models.py
  extensions.py
  seeds.py
run.py
requirements.txt
```
