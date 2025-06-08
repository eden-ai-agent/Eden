"""Tests for redaction.redactor module."""

from eden.redaction.redactor import redact


def test_redact_replaces_phrases():
    text = "this is top secret material"
    result = redact(text, ["top secret"])
    assert "[REDACTED]" in result

