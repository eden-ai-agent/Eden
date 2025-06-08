"""Utilities for managing audio input devices.

This module provides a small abstraction over ``sounddevice`` to list
available input devices and select one for recording.  The selected device
index is stored module wide and used by :mod:`eden.recorder.capture` when
starting a recording session.
"""

from __future__ import annotations

from typing import Dict, List, Optional, Union

import sounddevice as sd

_selected_device_index: Optional[int] = None


def list_input_devices() -> List[Dict[str, Union[int, str]]]:
    """Return a list of available input devices.

    Each device is represented as a dictionary with ``index`` and ``name``
    fields.  Only devices that support input channels are returned.
    """

    devices = []
    for idx, info in enumerate(sd.query_devices()):
        if info.get("max_input_channels", 0) > 0:
            devices.append({"index": idx, "name": info["name"]})
    return devices


def select_device(device: Union[int, str]) -> Dict:
    """Select an input device by index or by name.

    Parameters
    ----------
    device:
        Integer index or string name of the device to select.

    Returns
    -------
    dict
        The device information as returned by ``sounddevice.query_devices``.
    """

    global _selected_device_index

    if isinstance(device, int):
        _selected_device_index = device
    else:
        matches = [d["index"] for d in list_input_devices() if d["name"] == device]
        if not matches:
            raise ValueError(f"No device found matching '{device}'")
        _selected_device_index = matches[0]

    return sd.query_devices(_selected_device_index)


def get_selected_device() -> Optional[Dict]:
    """Return information for the currently selected device, if any."""

    if _selected_device_index is None:
        return None
    return sd.query_devices(_selected_device_index)
