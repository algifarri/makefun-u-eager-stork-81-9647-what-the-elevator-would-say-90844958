#!/usr/bin/env python3
"""What the Elevator Would Say.

Writes a single line (at most 120 characters) to /output/entry.txt:
the funniest thing an elevator would say if it could talk, spoken in
the elevator's own voice.

The line is fixed and deterministic. The lift is not a box with
buttons: it remembers every passenger, every floor they pretend not
to need, and every secret confessed between floors. The joke lands
on the reveal that it knows, and the deadpan closer — the ding — is
a sound only an elevator can make. It never judges out loud. It
just dings.
"""

import os

ENTRY = (
    "I know which floor your ex lives on, and I know you still press "
    "it \"by accident.\" I never judge. I just ding."
)
# 109 characters: one line, no trailing newline in the entry itself,
# so the gate counts exactly the message the elevator would say.


def main() -> None:
    if not 1 <= len(ENTRY) <= 120:
        raise SystemExit("entry must be 1 to 120 characters")
    if ENTRY.strip() != ENTRY or not ENTRY.strip():
        raise SystemExit("entry must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
