from app import db


class Note(db.Model):  # type: ignore
    __tablename__ = "notes"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(), index=True, unique=False, nullable=True)
    content = db.Column(db.String(), index=False, unique=False, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    request = db.relationship("Users")

    def __init__(self, title: str, content: str, user_id: int):
        self.title = title
        self.content = content
        self.user_id = user_id
