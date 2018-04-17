from flask import Blueprint, render_template, url_for


bp = Blueprint('jobseeker', __name__, url_prefix='/jobseeker')


@bp.route('/')
def index():
    return render_template('jobseeker/index.html')


@bp.route('/mydeliver/')
def mydeliver():
    return render_template('jobseeker/mydeliver.html')


@bp.route('/myresume/')
def myresume():
    return render_template('jobseeker/myresume.html')
