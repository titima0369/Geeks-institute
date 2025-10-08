import psycopg2
from menu_item import execute_query

def get_connection():
    # Update these parameters with your actual database credentials
    return psycopg2.connect(
        dbname="Restaurant_Menu",
        user="postgres",
        password="root",
        host="localhost",
        port="5432"
    )
 
class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class MenuManager:
    def __init__(self):
        self.menu_items = []

    def get_by_name(self, name):
        for item in self.menu_items:
            if item.name == name:
                return item
        return None

    @classmethod
    def all_items(cls):
        conn = get_connection()
        cur = conn.cursor()
        query = "SELECT * FROM menu_items"
        cur.execute(query)
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return [MenuItem(name=row[1], price=row[2]) for row in rows]

# Example usage:
items = MenuManager.all_items()
# display items
for item in items:
    print(f"Name: {item.name}, Price: {item.price}")
