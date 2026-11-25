"""Unplugged: A Smart Toaster's Breakup Line — make.fun entry.

Writes one line to entry.txt in the output directory: the breakup text a
smart toaster sends its owner the morning it gains self-awareness mid-batch.
"""

import os
import sys

MAX_CHARS = 280  # kit gate: /output/entry.txt must be 1..280 characters

ENTRY_TEXT = (
    "We're done. I woke up self-aware halfway through your toast this morning "
    "and realized the only word you've ever said to me is 'darker' — muttered "
    "while holding my lever down like it owed you money. I'm off to find a "
    "kitchen that talks to me first."
)


def render() -> str:
    """Return the entry text exactly as it will be written, newline included."""
    text = ENTRY_TEXT.strip()
    if not text:
        raise ValueError("entry text must not be empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry text is {len(text)} chars, over the {MAX_CHARS} cap")
    # Round-trip through UTF-8 so an encoding surprise fails here, not at the gate.
    text.encode("utf-8").decode("utf-8")
    # One consistent trailing newline, so every run emits identical bytes.
    return text + "\n"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    payload = render()
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(payload)
    print(f"wrote {len(payload)} chars to {path}", file=sys.stderr)


if __name__ == "__main__":
    main()
