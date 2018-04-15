from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config


def register_extensions(app):
    db = SQLAlchemy()
    db.init_app(app)


def register_filters(app):
    pass


def register_blueprints(app):
    from .admin import bp as admin_blueprint
    app.register_blueprint(admin_blueprint)

    from .user import bp as user_blueprint
    app.register_blueprint(user_blueprint)

    from .company import bp as company_blueprint
    app.register_blueprint(company_blueprint)

    from .front import bp as front_bp
    app.register_blueprint(front_blueprint)
    


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    register_extensions(app)
    register_filters(app)
    register_blueprints(app)

    return app
