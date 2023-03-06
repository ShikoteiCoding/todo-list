from flask_restx import Namespace, Resource
from structlog import get_logger

from app.api.auth.decorators import api_required
from app.api.auth.serializer import api_key_serializer

logger = get_logger(__name__)

ping_namespace = Namespace("ping")


class Ping(Resource):
    @ping_namespace.expect(api_key_serializer, validate=True)
    @api_required(is_admin=False)
    def get(self):
        """health check"""

        logger.debug("Ping.GET")
        return {"message": "ping"}, 200


ping_namespace.add_resource(Ping, "")
