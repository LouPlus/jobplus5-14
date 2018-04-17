from flask import Blueprint, render_template, url_for

bp = Blueprint('admin', __name__, url_prefix='/admin')


@bp.route('/')
def index():
    return render_template('base.html')



