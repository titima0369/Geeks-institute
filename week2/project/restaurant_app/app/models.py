from datetime import datetime
from .extensions import db

# Association table for MenuItem <-> Chef (many-to-many)
menu_item_chefs = db.Table(
    "menu_item_chefs",
    db.Column("menu_item_id", db.Integer, db.ForeignKey("menu_items.id", ondelete="CASCADE"), primary_key=True),
    db.Column("chef_id", db.Integer, db.ForeignKey("chefs.id", ondelete="CASCADE"), primary_key=True),
)

class Category(db.Model):
    __tablename__ = "categories"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    items = db.relationship(
        "MenuItem",
        back_populates="category",
        cascade="all, delete-orphan"
    )

class Chef(db.Model):
    __tablename__ = "chefs"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    bio = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    items = db.relationship(
        "MenuItem",
        secondary=menu_item_chefs,
        back_populates="chefs",
        passive_deletes=True
    )
#relation between menu items and categories is many to one
class MenuItem(db.Model):
    __tablename__ = "menu_items"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False, index=True)
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Numeric(10,2), nullable=False, default=0)
    is_available = db.Column(db.Boolean, default=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)

    category_id = db.Column(db.Integer, db.ForeignKey("categories.id", ondelete="SET NULL"), nullable=True)
    category = db.relationship("Category", back_populates="items")

    chefs = db.relationship(
        "Chef",
        secondary=menu_item_chefs,
        back_populates="items",
        passive_deletes=True
    )

    order_items = db.relationship("OrderItem", back_populates="menu_item", cascade="all, delete-orphan")
#relation between orders and menu items is one to many
class Order(db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(120), nullable=False)
    status = db.Column(db.String(20), default="pending")  # pending, paid, cancelled
    created_at = db.Column(db.DateTime, default=datetime.utcnow, index=True)

    items = db.relationship("OrderItem", back_populates="order", cascade="all, delete-orphan")
#relation between orders and menu items is one to many
class OrderItem(db.Model):
    __tablename__ = "order_items"
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("orders.id", ondelete="CASCADE"), nullable=False, index=True)
    menu_item_id = db.Column(db.Integer, db.ForeignKey("menu_items.id", ondelete="CASCADE"), nullable=False, index=True)
    quantity = db.Column(db.Integer, nullable=False, default=1)
    price_at_order = db.Column(db.Numeric(10,2), nullable=False)  # snapshot of price

    order = db.relationship("Order", back_populates="items")
    menu_item = db.relationship("MenuItem", back_populates="order_items")
