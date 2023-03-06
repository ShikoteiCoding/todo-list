from flask_restx import reqparse


post_user_serializer = reqparse.RequestParser()
post_user_serializer.add_argument("username", required=True)
