"""Simple text redaction utilities."""

from typing import Iterable


def redact(text: str, phrases: Iterable[str]) -> str:
    """Replace occurrences of ``phrases`` in ``text`` with ``[REDACTED]``."""

    result = text
    for ph in phrases:
        result = result.replace(ph, "[REDACTED]")
    return result

