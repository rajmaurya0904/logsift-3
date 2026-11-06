# LogSift

**A streaming CLI filter that strips noise, redacts PII, and structures messy unstructured stdout logs into clean JSON for rapid grep analysis.**

Logs clutter terminals, expose sensitive credentials or tokens in CI pipelines, and make grep slow and frustrating when debugging high-volume services. LogSift acts as a lightweight pipe between your commands and your screen or log aggregator, filtering out noise and standardizing output on the fly.

## Example

Filter a log stream with LogSift:

```bash
$ echo "2025-01-01T12:00:00 DEBUG [db] connecting to postgres://user:secret@localhost:5432" | logsift
{"timestamp": "2025-01-01T12:00:00", "level": "DEBUG", "component": "db", "message": "connecting to postgres://user:secret@localhost:5432 [REDACTED]"}
```

## Install

```bash
pip install -e ".[dev]"
```

## Usage

- `logsift`: Read from stdin and stream cleaned JSON output.
- `logsift --version`: Print the current package version and exit.

## How it works

- Reads log lines from standard input in real time.
- Strips ANSI color codes and extraneous control characters.
- Redacts common PII and secrets (like API keys, passwords, and IP addresses).
- Parses timestamps, log levels, and components into structured fields.
- Emits compact JSON lines for fast filtering with `jq` or `grep`.

## Limitations

- Does not tail log files on disk directly; designed for stdin piping (`tail -f app.log | logsift`).
- Regex-based redaction may occasionally miss domain-specific custom tokens unless configured.

## Development

```bash
pip install -e ".[dev]"
pytest -q
ruff check .
```

## License

MIT -- see [LICENSE](LICENSE).
