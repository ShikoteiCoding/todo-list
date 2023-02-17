from flask import jsonify, Response, request, url_for

from app import db
from app.api._users.models import User
from app.api.errors import bad_request

# TODO
# 1. Logging
# 2. Type db.models
# 3. Move exceptions away


def get_all_users() -> list[User]:
    """returns all users."""

    print("get_all_users")
    users = None
    try:
        users = User.query.all()
    except Exception as e:
        print(f"Unable to fetch all movies. {e}")
    return users  # type: ignore


def get_user_by_id(id: int) -> User:
    """returns a single user."""

    print("get_user_by_id")
    user = None

    try:
        user = User.query.get_or_404(id)
    except Exception as e:
        print(f"Unable to fetch all movies. {e}")
    return user  # type: ignore


def create_user(username: str) -> User:
    """creates a single user"""

    print("create_user")
    user = None

    try:
        user = User(username=username)
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        print(f"Unable to create a user. {e}")
    return user


def update_user(user: User, username: str) -> User:
    """updates a single user"""
    print("update_user")

    try:
        user.username = username
        db.session.commit()
    except Exception as e:
        print(f"Unable to update user {e}")
    return user


def delete_user(user: User) -> User | None:
    """deletes a single user"""
    print("delete_user")

    try:
        db.session.delete(user)
        db.session.commit()
    except Exception as e:
        print(f"Unable to delete user {e}")
    return user
