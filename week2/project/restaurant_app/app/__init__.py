import os
from flask import Flask
from flask_migrate import Migrate
from .extensions import db
from .models import *  # noqa

def create_app():
    app = Flask(__name__, template_folder="templates", static_folder="static")

    # Config
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "dev-secret")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
        "DATABASE_URL",
        "sqlite:///app.db"  # local fallback
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    Migrate(app, db)

    # Blueprints
    from .blueprints.items import bp as items_bp
    from .blueprints.chefs import bp as chefs_bp
    from .blueprints.categories import bp as categories_bp
    from .blueprints.orders import bp as orders_bp
    from .blueprints.main import bp as main_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(items_bp, url_prefix="/items")
    app.register_blueprint(chefs_bp, url_prefix="/chefs")
    app.register_blueprint(categories_bp, url_prefix="/categories")
    app.register_blueprint(orders_bp, url_prefix="/orders")

    # CLI: seed data
    @app.cli.command("seed")
    def seed_command():
        from .seeds import run_seeds
        run_seeds(app)
        print("✓ Seed complete.")

    return app
