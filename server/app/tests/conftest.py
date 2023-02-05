import pytest

from app import create_app, db

@pytest.fixture(scope='module')
def test_app():
    
    app = create_app()
    app.config.from_object("app.config.TestConfig")