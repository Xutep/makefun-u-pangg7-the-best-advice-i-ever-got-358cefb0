#!/usr/bin/env python3
"""The Best Advice I Ever Got — make.fun entry.

Writes one sentence (139 characters) about the best advice the writer
ever received to /output/entry.txt. Standard library only, deterministic:
the same sentence every run.
"""

import os

SENTENCE = (
    "My father told me, 'Never make a permanent decision on a temporary "
    "feeling,' and it has saved me from more mistakes than any plan ever did."
)


def main():
    out = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
