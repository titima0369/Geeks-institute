from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..extensions import db
from ..models import Chef
from ..forms.chef_forms import ChefForm

bp = Blueprint("chefs", __name__)

@bp.route("/")
def index():
    q = request.args.get("q", type=str, default="").strip()
    page = request.args.get("page", type=int, default=1)

    query = db.select(Chef).order_by(Chef.created_at.desc())
    if q:
        like = f"%{q.lower()}%"
        query = query.filter(Chef.name.ilike(like))

    pagination = db.paginate(query, page=page, per_page=6, error_out=False)
    return render_template("chefs/index.html", pagination=pagination, q=q)

@bp.route("/create", methods=["GET", "POST"])
def create():
    form = ChefForm()
    if form.validate_on_submit():
        chef = Chef(name=form.name.data, bio=form.bio.data)
        db.session.add(chef)
        db.session.commit()
        flash("Chef created", "success")
        return redirect(url_for("chefs.index"))
    return render_template("chefs/create.html", form=form)

@bp.route("/<int:chef_id>/edit", methods=["GET", "POST"])
def edit(chef_id):
    chef = Chef.query.get_or_404(chef_id)
    form = ChefForm(obj=chef)
    if form.validate_on_submit():
        chef.name = form.name.data
        chef.bio = form.bio.data
        db.session.commit()
        flash("Chef updated", "success")
        return redirect(url_for("chefs.index"))
    return render_template("chefs/edit.html", form=form, chef=chef)

@bp.route("/<int:chef_id>/delete", methods=["POST"])
def delete(chef_id):
    chef = Chef.query.get_or_404(chef_id)
    db.session.delete(chef)
    db.session.commit()
    flash("Chef deleted", "success")
    return redirect(url_for("chefs.index"))
