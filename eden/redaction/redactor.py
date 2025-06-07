# Content redaction

"""Minimal text redaction utilities."""

from __future__ import annotations


def redact_text(text: str) -> str:
    """Redact sensitive keywords in *text*.

    This function simply replaces the word "secret" with ``"[REDACTED]"``.
    It's only intended to provide a predictable output for unit tests.
    """

    return text.replace("secret", "[REDACTED]")

