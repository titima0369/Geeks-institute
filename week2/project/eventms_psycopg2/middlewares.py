from functools import wraps
from flask import request, jsonify
from database.index import get_conn, put_conn

def api_middleware(f):
    """
    Middleware decorator to protect API routes.
    Checks the X-API-KEY header against database.
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        # 1️⃣ Check if header exists
        api_key = request.headers.get('X-API-KEY')
        if not api_key:
            return jsonify({"error": "Unauthorized"}), 401

        # 2️⃣ Verify API key in database
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("SELECT id FROM api_keys WHERE key_value=%s", (api_key,))
        result = cur.fetchone()
        cur.close(); put_conn(conn)

        # 3️⃣ If key invalid → return 401
        if not result:
            return jsonify({"error": "Unauthorized"}), 401

        # 4️⃣ Key valid → proceed to the route
        return f(*args, **kwargs)

    return decorated

# -------------------------
# Optional: Global middleware for all /api/* routes
# -------------------------
def api_middleware_global(app):
    """
    Attach this function in create_app to protect all routes starting with /api/
    """
    @app.before_request
    def check_api_key_global():
        if request.path.startswith('/api/'):
            api_key = request.headers.get('X-API-KEY')
            if not api_key:
                return jsonify({"error": "Unauthorized"}), 401

            conn = get_conn()
            cur = conn.cursor()
            cur.execute("SELECT id FROM api_keys WHERE key_value=%s", (api_key,))
            result = cur.fetchone()
            cur.close(); put_conn(conn)

            if not result:
                return jsonify({"error": "Unauthorized"}), 401
