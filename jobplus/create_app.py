from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_bootstrap import Bootstrap


def register_extensions(app):
    db = SQLAlchemy()
    bootstrap = Bootstrap()

    db.init_app(app)
    bootstrap.init_app(app)


def register_filters(app):
    pass


def register_blueprints(app):
    from .handlers.admin import bp as admin_blueprint
    app.register_blueprint(admin_blueprint)

    from .handlers.jobseeker import bp as jobseeker_blueprint
    app.register_blueprint(jobseeker_blueprint)

    from .handlers.company import bp as company_blueprint
    app.register_blueprint(company_blueprint)

    from .handlers.front import bp as front_blueprint
    app.register_blueprint(front_blueprint)


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config.get(config_name))

    register_extensions(app)
    register_filters(app)
    register_blueprints(app)

    return app
