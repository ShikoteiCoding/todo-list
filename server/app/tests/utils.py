import string

from random import choice


def random_string() -> str:
    letters = string.ascii_lowercase
    return "".join(choice(letters) for _ in range(16))
