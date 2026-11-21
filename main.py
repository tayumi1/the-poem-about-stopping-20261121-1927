#!/usr/bin/env python3
"""Write the poem to /output/entry.txt.

Deterministic: the poem is a fixed literal, so every run writes the
same bytes. Standard library only, no network, no other side effects.
"""

import os

POEM = (
    "The river begs the stone to move.\n"
    "The stone stays. The river learns its name.\n"
    "I plant my feet. I close the gate.\n"
    "I let the hurrying world go past.\n"
    "Not everything that moves is free.\n"
    "Some of us are free by staying.\n"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
