from flask import Blueprint, render_template, request, redirect, url_for, flash
from ..extensions import db
from ..models import MenuItem, Category, Chef
from ..forms.item_forms import ItemForm, category_choices, chef_choices

bp = Blueprint("items", __name__)

@bp.route("/")
def index():
    q = request.args.get("q", type=str, default="").strip()
    page = request.args.get("page", type=int, default=1)

    query = db.select(MenuItem).order_by(MenuItem.created_at.desc())
    if q:
        like = f"%{q.lower()}%"
        query = query.filter(MenuItem.title.ilike(like))

    pagination = db.paginate(query, page=page, per_page=6, error_out=False)
    return render_template("items/index.html", pagination=pagination, q=q)

@bp.route("/create", methods=["GET", "POST"])
def create():
    form = ItemForm()
    form.category_id.choices = [("", "-- None --")] + category_choices()
    form.chef_ids.choices = chef_choices()
    if form.validate_on_submit():
        item = MenuItem(
            title=form.title.data,
            description=form.description.data,
            price=form.price.data,
            is_available=form.is_available.data,
            category_id=int(form.category_id.data) if form.category_id.data else None,
        )
        if form.chef_ids.data:
            chefs = Chef.query.filter(Chef.id.in_([int(cid) for cid in form.chef_ids.data])).all()
            item.chefs = chefs
        db.session.add(item)
        db.session.commit()
        flash("Item created successfully", "success")
        return redirect(url_for("items.index"))
    return render_template("items/create.html", form=form)

@bp.route("/<int:item_id>/edit", methods=["GET", "POST"])
def edit(item_id):
    item = MenuItem.query.get_or_404(item_id)
    form = ItemForm(obj=item)
    form.category_id.choices = [("", "-- None --")] + category_choices()
    form.chef_ids.choices = chef_choices()
    form.category_id.data = str(item.category_id) if item.category_id else ""
    form.chef_ids.data = [str(c.id) for c in item.chefs]
    if form.validate_on_submit():
        item.title = form.title.data
        item.description = form.description.data
        item.price = form.price.data
        item.is_available = form.is_available.data
        item.category_id = int(form.category_id.data) if form.category_id.data else None
        item.chefs = Chef.query.filter(Chef.id.in_([int(cid) for cid in form.chef_ids.data])).all()
        db.session.commit()
        flash("Item updated successfully", "success")
        return redirect(url_for("items.index"))
    return render_template("items/edit.html", form=form, item=item)

@bp.route("/<int:item_id>/delete", methods=["POST"])
def delete(item_id):
    item = MenuItem.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    flash("Item deleted", "success")
    return redirect(url_for("items.index"))
