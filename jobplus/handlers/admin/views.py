from flask import render_template, url_for
from . import bp


@bp.route('/')
def index():
    return render_template('base.html')




