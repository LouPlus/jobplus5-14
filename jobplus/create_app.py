from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
from flask_bootstrap import Bootstrap
from flask_login import LoginManager

db = SQLAlchemy()
bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'front.login'
login_manager.login_message = '请先登录'
login_manager.login_message_category = 'info'
login_manager.refresh_view = 'front.login'
login_manager.needs_refresh_message = '需要登录验证'
login_manager.needs_refresh_message_category = 'refresh_info'


def register_extensions(app):
    db.init_app(app)
    bootstrap.init_app(app)
    login_manager.init_app(app)


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
