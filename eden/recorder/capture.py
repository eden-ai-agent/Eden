"""Audio recording utilities."""

from __future__ import annotations

import threading
import wave
from pathlib import Path
from typing import Optional

import numpy as np
import sounddevice as sd

from .device_manager import get_selected_device


_stream: Optional[sd.InputStream] = None
_wave_file: Optional[wave.Wave_write] = None
_lock = threading.Lock()


def _callback(indata, frames, time, status):
    """Write audio chunks from ``sounddevice`` into the wave file."""

    if status:
        # We simply print overrun/underrun information for debugging
        print(status, flush=True)
    if _wave_file is not None:
        _wave_file.writeframes(indata.copy().tobytes())


def start_recording(
    path: str | Path,
    *,
    samplerate: int = 44_100,
    channels: int = 1,
    dtype: str = "int16",
) -> None:
    """Start recording audio to ``path``.

    Parameters
    ----------
    path:
        Destination file for the recorded audio.  The file will be created as a
        WAV file with the given sample rate, channel count and data type.
    samplerate:
        Audio sample rate in Hertz.  Defaults to ``44100``.
    channels:
        Number of channels to record.  Defaults to ``1``.
    dtype:
        Numpy data type used by ``sounddevice``.  Defaults to ``"int16"``.
    """

    global _stream, _wave_file

    with _lock:
        if _stream is not None:
            raise RuntimeError("Recording already in progress")

        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)

        sample_width = np.dtype(dtype).itemsize

        _wave_file = wave.open(str(path), "wb")
        _wave_file.setnchannels(channels)
        _wave_file.setsampwidth(sample_width)
        _wave_file.setframerate(samplerate)

        device_info = get_selected_device()
        device = device_info["index"] if device_info else None

        _stream = sd.InputStream(
            samplerate=samplerate,
            channels=channels,
            dtype=dtype,
            device=device,
            callback=_callback,
        )
        _stream.start()


def stop_recording() -> None:
    """Stop the currently running recording session."""

    global _stream, _wave_file

    with _lock:
        if _stream is None:
            return

        _stream.stop()
        _stream.close()
        _stream = None

        if _wave_file is not None:
            _wave_file.close()
            _wave_file = None


def is_recording() -> bool:
    """Return ``True`` if a recording session is active."""

    with _lock:
        return _stream is not None
