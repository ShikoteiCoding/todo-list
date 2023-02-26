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
    ...


class NoteDetail(Resource):
    ...


# notes_namespace.add_resource(NoteList, "")
# notes_namespace.add_resource(NoteDetail, "/<int:note_id>")
