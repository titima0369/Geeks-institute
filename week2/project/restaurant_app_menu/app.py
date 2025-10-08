import os
import psycopg2
from flask import Flask, render_template, request, redirect, url_for
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

def get_db_connection():
    try:
        conn = psycopg2.connect(os.getenv("DATABASE_URL"))
        print("Database connection established.")
    except psycopg2.Error as e:
        print(f"Error connecting to database: {e}")
        return None
    return psycopg2.connect(os.getenv("DATABASE_URL"))

# ---------------- Routes ---------------- #

@app.route("/")
def index():
    return redirect(url_for("menu"))
@app.route("/menu")
def menu():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, item_name, item_price FROM menu_items ORDER BY id;")
    items = cur.fetchall()
    cur.close()
    conn.close()
    return render_template("menu.html", items=items)

@app.route("/add", methods=["GET", "POST"])
def add_item():
    if request.method == "POST":
        name = request.form["name"]
        price = request.form["price"]
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO menu_items (item_name, item_price) VALUES (%s, %s)", (name, price))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for("menu"))
    return render_template("add_item.html")

@app.route("/delete/<int:item_id>")
def delete_item(item_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM menu_items WHERE id=%s", (item_id,))
    conn.commit()
    cur.close()
    conn.close()
    return redirect(url_for("menu"))

@app.route("/update/<int:item_id>", methods=["GET", "POST"])
def update_item(item_id):
    conn = get_db_connection()
    cur = conn.cursor()
    if request.method == "POST":
        name = request.form["name"]
        price = request.form["price"]
        cur.execute("UPDATE menu_items SET item_name=%s, item_price=%s WHERE id=%s",
                    (name, price, item_id))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for("menu"))
    cur.execute("SELECT id, item_name, item_price FROM menu_items WHERE id=%s", (item_id,))
    item = cur.fetchone()
    cur.close()
    conn.close()
    return render_template("update_item.html", item=item)

if __name__ == "__main__":
    app.run(debug=True)
