import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))

from eden.controller import EdenController


def test_pipeline(tmp_path):
    ctrl = EdenController(out_dir=str(tmp_path))
    meta = ctrl.run()

    assert (tmp_path / meta["audio"]).exists()
    assert (tmp_path / meta["transcript"]).exists()
    assert (tmp_path / meta["encrypted_audio"]).exists()
    assert (tmp_path / meta["encrypted_transcript"]).exists()
    assert (tmp_path / "metadata.json").exists()
