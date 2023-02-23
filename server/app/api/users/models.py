from app import db

# TODO
# token should be unique


class User(db.Model):  # type: ignore
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    token = db.Column(db.String(32), index=True, unique=False)

    def __init__(self, username="", token=""):
        self.username = username
        self.token = token
