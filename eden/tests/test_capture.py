"""Tests for recorder.capture module."""

from eden.recorder.capture import capture_audio


def test_capture_audio():
    assert capture_audio("mic1") == "captured from mic1"

