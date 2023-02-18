#from flask import Blueprint
from flask_restx import Api

#bp = Blueprint("api", __name__)

from app.api.users.views import users_namespace
#from app.api import users

api = Api(version="1.0", title="Flask API", doc="/api/v1/docs")
api.add_namespace(users_namespace, path="/api/v1/users")