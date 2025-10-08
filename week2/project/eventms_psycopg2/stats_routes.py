from flask import Blueprint, jsonify, render_template
from database.index import get_conn, put_conn

stats_bp = Blueprint('events_stats', __name__)





# web jinja templates

@stats_bp.route('/stats')
def stats_index():
    return render_template('stats.html')

@stats_bp.route('/stats/api/events-per-organizer')
def events_per_organizer():
    conn = get_conn(); cur = conn.cursor()
    cur.execute("""
        SELECT o.name, COUNT(e.id)
        FROM organizers o
        LEFT JOIN events e ON e.organizer_id=o.id
        GROUP BY o.id, o.name
        ORDER BY o.name
    """)
    rows = cur.fetchall(); cur.close(); put_conn(conn)
    labels = [r[0] for r in rows]; data = [r[1] for r in rows]
    return jsonify({'labels': labels, 'data': data})

@stats_bp.route('/stats/api/events-popularity')
def events_popularity():
    conn = get_conn(); cur = conn.cursor()
    cur.execute("""
        SELECT e.name, COUNT(t.id) as cnt
        FROM events e
        LEFT JOIN tickets t ON t.event_id=e.id
        GROUP BY e.id, e.name
        ORDER BY cnt DESC, e.name ASC
        LIMIT 10
    """)
    rows = cur.fetchall(); cur.close(); put_conn(conn)
    labels = [r[0] for r in rows]; data = [r[1] for r in rows]
    return jsonify({'labels': labels, 'data': data})

@stats_bp.route('/stats/api/attendees-over-time')
def attendees_over_time():
    conn = get_conn(); cur = conn.cursor()
    cur.execute("""
        SELECT date_trunc('month', t.created_at)::date AS m, COUNT(*) 
        FROM tickets t
        GROUP BY m
        ORDER BY m
    """)
    rows = cur.fetchall(); cur.close(); put_conn(conn)
    labels = [r[0].isoformat() for r in rows]; data = [r[1] for r in rows]
    return jsonify({'labels': labels, 'data': data})
