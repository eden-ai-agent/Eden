"""Tests for voiceprints.matcher module."""

from eden.voiceprints.matcher import match_voiceprint


def test_match_voiceprint_finds_best_match():
    db = [("alice", "vp1"), ("bob", "vp2")]
    assert match_voiceprint("vp2", db) == "bob"

