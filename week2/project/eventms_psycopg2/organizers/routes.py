from helpers import *

organizers_bp = Blueprint('organizers', __name__, template_folder='../templates/organizers')

@organizers_bp.route('/')
def list_organizers():
    page, per_page, offset = paginate_params(request, per_page=6)
    conn = get_conn(); cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM organizers")
    total = cur.fetchone()[0]
    cur.execute("""
        SELECT id, name, contact_info
        FROM organizers
        ORDER BY name ASC
        LIMIT %s OFFSET %s
    """, (per_page, offset))
    rows = cur.fetchall(); cur.close(); put_conn(conn)
    return render_template('organizers/index.html', organizers=rows, page=page, per_page=per_page, total=total, title='Organizers')

@organizers_bp.route('/create', methods=['GET','POST'])
@login_required
def create_organizer():
    if request.method == 'POST':
        name = request.form.get('name'); contact_info = request.form.get('contact_info')
        if not name:
            flash('Name is required.', 'error')
            return redirect(url_for('organizers.create_organizer'))
        conn = get_conn(); cur = conn.cursor()
        try:
            cur.execute("INSERT INTO organizers (name, contact_info) VALUES (%s,%s)", (name, contact_info))
            conn.commit(); flash('Organizer created.', 'success')
            return redirect(url_for('organizers.list_organizers'))
        except Exception as e:
            conn.rollback(); flash('Create failed: '+str(e), 'error')
        finally:
            cur.close(); put_conn(conn)
    return render_template('organizers/create.html', title='Create Organizer')

@organizers_bp.route('/<int:org_id>/edit', methods=['GET','POST'])
@login_required
def edit_organizer(org_id):
    conn = get_conn(); cur = conn.cursor()
    if request.method == 'POST':
        name = request.form.get('name'); contact_info = request.form.get('contact_info')
        try:
            cur.execute("UPDATE organizers SET name=%s, contact_info=%s WHERE id=%s", (name, contact_info, org_id))
            conn.commit(); flash('Organizer updated.', 'success')
            return redirect(url_for('organizers.list_organizers'))
        except Exception as e:
            conn.rollback(); flash('Update failed: '+str(e), 'error')
        finally:
            cur.close(); put_conn(conn)
    else:
        cur.execute("SELECT id, name, contact_info FROM organizers WHERE id=%s", (org_id,))
        org = cur.fetchone(); cur.close(); put_conn(conn)
        if not org:
            flash('Organizer not found.', 'error')
            return redirect(url_for('organizers.list_organizers'))
        return render_template('organizers/edit.html', organizer=org, title='Edit Organizer')

@organizers_bp.route('/<int:org_id>/delete', methods=['POST'])
@login_required
def delete_organizer(org_id):
    conn = get_conn(); cur = conn.cursor()
    try:
        cur.execute("DELETE FROM organizers WHERE id=%s", (org_id,))
        conn.commit(); flash('Organizer deleted.', 'success')
        
    except Exception as e:
        conn.rollback(); flash('Delete failed: '+str(e), 'error')
    finally:
        cur.close(); put_conn(conn)
    return redirect(url_for('organizers.list_organizers'))





# ----------------- API routes -----------------

# List organizers
@organizers_bp.route('/api/organizers', methods=['GET'])
@api_middleware
def api_list_organizers():
    conn = get_conn(); cur = conn.cursor()
    cur.execute("SELECT id, name, contact_info FROM organizers ORDER BY name")
    rows = cur.fetchall(); cur.close(); put_conn(conn)
    organizers = [{"id": r[0], "name": r[1], "contact_info": r[2]} for r in rows]
    return jsonify({"organizers": organizers})

# Get organizer by id
@organizers_bp.route('/api/organizers/<int:organizer_id>', methods=['GET'])
@api_middleware
def api_get_organizer(organizer_id):
    conn = get_conn(); cur = conn.cursor()
    cur.execute("SELECT id, name, contact_info FROM organizers WHERE id=%s", (organizer_id,))
    org = cur.fetchone(); cur.close(); put_conn(conn)
    if org:
        return jsonify({"id": org[0], "name": org[1], "contact_info": org[2]})
    return jsonify({"error": "Organizer not found"}), 404

# Create organizer
@organizers_bp.route('/api/organizers', methods=['POST'])
@api_middleware
def api_create_organizer():
    data = request.get_json()
    name = data.get("name")
    contact_info = data.get("contact_info", "")
    if not name:
        return jsonify({"error": "Name is required"}), 400

    conn = get_conn(); cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO organizers (name, contact_info) VALUES (%s, %s) RETURNING id",
            (name, contact_info)
        )
        org_id = cur.fetchone()[0]
        conn.commit()
        return jsonify({"id": org_id}), 201
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        cur.close(); put_conn(conn)

# Update organizer
@organizers_bp.route('/api/organizers/<int:organizer_id>', methods=['PUT'])
@api_middleware
def api_update_organizer(organizer_id):
    data = request.get_json()
    name = data.get("name")
    contact_info = data.get("contact_info", "")

    if not name:
        return jsonify({"error": "Name is required"}), 400

    conn = get_conn(); cur = conn.cursor()
    try:
        cur.execute(
            "UPDATE organizers SET name=%s, contact_info=%s WHERE id=%s",
            (name, contact_info, organizer_id)
        )
        conn.commit()
        return jsonify({"success": True}), 204
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        cur.close(); put_conn(conn)

# Delete organizer
@organizers_bp.route('/api/organizers/<int:organizer_id>', methods=['DELETE'])
@api_middleware
def api_delete_organizer(organizer_id):
    conn = get_conn(); cur = conn.cursor()
    try:
        cur.execute("DELETE FROM organizers WHERE id=%s", (organizer_id,))
        conn.commit()
        return jsonify({"success": True}), 204
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        cur.close(); put_conn(conn)