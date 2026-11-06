"""Command-line interface for LogSift."""

import argparse

from logsift_3 import __version__


def build_parser() -> argparse.ArgumentParser:
    """Build the argument parser for the LogSift CLI."""
    parser = argparse.ArgumentParser(prog="logsift", description="LogSift")
    parser.add_argument(
        "--version",
        action="version",
        version=__version__,
        help="print the package version and exit",
    )
    return parser


def main() -> None:
    """Entry point for the LogSift CLI.

    Parses arguments and prints a help placeholder.
    """
    parser = build_parser()
    parser.parse_args()
    # Simple placeholder output as per task requirement
    print("LogSift")


if __name__ == "__main__":
    main()