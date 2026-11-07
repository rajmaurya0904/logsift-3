# LogSift

**A streaming CLI filter that strips noise, redacts PII, and structures messy unstructured stdout logs into clean JSON for rapid grep analysis.**

Logs clutter terminals, expose sensitive customer credentials in shared CI/CD logs, and frustrate debugging. LogSift acts as a lightweight pipeline interceptor that cleans and formats output on the fly.

## Example

Run `logsift` in a pipeline:

```bash
$ echo "2023-10-25 10:00:00 [INFO] user=alice password=secret123" | logsift
{"timestamp": "2023-10-25 10:00:00", "level": "INFO", "message": "user=alice password=[REDACTED]"}
```

## Install

Install in editable mode from source:

```bash
pip install -e .
```

## Usage

- `-h, --help`: Show help message and exit.
- `--version`: Print package version and exit.

## How it works

- Reads lines from standard input as a continuous text stream.
- Detects and parses standard log levels and timestamps.
- Redacts sensitive patterns and PII such as passwords and keys.
- Emits structured JSON objects line by line to standard output.

## Limitations

- Does not support reading directly from log files without a stream redirection (`<` or `|`).
- Only recognizes standard common log level formats.
