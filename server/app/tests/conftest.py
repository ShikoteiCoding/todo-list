import pytest
from flask import Flask
from typing import Generator
from flask_sqlalchemy import SQLAlchemy

from app import create_app, db
from app.api.users.models import User


@pytest.fixture(scope="module")
def app() -> Generator[Flask, None, None]:
    """Fixture for app in testing mode."""

    app = create_app()
    app.config.from_object("app.config.TestConfig")
    with app.app_context():
        yield app


@pytest.fixture(scope="module")
def database() -> Generator[SQLAlchemy, None, None]:
    """Fixture for the database in testing mode."""
    db.create_all()
    yield db
    db.session.remove()
    db.drop_all()


@pytest.fixture(scope="module")
def add_user():
    def _add_user(username: str) -> User:
        user = User(username=username)
        db.session.add(user)
        db.session.commit()
        return user

    return _add_user


@pytest.fixture(scope="module")
def add_user_with_token():
    def _add_user(username: str, token: str) -> User:
        user = User(username=username, token=token)
        db.session.add(user)
        db.session.commit()
        return user

    return _add_user
