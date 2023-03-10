from marshmallow import Schema, fields


class APIKeysSchema(Schema):
    API_KEY_ID = fields.Str(required=True)
    API_SECRET_KEY = fields.Str(required=True)


class AuthSchema(Schema):
    header = fields.Nested(APIKeysSchema, required=True)


auth_serializer = AuthSchema()
