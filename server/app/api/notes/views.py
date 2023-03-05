from flask_restx import Namespace, Resource, fields
from structlog import get_logger

from app.api.notes.models import Note

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
    resources for /api/v1/users/<int:user_id>/notes
    """

    @api_required()
    @notes_namespace.marshal_with(note, as_list=True)
    def get(self, user_id: int):
        """return all notes of user"""

        logger.debug("NoteList.GET")
        return get_all_notes(user_id), 200

    @api_required()
    @notes_namespace.expect(post_note_serializer, validate=True)
    @notes_namespace.marshal_with(note)
    def post(self, user_id: int):
        """creates a single user"""

        logger.debug("NoteList.POST")
        args = post_note_serializer.parse_args()

        return create_note(user_id, args["title"], args["content"]), 201


class NoteDetail(Resource):
    """
    ressource for /api/v1/users/<int:user_id>/notes/<int:note_id>
    """

    @api_required()
    @notes_namespace.marshal_with(note)
    def get(self, user_id: int, note_id: int):
        """return a single note"""

        logger.debug("NoteDetail.GET")
        note = get_note_by_id(user_id, note_id)
        if not note:
            notes_namespace.abort(404, "note does not exist")
        return note, 200

    @api_required()
    @notes_namespace.expect(post_note_serializer, validate=True)
    @notes_namespace.marshal_with(note)
    def put(self, user_id: int, note_id: int):
        """update a single note"""

        logger.debug("NoteDetail.PUT")
        args = post_note_serializer.parse_args()
        note = get_note_by_id(user_id, note_id)
        if not note:
            notes_namespace.abort(404, "note does not exist")
        return update_note(note, args["title"], args["content"]), 200

    @api_required()
    @notes_namespace.marshal_with(note)
    def delete(self, user_id: int, note_id: int):
        """delete a single note"""

        logger.debug("NoteDetail.DELETE")
        note = get_note_by_id(user_id, note_id)
        if not note:
            notes_namespace.abort(404, "note does not exist")
        return delete_note(note), 200


notes_namespace.add_resource(NoteList, "")
notes_namespace.add_resource(NoteDetail, "/<int:note_id>")
