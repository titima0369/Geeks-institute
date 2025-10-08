from helpers import *
# events/routes.py
from flask import Blueprint, render_template, request, redirect, url_for, flash
# أو أي imports آخرين اللي تستعملهم هنا
events_bp = Blueprint('events', __name__, template_folder='../templates/events')

tickets_bp = Blueprint('tickets', __name__, template_folder='../templates/tickets')

@tickets_bp.route('/register', methods=['GET','POST'])
@login_required
def register_ticket():
    conn = get_conn(); cur = conn.cursor()
    if request.method == 'POST':
        event_id = request.form.get('event_id'); attendee_id = request.form.get('attendee_id')
        try:
            cur.execute("INSERT INTO tickets (event_id, attendee_id) VALUES (%s,%s)", (event_id, attendee_id))
            conn.commit(); flash('Registration added.', 'success')
            return redirect(url_for('events.details', event_id=event_id))
        except Exception as e:
            conn.rollback(); flash('Registration failed: '+str(e), 'error')
        finally:
            cur.close(); put_conn(conn)
    # GET: show simple form
    cur = get_conn().cursor()
    conn2 = get_conn()
    cur1 = conn.cursor(); cur2 = conn2.cursor()
    cur1.execute("SELECT id, name FROM events ORDER BY date ASC")
    events = cur1.fetchall()
    cur2.execute("SELECT id, name FROM attendees ORDER BY name ASC")
    attendees = cur2.fetchall()
    cur1.close(); put_conn(conn)
    cur2.close(); put_conn(conn2)
    return render_template('tickets/create.html', events=events, attendees=attendees, title='Register Ticket')

@tickets_bp.route('/<int:ticket_id>/delete', methods=['POST'])
@login_required
def delete_ticket(ticket_id):
    conn = get_conn(); cur = conn.cursor()
    # need event_id to redirect back
    cur.execute("SELECT event_id FROM tickets WHERE id=%s", (ticket_id,))
    row = cur.fetchone()
    if not row:
        flash('Ticket not found.', 'error')
        cur.close(); put_conn(conn)
        return redirect(url_for('events.list_events'))
    event_id = row[0]
    try:
        cur.execute("DELETE FROM tickets WHERE id=%s", (ticket_id,))
        conn.commit(); flash('Registration removed.', 'success')
    except Exception as e:
        conn.rollback(); flash('Delete failed: '+str(e), 'error')
    finally:
        cur.close(); put_conn(conn)
    return redirect(url_for('events.details', event_id=event_id))


# ----------------- API routes -----------------

# List all tickets
@tickets_bp.route('/api/tickets', methods=['GET'])
@api_middleware
def api_list_tickets():
    conn = get_conn(); cur = conn.cursor()
    cur.execute("""
        SELECT t.id, e.name AS event_name, a.name AS attendee_name, t.created_at
        FROM tickets t
        JOIN events e ON t.event_id=e.id
        JOIN attendees a ON t.attendee_id=a.id
        ORDER BY t.created_at DESC
    """)
    rows = cur.fetchall(); cur.close(); put_conn(conn)
    tickets = [{"id": r[0], "event_name": r[1], "attendee_name": r[2], "created_at": r[3].isoformat()} for r in rows]
    return jsonify({"tickets": tickets})

# Get ticket by id
@tickets_bp.route('/api/tickets/<int:ticket_id>', methods=['GET'])
@api_middleware
def api_get_ticket(ticket_id):
    conn = get_conn(); cur = conn.cursor()
    cur.execute("""
        SELECT t.id, e.name AS event_name, a.name AS attendee_name, t.created_at
        FROM tickets t
        JOIN events e ON t.event_id=e.id
        JOIN attendees a ON t.attendee_id=a.id
        WHERE t.id=%s
    """, (ticket_id,))
    row = cur.fetchone(); cur.close(); put_conn(conn)
    if row:
        return jsonify({"id": row[0], "event_name": row[1], "attendee_name": row[2], "created_at": row[3].isoformat()})
    return jsonify({"error": "Ticket not found"}), 404

# Create ticket
@tickets_bp.route('/api/tickets', methods=['POST'])
@api_middleware
def api_create_ticket():
    data = request.get_json()
    event_id = data.get("event_id")
    attendee_id = data.get("attendee_id")

    if not (event_id and attendee_id):
        return jsonify({"error": "event_id and attendee_id are required"}), 400

    conn = get_conn(); cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO tickets (event_id, attendee_id) VALUES (%s, %s) RETURNING id",
            (event_id, attendee_id)
        )
        ticket_id = cur.fetchone()[0]
        conn.commit()
        return jsonify({"id": ticket_id}), 201
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        cur.close(); put_conn(conn)

# Delete ticket
@tickets_bp.route('/api/tickets/<int:ticket_id>', methods=['DELETE'])
@api_middleware
def api_delete_ticket(ticket_id):
    conn = get_conn(); cur = conn.cursor()
    try:
        cur.execute("DELETE FROM tickets WHERE id=%s", (ticket_id,))
        conn.commit()
        return jsonify({"success": True}), 204
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        cur.close(); put_conn(conn)
