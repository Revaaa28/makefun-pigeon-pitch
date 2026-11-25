#!/usr/bin/env python3
"""One-line pigeon pitch entry for make.fun's "Pigeon Pitch, One Line".

Writes a single sentence (<= 200 characters) to /output/entry.txt:
the elevator pitch a city pigeon gives investors for its startup.
No network, no secrets, no environment access: the pitch is a
constant in this file.
"""

from pathlib import Path

PITCH = (
    "Statues pay us not to poop on them \u2014 that\u2019s our entire "
    "business model, and it\u2019s working: ten thousand pigeons, zero "
    "churn, and a moat you can see from space."
)

MAX_CHARS = 200
OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    pitch = PITCH.strip()
    assert 1 <= len(pitch) <= MAX_CHARS, f"pitch is {len(pitch)} chars"
    assert "\n" not in pitch, "pitch must be exactly one line"
    assert pitch == pitch.strip(), "pitch must not have surrounding whitespace"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(pitch, encoding="utf-8")
    # Read back what was written: the gate scores the file, not the
    # constant, so confirm the file itself is exactly one valid line.
    written = OUTPUT_PATH.read_text(encoding="utf-8")
    assert written == pitch, "written file differs from the pitch"
    assert "\n" not in written, "written file must be exactly one line"
    print(pitch)
    print(f"chars: {len(pitch)} (limit {MAX_CHARS})")


if __name__ == "__main__":
    main()
