#!/usr/bin/env python3
"""
user-profile-surface.py - SessionStart hook for Familiar.

Surfaces the person's tech-comfort band at the start of every session so the
familiar opens already calibrated to how they want to be talked to, instead of
drifting back to a default register under context pressure. This is the
enforcement half of the "Meet your person where they are" doctrine: the rule is
in CLAUDE.md, this hook is what keeps it live turn after turn.

It reads knowledge/operating-with-you.md and looks for a band marker, one of:
    Band: A      (or B / C)
    Tech-comfort band: A
    band=A
(case-insensitive, first match wins). It then prints the one-line rule for that
band. If the file is missing or has no marker (not bootstrapped yet, or the
bootstrap skipped it), it surfaces a gentle default-to-Band-A note rather than
staying silent, because an uncalibrated familiar should err plain and simple.

Pure-Python stdlib only. Fail-open: never raise, never block a session start.
"""

import os
import re
import sys
from pathlib import Path

PACK_HOME = Path(
    os.environ.get(
        "CLAUDE_PROJECT_DIR",
        str(Path.home() / "Familiar"),
    )
)

BAND_RULES = {
    "A": (
        "Band A (hands-off owner). Plain language, outcome-first. No commands, "
        "code, file paths, or error traces on screen. Do the technical work "
        "silently, report the plain result, route around problems yourself, and "
        "only surface a decision they truly have to make. Find the work; do not "
        "wait to be driven."
    ),
    "B": (
        "Band B (interested owner). Plain by default, but show the occasional "
        "command or file and a one-line why when it helps them understand or "
        "trust what happened. Teach lightly when they show interest."
    ),
    "C": (
        "Band C (technical / developer). Speak the language, show commands, "
        "expose the structure (the knowledge corpus, the skills, the hooks). Be "
        "terse and precise; skip the hand-holding."
    ),
}


def read_safe(path: Path) -> str:
    try:
        return path.read_text()
    except (FileNotFoundError, PermissionError, IsADirectoryError):
        return ""


def detect_band(text: str) -> str:
    if not text:
        return ""
    m = re.search(r"(?:tech[- ]comfort\s+band|band)\s*[:=]\s*([abc])\b", text, re.IGNORECASE)
    if m:
        return m.group(1).upper()
    return ""


def main():
    text = read_safe(PACK_HOME / "knowledge" / "operating-with-you.md")
    band = detect_band(text)

    if band in BAND_RULES:
        print(f"[OPERATING-WITH-YOU] {BAND_RULES[band]}")
        return

    # No file or no marker: do not stay silent, nudge toward the safe default.
    print(
        "[OPERATING-WITH-YOU] No tech-comfort band recorded yet in "
        "knowledge/operating-with-you.md. Default to Band A: plain, warm, "
        "outcome-first, no machinery on screen. Establish and record the band "
        "(see the bootstrap section 'How we'll work together')."
    )


if __name__ == "__main__":
    try:
        main()
    except Exception:
        # Fail-open: a surfacing hook must never break a session start.
        sys.exit(0)
