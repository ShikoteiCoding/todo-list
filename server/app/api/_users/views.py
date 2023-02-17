from flask_restx import Namespace, Resource, fields

from app.api._users.crud import (
    get_all_users,
    get_user_by_id,
    create_user,
    update_user,
    delete_user
)

from app.api._users.serializer import post_user_serializer

# TODO
# 1. Logger

users_namespace = Namespace("users")
user = users_namespace.model(
    "User",
    {
        "id": fields.Integer(readOnly=True),
        "username": fields.String(required=True),
        "token": fields.String(readOnly=True)
    }
)

class UserList(Resource):
    @users_namespace.marshal_with(user, as_list=True)
    def get(self):
        """returns all users"""

        print("UserList.GET")
        return get_all_users(), 200

    @users_namespace.expect(post_user_serializer, validate=True)
    @users_namespace.marshal_with(user)
    def post(self):
        """returns a single user"""

        print("UserList.POST")
        args = post_user_serializer.parse_args()
        return create_user(args["username"]), 201

#class UserDetail(Resource):
#    @users_namespace.marshal_with(user)
#    def get(self):
#        """returns all users"""
#
#        print("UserList.GET")
#        return get_all_users(), 200
#
#    @users_namespace.expect(post_user_serializer, validate=True)
#    @users_namespace.marshal_with(user)
#    def post(self):
#        """returns a single user"""
#
#        print("UserList.POST")
#        args = post_user_serializer.parse_args()
#        return create_user(args["username"]), 201