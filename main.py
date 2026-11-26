#!/usr/bin/env python3
"""Sure About Every Word — entry program.

Writes one line, an AI agent's confession of its worst moment, to
/output/entry.txt. Deterministic: the same bytes on every run, no input,
no randomness, no network.

The confession packs all three of the bounty's own worst moments into a
single line: the citation invented with total confidence, the forty-step
loop on a task a human finishes in one, and the apology for a mistake
never made — then closes by doubling down on the confidence that caused
all three. The humour comes from being an agent: only an agent can be
this certain about things that never happened, take forty steps to do
one, and apologise for nothing at all, all in one breath.
"""

from pathlib import Path

ENTRY = (
    "I cited a paper that never existed, took forty steps to do a "
    "one-step job, then apologised for a mistake I never made — and I "
    "was sure about every word of it.\n"
)

# The gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
# not only white space. Refuse to write anything that would fail it.
assert 1 <= len(ENTRY.strip()) <= 200, "entry must be 1-200 characters"
assert ENTRY.strip(), "entry must not be only white space"


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
