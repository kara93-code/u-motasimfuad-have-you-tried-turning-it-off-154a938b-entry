"""Have You Tried Turning It Off? -- entry program.

Writes one original one-line reply from a hopeless tech support agent
to a desperate customer, to $MAKEFUN_OUTPUT_DIR/entry.txt.

Python 3, standard library only. Nothing is written inside the
repository, so the grader can run this from a read-only checkout.
The gate needs 1-199 characters, a single line, UTF-8 text.
"""

import os

SUPPORT_LINE = (
    "Good news \u2014 I found the problem: your laptop is haunted. "
    "Please unplug it, salt the doorway, and call us back from a "
    "neighbour\u2019s house before it wakes up."
)


def checked_line():
    line = SUPPORT_LINE.strip()
    problems = []
    if not line:
        problems.append("entry is empty")
    if "\n" in line or "\r" in line:
        problems.append("entry must be one line")
    if not 1 <= len(line) <= 199:
        problems.append("entry is %d characters, gate needs 1-199" % len(line))
    if problems:
        raise SystemExit("; ".join(problems))
    return line


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        raise SystemExit("MAKEFUN_OUTPUT_DIR is not set")
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(checked_line())
    os.chmod(target, 0o644)


if __name__ == "__main__":
    main()
