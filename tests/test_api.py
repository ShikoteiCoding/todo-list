import json
import pytest
import requests
import sys

# Import local package
sys.path.append("api")

from api.app import create_app, db

from api.config import Config


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///app.db"
    ELASTICSEARCH_URL = None

@pytest.fixture()
def app():
    app = create_app(TestConfig())
    db.create_all()
    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


def test_wrong_url(client):
    response = client.get("/")
    assert response.status_code == 404


def test_create_user(client):
   response = client.post(
        "/api/users",
        json={"username": "Test Username"}
   )
   assert response.status_code == 201
   #assert json.loads(response.text) == {"id": 1, "username": "Test Username"}

#
# def test_get_user(client):
#    response = client.get("/api/users/1")
#    assert response.status_code == 200
#    assert json.loads(response.data) == {"id": 1, "username": "Test Username"}
