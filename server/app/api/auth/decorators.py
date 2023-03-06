from flask import request
from typing import Callable
from hmac import compare_digest
from structlog import get_logger

from app.api.users.models import User

from structlog import get_logger

logger = get_logger(__name__)


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


def api_required(is_admin: bool = False):
    """API verification wrapper"""

    def decorator(func: Callable):
        def wrapper(*args, **kwargs):
            try:
                json = request.get_json(silent=True)
            except Exception as e:
                json = None
                logger.debug(f"json not provided: {e}")

            if json:
                header = json.get("header")
                api_access_key_id = header.get("API-KEY-ID")
                api_secret_access_key = header.get("API-SECRET-KEY")
            else:
                return {"message": "please provide API keys"}, 400

            if (
                api_access_key_id
                and api_secret_access_key
                and is_valid(api_access_key_id, api_secret_access_key, is_admin)
            ):
                return func(*args, **kwargs)
            else:
                return {"message": "the provided API keys are not valid"}, 403

        return wrapper

    return decorator
