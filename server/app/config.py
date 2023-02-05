import os

class BaseConfig:
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")

class TestConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_TEST_URL")
