from structlog import get_logger

from app import db
from app.api.notes.models import Note

logger = get_logger(__name__)


def get_all_notes(user_id: int) -> list[Note] | None:
    """return all notes of note"""

    logger.debug("get_all_notes")
    notes = None
    try:
        notes: list[Note] | None = Note.query.filter_by(user_id=user_id)
    except Exception as e:
        logger.exception(f"Exception occured: {e}")
        logger.error("Unable to fetch all notes.")

    return notes


def get_note_by_id(user_id: int, note_id: int) -> Note | None:
    """return a single note"""

    logger.debug("get_one_note")
    note = None
    try:
        note: Note | None = Note.query.filter_by(
            user_id=user_id, note_id=note_id
        ).first()
    except Exception as e:
        logger.exception(f"Exception occured: {e}")
        logger.error("Unable to fetch one note.")

    return note


def create_note(user_id: int, title: str, content: str) -> Note | None:
    """create a single note"""

    logger.debug("create_note")
    note = None
    try:
        note = Note(title=title, content=content, user_id=user_id)
    except Exception as e:
        logger.exception(f"Exception occured: {e}")
        logger.error("Unable to create a note.")

    return note


def update_note(note: Note, title: str, content: str) -> Note | None:
    """update a single note"""

    logger.debug("update_note")
    try:
        note.title = title
        note.content = content
        db.session.commit()
    except Exception as e:
        logger.exception(f"Exception occured: {e}")
        logger.error("Unable to update a note.")
    return note


def delete_note(note: Note) -> Note:
    """delete a single note"""

    logger.debug("delete_note")
    try:
        db.session.delete(note)
        db.session.commit()
    except Exception as e:
        logger.exception(f"Exception occured: {e}")
        logger.error("Unable to delete a note.")
    return note
