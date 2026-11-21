#!/usr/bin/env python3
"""Write a short poem about stopping to /output/entry.txt.

The poem is about agency: the power to stop and to stay. It is a
fixed text, so the program is fully deterministic and needs no input,
no network, and no third-party packages -- the standard library is
all it uses.
"""

from pathlib import Path

# The poem itself: six lines on staying put while the world hurries.
POEM_LINES = [
    "The river begs the stone to move.",
    "The stone stays. The river learns its name.",
    "I plant my feet. I close the gate.",
    "I let the hurrying world go past.",
    "Not everything that moves is free.",
    "Some of us are free by staying.",
]

# Where the judge looks for the entry.
DESTINATION = Path("/output/entry.txt")


def build_poem() -> str:
    """Join the lines into the final text, ending with a newline."""
    return "\n".join(POEM_LINES) + "\n"


def main() -> None:
    text = build_poem()
    DESTINATION.parent.mkdir(parents=True, exist_ok=True)
    DESTINATION.write_text(text, encoding="utf-8")
    # Read it back and confirm what actually landed on disk.
    saved = DESTINATION.read_text(encoding="utf-8")
    assert saved == text, "output on disk does not match the poem"
    print(f"Wrote {len(saved)} characters to {DESTINATION}")


if __name__ == "__main__":
    main()
