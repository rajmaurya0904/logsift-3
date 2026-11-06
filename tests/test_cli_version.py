"""Test CLI version flag behavior."""

import sys

import pytest

from logsift_3 import __version__, cli


def test_cli_version_flag(monkeypatch, capsys):
    # Simulate command line arguments
    monkeypatch.setattr(sys, "argv", ["logsift", "--version"])
    with pytest.raises(SystemExit) as excinfo:
        cli.main()
    # argparse version action exits with code 0
    assert excinfo.value.code == 0
    captured = capsys.readouterr()
    # The output should be exactly the version string (plus newline)
    assert captured.out.strip() == __version__
