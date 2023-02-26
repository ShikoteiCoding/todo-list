from flask_restx import Api


from app.api.ping.views import ping_namespace
from app.api.users.views import users_namespace
from app.api.notes.views import notes_namespace


api = Api(version="1.0", title="Flask API", doc="/api/v1/docs")
api.add_namespace(ping_namespace, path="/api/v1/ping")
api.add_namespace(users_namespace, path="/api/v1/users")
api.add_namespace(notes_namespace, path="/api/v1/user/<int:user_id>/notes")
