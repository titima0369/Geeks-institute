import psycopg2

def get_connection():
    conn = psycopg2.connect(
        dbname="Restaurant_Menu",
        user="postgres",
        password="root",
        host="localhost",
        port="5432"
    )
    return conn

def execute_query(query, params=None):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(query, params)
        conn.commit()
    finally:
        cur.close()
        conn.close()

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def save(self):
        query = "INSERT INTO menu_items (item_name, item_price) VALUES (%s, %s)"
        execute_query(query, (self.name, self.price))
        
    def delete(self):
        query = "DELETE FROM menu_items WHERE item_name = %s"
        execute_query(query, (self.name,))
        
    def update(self, new_name, new_price):
        query = "UPDATE menu_items SET item_name = %s, item_price = %s WHERE item_name = %s"
        execute_query(query, (new_name, new_price, self.name))
