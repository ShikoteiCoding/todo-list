from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

from .config import BaseConfig

db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()


def create_app(*, config: BaseConfig|None=None) -> Flask:
    app = Flask(__name__)

    if config:
        app.config.from_object(config)

    db.init_app(app)
    migrate.init_app(app, db)
    login.init_app(app)

    # Blueprint registration
    from app.api import bp as api_bp

    app.register_blueprint(api_bp, url_prefix="/api")

    if not app.debug and not app.testing:
        print("Running in production")
    else:
        print("Running in dev mode")

    return app


from app import routes, models
