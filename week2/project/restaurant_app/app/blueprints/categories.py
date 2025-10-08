from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..extensions import db
from ..models import Category
from ..forms.category_forms import CategoryForm

bp = Blueprint("categories", __name__)

@bp.route("/")
def index():
    q = request.args.get("q", type=str, default="").strip()
    page = request.args.get("page", type=int, default=1)

    query = db.select(Category).order_by(Category.created_at.desc())
    if q:
        like = f"%{q.lower()}%"
        query = query.filter(Category.name.ilike(like))

    pagination = db.paginate(query, page=page, per_page=6, error_out=False)
    return render_template("categories/index.html", pagination=pagination, q=q)

@bp.route("/create", methods=["GET", "POST"])
def create():
    form = CategoryForm()
    if form.validate_on_submit():
        cat = Category(name=form.name.data)
        db.session.add(cat)
        db.session.commit()
        flash("Category created", "success")
        return redirect(url_for("categories.index"))
    return render_template("categories/create.html", form=form)

@bp.route("/<int:cat_id>/edit", methods=["GET", "POST"])
def edit(cat_id):
    cat = Category.query.get_or_404(cat_id)
    form = CategoryForm(obj=cat)
    if form.validate_on_submit():
        cat.name = form.name.data
        db.session.commit()
        flash("Category updated", "success")
        return redirect(url_for("categories.index"))
    return render_template("categories/edit.html", form=form, category=cat)

@bp.route("/<int:cat_id>/delete", methods=["POST"])
def delete(cat_id):
    cat = Category.query.get_or_404(cat_id)
    db.session.delete(cat)
    db.session.commit()
    flash("Category deleted", "success")
    return redirect(url_for("categories.index"))
