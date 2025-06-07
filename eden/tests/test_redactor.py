"""Tests for the :mod:`eden.redaction.redactor` module."""

from __future__ import annotations

import os
import sys

# Ensure the project root is on ``sys.path`` when tests are executed directly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from eden.redaction.redactor import Redactor, redact_pii


def test_redacts_names():
    text = "Alice Smith met Bob Jones yesterday."
    expected = "[REDACTED] met [REDACTED] yesterday."
    assert redact_pii(text) == expected


def test_redacts_phone_numbers():
    text = "Call me at 555-123-4567 tomorrow."
    expected = "Call me at [REDACTED] tomorrow."
    assert redact_pii(text) == expected


def test_redacts_addresses():
    text = "He lives at 123 Main Street near the park."
    expected = "He lives at [REDACTED] near the park."
    assert redact_pii(text) == expected


def test_redactor_class_equivalent():
    r = Redactor()
    text = "Contact Jane Doe at (123) 456-7890, 42 Oak Road."
    expected = "Contact [REDACTED] at [REDACTED], [REDACTED]."
    assert r.redact(text) == expected
