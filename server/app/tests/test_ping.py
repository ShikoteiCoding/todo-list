"""
Test ping route
"""
import json

from typing import Callable
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask.testing import FlaskClient

from app.api.users.models import User

from utils import error_message, header_from_user


def test_ping_200(
    client: FlaskClient, database: SQLAlchemy, add_random_user: Callable[[], User]
):
    """Ping.GET - 200"""

    _user = add_random_user()
    response = client.get(
        "/api/v1/ping",
        json=header_from_user(_user),
        content_type="application/json",
    )
    data = json.loads(response.data.decode())

    assert response.status_code == 200
    assert response.content_type == "application/json"
    assert "ping" in data["message"]


def test_ping_400(client: FlaskClient, database: SQLAlchemy):
    """Ping.GET - 400"""

    response = client.get(
        "/api/v1/ping",
    )
    data = json.loads(response.data.decode())

    assert response.status_code == 400
    assert response.content_type == "application/json"
    assert error_message(400) in data["message"]


def test_ping_403(client: FlaskClient, database: SQLAlchemy):
    """Ping.GET - 403"""

    response = client.get(
        "/api/v1/ping",
        json={
            "header": {
                "API-KEY-ID": "ping_403",
                "API-SECRET-KEY": "ping_403",
            }
        },
        content_type="application/json",
    )
    data = json.loads(response.data.decode())

    assert response.status_code == 403
    assert response.content_type == "application/json"
    assert error_message(403) in data["message"]
