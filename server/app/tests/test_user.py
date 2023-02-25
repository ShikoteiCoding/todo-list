"""
Test user routes.
"""
import json

from typing import Callable
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def test_user_list_200(app: Flask, database: SQLAlchemy, add_user_with_token: Callable):
    """UserList.GET"""

    _user = add_user_with_token(username="users_200", token="users_200")
    client = app.test_client()
    response = client.get(
        "/api/v1/users",
        data=json.dumps(
            {
                "username": _user.username,
                "api_key": _user.token,
            }
        ),
        content_type="application/json",
    )

    assert response.status_code == 200
    assert response.content_type == "application/json"


def test_user_list_400(app: Flask, database: SQLAlchemy):
    """UserList.GET - 400"""

    client = app.test_client()
    response = client.get("/api/v1/users")

    assert response.status_code == 400
    assert response.content_type == "application/json"


def test_user_list_403(app: Flask, database: SQLAlchemy, add_user_with_token: Callable):
    """UserList.GET - 403"""

    client = app.test_client()
    response = client.get(
        "/api/v1/users",
        data=json.dumps(
            {
                "username": "users_403",
                "api_key": "users_403",
            }
        ),
        content_type="application/json",
    )

    assert response.status_code == 403
    assert response.content_type == "application/json"


def test_user_get_200(
    app: Flask, database: SQLAlchemy, add_user_with_token: Callable
) -> None:
    """UserDetail.GET - 200"""

    _user = add_user_with_token(username="user_200", token="user_200")
    client = app.test_client()
    response = client.get(
        f"/api/v1/users/{_user.id}",
        data=json.dumps(
            {
                "username": _user.username,
                "api_key": _user.token,
            }
        ),
        content_type="application/json",
    )

    assert response.status_code == 200
    assert response.content_type == "application/json"


def test_user_get_400(
    app: Flask, database: SQLAlchemy, add_user_with_token: Callable
) -> None:
    """UserDetail.GET - 400"""

    client = app.test_client()
    response = client.get(
        f"/api/v1/users/1",
    )

    assert response.status_code == 400
    assert response.content_type == "application/json"


def test_user_get_403(
    app: Flask, database: SQLAlchemy, add_user_with_token: Callable
) -> None:
    """UserDetail.GET - 403"""

    client = app.test_client()
    response = client.get(
        f"/api/v1/users/1",
        data=json.dumps(
            {
                "username": "user_403",
                "api_key": "user_403",
            }
        ),
        content_type="application/json",
    )

    assert response.status_code == 403
    assert response.content_type == "application/json"


def test_user_get_404(
    app: Flask, database: SQLAlchemy, add_user_with_token: Callable
) -> None:
    """UserDetail.GET - 404"""

    _user = add_user_with_token(username="user_404", token="user_404")
    client = app.test_client()
    response = client.get(
        "/api/v1/users/111",
        data=json.dumps(
            {
                "username": "user_404",
                "api_key": "user_404",
            }
        ),
        content_type="application/json",
    )
    data = json.loads(response.data.decode())

    assert response.status_code == 404
    assert "user does not exist" in data["message"]
