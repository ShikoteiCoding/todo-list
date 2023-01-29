from app.api import bp


@bp.route("/users/<int:id>", methods=["GET"])  # type: ignore
def get_user(id: int):
    pass


@bp.route("/users", methods=["GET"])  # type: ignore
def get_users():
    pass


@bp.route("/users", methods=["POST"])  # type: ignore
def create_user():
    pass


@bp.route("/users/<int:id>", methods=["PUT"])  # type: ignore
def update_user(id: int):
    pass


@bp.route("/users/<int:id>/notes", methods=["GET"])  # type: ignore
def get_notes(id: int):
    pass


@bp.route("/users/<int:id>/notes", methods=["GET"])  # type: ignore
def get_note(user_id: int, note_id: int):
    pass
