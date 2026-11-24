"""Last Text at One Percent — the dying phone's final text.

A phone at 1% spends its last power deleting its owner's search history
— "because someone has to love you" — then signs off with "You're
welcome", a martyr expecting no thanks. The joke lands twice: the
deletion itself (a final act of protection only the phone can do) and
the reason (tender and petty at once). No stock lines: no "drained",
no goodbye to Siri, no "tell my apps". One breath, 99 characters.
"""

import os
import sys

LINE = "Battery at 1%. Deleting your search history first, because someone has to love you. You're welcome."

MAX_CHARS = 200


def validate(line):
    """Check the line meets the competition gate: one line, 1-200 chars."""
    if not line or not line.strip():
        raise ValueError("entry line must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"entry line is {len(line)} characters, over the {MAX_CHARS}-character limit"
        )
    return line


def output_path():
    """Resolve the output directory from the environment, as the kit sets it."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    # MAKEFUN_OUTPUT_DIR is a directory; a bare path ending in entry.txt
    # is also honoured so local runs behave the same either way.
    if out_dir.endswith("entry.txt"):
        return out_dir
    return os.path.join(out_dir, "entry.txt")


def main():
    line = validate(LINE)
    path = output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    sys.stdout.write(line + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
