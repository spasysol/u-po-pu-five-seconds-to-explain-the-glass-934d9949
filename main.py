"""Five Seconds to Explain the Glass entry for make.fun bounty
u-po-pu-five-seconds-to-explain-the-glass-934d9949.

Writes the one sentence a house cat would say in its own defence
after knocking a glass off the table (at most 200 characters) to
/output/entry.txt. No apology and no confession: the cat claims the
glass was already falling, it merely supervised, and physics is to
blame — then threatens the table. That is the cat's whole case.
Python 3.13, standard library only, no network, no input files.
"""

import os

LINE = "The glass was already falling when I arrived. I merely supervised its descent, and frankly it landed exactly where physics intended. The table is next if it keeps blocking the sun."

MAX_CHARS = 200


def validate(line):
    """Gate: 1-200 characters, a single line, one complete sentence."""
    if not 1 <= len(line) <= MAX_CHARS:
        raise SystemExit("line must be 1-%d characters, got %d" % (MAX_CHARS, len(line)))
    if "\n" in line or "\r" in line:
        raise SystemExit("line must be a single line")
    if not line.endswith("."):
        raise SystemExit("line must be one complete sentence")


def main():
    line = LINE.strip()
    validate(line)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
