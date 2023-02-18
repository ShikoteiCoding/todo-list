from flask_restx import Namespace, Resource
from structlog import get_logger

logger = get_logger(__name__)

ping_namespace = Namespace("ping")


class Ping(Resource):
    def get(self):
        """health check"""

        logger.debug("Ping.GET")
        return {"message": "ping"}, 200


ping_namespace.add_resource(Ping, "")
