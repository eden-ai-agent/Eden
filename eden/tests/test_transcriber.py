import os
import sys
import types

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from eden.transcription import transcriber
from eden.diarization import diarizer


class FakeWhisperModel:
    def transcribe(self, path):
        return {"segments": [{"start": 0.0, "end": 1.0, "text": "hello"}]}


class FakePipeline:
    def __call__(self, path):
        class Dummy:
            def itertracks(self, yield_label=True):
                yield types.SimpleNamespace(start=0.0, end=1.0), None, "A"
        return Dummy()


def test_transcribe(monkeypatch):
    monkeypatch.setattr(transcriber, "_load_model", lambda name: FakeWhisperModel())
    segments = transcriber.transcribe("dummy.wav")
    assert segments == [{"start": 0.0, "end": 1.0, "text": "hello"}]


def test_transcribe_with_diarization(monkeypatch):
    monkeypatch.setattr(transcriber, "_load_model", lambda name: FakeWhisperModel())
    monkeypatch.setattr(diarizer, "_load_pipeline", lambda model: FakePipeline())
    d = diarizer.SpeakerDiarizer()
    result = transcriber.transcribe_with_diarization("dummy.wav", diarizer=d)
    assert result == [{"speaker": "A", "start": 0.0, "end": 1.0, "text": "hello"}]
