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


def sqlalchemi_database_uri() -> str:
    POSTGRES_USER = getenv_required("POSTGRES_USER")
    POSTGRES_PASSWORD = getenv_required("POSTGRES_PASSWORD")
    POSTGRES_HOST = getenv_required("POSTGRES_EXTERNAL_HOST")
    POSTGRES_PORT = getenv_required("POSTGRES_PORT")
    POSTGRES_DB = getenv_required("POSTGRES_DB")
    return f"postgres://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"


class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = sqlalchemi_database_uri()
