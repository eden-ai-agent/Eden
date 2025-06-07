import os
import sys
import pytest

# Ensure the repository root is on the path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from eden.encryption import encryptor


def test_encrypt_decrypt_roundtrip():
    key = encryptor.generate_key()
    data = b"secret message"
    blob = encryptor.encrypt(data, key)
    assert data == encryptor.decrypt(blob, key)


def test_unique_keys():
    k1 = encryptor.generate_key()
    k2 = encryptor.generate_key()
    assert k1 != k2
    assert len(k1) == encryptor.KEY_SIZE
    assert len(k2) == encryptor.KEY_SIZE
