from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

import os

from .config import BaseConfig

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()


def create_app(*, config: BaseConfig | None = None) -> Flask:
    app = Flask(__name__)

    # set config
    if config:
        app.config.from_object(config)
    else:
        app_settings = os.getenv("APP_SETTINGS")
        app.config.from_object(app_settings)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)

    # Blueprint registration
    from app.api import bp as api_bp

    app.register_blueprint(api_bp, url_prefix="/api/v1")

    if not app.debug and not app.testing:
        print("Running in production")
    else:
        print("Running in dev mode")

    return app


from app import routes, models
