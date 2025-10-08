import random
from decimal import Decimal
from .extensions import db
from .models import Category, Chef, MenuItem, Order, OrderItem

CATEGORIES = ["Pizzas", "Burgers", "Pasta", "Salads", "Desserts"]
CHEFS = [
    "Youssef Amrani","Salma Benali","Hicham Lahlou","Zineb El Idrissi","Khalid Bensaid",
    "Nadia Kabbaj","Omar Chentouf","Sara Laaroussi","Anas El Fassi","Meryem Berrada",
]
ITEMS = [
    ("Pizza Margherita", "Classic tomato, mozzarella, basil", Decimal("45.00"), "Pizzas"),
    ("Pizza Pepperoni", "Spicy pepperoni, cheese", Decimal("55.00"), "Pizzas"),
    ("Veggie Burger", "Grilled veggies, sauce", Decimal("35.00"), "Burgers"),
    ("Beef Burger", "Beef patty, cheddar", Decimal("40.00"), "Burgers"),
    ("Chicken Alfredo", "Creamy pasta", Decimal("60.00"), "Pasta"),
    ("Spaghetti Bolognese", "Rich ragu", Decimal("58.00"), "Pasta"),
    ("Greek Salad", "Feta, olives", Decimal("30.00"), "Salads"),
    ("Caesar Salad", "Romaine, parmesan", Decimal("32.00"), "Salads"),
    ("Chocolate Cake", "Dark chocolate", Decimal("28.00"), "Desserts"),
    ("Cheesecake", "Creamy New York style", Decimal("30.00"), "Desserts"),
]

def run_seeds(app):
    with app.app_context():
        db.drop_all()
        db.create_all()

        # Categories
        cats = {}
        for name in CATEGORIES:
            c = Category(name=name)
            db.session.add(c)
            cats[name] = c
        db.session.commit()

        # Chefs
        chefs = []
        for name in CHEFS:
            ch = Chef(name=name, bio="")
            db.session.add(ch)
            chefs.append(ch)
        db.session.commit()

        # Items
        items = []
        for title, desc, price, cat_name in ITEMS:
            it = MenuItem(
                title=title, description=desc, price=price, category=cats[cat_name], is_available=True
            )
            # assign 1-3 random chefs
            it.chefs = random.sample(chefs, k=random.randint(1,3))
            db.session.add(it)
            items.append(it)
        db.session.commit()

        # Random orders
        for _ in range(8):
            o = Order(customer_name=random.choice(["Brahim","Ali","Oumaima","Hajar","Yassine","Khadija"]))
            db.session.add(o)
            db.session.flush()
            for _ in range(random.randint(1,4)):
                mi = random.choice(items)
                q = random.randint(1,3)
                db.session.add(OrderItem(order_id=o.id, menu_item_id=mi.id, quantity=q, price_at_order=mi.price))
            db.session.commit()
