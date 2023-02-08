import os

def get_required(name: str) -> str:
    var = os.getenv(name, None)
    if not var:
        raise Exception(f"Missing environment variable: {name}")
    return var

class BaseConfig:
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "LOAD_ME"


class DevConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = get_required("DATABASE_URL")


class TestConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = get_required("DATABASE_TEST_URL")
