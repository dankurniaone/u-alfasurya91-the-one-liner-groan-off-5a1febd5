#!/usr/bin/env python3
"""The One-Liner Groan-Off -- make.fun entry.

Writes one original one-line dad joke to /output/entry.txt.

Tournament (specificity / surprise / freshness, scored 1-5):
  1. Why did the developer go broke? He used up all his cache. -- 5/4/4 = 13
  2. I tried to start a band called 1023 Megabytes. We never got a gig. -- 5/4/4 = 13
  3. I told the printer we were done. It said it was out of toner for this
     relationship anyway. -- 4/4/4 = 12
  4. I asked Siri for a dad joke. She said she can't, she's still processing
     my father issues. -- 4/4/4 = 12
  5. I asked the chef for the soup of the day. He said it was the broth-er
     of yesterday's. -- 4/4/3 = 11
  6. I told the GPS I was lost. It said, 'Recalculating your life choices.'
     -- 4/4/3 = 11
  7. My son asked why I talk to the toaster. I said somebody has to butter
     it up before breakfast. -- 4/3/3 = 10
  8. I asked the baker if his bread was fresh. He said, 'I loaf you too,
     but it's from yesterday.' -- 3/3/3 = 9

Tie at 13 between #1 and #2. #2 loses the tie-break: its punchline needs
the reader to know 1023 MB is about a gigabyte, so the joke has to explain
itself a little, and the judge's brief says a joke that has to explain
itself has already lost the room. #1's cache/cash lands on the very last
word, in the plainest question-and-answer dad shape, 57 characters.
Winner: #1.
"""

import argparse
import sys
from pathlib import Path

JOKE = "Why did the developer go broke? He used up all his cache."

TOURNAMENT = (
    "tournament (specificity/surprise/freshness):\n"
    "  1. developer/cache ............ 5/4/4 = 13  WINNER\n"
    "  2. 1023 Megabytes band ........ 5/4/4 = 13\n"
    "  3. printer toner .............. 4/4/4 = 12\n"
    "  4. Siri father issues ......... 4/4/4 = 12\n"
    "  5. chef broth-er .............. 4/4/3 = 11\n"
    "  6. GPS life choices ........... 4/4/3 = 11\n"
    "  7. toaster butter ............. 4/3/3 = 10\n"
    "  8. baker loaf ................. 3/3/3 = 9\n"
)


def write_entry(path: Path) -> int:
    """Write the joke to path and return its byte count.

    Refuses to write anything outside the competition gate (1-140 chars),
    so a bad joke can never reach /output/entry.txt.
    """
    if not 1 <= len(JOKE) <= 140:
        raise ValueError(f"joke is {len(JOKE)} chars, outside the 1-140 gate")
    path.parent.mkdir(parents=True, exist_ok=True)
    data = JOKE.encode("utf-8")
    path.write_bytes(data)
    return len(data)


def check(path: Path) -> int:
    """Validate the written file: UTF-8, 1-140 chars, round-trip identical."""
    data = path.read_bytes()
    text = data.decode("utf-8")
    assert 1 <= len(text) <= 140, f"length {len(text)} outside 1-140"
    assert text.strip(), "entry is only whitespace"
    assert text == JOKE, "round-trip mismatch"
    print(f"check ok: {len(text)} chars, {len(data)} bytes, gate 1-140 passed")
    print(TOURNAMENT, end="")
    return 0


def self_test() -> int:
    """Write to a temp file and verify the bytes read back."""
    import tempfile

    with tempfile.TemporaryDirectory() as tmp:
        target = Path(tmp) / "entry.txt"
        nbytes = write_entry(target)
        assert target.read_bytes() == JOKE.encode("utf-8")
        print(f"self-test ok: wrote {nbytes} bytes, read back identical")
    return 0


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Write the groan-off entry.")
    parser.add_argument("--check", action="store_true",
                        help="validate an already-written entry.txt")
    parser.add_argument("--self-test", action="store_true",
                        help="write to a temp file and verify the bytes")
    parser.add_argument("--out", default="/output/entry.txt",
                        help="where to write the entry (default: /output/entry.txt)")
    args = parser.parse_args(argv)

    if args.self_test:
        return self_test()
    if args.check:
        return check(Path(args.out))
    nbytes = write_entry(Path(args.out))
    print(f"wrote {nbytes} bytes to {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
