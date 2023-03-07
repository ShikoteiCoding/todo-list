from flask_restx import Namespace, Resource, fields
from structlog import get_logger

from app.api.auth.decorators import header_required, login

from app.api.users.crud import get_all_users, get_user_by_id, create_user, update_user

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
        "api_access_key_id": fields.String(required=True),
        "api_secret_access_key": fields.String(required=True),
        "is_admin": fields.Boolean(required=True),
    },
)


class UserList(Resource):
    """
    resources for /api/v1/users
    """

    @users_namespace.marshal_with(user, as_list=True)
    @header_required()
    @login(is_admin=False)
    def get(self):
        """returns all users"""

        logger.debug("UserList.GET")
        return get_all_users(), 200

    @header_required()
    @login(is_admin=True)
    @users_namespace.expect(post_user_serializer, validate=True)
    @users_namespace.marshal_with(user, as_list=True)
    def post(self):
        """returns all users"""

        logger.debug("UserList.POST")
        args = post_user_serializer.parse_args()
        return create_user(username=args["username"]), 201


class UserDetail(Resource):
    """
    resources for /api/v1/user/<int:user_id>
    """

    @header_required()
    @login(is_admin=True)
    @users_namespace.marshal_with(user)
    def get(self, user_id: int):
        """returns a single user"""

        logger.debug("UserDetail.GET")
        user = get_user_by_id(user_id)
        if not user:
            users_namespace.abort(404, "user does not exist")
        return user, 200

    @header_required()
    @login(is_admin=True)
    @users_namespace.expect(post_user_serializer, validate=True)
    @users_namespace.marshal_with(user)
    def put(self, user_id: int):
        """updates a single user"""

        logger.debug("UserDetail.PUT")
        user = get_user_by_id(user_id)
        if not user:
            users_namespace.abort(404, "user does not exist")
        args = post_user_serializer.parse_args()
        return update_user(user, args["username"]), 200


users_namespace.add_resource(UserList, "")
users_namespace.add_resource(UserDetail, "/<int:user_id>")
