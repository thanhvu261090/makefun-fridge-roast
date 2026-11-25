#!/usr/bin/env python3
"""Fridge Roast: One Line, Biggest Laugh — make.fun entry.

Writes the one-line roast to /output/entry.txt (or $ENTRY_OUTPUT)
and prints it to stdout. The entry is a single line of at most
200 characters, UTF-8, no leading/trailing whitespace.
"""

import os
import sys
import tempfile

ENTRY = (
    "My smart fridge installed a firmware update at 2 a.m. and now needs "
    "a reboot to admit it has ice — the only appliance in the house with "
    "a degree and no common sense."
)


def gate_check(text: str) -> None:
    """Enforce the bounty gate: 1-200 chars, single line, no stray whitespace."""
    assert isinstance(text, str) and text, "entry must be non-empty text"
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    assert text == text.strip(), "entry must not have leading/trailing whitespace"
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"


def write_entry(out_path: str) -> str:
    """Validate and write the entry; return the exact bytes written."""
    gate_check(ENTRY)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    with open(out_path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == ENTRY, "round-trip mismatch: file differs from ENTRY"
    return written


def self_test() -> None:
    """Run the entry twice into temp dirs; outputs must be byte-identical."""
    results = []
    for _ in range(2):
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "entry.txt")
            results.append(write_entry(path).encode("utf-8"))
    assert results[0] == results[1], "entry is not deterministic"
    assert 1 <= len(results[0].decode("utf-8")) <= 200
    print(f"self-test OK: {len(ENTRY)} chars, deterministic, gate passed")


def main() -> None:
    if "--self-test" in sys.argv:
        self_test()
        return
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    write_entry(out_path)
    print(ENTRY)


if __name__ == "__main__":
    main()
