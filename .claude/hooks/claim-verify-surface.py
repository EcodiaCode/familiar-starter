#!/usr/bin/env python3
"""
claim-verify-surface.py - Stop hook for your Familiar.

The factual-verification gate. The familiar bar is "factually verified and
correct": every load-bearing claim on a surface someone reads as authoritative
either cites its source or is marked UNVERIFIED. This hook enforces that without
bricking a non-technical user mid-flow.

When this turn wrote to a deliverable surface (a draft, a brief, a proposal,
outbound mail, a client/people knowledge file, or a mail body) and that content
asserts a load-bearing claim WITHOUT a citation marker, the hook blocks the stop
once and tells the Familiar to cite it or mark it UNVERIFIED before finishing.

Two claim shapes are caught, because these are the two that have actually burned
people:
  1. Named-person role attribution ("Jess is the CEO of Acme", "Kurt runs Co-Exist").
     A wrong one of these in a client-facing brief is a credibility hit.
  2. Confident vendor-UI clickpaths quoted from memory ("click Settings then
     Connectors") when vendors relabel their UI constantly.

A claim is treated as cited (and passes) if the same content carries any of:
  Source:, UNVERIFIED:, <!-- source, verified-from:, "according to", "per her",
  "per the", or a parenthetical "(source ...)".

Loop-safe: respects stop_hook_active so it never blocks twice in a row.
Fail-open: any parse problem exits 0 (silent), never bricks a session.
Pure-Python stdlib only.
"""

import json
import re
import sys
from pathlib import Path

EDITS = {"Write", "Edit", "MultiEdit"}
OUTBOUND = {"gmail_send", "gmail_reply"}

# A write counts as a deliverable surface if its path contains any of these.
DELIVERABLE_MARKERS = (
    "/drafts/",
    "/outbound/",
    "/briefs/",
    "/proposals/",
    "/email/",
    "/mail/",
    "/posts/",
    "/social/",
    "knowledge/clients/",
    "knowledge/people/",
)

# Citation markers: if any appears in the content, treat its claims as sourced.
CITATION_RE = re.compile(
    r"(?:source\s*:|unverified\s*:|<!--\s*source|verified-from\s*:|according to|"
    r"per her\b|per the\b|per his\b|\(source\b)",
    re.IGNORECASE,
)

# Shape 1: a capitalised name asserting a role.
ROLE_RE = re.compile(
    r"\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)?\s+"
    r"(?:is|was|runs|leads|heads|founded|owns|manages|chairs)\s+"
    r"(?:the\s+|a\s+)?"
    r"(?:CEO|CFO|COO|CTO|founder|co-founder|director|head|owner|principal|chair|"
    r"chairman|chairwoman|manager|lead|president|VP|vice president|partner|"
    r"secretary|treasurer)\b",
)

# Shape 2: a vendor anchor word plus a UI-step pattern (a memorised clickpath).
VENDOR_RE = re.compile(
    r"\b(?:linkedin|xero|hubspot|hubdoc|google|gmail|calendar|stripe|vercel|"
    r"notion|mailchimp|slack|quickbooks|canva|squarespace|wordpress|shopify)\b",
    re.IGNORECASE,
)
UI_STEP_RE = re.compile(
    r"\b(?:click|tap|go to|navigate to|select|press|open the|under|in the|head to)\b"
    r"[^.\n]{0,40}\b(?:button|tab|menu|settings|dashboard|panel|field|toggle|"
    r"page|section|dropdown|icon|link)\b",
    re.IGNORECASE,
)


def tool_base_name(name: str) -> str:
    if name.startswith("mcp__"):
        return name.split("__")[-1]
    return name


def is_deliverable_path(path: str) -> bool:
    p = path.lower()
    return any(m in p for m in DELIVERABLE_MARKERS)


def unsourced_claims(content: str) -> list:
    """Return the load-bearing claims in content that lack a citation marker."""
    if not content.strip():
        return []
    if CITATION_RE.search(content):
        # Author has shown their work somewhere in this content; do not nag.
        return []
    findings = []
    m = ROLE_RE.search(content)
    if m:
        findings.append(f"role attribution: \"{m.group(0).strip()}\"")
    if VENDOR_RE.search(content) and UI_STEP_RE.search(content):
        ui = UI_STEP_RE.search(content)
        findings.append(f"vendor clickpath from memory: \"{ui.group(0).strip()}\"")
    return findings


def main() -> None:
    try:
        payload = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return
    if not isinstance(payload, dict):
        return
    if payload.get("stop_hook_active"):
        return  # never loop

    transcript_path = payload.get("transcript_path")
    if not transcript_path:
        return
    try:
        lines = Path(transcript_path).read_text().splitlines()
    except (FileNotFoundError, PermissionError, OSError):
        return

    flagged = []  # (label, [claims])

    for line in lines:
        line = line.strip()
        if not line:
            continue
        try:
            evt = json.loads(line)
        except (json.JSONDecodeError, ValueError):
            continue
        msg = evt.get("message") if isinstance(evt, dict) else None
        content_blocks = msg.get("content") if isinstance(msg, dict) else None
        if not isinstance(content_blocks, list):
            continue
        for block in content_blocks:
            if not isinstance(block, dict) or block.get("type") != "tool_use":
                continue
            name = tool_base_name(str(block.get("name", "")))
            tin = block.get("input", {}) or {}
            text = ""
            label = ""
            if name in EDITS:
                fp = str(tin.get("file_path", "") or "")
                if not is_deliverable_path(fp):
                    continue
                text = str(tin.get("content", "") or tin.get("new_string", "") or "")
                label = fp
            elif name in OUTBOUND:
                text = str(tin.get("body", "") or "")
                label = "outbound mail: " + str(tin.get("subject", "") or "(no subject)")
            else:
                continue
            claims = unsourced_claims(text)
            if claims:
                flagged.append((label, claims))

    if not flagged:
        return  # clean: allow the stop

    # Build the block reason. Cap at a few so the message stays readable.
    lines_out = [
        "Before you stop: this turn wrote load-bearing factual claims to a "
        "surface someone reads as authoritative, with no source shown. The "
        "familiar bar is factually verified and correct: cite each claim inline "
        "(Source: ...) against where it came from, or mark it UNVERIFIED: and "
        "name the gap. For a vendor clickpath, drive the live surface and quote "
        "what is actually on screen rather than a path from memory. Findings:",
    ]
    for label, claims in flagged[:5]:
        lines_out.append(f"  - {label}: " + "; ".join(claims))
    lines_out.append(
        "Add the citations or UNVERIFIED markers, then finish. (If a flagged "
        "line is genuinely not load-bearing, an inline Source: or a one-word "
        "context note clears it.)"
    )
    print(json.dumps({"decision": "block", "reason": "\n".join(lines_out)}))


if __name__ == "__main__":
    main()
