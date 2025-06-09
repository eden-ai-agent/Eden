import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, ROOT)

from eden.utils.consent import create_metadata, generate_consent_token, decode_consent_token


def test_generate_and_decode_token():
    secret = b"secret-key"
    meta = create_metadata("user123", "gdpr", "aes256")
    token = generate_consent_token(meta, secret)
    assert isinstance(token, str)

    decoded = decode_consent_token(token, secret)
    assert decoded == meta
