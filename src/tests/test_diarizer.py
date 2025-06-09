"""Tests for diarization.diarizer module."""

from eden.diarization.diarizer import diarize


def test_diarize_returns_single_block():
    blocks = diarize("hello")
    assert blocks == [{"speaker": "speaker1", "start": 0, "end": 5}]

