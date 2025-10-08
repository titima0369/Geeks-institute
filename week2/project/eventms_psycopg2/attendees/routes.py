from helpers import *

attendees_bp = Blueprint('attendees', __name__, template_folder='../templates/attendees')

@attendees_bp.route('/')
def list_attendees():
    page, per_page, offset = paginate_params(request, per_page=6)
    conn = get_conn(); cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM attendees")
    total = cur.fetchone()[0]
    cur.execute("""
        SELECT id, name, email, phone
        FROM attendees
        ORDER BY name ASC
        LIMIT %s OFFSET %s
    """, (per_page, offset))
    rows = cur.fetchall(); cur.close(); put_conn(conn)
    return render_template('attendees/index.html', attendees=rows, page=page, per_page=per_page, total=total, title='Attendees')

@attendees_bp.route('/create', methods=['GET','POST'])
@login_required
def create_attendee():
    if request.method == 'POST':
        name = request.form.get('name'); email = request.form.get('email'); phone = request.form.get('phone')
        if not (name and email):
            flash('Name and email are required.', 'error')
            return redirect(url_for('attendees.create_attendee'))
        conn = get_conn(); cur = conn.cursor()
        try:
            cur.execute("INSERT INTO attendees (name, email, phone) VALUES (%s,%s,%s)", (name, email, phone))
            conn.commit(); flash('Attendee created.', 'success')
            return redirect(url_for('attendees.list_attendees'))
        except Exception as e:
            conn.rollback(); flash('Create failed: '+str(e), 'error')
        finally:
            cur.close(); put_conn(conn)
    return render_template('attendees/create.html', title='Create Attendee')

@attendees_bp.route('/<int:attendee_id>/edit', methods=['GET','POST'])
@login_required
def edit_attendee(attendee_id):
    conn = get_conn(); cur = conn.cursor()
    if request.method == 'POST':
        name = request.form.get('name'); email = request.form.get('email'); phone = request.form.get('phone')
        try:
            cur.execute("UPDATE attendees SET name=%s, email=%s, phone=%s WHERE id=%s", (name, email, phone, attendee_id))
            conn.commit(); flash('Attendee updated.', 'success')
            return redirect(url_for('attendees.list_attendees'))
        except Exception as e:
            conn.rollback(); flash('Update failed: '+str(e), 'error')
        finally:
            cur.close(); put_conn(conn)
    else:
        cur.execute("SELECT id, name, email, phone FROM attendees WHERE id=%s", (attendee_id,))
        row = cur.fetchone(); cur.close(); put_conn(conn)
        if not row:
            flash('Attendee not found.', 'error')
            return redirect(url_for('attendees.list_attendees'))
        return render_template('attendees/edit.html', attendee=row, title='Edit Attendee')

@attendees_bp.route('/<int:attendee_id>/delete', methods=['POST'])
@login_required
def delete_attendee(attendee_id):
    conn = get_conn(); cur = conn.cursor()
    try:
        cur.execute("DELETE FROM attendees WHERE id=%s", (attendee_id,))
        conn.commit(); flash('Attendee deleted.', 'success')
    except Exception as e:
        conn.rollback(); flash('Delete failed: '+str(e), 'error')
    finally:
        cur.close(); put_conn(conn)
    return redirect(url_for('attendees.list_attendees'))



# ----------------- API routes -----------------

# List attendees
@attendees_bp.route('/api/attendees', methods=['GET'])
@api_middleware
def api_list_attendees():
    conn = get_conn(); cur = conn.cursor()
    cur.execute("SELECT id, name, email, phone FROM attendees ORDER BY name")
    rows = cur.fetchall(); cur.close(); put_conn(conn)
    attendees = [{"id": r[0], "name": r[1], "email": r[2], "phone": r[3]} for r in rows]
    return jsonify({"attendees": attendees})

# Get attendee by id
@attendees_bp.route('/api/attendees/<int:attendee_id>', methods=['GET'])
@api_middleware
def api_get_attendee(attendee_id):
    conn = get_conn(); cur = conn.cursor()
    cur.execute("SELECT id, name, email, phone FROM attendees WHERE id=%s", (attendee_id,))
    row = cur.fetchone(); cur.close(); put_conn(conn)
    if row:
        return jsonify({"id": row[0], "name": row[1], "email": row[2], "phone": row[3]})
    return jsonify({"error": "Attendee not found"}), 404

# Create attendee
@attendees_bp.route('/api/attendees', methods=['POST'])
@api_middleware
def api_create_attendee():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    phone = data.get("phone", "")

    if not (name and email):
        return jsonify({"error": "Name and email are required"}), 400

    conn = get_conn(); cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO attendees (name, email, phone) VALUES (%s, %s, %s) RETURNING id",
            (name, email, phone)
        )
        attendee_id = cur.fetchone()[0]
        conn.commit()
        return jsonify({"id": attendee_id}), 201
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        cur.close(); put_conn(conn)

# Update attendee
@attendees_bp.route('/api/attendees/<int:attendee_id>', methods=['PUT'])
@api_middleware
def api_update_attendee(attendee_id):
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    phone = data.get("phone", "")

    if not (name and email):
        return jsonify({"error": "Name and email are required"}), 400

    conn = get_conn(); cur = conn.cursor()
    try:
        cur.execute(
            "UPDATE attendees SET name=%s, email=%s, phone=%s WHERE id=%s",
            (name, email, phone, attendee_id)
        )
        conn.commit()
        return jsonify({"success": True}), 204
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        cur.close(); put_conn(conn)

# Delete attendee
@attendees_bp.route('/api/attendees/<int:attendee_id>', methods=['DELETE'])
@api_middleware
def api_delete_attendee(attendee_id):
    conn = get_conn(); cur = conn.cursor()
    try:
        cur.execute("DELETE FROM attendees WHERE id=%s", (attendee_id,))
        conn.commit()
        return jsonify({"success": True}), 204
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        cur.close(); put_conn(conn)