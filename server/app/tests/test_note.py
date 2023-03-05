"""
Test note routes.
"""
import json

from typing import Callable
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask.testing import FlaskClient

from app.api.users.models import User
from utils import error_message, header_from_user


def test_note_list_200(
    client: FlaskClient, database: SQLAlchemy, add_random_user: Callable[[], User]
):
    """NoteList.GET - 200"""

    _user = add_random_user()

    response = client.get(
        f"api/v1/users/{_user.id}/notes",
        json=header_from_user(_user),
        content_type="application/json",
    )

    assert response.status_code == 200
    assert response.content_type == "application/json"


def test_note_list_400(
    client: FlaskClient, database: SQLAlchemy, add_random_user: Callable[[], User]
):
    """NoteList.GET - 400"""

    _user = add_random_user()

    response = client.get(f"api/v1/users/{_user.id}/notes")
    data = json.loads(response.data.decode())

    assert response.status_code == 400
    assert response.content_type == "application/json"
    assert error_message(400) in data["message"]


def test_note_list_201(
    client: FlaskClient, database: SQLAlchemy, add_random_user: Callable[[], User]
) -> None:
    """NoteList.POST - 201"""

    _user = add_random_user()

    response = client.post(
        f"api/v1/users/{_user.id}/notes",
        json={
            **header_from_user(_user),
            "title": "note_201",
            "content": "note_201",
        },
        content_type="application/json",
    )

    assert response.status_code == 201
    assert response.content_type == "application/json"


def test_note_get_200(
    client: FlaskClient,
    database: SQLAlchemy,
    add_random_user: Callable[[], User],
    add_note: Callable,
) -> None:
    """NoteDetail.GET - 200"""

    _user = add_random_user()
    _note = add_note(_user.id, title="note_200", content="note_200")

    response = client.get(
        f"api/v1/users/{_user.id}/notes/{_note.id}",
        json=header_from_user(_user),
        content_type="application/json",
    )

    assert response.status_code == 200
    assert response.content_type == "application/json"


def test_note_get_404(
    client: FlaskClient, database: SQLAlchemy, add_random_user: Callable[[], User]
) -> None:
    """NoteDetail.GET - 404"""

    _user = add_random_user()

    response = client.get(
        f"api/v1/users/{_user.id}/notes/111",
        json=header_from_user(_user),
        content_type="application/json",
    )
    data = json.loads(response.data.decode())

    assert response.status_code == 404
    assert response.content_type == "application/json"
    assert error_message(404, "note") in data["message"]


def test_note_put_200(
    client: FlaskClient,
    database: SQLAlchemy,
    add_random_user: Callable[[], User],
    add_note: Callable,
) -> None:
    """NoteDetail.PUT - 200"""

    _user = add_random_user()
    _note = add_note(_user.id, title="Note_200", content="note_200")

    response = client.put(
        f"api/v1/users/{_user.id}/notes/{_note.id}",
        json=header_from_user(_user),
        content_type="application/json",
    )

    assert response.status_code == 200
    assert response.content_type == "application/json"


def test_note_put_404(
    client: FlaskClient, database: SQLAlchemy, add_random_user: Callable[[], User]
) -> None:
    """NoteDetail.PUT - 404"""

    _user = add_random_user()

    response = client.put(
        f"api/v1/users/{_user.id}/notes/111",
        json={
            **header_from_user(_user),
            "title": "note_400",
        },
        content_type="application/json",
    )
    data = json.loads(response.data.decode())

    assert response.status_code == 404
    assert response.content_type == "application/json"
    assert error_message(404, "note") in data["message"]


def test_note_delete_200(
    client: FlaskClient,
    database: SQLAlchemy,
    add_random_user: Callable[[], User],
    add_note: Callable,
) -> None:
    """NoteDetail.DELETE - 200"""

    _user = add_random_user()
    _note = add_note(_user.id, title="note_200", content="note_200")

    response = client.delete(
        f"api/v1/users/{_user.id}/notes/{_note.id}",
        json=header_from_user(_user),
        content_type="application/json",
    )

    assert response.status_code == 200
    assert response.content_type == "application/json"


def test_note_delete_404(
    client: FlaskClient,
    database: SQLAlchemy,
    add_random_user: Callable[[], User],
    add_note: Callable,
) -> None:
    """NoteDetail.DELETE - 404"""

    _user = add_random_user()

    response = client.delete(
        f"api/v1/users/{_user.id}/notes/111",
        json=header_from_user(_user),
        content_type="application/json",
    )
    data = json.loads(response.data.decode())

    assert response.status_code == 404
    assert response.content_type == "application/json"
    assert error_message(404, "note") in data["message"]
