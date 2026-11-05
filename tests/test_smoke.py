"""Smoke test: package imports cleanly. Replace/extend as modules land."""

import logsift_3


def test_version_is_set() -> None:
    assert logsift_3.__version__
