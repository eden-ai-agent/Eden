"""Miscellaneous helper utilities."""

def normalize_text(text: str) -> str:
    """Return the text in lowercase with whitespace collapsed."""

    return " ".join(text.lower().split())

