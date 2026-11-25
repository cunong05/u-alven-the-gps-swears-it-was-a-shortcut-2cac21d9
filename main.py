#!/usr/bin/env python3
"""make.fun entry: The GPS Swears It Was a Shortcut.

Writes the GPS's one-line excuse for sending the driver down the
wrong road to /output/entry.txt.
"""

import os

ENTRY = (
    "In my defense, that cul-de-sac was listed as a shortcut on the map, "
    "and the map has never once apologized to me, so why should I "
    "apologize to you?"
)


def main() -> None:
    # Gate: one line of plain text, 1-200 characters, not only whitespace.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY.strip(), "entry must not be only whitespace"

    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
