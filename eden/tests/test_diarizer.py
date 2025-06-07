import os
import sys
import types

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from eden.diarization import diarizer


class FakePipeline:
    def __call__(self, path):
        class Dummy:
            def itertracks(self, yield_label=True):
                yield types.SimpleNamespace(start=0.0, end=1.0), None, "A"
        return Dummy()


def test_diarize(monkeypatch):
    monkeypatch.setattr(diarizer, "_load_pipeline", lambda model: FakePipeline())
    d = diarizer.SpeakerDiarizer()
    result = d.diarize("dummy.wav")
    assert result == [{"start": 0.0, "end": 1.0, "speaker": "A"}]
