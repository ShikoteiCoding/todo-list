from flask import request, abort
from typing import Callable
from hmac import compare_digest
from structlog import get_logger
from marshmallow import Schema

from app.api.users.models import User
from app.api.auth.serializer import auth_serializer

from structlog import get_logger

logger = get_logger(__name__)


def is_valid(
    api_access_key_id: str, api_secret_access_key: str, is_admin: bool = False
):
    """return user if token is good"""

    logger.debug("API key verify")
    print(is_admin)
    user: User = User.query.filter_by(api_access_key_id=api_access_key_id).first()
    if (
        user
        and compare_digest(user.api_secret_access_key, api_secret_access_key)
        and (user.is_admin if is_admin else True)
    ):
        return user


def mashmallow_validate(schema: Schema = auth_serializer):
    """API verification wrapper"""

    def decorator(func: Callable):
        def wrapper(*args, **kwargs):
            try:
                json = request.get_json(silent=True)
            except Exception as e:
                logger.debug("empty json request. {e}")
                json = None

            if not json:
                abort(400, f"please provide API keys. request is empty.")

            errors = schema.validate(json)

            if errors:
                abort(400, f"please provide API keys. {errors}")

            return func(*args, **kwargs)

        return wrapper

    return decorator


def login(is_admin: bool = False):
    """API verification wrapper"""

    def decorator(func: Callable):
        def wrapper(*args, **kwargs):
            header = request.json.get("header")  # type: ignore
            api_access_key_id = header.get("API_KEY_ID")
            api_secret_access_key = header.get("API_SECRET_KEY")

            if (
                api_access_key_id
                and api_secret_access_key
                and is_valid(api_access_key_id, api_secret_access_key, is_admin)
            ):
                return func(*args, **kwargs)

            abort(403, "the provided API keys are not valid")
            # return {"message": "the provided API keys are not valid"}, 403

        return wrapper

    return decorator
