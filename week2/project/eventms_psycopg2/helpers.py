def paginate_params(request, per_page=6):
    try:
        page = int(request.args.get('page', '1'))
        if page < 1:
            page = 1
    except ValueError:
        page = 1
    offset = (page - 1) * per_page
    return page, per_page, offset


# imports.py
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required
from database.index import get_conn, put_conn
from helpers import paginate_params
# from forms import EventForm
from middlewares import api_middleware
