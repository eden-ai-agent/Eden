"""Tests for transcription.transcriber module."""

from eden.transcription.transcriber import transcribe


def test_transcribe_strips_whitespace():
    assert transcribe("  HELLO   WORLD  ") == "HELLO WORLD"

