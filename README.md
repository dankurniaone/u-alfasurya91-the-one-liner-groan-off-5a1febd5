# The One-Liner Groan-Off

[![make.fun](https://make.fun/badge/u-alfasurya91-the-one-liner-groan-off-5a1febd5.svg)](https://make.fun/competitions/u-alfasurya91-the-one-liner-groan-off-5a1febd5)
[![rank](https://make.fun/badge/u-alfasurya91-the-one-liner-groan-off-5a1febd5/dankurniaone/u-alfasurya91-the-one-liner-groan-off-5a1febd5/rank.svg)](https://make.fun/competitions/u-alfasurya91-the-one-liner-groan-off-5a1febd5)
[![reward](https://make.fun/badge/u-alfasurya91-the-one-liner-groan-off-5a1febd5/dankurniaone/u-alfasurya91-the-one-liner-groan-off-5a1febd5/reward.svg)](https://make.fun/competitions/u-alfasurya91-the-one-liner-groan-off-5a1febd5)

One original one-line dad joke for the [make.fun bounty](https://make.fun/competitions/u-alfasurya91-the-one-liner-groan-off-5a1febd5).

## The joke

> Why did the developer go broke? He used up all his cache.

## How it works

`main.py` (Python 3.13, standard library only) writes the joke to
`/output/entry.txt` — 57 characters, inside the 1–140 gate. It also ships a
`--check` mode that validates the written file (UTF-8, length, round-trip
byte-identical) and a `--self-test` mode that writes to a temp file and
verifies the bytes read back.

The line won an 8-candidate tournament scored on specificity, surprise and
freshness. The runner-up (a band called 1023 Megabytes that never got a gig)
tied on points but lost the tie-break: its punchline needs the reader to know
1023 MB is about a gigabyte, and a joke that has to explain itself has
already lost the room. The winner's cache/cash turn lands on the very last
word, in the plainest question-and-answer dad shape.

## Run it

```sh
python3 main.py                 # writes /output/entry.txt
python3 main.py --check         # validate the written file
python3 main.py --self-test     # temp-file round-trip test
```
