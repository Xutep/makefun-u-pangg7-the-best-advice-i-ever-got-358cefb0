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

MAX_CHARS = 200


def validate(sentence):
    """Check the sentence before writing it out; fail loudly if invalid."""
    if not isinstance(sentence, str):
        raise TypeError("entry must be a string, got %s" % type(sentence).__name__)
    sentence.encode("utf-8")  # raises UnicodeEncodeError on bad data
    if not sentence.strip():
        raise ValueError("entry must not be blank or only whitespace")
    if len(sentence) > MAX_CHARS:
        raise ValueError(
            "entry is %d characters, over the %d-character limit"
            % (len(sentence), MAX_CHARS)
        )
    if sentence.count(".") != 1 or not sentence.rstrip().endswith("."):
        raise ValueError("entry must be exactly one sentence ending in a period")


def main():
    validate(SENTENCE)
    out = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
