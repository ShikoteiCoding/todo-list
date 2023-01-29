from flask_login import UserMixin
from flask import url_for
from sqlalchemy.sql import func

from app import db, login

class PaginatedAPIMixin(object):
    @staticmethod
    def to_collection_dict(query, page, per_page, endpoint, **kwargs):
        resources = query.paginate(page=page, per_page=per_page, error_out=False)
        data = {
            "items": [item.to_dict() for item in resources.items],
            "_meta": {
                "page": page,
                "per_page": per_page,
                "total_pages": resources.pages,
                "total_items": resources.total,
            },
            "_links": {
                "self": url_for(endpoint, page=page, per_page=per_page, **kwargs),
                "next": url_for(endpoint, page=page + 1, per_page=per_page, **kwargs)
                if resources.has_next
                else None,
                "prev": url_for(endpoint, page=page - 1, per_page=per_page, **kwargs)
                if resources.has_prev
                else None,
            },
        }
        return data


# https://realpython.com/token-based-authentication-with-flask/ token auth for later (JWT)
class User(PaginatedAPIMixin, UserMixin, db.Model):  # type: ignore
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    token = db.Column(db.String(32), index=True, unique=True)

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "username": self.username,
            "token": self.token,
            "_links": {
                "self": url_for("api.get_user", id=self.id),
            },
        }

    def from_dict(self, data: dict):
        for field in ["username"]:
            if field in data:
                setattr(self, field, data[field])

    def get_token(self):
        ...


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class Note(db.Model):  # type: ignore
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), index=True, unique=True)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    create_date = db.Column(db.DateTime(timezone=False), default=func.now())
    modify_date = db.Column(db.DateTime(timezone=False), default=func.now())
    deleted = db.Column(db.Boolean, default=False)

    def __repr__(self) -> str:
        return "<Note {!r}>".format(vars(self))


