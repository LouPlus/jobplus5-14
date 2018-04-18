from functools import wraps
from flask import abort
from flask_login import current_user
from .models import User


def Role_required(role):
    def decorator(func):
        @wraps(func)
        def decorated_function(*args, **kwargs):
            if not current_user.is_authenticated or current_user.role < role:
                abort(403)  # 403表示权限错误
            return func(*args, **kwargs)
        return decorated_function
    return decorator


def admin_required(func):
    return Role_required(User.ROLE_ADMIN)(func)
