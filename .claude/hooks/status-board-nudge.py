#!/usr/bin/env python3
"""
status-board-nudge.py - Stop hook for {{FAMILIAR_NAME}}.

Keeps the status board absolutely current. When a turn did substantive,
state-changing work but never touched status-board.md, this hook blocks the
stop once and tells {{FAMILIAR_NAME}} to update the board before finishing.

"Substantive" is a deliberately high bar so trivial turns are not nagged:
  - at least one outbound (a Gmail send or reply), OR
  - two or more file Write/Edit operations
AND status-board.md was not written this turn.

Loop-safe: respects stop_hook_active so it never blocks twice in a row.
Fail-open: any parsing problem exits 0 (silent), never bricks a session.

Reads the Stop event JSON from stdin (fields: transcript_path, stop_hook_active).
Emits {"decision": "block", "reason": ...} to ask the model to continue, or
exits 0 to allow the stop.
"""

import json
import sys
from pathlib import Path

# Tool names that count as a real state change worth tracking on the board.
OUTBOUND = {"gmail_send", "gmail_reply"}
EDITS = {"Write", "Edit", "MultiEdit"}


def tool_base_name(name: str) -> str:
    # MCP tools arrive as mcp__<server>__<tool>; reduce to the bare tool name.
    if name.startswith("mcp__"):
        return name.split("__")[-1]
    return name


def main() -> None:
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return
    if not isinstance(payload, dict):
        return

    # Never loop: if we already blocked once this stop, let it through.
    if payload.get("stop_hook_active"):
        return

    transcript_path = payload.get("transcript_path")
    if not transcript_path:
        return
    try:
        lines = Path(transcript_path).read_text().splitlines()
    except (FileNotFoundError, PermissionError, OSError):
        return

    edits = 0
    outbound = 0
    board_touched = False

    for line in lines:
        line = line.strip()
        if not line:
            continue
        try:
            evt = json.loads(line)
        except (json.JSONDecodeError, ValueError):
            continue
        # Walk assistant message content for tool_use blocks.
        msg = evt.get("message") if isinstance(evt, dict) else None
        content = msg.get("content") if isinstance(msg, dict) else None
        if not isinstance(content, list):
            continue
        for block in content:
            if not isinstance(block, dict) or block.get("type") != "tool_use":
                continue
            name = tool_base_name(str(block.get("name", "")))
            tin = block.get("input", {}) or {}
            if name in EDITS:
                edits += 1
                fp = str(tin.get("file_path", "") or "")
                if fp.endswith("status-board.md"):
                    board_touched = True
            elif name in OUTBOUND:
                outbound += 1
            elif name in ("knowledge_write",):
                # A board row is markdown; a write to it via the knowledge tool counts too.
                rp = str(tin.get("relpath", "") or "")
                if rp.endswith("status-board.md"):
                    board_touched = True

    substantive = outbound >= 1 or edits >= 2
    if substantive and not board_touched:
        reason = (
            "This turn changed real state "
            f"({outbound} outbound, {edits} file edits) but did not update "
            "status-board.md. Before you stop: open the status board, add or "
            "update the row for whatever you just moved (client, project, task, "
            "or thread), set its next-action and owner, and move anything you "
            "resolved to archived. Keeping the board current is non-negotiable. "
            "Then finish."
        )
        print(json.dumps({"decision": "block", "reason": reason}))
        return
    # Otherwise allow the stop.


if __name__ == "__main__":
    main()
