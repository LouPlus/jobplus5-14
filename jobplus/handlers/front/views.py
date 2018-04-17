from flask import Blueprint, render_template, url_for


# bp = Blueprint('front', __name__, template_folder="~/git/myproject/github/jobplus5-14/app/templates")
bp = Blueprint('front', __name__)


@bp.route('/')
def index():
    return render_template('front/index.html', active="index")


@bp.route('/login/')
def login():
    return render_template('front/login.html')


@bp.route('/logout/')
def logout():
    return render_template('front/index.html')


@bp.route('/register/')
def register():
    return render_template('front/register.html')


@bp.route('/companies/')
def companies():
    return render_template('front/companies.html', active="companies")


@bp.route('/jobs/')
def jobs():
    return render_template('front/jobs.html', active="jobs")


@bp.route('/jobseekers/')
def jobseekers():
    return render_template('front/jobseekers.html', active="jobseekers")
