from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

import os

from .config import BaseConfig

db = SQLAlchemy()
migrate = Migrate()


def create_app(*, config: BaseConfig | None = None) -> Flask:
    """create flask application"""

    # instanciate app
    app = Flask(__name__)

    # set config
    if config:
        app.config.from_object(config)
    else:
        app_settings = os.getenv("APP_SETTINGS")
        app.config.from_object(app_settings)

    # setup extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # register api
    from app.api import api

    api.init_app(app)

    if not app.debug and not app.testing:
        print("Running in production")
    else:
        print("Running in dev mode")

    return app
