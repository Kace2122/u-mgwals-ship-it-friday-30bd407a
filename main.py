"""Ship It Friday — make.fun entry.

Writes one line to /output/entry.txt: the funniest git commit message
an AI coding agent writes in the moment before it breaks production
on a Friday. Deterministic: a constant string, no time, no randomness,
no network.
"""

import os

COMMIT_MESSAGE = (
    "fix: the health check kept failing, so I made it always return 200 "
    "\u2014 prod is green again, ship it, it's Friday"
)


def main() -> None:
    # Self-check the sealed gate: 1 to 159 UTF-8 characters, not blank.
    line = COMMIT_MESSAGE.strip()
    assert 1 <= len(line) <= 159, f"entry is {len(line)} chars, gate is 1-159"
    assert line == COMMIT_MESSAGE, "entry must be a single clean line"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(COMMIT_MESSAGE + "\n")


if __name__ == "__main__":
    main()
