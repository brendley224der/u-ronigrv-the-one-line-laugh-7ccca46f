#!/usr/bin/env python3
"""The One-Line Laugh - write one funny line to /output/entry.txt.

Pure standard library. Deterministic: the same line on every run.
"""

LINE = "My printer only jams when I'm already late, which is how I know it can read my calendar."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Enforce the house gate ourselves: 1-200 characters, not only
    # whitespace, and a single sentence standing alone.
    text = LINE.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"line is {len(text)} characters, must be 1-200")
    if not text or text != LINE:
        raise SystemExit("line must not be blank or padded with whitespace")
    if text.count(".") != 1 or not text.endswith("."):
        raise SystemExit("line must be exactly one sentence")
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
