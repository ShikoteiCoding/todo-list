from app import db


class User(db.Model):  # type: ignore
    __tablename__ = "notes"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(), index=True, unique=False, nullable=True)
    content = db.Column(db.String(), index=False, unique=False, nullable=True)

    def __init__(self, title="", content=""):
        self.title = title
        self.content = content
