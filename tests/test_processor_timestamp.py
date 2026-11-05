"""Test timestamp handling in logsift_3.processor."""

from logsift_3.processor import process_line


def test_malformed_timestamp_no_timestamp_key() -> None:
    # Example of a malformed ISO-8601 timestamp (invalid month "13")
    line = "2021-13-01T12:00:00 Something happened"
    result = process_line(line, redact=False)
    # The processor should not add a 'timestamp' key for malformed timestamps
    assert "timestamp" not in result
