#!/usr/bin/env python3
"""
sidecar-surface.py - UserPromptSubmit hook for your Familiar.

Closes the feedback loop for the PostToolUse scorers. A hook like
voice-score-outbound.py writes a one-shot "sidecar" file when it catches drift
(an em-dash, AI-assistant register, banned vocab in an outbound draft), but a
sidecar only does anything if something surfaces it on the next turn. This hook
is that something.

On every prompt it looks for any pending sidecar under FAMILIAR_HOME/.claude
matching `.*-sidecar`, prints the contents to stdout (which Claude Code injects
into the session as context so your Familiar reads it before acting), and
then deletes it so the warning fires exactly once. Generic by design: any future
PostToolUse scorer can drop a `.claude/.<name>-sidecar` file and it surfaces for
free, no change to this hook.

Pure-Python stdlib only. Fail-open: any problem exits 0 (silent), never bricks a
turn or blocks a prompt.
"""

import os
import sys
from pathlib import Path

FAMILIAR_HOME = Path(os.environ.get("FAMILIAR_HOME", str(Path.home() / "resi")))
SIDECAR_DIR = FAMILIAR_HOME / ".claude"


def main() -> None:
    # Drain stdin so the hook harness does not block; we do not need the prompt.
    try:
        sys.stdin.read()
    except (OSError, ValueError):
        pass

    try:
        if not SIDECAR_DIR.is_dir():
            return
        # Hidden one-shot sidecar files, e.g. .voice-score-sidecar
        pending = sorted(SIDECAR_DIR.glob(".*-sidecar"))
    except (OSError, PermissionError):
        return

    surfaced = []
    for f in pending:
        try:
            text = f.read_text().strip()
        except (OSError, PermissionError):
            continue
        if text:
            surfaced.append(text)
        # One-shot: remove whether or not it had content, so it never re-fires.
        try:
            f.unlink()
        except (OSError, PermissionError):
            pass

    if surfaced:
        print("\n".join(surfaced))


if __name__ == "__main__":
    main()
