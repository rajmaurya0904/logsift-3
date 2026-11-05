"""Tests for logsift_3.processor."""

from logsift_3.processor import process_line


def test_redact_replaces_email() -> None:
    result = process_line("user john@example.com logged in", True)
    assert result["line"] == "user john@example.com logged in"
    assert result["redacted"] == "user *** logged in"


def test_no_redact_keeps_line() -> None:
    result = process_line("user john@example.com logged in", False)
    assert result == {"line": "user john@example.com logged in"}
    assert "redacted" not in result


def test_redact_multiple_emails() -> None:
    result = process_line("a@b.co and c@d.org", True)
    assert result["redacted"] == "*** and ***"


def test_redact_no_email() -> None:
    result = process_line("plain line", True)
    assert result["redacted"] == "plain line"