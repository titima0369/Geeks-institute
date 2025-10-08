from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from database.index import get_conn, put_conn
from middlewares import api_middleware

auth_bp = Blueprint('auth', __name__, template_folder='../templates/auth')
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

class User(UserMixin):
    def __init__(self, id, username, email, password_hash):
        self.id = str(id)
        self.username = username
        self.email = email
        self.password_hash = password_hash

@login_manager.user_loader
def load_user(user_id):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, username, email, password_hash FROM users WHERE id=%s", (user_id,))
    row = cur.fetchone()
    cur.close(); put_conn(conn)
    if row:
        return User(*row)
    return None

def ensure_admin_seed():
    conn = get_conn(); cur = conn.cursor()
    cur.execute("SELECT id FROM users WHERE username=%s", ('admin',))
    if not cur.fetchone():
        cur.execute(
            "INSERT INTO users (username, email, password_hash) VALUES (%s,%s,%s)",
            ('admin', 'admin@example.com', generate_password_hash('password'))
        )
        conn.commit()
    cur.close(); put_conn(conn)

# ----------------- Web routes -----------------
@auth_bp.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username'); password = request.form.get('password')
        conn = get_conn(); cur = conn.cursor()
        cur.execute("SELECT id, username, email, password_hash FROM users WHERE username=%s", (username,))
        row = cur.fetchone(); cur.close(); put_conn(conn)
        if row and check_password_hash(row[3], password):
            user = User(*row)
            login_user(user)
            flash('Logged in successfully.', 'success')
            return redirect(url_for('events.list_events'))
        flash('Invalid credentials.', 'error')
    return render_template('auth/login.html', title='Login')

@auth_bp.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username'); email = request.form.get('email'); password = request.form.get('password')
        if not username or not email or not password:
            flash('All fields are required.', 'error')
            return render_template('auth/register.html', title='Register')
        conn = get_conn(); cur = conn.cursor()
        try:
            cur.execute(
                "INSERT INTO users (username, email, password_hash) VALUES (%s,%s,%s) RETURNING id",
                (username, email, generate_password_hash(password))
            )
            conn.commit()
            flash('Account created. Please login.', 'success')
            return redirect(url_for('auth.login'))
        except Exception as e:
            conn.rollback(); flash('Registration failed: ' + str(e), 'error')
        finally:
            cur.close(); put_conn(conn)
    return render_template('auth/register.html', title='Register')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out.', 'success')
    return redirect(url_for('auth.login'))

# ----------------- API routes -----------------
@auth_bp.route('/api/users', methods=['GET'])
@api_middleware
def api_list_users():
    conn = get_conn(); cur = conn.cursor()
    cur.execute("SELECT id, username, email FROM users ORDER BY id ASC")
    rows = cur.fetchall(); cur.close(); put_conn(conn)
    users = [{"id": r[0], "username": r[1], "email": r[2]} for r in rows]
    return jsonify({"users": users})

@auth_bp.route('/api/users', methods=['POST'])
@api_middleware
def api_create_user():
    data = request.get_json()
    username = data.get("username"); email = data.get("email"); password = data.get("password")
    if not username or not email or not password:
        return jsonify({"error": "Missing fields"}), 400
    conn = get_conn(); cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO users (username, email, password_hash) VALUES (%s,%s,%s) RETURNING id",
            (username, email, generate_password_hash(password))
        )
        user_id = cur.fetchone()[0]; conn.commit()
        return jsonify({"id": user_id, "username": username, "email": email}), 201
    except Exception as e:
        conn.rollback(); return jsonify({"error": str(e)}), 400
    finally:
        cur.close(); put_conn(conn)
@auth_bp.route('/api/users/<int:user_id>', methods=['GET'])
@api_middleware
def api_get_user(user_id):
    conn = get_conn(); cur = conn.cursor()
    cur.execute("SELECT id, username, email FROM users WHERE id=%s", (user_id,))
    user = cur.fetchone(); cur.close(); put_conn(conn)
    if user:
        return jsonify({"id": user[0], "username": user[1], "email": user[2]})
    return jsonify({"error": "User not found"}), 404
