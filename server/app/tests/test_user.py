"""
Test user routes.
"""
import json

from typing import Callable
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def test_get_users(app: Flask, database: SQLAlchemy):
    """ Test get list of users. """
    client = app.test_client()
    response = client.get("api/v1/users")

    assert response.status_code == 200
    assert response.content_type == "application/json"


def test_create_user(app:Flask, database: SQLAlchemy):
    """ Test post user. """
    client = app.test_client()
    response = client.post(
            "/api/v1/users",
            data=json.dumps({"username": "Test Username"}),
            content_type="application/json"
    )
    assert response.status_code == 201
    assert response.content_type == "application/json"

def test_get_user(app: Flask, database: SQLAlchemy, add_user: Callable):
    """ Test get one user. """
    _user = add_user("User 200")
    client = app.test_client()
    response = client.get(
        f"api/v1/users/{_user.id}",
        content_type="application/json"
    )
    data = json.loads(response.data.decode())
    assert response.status_code == 200
    assert response.content_type == "application/json"
    assert data == _user.to_dict()