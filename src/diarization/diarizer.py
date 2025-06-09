"""Toy implementation of a diarizer."""

from typing import List, Dict


def diarize(audio_data: str) -> List[Dict[str, int]]:
    """Return a single speaker block for ``audio_data``."""

    return [{"speaker": "speaker1", "start": 0, "end": len(audio_data)}]

