from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

# AES-GCM parameters
NONCE_SIZE = 12
KEY_SIZE = 32


def generate_key(size: int = KEY_SIZE) -> bytes:
    """Return a new random key of ``size`` bytes."""
    return AESGCM.generate_key(bit_length=size * 8)


def generate_nonce(size: int = NONCE_SIZE) -> bytes:
    """Return a secure random nonce."""
    return os.urandom(size)


def encrypt(data: bytes, key: bytes) -> bytes:
    """Encrypt ``data`` with ``key`` and return ``nonce`` + ciphertext."""
    if isinstance(data, str):
        data = data.encode("utf-8")
    aesgcm = AESGCM(key)
    nonce = generate_nonce()
    ciphertext = aesgcm.encrypt(nonce, data, None)
    return nonce + ciphertext


def decrypt(blob: bytes, key: bytes) -> bytes:
    """Decrypt a blob produced by :func:`encrypt`."""
    nonce = blob[:NONCE_SIZE]
    ciphertext = blob[NONCE_SIZE:]
    aesgcm = AESGCM(key)
    return aesgcm.decrypt(nonce, ciphertext, None)
