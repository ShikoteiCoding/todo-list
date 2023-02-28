import pytest

from flask import Flask
from typing import Generator
from flask_sqlalchemy import SQLAlchemy
from typing import Callable
from flask.testing import FlaskClient

from app import create_app, db
from app.api.users.models import User
from app.api.notes.models import Note

from utils import random_string


@pytest.fixture(scope="module")
def app() -> Generator[Flask, None, None]:
    """fixture for app context"""

    app = create_app()
    app.config.from_object("app.config.TestConfig")
    with app.app_context():
        yield app


@pytest.fixture(scope="module")
def client(app: Flask) -> FlaskClient:
    return app.test_client()


@pytest.fixture(scope="module")
def database() -> Generator[SQLAlchemy, None, None]:
    """fixture for the database init"""

    db.create_all()
    yield db
    db.session.remove()
    db.drop_all()


@pytest.fixture(scope="module")
def add_user() -> Callable[[str, str], User]:
    """fixture to create a user"""

    def _add_user(api_access_key_id: str, api_secret_access_key: str) -> User:
        user = User(
            api_access_key_id=api_access_key_id,
            api_secret_access_key=api_secret_access_key,
        )
        db.session.add(user)
        db.session.commit()
        return user

    return _add_user


@pytest.fixture(scope="module")
def add_random_user() -> Callable[[], User]:
    """fixture to create a user"""

    def _add_user() -> User:
        user = User(
            username=random_string(),
            api_access_key_id=random_string(),
            api_secret_access_key=random_string(),
        )
        db.session.add(user)
        db.session.commit()
        return user

    return _add_user


@pytest.fixture(scope="module")
def add_note() -> Callable[[int, str, str], Note]:
    """fixture to create a note"""

    def _add_note(user_id: int, title: str, content: str) -> Note:
        note = Note(title=title, content=content, user_id=user_id)
        db.session.add(note)
        db.session.commit()
        return note

    return _add_note
