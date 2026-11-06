"""Core log line processing for LogSift."""

from __future__ import annotations

import re

_EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")


def process_line(line: str, redact: bool) -> dict[str, str]:
    """Process a single log line.

    Returns a dict with the original line and, when ``redact`` is true, a
    ``redacted`` copy where email-like patterns are replaced with ``***``.
    """
    result: dict[str, str] = {"line": line}
    if redact:
        result["redacted"] = _EMAIL_RE.sub("***", line)
    return result