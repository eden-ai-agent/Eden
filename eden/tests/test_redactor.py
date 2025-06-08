"""Tests for redaction.redactor module."""

from eden.redaction.redactor import redact


def test_redact_replaces_phrases_case_insensitive():
    text = "This is Top Secret material"
    result = redact(text, ["top secret"])
    assert result == "This is [REDACTED] material"


def test_redact_multiple_occurrences():
    text = "secret SECRET Secret"
    result = redact(text, ["secret"])
    assert result == "[REDACTED] [REDACTED] [REDACTED]"


def test_redact_when_no_phrase_found():
    text = "nothing to redact here"
    result = redact(text, ["classified"])
    assert result == text

