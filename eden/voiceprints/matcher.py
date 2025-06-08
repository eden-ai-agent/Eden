"""Very small voiceprint matcher for demonstration."""

from typing import Iterable, Tuple, Optional


def match_voiceprint(voiceprint: str, database: Iterable[Tuple[str, str]]) -> Optional[str]:
    """Return the name from ``database`` whose voiceprint exactly matches."""

    for name, vp in database:
        if vp == voiceprint:
            return name
    return None

