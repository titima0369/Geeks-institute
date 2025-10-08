import psycopg2

def get_connection():
    try:
        return psycopg2.connect(
            dbname="restaurant_menu",
            user="postgres",
            password="root",
            host="localhost",
            port="5432"
        )
    except Exception as e:
        print("Error connecting to the database:", e)
        return None

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def save(self):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO menu_items (item_name, item_price) VALUES (%s, %s)",
                    (self.name, self.price))
        conn.commit()
        cur.close()
        conn.close()
        print(f"{self.name} added successfully!")

    def delete(self):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM menu_items WHERE item_name = %s", (self.name,))
        if cur.rowcount > 0:
            print(f"{self.name} deleted successfully!")
        else:
            print("Item not found")
        conn.commit()
        cur.close()
        conn.close()

    def update(self, new_name, new_price):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("UPDATE menu_items SET item_name=%s, item_price=%s WHERE item_name=%s",
                    (new_name, new_price, self.name))
        if cur.rowcount > 0:
            print(f"Updated {self.name} → {new_name} ({new_price} MAD)")
        else:
            print("Item not found")
        conn.commit()
        cur.close()
        conn.close()
