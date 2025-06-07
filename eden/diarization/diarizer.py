# Speaker diarization

"""Stub for speaker diarization."""

from __future__ import annotations

from typing import List, Dict


def diarize(audio_path: str) -> List[Dict[str, float | str]]:
    """Return fake diarization segments for *audio_path*."""

    # A real implementation would analyze the audio and return timestamps for
    # each speaker. Here we provide a single dummy segment so tests can verify
    # the pipeline runs.
    return [{"speaker": "A", "start": 0.0, "end": 1.0}]

