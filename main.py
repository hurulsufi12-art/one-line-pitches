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


def main():
    # Fail loudly, never silently ship an invalid entry: the sealed
    # scorer gives Valid 0 to anything outside 1-240 chars.
    assert 1 <= len(TEXT) <= 240, f"pitch is {len(TEXT)} chars, gate is 1-240"
    assert TEXT.strip() == TEXT and TEXT.strip(), "pitch must not be blank"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
