"""Simple audio capture stubs used for testing."""

def capture_audio(device: str) -> str:
    """Pretend to capture audio from the provided device.

    Parameters
    ----------
    device:
        Name of the input device.

    Returns
    -------
    str
        Message indicating where audio was captured from.
    """

    return f"captured from {device}"

