"""Utility helpers for converting audio to text."""

from __future__ import annotations

import os
from typing import Optional

try:  # ``speech_recognition`` is optional for running the tests
    import speech_recognition as sr  # type: ignore
except Exception:  # pragma: no cover - optional dependency
    sr = None


def _transcribe_file(path: str) -> Optional[str]:
    """Return transcription of ``path`` using ``speech_recognition`` if available."""

    if sr is None:
        return None

    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(path) as source:
            audio = recognizer.record(source)
        return recognizer.recognize_sphinx(audio)
    except Exception:
        return None


def transcribe(audio_data: str) -> str:
    """Convert ``audio_data`` to text if possible.

    ``audio_data`` can be either a path to an audio file or a text string.  When
    the ``speech_recognition`` package is available and ``audio_data`` points to
    an existing file, the audio will be transcribed using the PocketSphinx
    backend.  Otherwise the input is treated as already text and simply cleaned
    of extra whitespace.
    """

    if os.path.exists(audio_data):
        transcript = _transcribe_file(audio_data)
        if transcript is not None:
            return " ".join(transcript.strip().split())

    return " ".join(audio_data.strip().split())

