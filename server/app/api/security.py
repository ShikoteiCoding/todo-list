import secrets

from hmac import compare_digest, digest
from functools import wraps
from typing import Callable
from flask import request
from structlog import get_logger

from app.api.users.models import User

logger = get_logger(__name__)

# TODO
# Control the size of tokens in characters and bytes
# Currently it's not optimized in the database
# Can lead to errors if oversized strings are generated


def generate_api_keys() -> tuple[str, str]:
    api_access_key_id = secrets.token_urlsafe(16)
    api_secret_access_key = secrets.token_hex(16)
    return api_access_key_id, api_secret_access_key


def is_valid(
    api_access_key_id: str, api_secret_access_key: str, is_admin: bool = False
):
    """return user if token is good"""

    logger.debug("API key verify")
    user: User = User.query.filter_by(api_access_key_id=api_access_key_id).first()
    if (
        user
        and compare_digest(user.api_secret_access_key, api_secret_access_key)
        and (user.is_admin if is_admin else True)
    ):
        return user


# TODO
# Fix return types of decorator not compatible by flask_restx
def api_required(is_admin: bool = False):
    """API verification wrapper"""

    def decorator(func: Callable):
        def wrapper(*args, **kwargs):
            if request.json:
                api_access_key_id = request.json.get("api_access_key_id")
                api_secret_access_key = request.json.get("api_secret_access_key")
            else:
                return {"message": "please provide an API keys"}, 400

            if (
                api_access_key_id
                and api_secret_access_key
                and is_valid(api_access_key_id, api_secret_access_key, is_admin)
            ):
                return func(*args, **kwargs)
            else:
                return {"message": "the provided API key is not valid"}, 403

        return wrapper

    return decorator
