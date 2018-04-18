import os
from jobplus.create_app import create_app
from flask import render_template, g
from flask_login import current_user

app = create_app(os.getenv('FLASK_CONFIG') or 'default')


@app.errorhandler(404)
def page_not_found():
    return render_template('404.html'), 404


@app.before_request
def before_request():
    g.user = current_user


if __name__ == '__main__':
    app.run()
