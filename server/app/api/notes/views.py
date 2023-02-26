from flask_restx import Namespace, Resource, fields
from structlog import get_logger

from app.api.security import api_required

from app.api.notes.crud import (
    get_all_notes,
    get_note_by_id,
    create_note,
    update_note,
    delete_note,
)

from app.api.notes.serializer import post_note_serializer

logger = get_logger(__name__)

# set the namespace
notes_namespace = Namespace("notes")

# set the model
note = notes_namespace.model(
    "Note",
    {
        "id": fields.Integer(readOnly=True),
        "title": fields.String(required=True),
        "content": fields.String(required=True),
        "user_id": fields.Integer(required=True),
    },
)


class NoteList(Resource):
    """
    resources for /api/v1/user/<user_id:int>/notes
    """

    @api_required
    @notes_namespace.marshal_with(note, as_list=True)
    def get(self, user_id: int):
        """return all notes of user"""

        logger.debug("NoteList.GET")
        return get_all_notes(user_id), 200


class NoteDetail(Resource):
    ...


notes_namespace.add_resource(NoteList, "")
# notes_namespace.add_resource(NoteDetail, "/<int:note_id>", "users/<int:user_id>")
