from flask_restx import reqparse


post_note_serializer = reqparse.RequestParser()
post_note_serializer.add_argument("title", required=False)
post_note_serializer.add_argument("content", required=False)
post_note_serializer.add_argument("user_id", required=False)
