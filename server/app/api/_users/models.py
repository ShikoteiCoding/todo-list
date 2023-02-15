from app import db


class User(db.Model):  # type: ignore
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    token = db.Column(db.String(32), index=True, unique=True)

    def __init__(self, username=""):
        self.username = username
