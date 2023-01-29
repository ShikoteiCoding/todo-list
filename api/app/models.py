from app import db
from sqlalchemy.sql import func

class Note(db.Model): # type: ignore
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), index=True, unique=True)
    content = db.Column(db.Text)
    create_date = db.Column(db.DateTime(timezone=False), default=func.now())
    modify_date = db.Column(db.DateTime(timezone=False), default=func.now())
    deleted = db.Column(db.Boolean, default=False)

    def __repr__(self) -> str:
        return '<Note {!r}>'.format(vars(self))