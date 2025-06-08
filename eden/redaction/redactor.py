"""Simple text redaction utilities."""

from typing import Iterable
import re


def redact(text: str, phrases: Iterable[str], ignore_case: bool = True) -> str:
    """Replace occurrences of ``phrases`` in ``text`` with ``[REDACTED]``.

    Parameters
    ----------
    text:
        Original string in which to perform redaction.
    phrases:
        Iterable of phrases that should be replaced.
    ignore_case:
        If ``True`` (default), matches are done case-insensitively.

    Returns
    -------
    str
        A new string with all occurrences of the provided phrases replaced by
        ``"[REDACTED]"``.
    """

    flags = re.IGNORECASE if ignore_case else 0
    result = text
    for ph in phrases:
        pattern = re.compile(re.escape(ph), flags)
        result = pattern.sub("[REDACTED]", result)
    return result

