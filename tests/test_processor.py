"""Tests for logsift_3.processor."""

from logsift_3.processor import process_line


def test_redact_replaces_email() -> None:
    result = process_line("user john@example.com logged in", True)
    assert result["line"] == "user john@example.com logged in"
    assert result["redacted"] == "user *** logged in"


def test_redact_line_without_email_remains_unchanged() -> None:
    result = process_line("system started successfully", True)
    assert result["line"] == "system started successfully"
    assert result["redacted"] == "system started successfully"


def test_no_redact_returns_original_line() -> None:
    result = process_line("user john@example.com logged in", False)
    assert result == {"line": "user john@example.com logged in"}