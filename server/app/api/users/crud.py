from flask import jsonify, Response, request, url_for

from structlog import get_logger

from app import db
from app.api.users.models import User
from app.api.errors import bad_request

# TODO
# 1. Type db.models
# 2. Move exceptions away

logger = get_logger(__name__)


def get_all_users() -> list[User]:
    """returns all users."""

    logger.debug("get_all_users")
    users = None
    try:
        users = User.query.all()
    except Exception as e:
        logger.exception(f"Exception occured: {e}")
        logger.error("Unable to fetch all movies.")
    return users  # type: ignore


def get_user_by_id(id: int) -> User:
    """returns a single user."""

    logger.debug("get_user_by_id")
    user = None

    try:
        user = User.query.get_or_404(id)
    except Exception as e:
        logger.exception(f"Exception occured: {e}")
        logger.error("Unable to fetch all movies.")
    return user  # type: ignore


def create_user(username: str) -> User:
    """creates a single user"""

    logger.debug("create_user")
    user = None

    try:
        user = User(username=username)
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        logger.exception(f"Exception occured: {e}")
        logger.error("Unable to create a user.")
    return user


def update_user(user: User, username: str) -> User:
    """updates a single user"""
    logger.debug("update_user")

    try:
        user.username = username
        db.session.commit()
    except Exception as e:
        logger.exception(f"Exception occured: {e}")
        logger.error("Unable to update user {e}")
    return user


def delete_user(user: User) -> User | None:
    """deletes a single user"""
    logger.debug("delete_user")

    try:
        db.session.delete(user)
        db.session.commit()
    except Exception as e:
        logger.exception(f"Exception occured: {e}")
        logger.error("Unable to delete user {e}")
    return user
