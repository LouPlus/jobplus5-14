from flask import Blueprint, render_template, url_for


bp = Blueprint('company', __name__, url_prefix='/company')


@bp.route('/')
def index():
    return render_template('company/index.html')


@bp.route('/company_detail/')
def company_detail():
    return render_template('company/company_detail.html')


@bp.route('/joblist/')
def joblist():
    return render_template('company/joblist.html')


@bp.route('/jobdetail/')
def jobdetail():
    return render_template('company/jobdetail.html')
