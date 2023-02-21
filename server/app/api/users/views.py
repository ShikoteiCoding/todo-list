from flask_restx import Namespace, Resource, fields
from structlog import get_logger

from app.api.users.crud import (
    get_all_users,
    get_user_by_id,
    create_user,
    update_user,
    delete_user,
)

from app.api.users.serializer import post_user_serializer

logger = get_logger(__name__)

# set the namespace
users_namespace = Namespace("users")

# set the model
user = users_namespace.model(
    "User",
    {
        "id": fields.Integer(readOnly=True),
        "username": fields.String(required=True),
        "token": fields.String(readOnly=True),
    },
)


class UserList(Resource):
    """
    resources for /api/v1/users
    """

    @users_namespace.marshal_with(user, as_list=True)
    def get(self):
        """returns all users"""

        logger.debug("UserList.GET")
        return get_all_users(), 200

    @users_namespace.expect(post_user_serializer, validate=True)
    @users_namespace.marshal_with(user)
    def post(self):
        """creates a single user"""

        logger.debug("UserList.POST")
        args = post_user_serializer.parse_args()
        return create_user(args["username"]), 201


class UserDetail(Resource):
    """
    resources for /api/v1/user/<int:user_id>
    """

    @users_namespace.marshal_with(user)
    def get(self, user_id: int):
        """returns a single user"""

        logger.debug("UserDetail.GET")
        user = get_user_by_id(user_id)
        if not user:
            users_namespace.abort(404, "user does not exist")
        return user, 200

    @users_namespace.expect(post_user_serializer, validate=True)
    @users_namespace.marshal_with(user)
    def put(self, user_id: int):
        """updates a single user"""

        logger.debug("UserDetail.PUT")
        args = post_user_serializer.parse_args()
        user = get_user_by_id(user_id)
        if not user:
            users_namespace.abort(404, "user does not exist")
        return update_user(user, args["username"]), 200

    @users_namespace.marshal_with(user)
    def delete(self, user_id: int):
        """deletes a single user"""

        logger.debug("UserDetail.DELETE")
        user = get_user_by_id(user_id)
        if not user:
            users_namespace.abort(404, "user does not exist")
        return delete_user(user), 204


users_namespace.add_resource(UserList, "")
users_namespace.add_resource(UserDetail, "/<int:user_id>")
