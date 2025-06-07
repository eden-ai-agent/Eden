"""Speaker diarization utilities using pyannote.audio."""

from __future__ import annotations

from importlib import import_module
from typing import List, Dict


def _load_pipeline(model: str):
    """Load a pyannote.audio Pipeline for diarization."""
    try:
        pyannote = import_module("pyannote.audio")
    except Exception as exc:  # pragma: no cover - executed only when missing
        raise ImportError("pyannote.audio is required for speaker diarization") from exc
    Pipeline = pyannote.Pipeline
    return Pipeline.from_pretrained(model)


class SpeakerDiarizer:
    """Wrapper around :mod:`pyannote.audio` for diarization."""

    def __init__(self, model: str = "pyannote/speaker-diarization") -> None:
        self.pipeline = _load_pipeline(model)

    def diarize(self, audio_path: str) -> List[Dict]:
        """Return diarization segments for ``audio_path``."""
        diarization = self.pipeline(audio_path)
        segments: List[Dict] = []
        for turn, _, speaker in diarization.itertracks(yield_label=True):
            segments.append(
                {
                    "start": float(turn.start),
                    "end": float(turn.end),
                    "speaker": speaker,
                }
            )
        return segments

