from __future__ import annotations

import json
import logging
import os
from typing import Any, Dict

from .recorder.capture import capture_audio
from .transcription.transcriber import transcribe
from .diarization.diarizer import diarize
from .redaction.redactor import redact_text
from .encryption.encryptor import encrypt_file


class EdenController:
    """High level pipeline tying together the Eden components."""

    def __init__(self, out_dir: str = "output") -> None:
        self.out_dir = out_dir
        os.makedirs(self.out_dir, exist_ok=True)
        self.logger = logging.getLogger(__name__)

    def run(self) -> Dict[str, Any]:
        """Execute the capture/transcription pipeline."""

        self.logger.info("Capturing audio")
        audio_path = os.path.join(self.out_dir, "audio.wav")
        capture_audio(audio_path)

        self.logger.info("Transcribing audio")
        transcript = transcribe(audio_path)

        self.logger.info("Running diarization")
        speakers = diarize(audio_path)

        self.logger.info("Redacting transcript")
        redacted_text = redact_text(transcript)
        transcript_path = os.path.join(self.out_dir, "transcript.txt")
        with open(transcript_path, "w", encoding="utf-8") as f:
            f.write(redacted_text)

        self.logger.info("Encrypting artifacts")
        enc_audio_path = os.path.join(self.out_dir, "audio.wav.enc")
        enc_transcript_path = os.path.join(self.out_dir, "transcript.txt.enc")
        key = encrypt_file(audio_path, enc_audio_path)
        encrypt_file(transcript_path, enc_transcript_path, key)

        meta = {
            "audio": os.path.basename(audio_path),
            "transcript": os.path.basename(transcript_path),
            "encrypted_audio": os.path.basename(enc_audio_path),
            "encrypted_transcript": os.path.basename(enc_transcript_path),
            "speakers": speakers,
        }
        meta_path = os.path.join(self.out_dir, "metadata.json")
        with open(meta_path, "w", encoding="utf-8") as f:
            json.dump(meta, f, indent=2)

        self.logger.info("Pipeline complete")
        return meta
