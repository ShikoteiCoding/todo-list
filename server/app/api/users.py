from flask import jsonify, Response, request, url_for

from app import db
from app.api import bp
from app.models import User
from app.api.errors import bad_request

import json


@bp.route("/users/<int:id>", methods=["GET"])
def get_user(id: int) -> Response:
    return jsonify(User.query.get_or_404(id).to_dict())


@bp.route("/users", methods=["GET"])
def get_users() -> Response:
    page = request.args.get("page", 1, type=int)
    per_page = min(request.args.get("per_page", 10, type=int), 100)
    data = User.to_collection_dict(User.query, page, per_page, "api.get_users")
    return jsonify(data)


@bp.route("/users", methods=["POST"])
def create_user() -> Response:
    print("Received")
    data = request.get_json() or {}
    if "username" not in data:
        return bad_request("Must include username.")
    print(f"JSON is a dict {data}, {type(data)}")
    #print(User.query)
    if (User
        .query
        .filter_by(username=data["username"])
        .first()
    ):
        return bad_request("Please use a different username.")
    print("JSON is valid")
    user = User()
    user.from_dict(data, new_user=True)
    db.session.add(user)
    db.session.commit()
    response = jsonify(user.to_dict())
    response.status_code = 201
    response.headers["Location"] = url_for("api.get_user", id=user.id)
    return response


@bp.route("/users/<int:id>", methods=["PUT"])
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


@bp.route("/users/<int:id>/notes", methods=["GET"])  # type: ignore
def get_notes(id: int):
    pass


@bp.route("/users/<int:id>/notes", methods=["GET"])  # type: ignore
def get_note(user_id: int, note_id: int):
    pass
