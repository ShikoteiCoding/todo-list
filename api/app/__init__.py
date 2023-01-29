from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate # type: ignore
from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app(config:Config=Config()) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)
    migrate.init_app(app, db)

    if not app.debug and not app.testing:
        print("Not in debug or testing mode")

    return app

from app import routes, models