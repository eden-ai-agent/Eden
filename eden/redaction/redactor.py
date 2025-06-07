"""Utilities for redacting Personally Identifiable Information (PII)."""

from __future__ import annotations

import re


class Redactor:
    """Redact PII such as names, phone numbers and addresses.

    The implementation is intentionally simple and relies solely on regular
    expressions.  It is not meant to be exhaustive but rather to provide a
    lightweight solution for unit tests and examples.
    """

    #: Regex matching ``First Last`` style names.  This obviously does not cover
    #: every possible name but works well enough for short demonstrations.
    NAME_PATTERN = re.compile(r"\b[A-Z][a-z]+\s+[A-Z][a-z]+\b(?!\s+[A-Z])")

    #: Regex for common US phone number formats such as ``123-456-7890`` or
    #: ``(123) 456 7890``.
    PHONE_PATTERN = re.compile(
        r"(?:\+?\d{1,2}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b"
    )

    #: Very small address detector that looks for a street number followed by a
    #: street name and type (e.g. ``Main Street``).  It supports a handful of
    #: common street types and is case-insensitive.
    ADDRESS_PATTERN = re.compile(
        r"\b\d{1,5}\s+(?:[A-Za-z0-9]+\s+)*(?:Street|St|Road|Rd|Avenue|Ave|"
        r"Boulevard|Blvd|Lane|Ln|Drive|Dr|Court|Ct)\b",
        re.IGNORECASE,
    )

    #: Text that replaces any detected PII
    REPLACEMENT = "[REDACTED]"

    def redact(self, text: str) -> str:
        """Return ``text`` with any recognised PII replaced."""

        patterns = [
            # Order matters: redact addresses before names so that street names
            # do not get replaced individually.
            self.ADDRESS_PATTERN,
            self.NAME_PATTERN,
            self.PHONE_PATTERN,
        ]

        redacted = text
        for pattern in patterns:
            redacted = pattern.sub(self.REPLACEMENT, redacted)
        return redacted


def redact_pii(text: str) -> str:
    """Convenience function that uses :class:`Redactor`."""

    return Redactor().redact(text)

