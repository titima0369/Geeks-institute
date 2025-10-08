from flask import Blueprint, render_template, request, redirect, url_for, flash
import psycopg2
from urllib.parse import urlparse
import os
from dotenv import load_dotenv

bp = Blueprint("orders", __name__)

# Load environment
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

# ---- Routes ----

@bp.route("/")
def index():
    page = request.args.get("page", type=int, default=1)
    per_page = 6
    offset = (page - 1) * per_page

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT id, customer_name, status, created_at
        FROM orders
        ORDER BY created_at DESC
        LIMIT %s OFFSET %s
    """, (per_page, offset))
    orders = cur.fetchall()
    cur.execute("SELECT COUNT(*) FROM orders")
    total = cur.fetchone()[0]
    cur.close()
    conn.close()

    pagination = {
        "items": orders,
        "page": page,
        "per_page": per_page,
        "total": total,
        "pages": (total + per_page - 1) // per_page
    }
    return render_template("orders/index.html", pagination=pagination)

@bp.route("/create", methods=["GET", "POST"])
def create():
    from ..forms.order_forms import OrderForm, item_choices
    form = OrderForm()
    choices = [("", "-- Select --")] + item_choices()
    for line in form.lines:
        line.form.menu_item_id.choices = choices

    if form.validate_on_submit():
        conn = get_connection()
        cur = conn.cursor()
        # Insert order
        cur.execute("INSERT INTO orders (customer_name, status, created_at) VALUES (%s, %s, NOW()) RETURNING id",
                    (form.customer_name.data, "pending"))
        order_id = cur.fetchone()[0]

        for lf in form.lines.entries:
            item_id_raw = lf.form.menu_item_id.data
            qty = lf.form.quantity.data or 0
            if item_id_raw and qty and int(qty) > 0:
                cur.execute("SELECT price FROM menu_items WHERE id = %s", (int(item_id_raw),))
                price = cur.fetchone()[0]
                cur.execute("""
                    INSERT INTO order_items (order_id, menu_item_id, quantity, price_at_order)
                    VALUES (%s, %s, %s, %s)
                """, (order_id, int(item_id_raw), int(qty), price))
        conn.commit()
        cur.close()
        conn.close()
        flash("Order created", "success")
        return redirect(url_for("orders.index"))

    return render_template("orders/create.html", form=form)

@bp.route("/<int:order_id>")
def show(order_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, customer_name, status, created_at FROM orders WHERE id = %s", (order_id,))
    order = cur.fetchone()
    # get items
    cur.execute("""
        SELECT oi.id, mi.title, oi.quantity, oi.price_at_order
        FROM order_items oi
        JOIN menu_items mi ON mi.id = oi.menu_item_id
        WHERE oi.order_id = %s
    """, (order_id,))
    items = cur.fetchall()
    cur.close()
    conn.close()
    return render_template("orders/show.html", order=order, items=items)

@bp.route("/<int:order_id>/delete", methods=["POST"])
def delete(order_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM orders WHERE id = %s", (order_id,))
    conn.commit()
    cur.close()
    conn.close()
    flash("Order deleted", "success")
    return redirect(url_for("orders.index"))

@bp.route("/<int:order_id>/mark_paid", methods=["POST"])
def mark_paid(order_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE orders SET status = 'paid' WHERE id = %s", (order_id,))
    conn.commit()
    cur.close()
    conn.close()
    flash("Order marked as paid", "success")
    return redirect(url_for("orders.show", order_id=order_id))
