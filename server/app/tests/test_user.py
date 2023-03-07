"""
Test user routes.
"""
import json

from typing import Callable
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask.testing import FlaskClient

from app.api.users.models import User

from conftest import DEFAULT_API_ACCESS_KEY_ID, DEFAULT_API_SECRET_ACCESS_KEY

from utils import error_message, header_from_user


def test_user_list_200(
    client: FlaskClient, database: SQLAlchemy, add_random_user: Callable[[], User]
):
    """UserList.GET - 200"""

    response = client.get(
        "/api/v1/users",
        json={
            "header": {
                "API_KEY_ID": DEFAULT_API_ACCESS_KEY_ID,
                "API_SECRET_KEY": DEFAULT_API_SECRET_ACCESS_KEY,
            }
        },
        content_type="application/json",
    )

    assert response.status_code == 200
    assert response.content_type == "application/json"


def test_user_list_201(
    client: FlaskClient, database: SQLAlchemy, add_random_user: Callable[[], User]
):
    """UserList.POST - 201"""

    response = client.post(
        "/api/v1/users",
        json={
            "header": {
                "API_KEY_ID": DEFAULT_API_ACCESS_KEY_ID,
                "API_SECRET_KEY": DEFAULT_API_SECRET_ACCESS_KEY,
            },
            "username": "New_User",
        },
        content_type="application/json",
    )

    assert response.status_code == 201
    assert response.content_type == "application/json"


def test_user_list_400(client: FlaskClient, database: SQLAlchemy):
    """UserList.GET - 400"""

    response = client.get("/api/v1/users")
    data = json.loads(response.data.decode())

    print(data)

    assert response.status_code == 400
    assert response.content_type == "application/json"
    assert error_message(400) in data["message"]


def test_user_list_403(client: FlaskClient, database: SQLAlchemy):
    """UserList.GET - 403"""

    response = client.get(
        "/api/v1/users",
        json={"header": {"API_KEY_ID": "users_403", "API_SECRET_KEY": "users_403"}},
        content_type="application/json",
    )
    data = json.loads(response.data.decode())

    assert response.status_code == 403
    assert response.content_type == "application/json"
    assert error_message(403) in data["message"]


def test_user_get_200(
    client: FlaskClient, database: SQLAlchemy, add_random_user: Callable[[], User]
) -> None:
    """UserDetail.GET - 200"""

    _user = add_random_user()

    response = client.get(
        f"/api/v1/users/{_user.id}",
        json=header_from_user(_user),
        content_type="application/json",
    )

    assert response.status_code == 200
    assert response.content_type == "application/json"


def test_user_get_400(client: FlaskClient, database: SQLAlchemy) -> None:
    """UserDetail.GET - 400"""

    response = client.get(
        f"/api/v1/users",
    )
    data = json.loads(response.data.decode())

    assert response.status_code == 400
    assert response.content_type == "application/json"
    assert error_message(400, "user") in data["message"]


def test_user_get_403(
    client: FlaskClient, database: SQLAlchemy, add_random_user: Callable[[], User]
) -> None:
    """UserDetail.GET - 403"""

    _user = add_random_user()
    response = client.get(
        "/api/v1/users/1",
        json={
            "header": {
                "API_KEY_ID": _user.api_access_key_id,
                "API_SECRET_KEY": "user_403",
            }
        },
        content_type="application/json",
    )
    data = json.loads(response.data.decode())

    assert response.status_code == 403
    assert response.content_type == "application/json"
    assert error_message(403) in data["message"]


def test_user_get_404(
    client: FlaskClient, database: SQLAlchemy, add_random_user: Callable[[], User]
) -> None:
    """UserDetail.GET - 404"""

    _user = add_random_user()
    response = client.get(
        "/api/v1/users/111",
        json=header_from_user(_user),
        content_type="application/json",
    )
    data = json.loads(response.data.decode())

    assert response.status_code == 404
    assert response.content_type == "application/json"
    assert error_message(404, "user") in data["message"]


def test_user_put_200(
    client: FlaskClient, database: SQLAlchemy, add_random_user: Callable[[], User]
) -> None:
    """UserDetail.PUT - 200"""

    _user = add_random_user()
    response = client.put(
        f"api/v1/users/{_user.id}",
        json={
            **header_from_user(_user),
            "username": "User_Put_200",
        },
        content_type="application/json",
    )

    assert response.status_code == 200
    assert response.content_type == "application/json"
