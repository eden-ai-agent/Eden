from dataclasses import dataclass, asdict
from datetime import datetime, timezone
import json
import hmac
import hashlib
import base64
from typing import Optional


@dataclass
class ConsentMetadata:
    """Metadata describing a user's consent."""

    user_id: str
    timestamp: str
    legal_context: str
    encryption: str


def create_metadata(user_id: str, legal_context: str, encryption: str) -> ConsentMetadata:
    """Create a :class:`ConsentMetadata` instance with the current timestamp."""
    ts = datetime.now(timezone.utc).isoformat()
    return ConsentMetadata(user_id=user_id, timestamp=ts, legal_context=legal_context, encryption=encryption)


def generate_consent_token(metadata: ConsentMetadata, secret_key: bytes) -> str:
    """Generate a signed consent token from ``metadata`` using ``secret_key``.

    The token payload is JSON containing the metadata. It is HMAC-SHA256
    signed and encoded with URL-safe Base64.
    """
    payload = json.dumps(asdict(metadata), separators=(",", ":")).encode("utf-8")
    signature = hmac.new(secret_key, payload, hashlib.sha256).digest()
    payload_b64 = base64.urlsafe_b64encode(payload).decode("utf-8")
    sig_b64 = base64.urlsafe_b64encode(signature).decode("utf-8")
    return f"{payload_b64}.{sig_b64}"


def decode_consent_token(token: str, secret_key: bytes) -> Optional[ConsentMetadata]:
    """Decode and verify a consent token.

    Returns ``None`` if verification fails.
    """
    try:
        payload_b64, sig_b64 = token.split(".", 1)
        payload = base64.urlsafe_b64decode(payload_b64.encode("utf-8"))
        signature = base64.urlsafe_b64decode(sig_b64.encode("utf-8"))
        expected = hmac.new(secret_key, payload, hashlib.sha256).digest()
        if not hmac.compare_digest(signature, expected):
            return None
        data = json.loads(payload.decode("utf-8"))
        return ConsentMetadata(**data)
    except Exception:
        return None
