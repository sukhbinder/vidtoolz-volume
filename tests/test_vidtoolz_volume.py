import pytest
import subprocess
from unittest.mock import patch
import os
import vidtoolz_volume as w

from argparse import Namespace, ArgumentParser


def test_create_parser():
    subparser = ArgumentParser().add_subparsers()
    parser = w.create_parser(subparser)

    assert parser is not None

    result = parser.parse_args(["input_video.mp4", "3"])
    assert result.input_video == "input_video.mp4"
    assert result.volume_db == 3
    assert result.output is None


def test_plugin(capsys):
    w.volume_plugin.hello(None)
    captured = capsys.readouterr()
    assert "Hello! This is an example ``vidtoolz`` plugin." in captured.out


def test_adjust_volume_success():
    input_video = "input.mp4"
    volume_db = 3.0
    output_video = "output.mp4"

    with patch("subprocess.run") as mock_run:
        mock_run.return_value = None
        w.adjust_volume(input_video, volume_db, output_video)
        mock_run.assert_called_once_with(
            ["ffmpeg", "-i", input_video, "-filter:a", "volume=3.0dB", output_video],
            check=True,
        )
