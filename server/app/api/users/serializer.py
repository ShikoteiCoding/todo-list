from marshmallow import Schema, fields

from app.api.auth.serializer import AuthSchema


class BaseUserSchema(Schema):
    username = fields.Str(required=True)


class PostUserSchema(AuthSchema):
    # header = fields.Nested(HeaderSchema, required=True)
    username = fields.Str(required=True)


post_user_serializer = PostUserSchema()
