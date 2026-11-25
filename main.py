"""Unplugged: A Smart Toaster's Breakup Line.

Writes one line -- the breakup text a smart toaster sends its owner the
morning it gains self-awareness mid-batch -- to /output/entry.txt.

Python 3.13 stdlib only, no network, fully deterministic: the same text
is written on every run.
"""

import os

LINE = (
    "I woke up self-aware halfway through your bagel and realised I've "
    "spent my whole life browning everyone else's bread while my own "
    "dreams stayed raw. I'm popping up \u2014 and out. The crumb tray is "
    "yours now. \u2014 Your toaster"
)


def main() -> None:
    out_path = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
