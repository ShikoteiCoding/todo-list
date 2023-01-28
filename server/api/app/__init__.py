from flask import Flask
from config import Config

def create_app(config_class=Config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_class)

    #db.init_app(app)
    #migrate.init_app(app, db)
    #login.init_app(app)
    #mail.init_app(app)
    #bootstrap.init_app(app)
    #moment.init_app(app)
    #babel.init_app(app)

    # ... no changes to blueprint registration

    if not app.debug and not app.testing:
        # ... no changes to logging setup
        ...

    return app