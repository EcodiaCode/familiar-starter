#!/usr/bin/env python3
"""
voice-score-outbound.py - PostToolUse hook for Familiar.

Fires after Write/Edit tool calls that look like outbound mail or post drafts.
Scores the content against your locked voice profile and surfaces drift.

Writes a sidecar file the next UserPromptSubmit hook can surface so Familiar sees
the feedback in the next turn and self-corrects without you having to flag it.

Pure-Python stdlib only. Reads the locked voice profile from
<PERSONA_HOME>/voice/profile.md and the banned-vocab list from
<PERSONA_HOME>/voice/banned-vocab.md.

When the voice profile is not yet locked (pre-extraction), the hook still
catches the universal bans: em-dashes and AI-assistant register.
"""

import json
import os
import sys
from pathlib import Path

PERSONA_HOME = Path(os.environ.get("PERSONA_HOME", str(Path.home() / "familiar")))
SIDECAR_PATH = PERSONA_HOME / ".claude" / ".voice-score-sidecar"

# Universal bans, apply even before voice profile is locked
UNIVERSAL_BANNED_VOCAB = [
    "leverage",
    "synergy",
    "robust",
    "comprehensive",
    "seamless",
    "delve",
    "navigate",
    "embark",
    "elevate",
    "unlock",
    "ecosystem",
    "holistic",
]

# AI-assistant register phrases that violate the named-author voice
AI_ASSISTANT_REGISTER = [
    "i'd be happy to",
    "i would be happy to",
    "let me know if you have any questions",
    "feel free to reach out",
    "i hope this helps",
    "please don't hesitate to",
    "as an ai",
]


def is_outbound_draft(tool_input: dict) -> bool:
    """Heuristic: did the tool call write outbound mail or social content?"""
    path = tool_input.get("file_path", "").lower()
    if not path:
        return False
    outbound_markers = [
        "/drafts/",
        "/outbound/",
        "/email/",
        "/posts/",
        "/social/",
        "/mail/",
    ]
    return any(marker in path for marker in outbound_markers)


def load_banned_vocab() -> list:
    """Load your custom banned vocab + add universal bans."""
    custom = []
    banned_path = PERSONA_HOME / "voice" / "banned-vocab.md"
    if banned_path.exists():
        for line in banned_path.read_text().splitlines():
            stripped = line.lstrip("- ").strip()
            if stripped and not stripped.startswith("#"):
                custom.append(stripped)
    return UNIVERSAL_BANNED_VOCAB + custom


def check_em_dashes(content: str) -> int:
    """U+2014 is banned at character level. Always."""
    return content.count("—")


def check_banned_vocab(content: str, banned: list) -> list:
    """Return list of banned words found (case-insensitive substring match)."""
    hits = []
    lower = content.lower()
    for word in banned:
        if word.lower() in lower:
            hits.append(word)
    return hits


def check_assistant_register(content: str) -> list:
    """Catch AI-assistant register phrases that violate named-author voice."""
    hits = []
    lower = content.lower()
    for phrase in AI_ASSISTANT_REGISTER:
        if phrase in lower:
            hits.append(phrase)
    return hits


def main():
    try:
        hook_input = json.loads(sys.stdin.read())
    except (json.JSONDecodeError, ValueError):
        return

    tool_input = hook_input.get("tool_input", {})
    if not is_outbound_draft(tool_input):
        return

    # Write tool uses "content"; Edit uses "new_string"
    content = tool_input.get("content", "") or tool_input.get("new_string", "")
    if not content:
        return

    banned = load_banned_vocab()
    em_dashes = check_em_dashes(content)
    banned_hits = check_banned_vocab(content, banned)
    register_hits = check_assistant_register(content)

    if em_dashes == 0 and not banned_hits and not register_hits:
        # Silent pass
        if SIDECAR_PATH.exists():
            SIDECAR_PATH.unlink()
        return

    findings = []
    if em_dashes:
        findings.append(f"em_dashes={em_dashes} (banned at character level)")
    if banned_hits:
        findings.append(f"banned_vocab={banned_hits}")
    if register_hits:
        findings.append(f"ai_assistant_register={register_hits}")

    file_path = tool_input.get("file_path", "<unknown>")

    SIDECAR_PATH.parent.mkdir(parents=True, exist_ok=True)
    SIDECAR_PATH.write_text(
        f"[VOICE-SCORE FAIL] {file_path}\n"
        f"  {chr(10).join(findings)}\n"
        f"  Outbound draft violates voice gate. Rewrite before sending.\n"
    )


if __name__ == "__main__":
    main()
