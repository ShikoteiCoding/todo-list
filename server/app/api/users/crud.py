from structlog import get_logger

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
