
from menu_item import get_connection

class MenuManager:
    @classmethod
    def get_by_name(cls, name):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM menu_items WHERE item_name = %s", (name,))
        item = cur.fetchone()
        cur.close()
        conn.close()
        return item

    @classmethod
    def all_items(cls):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM menu_items")
        items = cur.fetchall()
        cur.close()
        conn.close()
        return items
