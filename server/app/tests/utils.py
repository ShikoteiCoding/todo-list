import string

from random import choice


def random_string() -> str:
    letters = string.ascii_lowercase
    return "".join(choice(letters) for _ in range(12))


def error_message(code: int) -> str | None:
    match code:
        case 400:
            return "please provide API keys"
        case 403:
            return "the provided API keys are not valid"
