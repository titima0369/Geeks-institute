import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

conn = psycopg2.connect(os.getenv("DATABASE_URL"))
cur = conn.cursor()

# Create table
cur.execute("""
CREATE TABLE IF NOT EXISTS menu_items (
    id SERIAL PRIMARY KEY,
    item_name VARCHAR(100) NOT NULL,
    item_price NUMERIC(10,2) NOT NULL
)
""")

# Seed data
cur.execute("SELECT COUNT(*) FROM menu_items;")
if cur.fetchone()[0] == 0:
    cur.execute("""
    INSERT INTO menu_items (item_name, item_price) VALUES
        ('Burger', 35.00),
        ('Pizza', 40.00),
        ('Pasta', 45.00)
    """)
    print("Seeded menu_items with sample data.")

conn.commit()
cur.close()
conn.close()
print("Database initialized successfully!")
