from flask import jsonify, Response, request, url_for

from app import db
from app.api._users.models import User
from app.api.errors import bad_request


def get_all_users() -> list[User] | None:
    """Returns all users."""

    print("get_all_users")
    users = None
    try:
        users = User.query.all()
    except Exception as e:
        print(f"Unable to fetch all movies. {e}")
        pass

    return users


def get_user_by_id(id: int) -> User | None:
    """Returns a singel user."""

    print("get_user_by_id")
    user = None
    try:
        user = User.query.get_or_404(id)
    except Exception as e:
        print(f"Unable to fetch all movies. {e}")
        pass
    return print(user)  # jsonify(User.query.get_or_404(id).to_dict())


def create_user() -> Response:
    data = request.get_json() or {}
    if "username" not in data:
        return bad_request("Must include username.")
    if User.query.filter_by(username=data["username"]).first():
        return bad_request("Please use a different username.")
    user = User()
    user.from_dict(data, new_user=True)
    db.session.add(user)
    db.session.commit()
    response = jsonify(user.to_dict())
    response.status_code = 201
    response.headers["Location"] = url_for("api.get_user", id=user.id)
    return response


def update_user(id: int) -> Response:
    user = User.query.get_or_404(id)
    data = request.get_json() or {}
    if (
        "username" in data
        and data["username"] != user.username
        and User.query.filter_by(username=data["username"]).first()
    ):
        return bad_request("Please use a different username")
    user.from_dict(data, new_user=False)
    db.session.commit()
    return jsonify(user.to_dict())
