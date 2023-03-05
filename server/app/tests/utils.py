import string

from random import choice
from app.api.users.models import User


def random_string() -> str:
    letters = string.ascii_lowercase
    return "".join(choice(letters) for _ in range(12))


def error_message(code: int, resource_name: str = "") -> str | None:
    match code:
        case 400:
            return "please provide API keys"
        case 403:
            return "the provided API keys are not valid"
        case 404:
            return f"{resource_name} does not exist"


def header_from_user(user: User) -> dict[str, dict[str, str]]:
    return {
        "header": {
            "API-KEY-ID": user.api_access_key_id,
            "API-SECRET-KEY": user.api_secret_access_key,
        }
    }
