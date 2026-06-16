#!/usr/bin/env python3
"""
skill-trigger-surface.py - UserPromptSubmit hook for {{FAMILIAR_NAME}}.

When {{CUSTOMER_FIRST_NAME}} mentions a keyword tied to a workflow, this hook
reminds {{FAMILIAR_NAME}} that a skill exists for it, or that one is worth
building. It reads a data file, keyword-triggers.json, so {{CUSTOMER_FIRST_NAME}}
and {{FAMILIAR_NAME}} can add their own triggers without touching Python. The
skill-creator skill walks through editing that file.

Contract: reads the UserPromptSubmit event JSON from stdin (the prompt is in
the "prompt" field), prints any matching reminders to stdout. stdout is injected
into the session as context. Silent when nothing matches. Pure stdlib, never
raises.
"""

import json
import re
import sys
from pathlib import Path

TRIGGERS_FILE = Path(__file__).resolve().parent / "keyword-triggers.json"


def read_prompt() -> str:
    try:
        data = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return ""
    if isinstance(data, dict):
        return str(data.get("prompt", "") or "")
    return ""


def load_triggers() -> list:
    try:
        data = json.loads(TRIGGERS_FILE.read_text())
    except (FileNotFoundError, PermissionError, json.JSONDecodeError, ValueError):
        return []
    if isinstance(data, dict):
        triggers = data.get("triggers", [])
        return triggers if isinstance(triggers, list) else []
    return []


def keyword_hit(prompt_lc: str, keyword: str) -> bool:
    kw = keyword.strip().lower()
    if not kw:
        return False
    # Word-boundary match so "money" does not fire inside "moneyball", and
    # multi-word phrases like "bank rec" match as a contiguous run.
    pattern = r"(?<![a-z0-9])" + re.escape(kw) + r"(?![a-z0-9])"
    return re.search(pattern, prompt_lc) is not None


def main() -> None:
    prompt = read_prompt()
    if not prompt.strip():
        return
    prompt_lc = prompt.lower()

    surfaced = []
    seen = set()
    for trig in load_triggers():
        if not isinstance(trig, dict):
            continue
        skill = str(trig.get("skill", "") or "")
        if skill in seen:
            continue
        keywords = trig.get("keywords", [])
        if not isinstance(keywords, list):
            continue
        if any(keyword_hit(prompt_lc, str(k)) for k in keywords):
            reminder = str(trig.get("reminder", "") or "").strip()
            if reminder:
                label = str(trig.get("label", "") or "SKILL-TRIGGER").strip()
                surfaced.append(f"[{label}] {reminder}")
                seen.add(skill)

    if surfaced:
        print("\n".join(surfaced))


if __name__ == "__main__":
    main()
