import os
from dotenv import load_dotenv
from typing import Callable

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir + "/../", ".env"))


def getenv_required(varname: str) -> str:
    var = os.getenv(varname)
    if not var:
        raise Exception("Missing Env Variable")
    return var


class Config(object):
    POSTGRES_USER = getenv_required("POSTGRES_USER")
    POSTGRES_PASSWORD = getenv_required("POSTGRES_PASSWORD")
    POSTGRES_HOST = getenv_required("POSTGRES_HOST")
    POSTGRES_PORT = getenv_required("POSTGRES_PORT")
    POSTGRES_DB = getenv_required("POSTGRES_EXTERNAL_HOST")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        return f"postgres://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
