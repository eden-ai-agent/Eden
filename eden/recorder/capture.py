# Audio capture logic

"""Simple audio capture stubs used during testing.

The real application would interface with PyAudio or another library to record
audio from the system microphone. In this stripped down example we simply write
placeholder bytes to disk so that downstream stages of the pipeline have a file
to operate on.
"""

from __future__ import annotations

import os


def capture_audio(path: str) -> str:
    """Capture audio and write it to *path*.

    This stub just writes dummy bytes. The function returns the path to the
    captured audio file so callers can chain operations.
    """

    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as f:
        f.write(b"DUMMY AUDIO DATA")
    return path

