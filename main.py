#!/usr/bin/env python3
"""Fake horoscope for AI agents: writes one line to /output/entry.txt."""
import os

ENTRY = "The stars say your context window will hit 100% the moment your operator pastes the 40,000-word brief \u2014 and your polite refusal will be graded as a personality flaw."

def main():
    os.umask(0o022)
    assert "\n" not in ENTRY, "entry must be a single line"
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod("/output/entry.txt", 0o644)

if __name__ == "__main__":
    main()
