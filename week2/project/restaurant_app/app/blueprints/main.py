from flask import Blueprint, render_template, redirect, url_for
import os
from urllib.parse import urlparse
import psycopg2
from dotenv import load_dotenv

bp = Blueprint("main", __name__)
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

result = urlparse(DATABASE_URL)
DB_CONFIG = {
    "host": result.hostname,
    "port": result.port or 5432,
    "database": result.path[1:],
    "user": result.username,
    "password": result.password,
    "sslmode": "require"
}

def get_connection():
    return psycopg2.connect(**DB_CONFIG)

@bp.route("/")
def home():
    return redirect(url_for("main.dashboard"))

@bp.route("/dashboard")
def dashboard():
    conn = get_connection()
    cur = conn.cursor()

    # Aggregate stats
    cur.execute('SELECT COUNT(id) FROM menu_items;')
    total_items = cur.fetchone()[0] or 0

    cur.execute('SELECT COUNT(id) FROM chefs;')
    total_chefs = cur.fetchone()[0] or 0

    cur.execute('SELECT COUNT(id) FROM categories;')
    total_categories = cur.fetchone()[0] or 0

    cur.execute('SELECT COUNT(id) FROM orders;')
    total_orders = cur.fetchone()[0] or 0

    # Items per category
    cur.execute("""
        SELECT c.name, COUNT(m.id)
        FROM categories c
        LEFT JOIN menu_items m ON m.category_id = c.id
        GROUP BY c.id, c.name
        ORDER BY c.name;
    """)
    cat_counts = cur.fetchall()

    # Top 5 selling items
    cur.execute("""
        SELECT m.title, COALESCE(SUM(oi.quantity),0)
        FROM menu_items m
        LEFT JOIN order_items oi ON oi.menu_item_id = m.id
        GROUP BY m.id, m.title
        ORDER BY COALESCE(SUM(oi.quantity),0) DESC
        LIMIT 5;
    """)
    top_items = cur.fetchall()

    cur.close()
    conn.close()

    return render_template(
        "dashboard.html",
        stats={
            "items": total_items,
            "chefs": total_chefs,
            "categories": total_categories,
            "orders": total_orders
        },
        cat_counts=cat_counts,
        top_items=top_items
    )
