"""
Test note routes.
"""
import json

from typing import Callable
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def test_note_list_200(app: Flask, database: SQLAlchemy, add_user: Callable):
    """NoteList.GET - 200"""

    _user = add_user(username="users_200", token="users_200")
    client = app.test_client()
    response = client.get(
        f"api/v1/users/{_user.id}/notes",
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


def test_note_list_400(app: Flask, database: SQLAlchemy, add_user: Callable):
    """NoteList.GET - 400"""

    _user = add_user(username="users_400", token="users_400")
    client = app.test_client()
    response = client.get(f"api/v1/users/{_user.id}/notes")

    assert response.status_code == 400
    assert response.content_type == "application/json"


def test_note_post_201(app: Flask, database: SQLAlchemy, add_user: Callable) -> None:
    """NoteDetail.POST - 201"""

    _user = add_user(username="user_201", token="user_201")
    client = app.test_client()
    response = client.post(
        f"api/v1/users/{_user.id}/notes",
        data=json.dumps(
            {
                "username": _user.username,
                "api_key": _user.token,
                "title": "note_201",
                "content": "note_201",
            }
        ),
        content_type="application/json",
    )

    assert response.status_code == 201
    assert response.content_type == "application/json"
