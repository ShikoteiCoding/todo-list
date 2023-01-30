import json
import pytest
import requests
import sys

# Import local package
sys.path.append("api")

from api.app import create_app

from api.config import Config


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///tests/app.db"

@pytest.fixture()
def app():
    app = create_app(TestConfig())
    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


# @pytest.fixture
# def client():
#    app = create_app(TestConfig())
#    app_context = app.app_context()
#    app_context.push()
#    yield client
def test_empty_db(client):
    response = client.get("/")
    assert response.status_code == 404


# def test_create_user(client):
#    response = requests.post(
#        "http://127.0.0.1:5000/api/users",
#        json=json.dumps({"username": "Test Username"}),
#    )
#    assert response.status_code == 201
#    assert json.loads(response.text) == {"id": 1, "username": "Test Username"}
#
#
# def test_get_user(client):
#    response = client.get("/api/users/1")
#    assert response.status_code == 200
#    assert json.loads(response.data) == {"id": 1, "username": "Test Username"}
