from flask import jsonify
from werkzeug.http import HTTP_STATUS_CODES


def error_response(status_code: int, message: str | None = None) -> dict[str, str]:
    """
    Generate a JSON error response with specified HTTP status code and message.
    :param status_code: HTTP status code
    :param message: Custom error message.
    :return: JSON error response with set status code and message.
    """
    payload = {"error": HTTP_STATUS_CODES.get(status_code, "Unknown error")}
    if message:
        payload["message"] = message
    response = jsonify(payload)
    response.status_code = status_code
    return response  # type: ignore


def bad_request(message):
    return error_response(400, message)
