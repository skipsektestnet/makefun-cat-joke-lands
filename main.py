"""The One-Line Cat Joke That Lands: writes the entry text to /output/entry.txt.

Why this line: a specific, concrete scene (work call, yowling at a wall) with
the punch as a reversal in the last words -- the cat has worked out the one
workplace protection humans do not have.
"""

import os

# The entry itself: one line, punch at the end, no explanation.
ENTRY = "My cat waits until I'm on a work call to start yowling at a wall, because she knows HR can't fire her."

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Guard: never submit a blank entry to the sealed gate.
    assert ENTRY and not ENTRY.isspace(), "entry must not be empty"
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print("wrote", OUTPUT_PATH, len(ENTRY), "chars")


if __name__ == "__main__":
    main()
