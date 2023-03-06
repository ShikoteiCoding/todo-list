import secrets


def generate_api_keys() -> tuple[str, str]:
    api_access_key_id = secrets.token_urlsafe(16)
    api_secret_access_key = secrets.token_hex(16)
    return api_access_key_id, api_secret_access_key
