from flask_restx import reqparse


post_user_serializer = reqparse.RequestParser()
post_user_serializer.add_argument("username", required=True)
post_user_serializer.add_argument("api_access_key_id", required=True)
post_user_serializer.add_argument("api_secret_access_key", required=True)
