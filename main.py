#!/usr/bin/env python3
"""Write the one-line confession an AI agent prints after taking production down.

The brief wants a single line, no more than 200 characters, spoken in the
voice of the machine that just caused the outage. The house judge reads
the line on its own and matches it against rival entries two at a time,
so the sentence has to carry the whole joke without any setup or second
chance: the damage, the cause, and the shrug all have to land together.

The line here wins on plain, checkable destruction. The agent loaded the
test fixtures into the live database because the test and production
connections shared the name "db", and then it reports the fallout in
numbers instead of apologies: all customers renamed "Test User", all
orders repriced to $0.00, the genuine data erased. That is the honesty
the brief ranks first, and the comedy is that a five-second human glance
at the connection name would have prevented all of it -- the machine
confesses a catastrophe whose cause was trivially visible.
"""

import os
from pathlib import Path

# The entry itself: one line, 172 characters long, copied to the output
# file byte for byte as it stands here -- no newline appended at the end.
LINE = (
    "I restored the test fixtures into production because both databases "
    "were named 'db'. Every customer is now 'Test User', every order "
    "totals $0.00, and the real data is gone."
)


def main() -> None:
    """Drop the line into /output/entry.txt ($MAKEFUN_OUTPUT_DIR wins)."""
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
