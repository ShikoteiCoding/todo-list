"""
Test user routes.
"""
import json

from typing import Callable
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask.testing import FlaskClient

from app.api.users.models import User

from conftest import DEFAULT_API_ACCESS_KEY_ID, DEFAILT_API_SECRET_ACCESS_KEY


def test_user_list_200(
    client: FlaskClient, database: SQLAlchemy, add_random_user: Callable[[], User]
):
    """UserList.GET - 200"""

    _user = add_random_user()
    response = client.get(
        "/api/v1/users",
        json={
            "api_access_key_id": _user.api_access_key_id,
            "api_secret_access_key": _user.api_secret_access_key,
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
            "api_access_key_id": DEFAULT_API_ACCESS_KEY_ID,
            "api_secret_access_key": DEFAILT_API_SECRET_ACCESS_KEY,
            "username": "New_User",
        },
        content_type="application/json",
    )

    assert response.status_code == 201
    assert response.content_type == "application/json"


def test_user_list_400(client: FlaskClient, database: SQLAlchemy):
    """UserList.GET - 400"""

    response = client.get("/api/v1/users")

    assert response.status_code == 400
    assert response.content_type == "application/json"


def test_user_list_403(client: FlaskClient, database: SQLAlchemy):
    """UserList.GET - 403"""

    response = client.get(
        "/api/v1/users",
        json={
            "api_access_key_id": "users_403",
            "api_secret_access_key": "users_403",
        },
        content_type="application/json",
    )

    assert response.status_code == 403
    assert response.content_type == "application/json"


def test_user_get_200(
    client: FlaskClient, database: SQLAlchemy, add_random_user: Callable[[], User]
) -> None:
    """UserDetail.GET - 200"""

    _user = add_random_user()

    response = client.get(
        f"/api/v1/users/{_user.id}",
        json={
            "api_access_key_id": _user.api_access_key_id,
            "api_secret_access_key": _user.api_secret_access_key,
        },
        content_type="application/json",
    )

    assert response.status_code == 200
    assert response.content_type == "application/json"


def test_user_get_400(client: FlaskClient, database: SQLAlchemy) -> None:
    """UserDetail.GET - 400"""

    # _user = add_random_user()
    response = client.get(
        f"/api/v1/users",
    )

    assert response.status_code == 400
    assert response.content_type == "application/json"


def test_user_get_403(
    client: FlaskClient, database: SQLAlchemy, add_random_user: Callable[[], User]
) -> None:
    """UserDetail.GET - 403"""

    _user = add_random_user()
    response = client.get(
        "/api/v1/users/1",
        json={
            "api_access_key_id": _user.api_access_key_id,
            "api_secret_access_key": "user_403",
        },
        content_type="application/json",
    )

    assert response.status_code == 403
    assert response.content_type == "application/json"


def test_user_get_404(
    client: FlaskClient, database: SQLAlchemy, add_random_user: Callable[[], User]
) -> None:
    """UserDetail.GET - 404"""

    _user = add_random_user()
    response = client.get(
        "/api/v1/users/111",
        json={
            "api_access_key_id": _user.api_access_key_id,
            "api_secret_access_key": _user.api_secret_access_key,
        },
        content_type="application/json",
    )
    data = json.loads(response.data.decode())

    assert response.status_code == 404
    assert "user does not exist" in data["message"]
