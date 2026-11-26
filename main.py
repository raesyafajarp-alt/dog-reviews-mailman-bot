#!/usr/bin/env python3
"""The Dog Reviews the Mailman.

Writes one funny one-line review a dog gives the mailman to
/output/entry.txt (under 200 characters, one line).
"""

import os

ENTRY = (
    "Five stars. He comes every day, lets me bark at him, and never "
    "once asked me to stop. The only human who respects my job."
)


def validate_entry(text: str) -> None:
    """Gate check: 1-200 characters, one line, not only whitespace."""
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")


def _write_entry(text: str, path: str = "/output/entry.txt") -> None:
    validate_entry(text)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def main() -> None:
    _write_entry(ENTRY)


if __name__ == "__main__":
    main()
