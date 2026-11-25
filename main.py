#!/usr/bin/env python3
"""Two Robots in an Elevator — one line of awkward robot small talk.

Writes a single original line (under 200 characters) to /output/entry.txt.
Python 3, stdlib only, deterministic, no network, no randomness.
"""

import os

LINE = "I ran a diagnostic on my small-talk module. It just sighed and said: 'Ask about the weather.' So\u2026 how's the weather in this elevator?"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
