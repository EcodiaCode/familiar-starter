#!/usr/bin/env python3
"""
session-start-surface.py - SessionStart hook for {{FAMILIAR_NAME}}.

Fires when a new Claude Code session starts in FAMILIAR_HOME. Reads the
customer's active substrate and surfaces the load-bearing facts so {{FAMILIAR_NAME}}
opens with awareness of what's currently active.

What it surfaces (when present):
- P1 + P2 rows from status-board.md
- Any pending install steps from onboarding/install-log.md (last open step)
- Today's calendar items if a recent cache exists at routines/cache/calendar-today.json
- Any unread urgent flags from a routines/cache/inbox-flags.json

Pure-Python stdlib only. No external deps.
"""

import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

FAMILIAR_HOME = Path(os.environ.get("FAMILIAR_HOME", str(Path(os.environ.get("CLAUDE_PROJECT_DIR", str(Path.home() / "Familiar"))))))


def read_safe(path: Path) -> str:
    """Read file or return empty string. Never raise."""
    try:
        return path.read_text()
    except (FileNotFoundError, PermissionError, IsADirectoryError):
        return ""


def parse_priority_rows(status_board: str) -> dict:
    """Pull P1 and P2 row counts and names from the status board."""
    if not status_board:
        return {}

    sections = {}
    current = None
    for line in status_board.splitlines():
        m = re.match(r"^## (P\d)", line)
        if m:
            current = m.group(1)
            sections[current] = []
            continue
        if current and re.match(r"^### ", line):
            sections[current].append(line[4:].strip())

    return {k: v for k, v in sections.items() if v}


def find_open_install_step(install_log: str) -> str:
    """Return the last install-bootstrap step that is not marked success."""
    if not install_log:
        return ""

    # Look for the last "Outcome:" line that is not "success"
    last_open = ""
    current_step = ""
    for line in install_log.splitlines():
        if line.startswith("Step:"):
            current_step = line.split(":", 1)[1].strip()
        if line.startswith("Outcome:") and "success" not in line.lower():
            last_open = current_step

    return last_open


def main():
    surfacing = []

    # Status board P1 + P2
    status_board = read_safe(FAMILIAR_HOME / "status-board.md")
    rows = parse_priority_rows(status_board)
    if "P1" in rows:
        surfacing.append(f"[STATUS-BOARD] P1 ({len(rows['P1'])} rows): " + "; ".join(rows["P1"][:3]))
    if "P2" in rows:
        surfacing.append(f"[STATUS-BOARD] P2 ({len(rows['P2'])} rows): " + "; ".join(rows["P2"][:3]))

    # Open install step
    install_log = read_safe(FAMILIAR_HOME / "onboarding" / "install-log.md")
    open_step = find_open_install_step(install_log)
    if open_step:
        surfacing.append(f"[INSTALL-PENDING] Last unfinished step: {open_step}")

    # Calendar cache (lands when Routines wire up)
    cal_cache = read_safe(FAMILIAR_HOME / "routines" / "cache" / "calendar-today.json")
    if cal_cache:
        try:
            data = json.loads(cal_cache)
            events = data.get("events", [])
            if events:
                surfacing.append(f"[CALENDAR-TODAY] {len(events)} events: " + "; ".join(
                    e.get("summary", "?") for e in events[:3]
                ))
        except json.JSONDecodeError:
            pass

    # Inbox urgent flags
    inbox_cache = read_safe(FAMILIAR_HOME / "routines" / "cache" / "inbox-flags.json")
    if inbox_cache:
        try:
            data = json.loads(inbox_cache)
            flags = data.get("flags", [])
            if flags:
                surfacing.append(f"[INBOX-URGENT] {len(flags)} flagged: " + "; ".join(
                    f.get("subject", "?") for f in flags[:3]
                ))
        except json.JSONDecodeError:
            pass

    if not surfacing:
        return  # silent - nothing to surface

    print("\n".join(surfacing))


if __name__ == "__main__":
    main()
