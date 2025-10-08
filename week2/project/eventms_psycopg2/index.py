import os
from flask import Flask, render_template, redirect, url_for, request, jsonify
from dotenv import load_dotenv
from database.index import init_db_pool
from auth.routes import auth_bp, login_manager, ensure_admin_seed
from events.routes import events_bp
from organizers.routes import organizers_bp
from attendees.routes import attendees_bp
from tickets.routes import tickets_bp
from stats_routes import stats_bp
from middlewares import api_middleware_global  # Global API middleware
from chat import chat_bp



load_dotenv()

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')

    # ------------------ Config ------------------
    app.config['SECRET_KEY'] = os.getenv("FLASK_SECRET_KEY")
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # ------------------ Init DB ------------------
    init_db_pool()

    # ------------------ Login Manager ------------------
    login_manager.init_app(app)
    ensure_admin_seed()  # makes sure default admin user exists with 'password'

    # ------------------ Global Middleware ------------------
    api_middleware_global(app)  # أي route يبدأ ب /api/ محمي

    # ------------------ Blueprints ------------------
    app.register_blueprint(auth_bp)
    app.register_blueprint(events_bp, url_prefix='/events')
    app.register_blueprint(organizers_bp, url_prefix='/organizers')
    app.register_blueprint(attendees_bp, url_prefix='/attendees')
    app.register_blueprint(tickets_bp, url_prefix='/tickets')
    app.register_blueprint(stats_bp)
    app.register_blueprint(chat_bp, url_prefix='/chat')

    # ------------------ Routes ------------------
    @app.route('/')
    def home():
        return redirect(url_for('events.list_events'))

    @app.route('/stats')
    def stats():
        
        return render_template('stats.html', title='Dashboard')

    # ------------------ Optional: Test API ------------------
    @app.route('/api/test', methods=['GET'])
    def api_test():
        return jsonify({"message": "API is working!"})

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
