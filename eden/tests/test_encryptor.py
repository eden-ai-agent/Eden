"""Tests for encryption.encryptor module."""

from eden.encryption.encryptor import encrypt, decrypt


def test_encrypt_decrypt_cycle():
    message = "secret"
    key = 42
    cipher = encrypt(message, key)
    assert cipher != message
    assert decrypt(cipher, key) == message

