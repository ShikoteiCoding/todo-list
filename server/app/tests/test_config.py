"""
Testing the Flask App configuration app.config.py
"""

import os
import pytest

from flask import Flask
import app.config as config


def test_environment_loader():
    os.unsetenv("SQLALCHEMY_DATABASE_URI")
    with pytest.raises(Exception):
        config.get_required("SQLALCHEMY_DATABASE_URI")


def test_development_config(app: Flask):
    app.config.from_object("app.config.DevConfig")
    assert not app.config["TESTING"]
    assert app.config["SECRET_KEY"] == "LOAD_ME"
    assert app.config["SQLALCHEMY_DATABASE_URI"] == os.getenv("DATABASE_URL")


def test_testing_config(app: Flask):
    app.config.from_object("app.config.TestConfig")
    assert app.config["TESTING"]
    assert app.config["SECRET_KEY"] == "LOAD_ME"
    assert app.config["SQLALCHEMY_DATABASE_URI"] == os.getenv("DATABASE_TEST_URL")
