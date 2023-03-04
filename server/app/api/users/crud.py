from structlog import get_logger

from app import db
from app.api.security import generate_api_keys
from app.api.users.models import User

# TODO
# 1. Type db.models
# 2. Move exceptions away

logger = get_logger(__name__)


def get_all_users() -> list[User] | None:
    """returns all users."""

    logger.debug("get_all_users")
    users = None
    try:
        users = User.query.all()
    except Exception as e:
        logger.exception(f"Exception occured: {e}")
        logger.error("Unable to fetch all users.")
    return users


def get_user_by_id(id: int) -> User | None:
    """returns a single user."""

    logger.debug("get_user_by_id")
    user = None
    try:
        user = User.query.filter_by(id=id).first()
    except Exception as e:
        logger.exception(f"Exception occured: {e}")
        logger.error("Unable to fetch one user.")
    return user


def create_user(username: str) -> User | None:
    """creates a single user."""

    logger.debug("create_user")
    user = None
    try:
        key_id, secret_key = generate_api_keys()
        user = User(
            username=username,
            api_access_key_id=key_id,
            api_secret_access_key=secret_key,
            is_admin=False,  # can only create non admin for now
        )
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        logger.exception(f"Exception occured: {e}")
        logger.error("Unable to create one user.")
    return user
