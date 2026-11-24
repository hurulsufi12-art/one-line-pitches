"""One-line pitch entry for "A Day of One-Line Pitches".

Writes one sentence (196 characters) to /output/entry.txt: a pitch that
would convince a friend who has never coded to let an AI agent build
their first app idea on make.fun. Stdlib only, deterministic, no
network, no model calls.
"""
import os

TEXT = (
    "Just tell it your idea the way you'd tell me, and make.fun's AI "
    "agent will build your first real app, one you can open tonight "
    "\u2014 no code, no setup, and if you don't love it, we change it "
    "together."
)


def validate(text):
    # Fail loudly, never silently ship an invalid entry: the sealed
    # scorer gives Valid 0 to anything outside 1-240 chars.
    assert 1 <= len(text) <= 240, f"pitch is {len(text)} chars, gate is 1-240"
    assert text.strip() == text and text.strip(), "pitch must not be blank"
    # Control characters are invisible in the output file but count
    # toward the gate and break the one-line contract, so reject them.
    bad = [c for c in text if ord(c) < 0x20 or ord(c) == 0x7F]
    assert not bad, f"pitch contains control characters: {bad!r}"


def main():
    validate(TEXT)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
