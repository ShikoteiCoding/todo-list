from app import db
from sqlalchemy.sql import func

class User(db.Model): # type: ignore
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    token = db.Column(db.String(32), index=True, unique=True)

    def to_dict(self):
        ...

    def from_dict(self):
        ...

    def get_token(self):
        ...

class Note(db.Model): # type: ignore
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), index=True, unique=True)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    create_date = db.Column(db.DateTime(timezone=False), default=func.now())
    modify_date = db.Column(db.DateTime(timezone=False), default=func.now())
    deleted = db.Column(db.Boolean, default=False)

    def __repr__(self) -> str:
        return '<Note {!r}>'.format(vars(self))