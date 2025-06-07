# Encryption utilities

"""Simple file encryption helpers using ``cryptography.fernet``."""

from __future__ import annotations

from cryptography.fernet import Fernet


def generate_key() -> bytes:
    """Return a new random key."""

    return Fernet.generate_key()


def encrypt_file(input_path: str, output_path: str, key: bytes | None = None) -> bytes:
    """Encrypt ``input_path`` and write the ciphertext to ``output_path``.

    The ``key`` used for encryption is returned. If ``key`` is ``None`` a new
    key will be generated.
    """

    key = key or generate_key()
    cipher = Fernet(key)
    with open(input_path, "rb") as f:
        data = f.read()
    token = cipher.encrypt(data)
    with open(output_path, "wb") as f:
        f.write(token)
    return key

