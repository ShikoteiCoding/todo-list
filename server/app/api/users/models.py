from app import db

# TODO
# token should be unique


class User(db.Model):  # type: ignore
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    api_access_key_id = db.Column(db.String(64), index=True, unique=True)
    api_secret_access_key = db.Column(db.String(64), index=True, unique=True)
    is_admin = db.Column(db.Boolean)
    notes = db.relationship("Note", backref="author", lazy="dynamic")

    def __init__(
        self,
        username: str = "",
        api_access_key_id: str = "",
        api_secret_access_key: str = "",
        is_admin: bool = False,
    ):
        self.username = username
        self.api_access_key_id = api_access_key_id
        self.api_secret_access_key = api_secret_access_key
        self.is_admin = is_admin
