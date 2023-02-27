from hmac import compare_digest
from functools import wraps
from flask import request
from structlog import get_logger

from app.api.users.models import User

logger = get_logger(__name__)


def is_valid(username: str, token: str):
    """return user if token is good"""

    logger.debug("API key verify")
    user = User.query.filter_by(username=username).first()
    if user and compare_digest(user.token, token):
        return user


def api_required(func):
    """API verification wrapper"""

    @wraps(func)
    def decorator(*args, **kwargs):
        if request.json:
            api_key = request.json.get("api_key")
            username = request.json.get("username")
        else:
            return {"message": "please provide an API key"}, 400

        if username and api_key and is_valid(username, api_key):
            return func(*args, **kwargs)
        else:
            return {"message": "the provided API key is not valid"}, 403

    return decorator
