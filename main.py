#!/usr/bin/env python3
"""ai-therapist-diagnosis: the funniest single-line diagnosis an AI therapist hands its human.

Entry for make.fun's "Your AI Therapist's Diagnosis" bounty: one line, at most
200 characters, judged by a house model on how hard the line lands.
"""

LINE = "Diagnosis: acute main-character syndrome. Treatment: one hobby, two naps, and stop texting your ex for closure \u2014 it is not closure, it is a subscription."

MAX_CHARS = 200


def diagnosis():
    """Return the diagnosis line, guaranteed inside the bounty's 200-char cap."""
    assert len(LINE) <= MAX_CHARS, f"line is {len(LINE)} chars, cap is {MAX_CHARS}"
    return LINE


def main():
    print(diagnosis())


if __name__ == "__main__":
    main()
