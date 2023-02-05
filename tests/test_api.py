import json
import pytest
import requests
import sys

from typing import Generator
from flask import Flask
from flask.testing import FlaskClient
from flask.testing import FlaskCliRunner

# Import local package
sys.path.append("api")

from api.app import create_app, db

from api.config import Config


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///app.db"
    ELASTICSEARCH_URL = None

    def to_dict(self) -> dict:
        return {
            'TESTING': self.TESTING,
            'SQLALCHEMY_DATABASE_URI': self.SQLALCHEMY_DATABASE_URI,
            'ELASTICSEARCH_URL': self.ELASTICSEARCH_URL,
        }

@pytest.fixture()
def config() -> TestConfig:
    return TestConfig()

@pytest.fixture()
def app(config: TestConfig) -> Generator[Flask, None, None]:
    app = create_app(config)
    app_context = app.app_context()
    app_context.push()
    db.create_all()

    yield app

    db.session.remove()
    db.drop_all()
    app_context.pop()

@pytest.fixture()
def test_client(app: Flask) -> FlaskClient:
    return app.test_client()

@pytest.fixture()
def client(test_client: FlaskClient, config: TestConfig) -> FlaskClient:
    test_client.environ_base |= config.to_dict()
    return test_client

@pytest.fixture()
def runner(app: Flask) -> FlaskCliRunner:
    return app.test_cli_runner()


#def test_wrong_route():
#    response = client.get("/")
#    assert response.status_code == 404


def test_create_user(app: Flask, client):
    with app.app_context():
        response = client.post(
            "/api/users",
            json={"username": "Test Username"}
        )
    #response =requests.post(
    #    "http://127.0.0.1:5000/api/users",
    #    json={"username": "Test Username"}
    #)
        assert response.status_code == 201
    #assert json.loads(response.text) == {"id": 1, "username": "Test Username"}

#
# def test_get_user(client):
#    response = client.get("/api/users/1")
#    assert response.status_code == 200
#    assert json.loads(response.data) == {"id": 1, "username": "Test Username"}
