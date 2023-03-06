from flask_restx import reqparse

api_key_serializer = reqparse.RequestParser()
api_key_serializer.add_argument("header", required=True)
