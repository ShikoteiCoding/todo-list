"""
Test /users route.
"""
import json

from typing import Callable
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def test_user_list_200(app: Flask, database: SQLAlchemy, add_user_with_token: Callable):
    """UserList.GET"""

    _user = add_user_with_token(username="user_200", token="user_200")
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
                "username": "user_403",
                "api_key": "user_403",
            }
        ),
        content_type="application/json",
    )

    assert response.status_code == 403
    assert response.content_type == "application/json"
