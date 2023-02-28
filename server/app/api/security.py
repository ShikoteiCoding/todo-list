from hmac import compare_digest
from functools import wraps
from flask import request
from structlog import get_logger

from app.api.users.models import User

logger = get_logger(__name__)


def is_valid(api_access_key_id: str, api_secret_access_key: str):
    """return user if token is good"""

    logger.debug("API key verify")
    user = User.query.filter_by(api_access_key_id=api_access_key_id).first()
    if user and compare_digest(user.api_secret_access_key, api_secret_access_key):
        return user


# TODO
# Fix return types of decorator not compatible by flask_restx
def api_required(func):
    """API verification wrapper"""

    @wraps(func)
    def decorator(*args, **kwargs):
        if request.json:
            api_access_key_id = request.json.get("api_access_key_id")
            api_secret_access_key = request.json.get("api_secret_access_key")
        else:
            return {"message": "please provide an API keys"}, 400

        if (
            api_access_key_id
            and api_secret_access_key
            and is_valid(api_access_key_id, api_secret_access_key)
        ):
            return func(*args, **kwargs)
        else:
            return {"message": "the provided API key is not valid"}, 403

    return decorator
