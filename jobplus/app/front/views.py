from flask import Blueprint, render_template


# bp = Blueprint('front', __name__, template_folder="~/git/myproject/github/jobplus5-14/app/templates")
bp = Blueprint('front', __name__)


@bp.route('/')
def index():
    return render_template('front/index.html')
