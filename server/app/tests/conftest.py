import pytest
from flask import Flask
from typing import Generator
from flask_sqlalchemy import SQLAlchemy

from app import create_app, db


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
