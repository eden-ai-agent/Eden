"""Utilities for transcribing audio files using Whisper."""

from __future__ import annotations

from dataclasses import dataclass
from importlib import import_module
from typing import List, Dict, Optional

from ..diarization.diarizer import SpeakerDiarizer


def _load_model(name: str):
    """Load a Whisper model by name."""
    try:
        whisper = import_module("whisper")
    except Exception as exc:  # pragma: no cover - executed only when missing
        raise ImportError("Whisper library is required for transcription") from exc
    return whisper.load_model(name)


@dataclass
class TranscriptSegment:
    start: float
    end: float
    text: str
    speaker: Optional[str] | None = None


def transcribe(audio_path: str, model_name: str = "base") -> List[Dict]:
    """Transcribe an audio file using the Whisper library.

    Parameters
    ----------
    audio_path:
        Path to the audio file to transcribe.
    model_name:
        Whisper model name. Defaults to ``"base"``.

    Returns
    -------
    List of dictionaries containing ``start``, ``end`` and ``text`` keys.
    """
    model = _load_model(model_name)
    result = model.transcribe(audio_path)
    segments: List[Dict] = []
    for segment in result.get("segments", []):
        segments.append(
            {
                "start": float(segment["start"]),
                "end": float(segment["end"]),
                "text": segment["text"].strip(),
            }
        )
    return segments


def transcribe_with_diarization(
    audio_path: str,
    model_name: str = "base",
    diarizer: Optional[SpeakerDiarizer] = None,
) -> List[Dict]:
    """Transcribe ``audio_path`` and annotate speaker labels.

    Parameters
    ----------
    audio_path:
        Path to the audio file.
    model_name:
        Whisper model name to use.
    diarizer:
        Optional :class:`~eden.diarization.diarizer.SpeakerDiarizer` instance. If
        not provided, a default one is created.

    Returns
    -------
    List of dictionaries with ``speaker``, ``start``, ``end`` and ``text`` keys.
    """
    diarizer = diarizer or SpeakerDiarizer()
    transcript_segments = transcribe(audio_path, model_name)
    speaker_segments = diarizer.diarize(audio_path)

    labelled: List[Dict] = []
    for seg in transcript_segments:
        midpoint = (seg["start"] + seg["end"]) / 2
        speaker = None
        for diar in speaker_segments:
            if diar["start"] <= midpoint <= diar["end"]:
                speaker = diar["speaker"]
                break
        labelled.append({"speaker": speaker, **seg})
    return labelled

