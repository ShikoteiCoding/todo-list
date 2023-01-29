import os
from dotenv import load_dotenv
from typing import Callable
import utils as utils

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir + "/../", ".env"))


def getenv_required(name: str) -> str:
    var = os.getenv(name)
    if not var:
        raise Exception("Missing Env Variable")
    return var


class Config(object):
    POSTGRES_USER = getenv_required("POSTGRES_USER")
    POSTGRES_PASSWORD = getenv_required("POSTGRES_PASSWORD")
    POSTGRES_HOST = getenv_required("POSTGRES_EXTERNAL_HOST")
    POSTGRES_PORT = getenv_required("POSTGRES_PORT")
    POSTGRES_DB = getenv_required("POSTGRES_DB")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        if utils.is_docker():
            return f"postgres://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        return "sqlite:///" + "app.db"  # macos uri
