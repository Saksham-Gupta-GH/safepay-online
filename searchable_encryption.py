import os
import hmac
import hashlib

KEY_PATH = os.path.join(os.path.dirname(__file__), "search_key.bin")


def _load_or_create_key() -> bytes:
    # Try loading from file first (local development)
    if os.path.exists(KEY_PATH):
        with open(KEY_PATH, "rb") as f:
            key = f.read()
        if len(key) >= 16:
            return key
    # Fallback: load from environment variable (Vercel / read-only filesystem)
    env_key = os.environ.get("SEARCH_KEY_B64")
    if env_key:
        import base64
        return base64.b64decode(env_key)
    # Last resort: generate new key (only works on writable filesystem)
    key = hashlib.sha256(os.urandom(32)).digest()
    try:
        with open(KEY_PATH, "wb") as f:
            f.write(key)
    except OSError:
        pass  # Read-only filesystem
    return key


_KEY = _load_or_create_key()


def token_for(value: str) -> str:
    """Return a deterministic token (hex) for searchable equality lookup."""
    if value is None:
        value = ""
    mac = hmac.new(_KEY, value.encode("utf-8"), hashlib.sha256)
    return mac.hexdigest()


def verify_token(value: str, token_hex: str) -> bool:
    return hmac.compare_digest(token_for(value), token_hex)
