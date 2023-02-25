"""
Test ping route
"""
import json

from typing import Callable
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def test_ping_200(app: Flask, database: SQLAlchemy, add_user_with_token: Callable):
    """UserList.GET - 200"""

    _user = add_user_with_token("Ping_200", "Ping_200")
    client = app.test_client()
    response = client.get(
        "/api/v1/ping",
        data=json.dumps(
            {
                "username": _user.username,
                "api_key": _user.token,
            }
        ),
        content_type="application/json",
    )
    data = json.loads(response.data.decode())

    assert response.status_code == 200
    assert response.content_type == "application/json"
    assert "ping" in data["message"]


def test_ping_400(app: Flask, database: SQLAlchemy):
    """UserList.GET - 400"""

    client = app.test_client()
    response = client.get(
        "/api/v1/ping",
    )
    data = json.loads(response.data.decode())

    assert response.status_code == 400
    assert response.content_type == "application/json"


def test_ping_403(app: Flask, database: SQLAlchemy):
    """UserList.GET - 403"""

    client = app.test_client()
    response = client.get(
        "/api/v1/ping",
        data=json.dumps({"username": "Ping_403", "api_key": "Ping_403"}),
        content_type="application/json",
    )
    data = json.loads(response.data.decode())

    assert response.status_code == 403
    assert response.content_type == "application/json"
