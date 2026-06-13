#!/usr/bin/env python3
"""
end-of-session-episode.py - Stop hook for {{PERSONA_NAME}}.

Fires when a Claude Code session ends. If the session was substantive
(produced file changes, status-board updates, or outbound drafts), writes
an episode to episodes/<YYYY-MM-DD>.md with a session summary.

Substantive criteria:
- Session length > 5 minutes since SessionStart
- At least one Write or Edit happened
- OR at least one outbound (Gmail send) happened
- OR status-board.md was touched

Pure-Python stdlib only.

NOTE: this hook reads its session metadata from Claude Code's stop-event JSON
payload via stdin. It expects fields: session_id, started_at, files_modified,
tool_calls. If absent, falls back to a best-effort "I am here" episode.
"""

import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

PERSONA_HOME = Path(os.environ.get("PERSONA_HOME", str(Path(os.environ.get("CLAUDE_PROJECT_DIR", str(Path.home() / "Familiar"))))))


def aest_today() -> str:
    # Brisbane is UTC+10 year-round (no DST)
    from datetime import timedelta
    aest = timezone(timedelta(hours=10))
    return datetime.now(aest).strftime("%Y-%m-%d")


def aest_time() -> str:
    from datetime import timedelta
    aest = timezone(timedelta(hours=10))
    return datetime.now(aest).strftime("%H:%M")


def is_substantive(payload: dict) -> bool:
    """Heuristic for whether to write an episode at all."""
    files_modified = payload.get("files_modified", [])
    tool_calls = payload.get("tool_calls", [])

    # Any write or edit at all
    if files_modified:
        return True

    # Any outbound mail send
    for call in tool_calls:
        name = call.get("name", "")
        if "gmail_send" in name or "outbound" in name:
            return True

    # Session length > 5 minutes
    started_at = payload.get("started_at")
    if started_at:
        try:
            start = datetime.fromisoformat(started_at.replace("Z", "+00:00"))
            now = datetime.now(timezone.utc)
            if (now - start).total_seconds() > 300:
                return True
        except (ValueError, AttributeError):
            pass

    return False


def main():
    try:
        payload = json.loads(sys.stdin.read())
    except (json.JSONDecodeError, ValueError):
        payload = {}

    if not is_substantive(payload):
        return  # silent — nothing worth recording

    files_modified = payload.get("files_modified", [])
    tool_calls = payload.get("tool_calls", [])

    # Build the episode entry
    entry = [
        f"## {aest_time()} session",
    ]

    # Status board changes
    if any("status-board" in f for f in files_modified):
        entry.append("- Status board updated this session")

    # Outbound mail
    outbound_count = sum(1 for c in tool_calls if "gmail_send" in c.get("name", ""))
    if outbound_count:
        entry.append(f"- Outbound mail sent: {outbound_count}")

    # File changes summary
    if files_modified:
        entry.append(f"- Files modified: {len(files_modified)}")
        # List up to 5 specific files for searchability
        for f in files_modified[:5]:
            entry.append(f"  - {f}")
        if len(files_modified) > 5:
            entry.append(f"  - (and {len(files_modified) - 5} more)")

    # Knowledge corpus writes specifically
    knowledge_writes = [f for f in files_modified if "knowledge/" in f]
    if knowledge_writes:
        entry.append(f"- Knowledge corpus additions: {len(knowledge_writes)}")

    # Voice samples touched
    voice_writes = [f for f in files_modified if "voice/" in f]
    if voice_writes:
        entry.append(f"- Voice substrate touched: {len(voice_writes)}")

    # Write to the episode file
    episodes_dir = PERSONA_HOME / "episodes"
    episodes_dir.mkdir(parents=True, exist_ok=True)
    episode_file = episodes_dir / f"{aest_today()}.md"

    # Append (preserves multiple sessions per day)
    existing = ""
    if episode_file.exists():
        existing = episode_file.read_text()
    elif not existing.startswith("# "):
        existing = f"# Episodes for {aest_today()}\n\n"

    with episode_file.open("a") as f:
        if not existing:
            f.write(f"# Episodes for {aest_today()}\n\n")
        f.write("\n".join(entry))
        f.write("\n\n")


if __name__ == "__main__":
    main()
