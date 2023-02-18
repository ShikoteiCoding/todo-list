"""
Test user routes.
"""
import json

from typing import Callable
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def test_user_list_200(app: Flask, database: SQLAlchemy):
    """UserList.GET"""
    
    client = app.test_client()
    response = client.get("/api/v1/users")

    assert response.status_code == 200
    assert response.content_type == "application/json"


def test_user_list_201(app: Flask, database: SQLAlchemy) -> None:
    """UserList.POST"""

    client = app.test_client()
    response = client.post(
        "/api/v1/users",
        data=json.dumps({"username": "Test Username"}),
        content_type="application/json",
    )
    assert response.status_code == 201
    assert response.content_type == "application/json"


def test_user_get_200(app: Flask, database: SQLAlchemy, add_user: Callable) -> None:
    """UserDetail.GET - 200"""

    _user = add_user("User_200")
    client = app.test_client()
    response = client.get(f"/api/v1/users/{_user.id}", content_type="application/json")

    assert response.status_code == 200
    assert response.content_type == "application/json"


def test_user_get_404(app: Flask, database: SQLAlchemy) -> None:
    """UserDetail.GET - 404"""

    client = app.test_client()
    response = client.get("/api/v1/users/111", content_type="application/json")
    data = json.loads(response.data.decode())

    assert response.status_code == 404
    assert "user does not exist" in data["message"]


def test_user_put_200(app: Flask, database: SQLAlchemy, add_user: Callable) -> None:
    """UserDetail.PUT - 200"""

    _user = add_user("User_Put")
    client = app.test_client()
    response = client.get(
        f"/api/v1/users/{_user.id}",
        content_type="application/json",
        data=json.dumps({"username": "User_Put_200"}),
    )

    assert response.status_code == 200
    assert response.content_type == "application/json"


def test_user_put_404(app: Flask, database: SQLAlchemy) -> None:
    """UserDetail.PUT - 404"""

    client = app.test_client()
    response = client.get(
        "/api/v1/users/111",
        content_type="application/json",
        data=json.dumps({"username": "User_Put_200"}),
    )
    data = json.loads(response.data.decode())

    assert response.status_code == 404
    assert "user does not exist" in data["message"]


def test_user_delete_204(app: Flask, database: SQLAlchemy, add_user: Callable) -> None:
    """UserDetail.DELETE - 204"""

    _user = add_user("User_Delete")
    client = app.test_client()
    response = client.delete(f"/api/v1/users/{_user.id}")

    assert response.status_code == 204
    assert response.content_type == "application/json"


def test_user_delete_404(app: Flask, database: SQLAlchemy) -> None:
    """UserDetail.DELETE - 404"""

    client = app.test_client()
    response = client.delete(f"/api/v1/users/111")
    data = json.loads(response.data.decode())

    assert response.status_code == 404
    assert "user does not exist" in data["message"]
