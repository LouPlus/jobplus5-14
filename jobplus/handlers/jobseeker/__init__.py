from flask import Blueprint

bp = Blueprint('jobseeker', __name__, url_prefix='/jobseeker')


from . import views