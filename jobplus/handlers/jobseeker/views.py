from flask import render_template, url_for
from . import bp

@bp.route('/edit')
def edit():
    return render_template('jobseeker/edit.html')


@bp.route('/mydeliver')
def mydeliver():
    return render_template('jobseeker/mydeliver.html')


@bp.route('/myresume')
def myresume():
    return render_template('jobseeker/myresume.html')
