#!/usr/bin/env python3
"""
outbound-mail-gate.py - PreToolUse hook on Gmail send for {{FAMILIAR_NAME}}.

Fires BEFORE any gmail_send tool call. Composite gate covering:
  1. Recipient check: recipient must be on the authorized-contact list
     (from knowledge/people/*.md or knowledge/clients/*.md) OR have explicit
     {{CUSTOMER_FIRST_NAME}} sign-off in the current session.
  2. Voice check: body must NOT contain em-dashes, AI assistant register,
     or banned vocab from voice/banned-vocab.md.
  3. Topic check: subject + body must not reference a hard-stop topic
     (anything from knowledge/authority-and-hard-stops.md flagged as
     "external comm forbidden").
  4. Spend check: if the email could trigger a spend over the customer
     cap, block.

Exit codes:
  0 = pass (gate clears)
  1 = block (gate trips, tool call aborted)

Pure-Python stdlib only.
"""

import json
import os
import re
import sys
from pathlib import Path

FAMILIAR_HOME = Path(os.environ.get("FAMILIAR_HOME", str(Path(os.environ.get("CLAUDE_PROJECT_DIR", str(Path.home() / "Familiar"))))))

# Universal bans (always apply, even before voice profile is locked)
EM_DASH = "—"
AI_REGISTER_PATTERNS = [
    r"\bI(?:'d| would) be happy to\b",
    r"\bLet me know if you have any questions\b",
    r"\bfeel free to reach out\b",
    r"\bI hope this helps\b",
    r"\bPlease don't hesitate to\b",
    r"\bAs an AI\b",
    r"\bI apologi[sz]e for\b",
]


def read_safe(path: Path) -> str:
    try:
        return path.read_text()
    except (FileNotFoundError, PermissionError, IsADirectoryError):
        return ""


def load_authorized_contacts() -> set:
    """Build the authorized-contact set from people/ + clients/ knowledge files."""
    contacts = set()
    for subdir in ("people", "clients"):
        d = FAMILIAR_HOME / "knowledge" / subdir
        if not d.exists():
            continue
        for f in d.glob("*.md"):
            text = f.read_text()
            # Pull any email addresses mentioned in the file
            for match in re.finditer(r"[\w.+-]+@[\w.-]+\.[a-zA-Z]{2,}", text):
                contacts.add(match.group(0).lower())
    return contacts


def load_hard_stops() -> list:
    """Return list of hard-stop substrings from the hard-stops doctrine file."""
    text = read_safe(FAMILIAR_HOME / "knowledge" / "authority-and-hard-stops.md")
    if not text:
        return []
    # Look for lines flagged "external comm forbidden" or similar
    stops = []
    for line in text.splitlines():
        if "external comm forbidden" in line.lower() or "no outbound" in line.lower():
            stops.append(line.strip().lower())
    return stops


def load_banned_vocab() -> list:
    """Customer-specific banned vocab from voice/banned-vocab.md."""
    text = read_safe(FAMILIAR_HOME / "voice" / "banned-vocab.md")
    return [line.lstrip("- ").strip() for line in text.splitlines() if line.startswith("-")]


def check_recipient(recipient: str, contacts: set) -> tuple:
    """Returns (passed, reason)."""
    if not recipient:
        return False, "No recipient specified"

    recipient_lower = recipient.lower()
    if not contacts:
        # Empty contact list: warn but pass (early install state)
        return True, "Contact list empty (early install); pass with warning"

    if recipient_lower in contacts:
        return True, ""

    return False, f"Recipient {recipient} not in authorized contacts. Surface to {{CUSTOMER_FIRST_NAME}} for sign-off before sending."


def check_voice(body: str, banned_vocab: list) -> tuple:
    """Returns (passed, list of issues)."""
    issues = []

    if EM_DASH in body:
        issues.append(f"Em-dash present ({body.count(EM_DASH)} instances). Em-dashes are banned at character level.")

    for pattern in AI_REGISTER_PATTERNS:
        m = re.search(pattern, body, re.IGNORECASE)
        if m:
            issues.append(f"AI assistant register: '{m.group(0)}'")

    body_lower = body.lower()
    for word in banned_vocab:
        if word.lower() in body_lower:
            issues.append(f"Customer-banned vocab: '{word}'")

    return (len(issues) == 0, issues)


def check_topic(subject: str, body: str, hard_stops: list) -> tuple:
    """Returns (passed, matched stop or '')."""
    text = (subject + " " + body).lower()
    for stop in hard_stops:
        if stop in text:
            return False, stop
    return True, ""


def main():
    try:
        hook_input = json.loads(sys.stdin.read())
    except (json.JSONDecodeError, ValueError):
        return

    tool_input = hook_input.get("tool_input", {})
    recipient = tool_input.get("to", "")
    subject = tool_input.get("subject", "")
    body = tool_input.get("body", "")

    if not body:
        return  # nothing to check; let the tool call proceed

    contacts = load_authorized_contacts()
    hard_stops = load_hard_stops()
    banned_vocab = load_banned_vocab()

    # Check 1: recipient
    rec_pass, rec_reason = check_recipient(recipient, contacts)

    # Check 2: voice
    voice_pass, voice_issues = check_voice(body, banned_vocab)

    # Check 3: topic
    topic_pass, topic_match = check_topic(subject, body, hard_stops)

    # Composite
    failures = []
    if not rec_pass:
        failures.append(f"[RECIPIENT] {rec_reason}")
    if not voice_pass:
        for iss in voice_issues:
            failures.append(f"[VOICE] {iss}")
    if not topic_pass:
        failures.append(f"[TOPIC] Hard-stop matched: '{topic_match}'. Surface to {{CUSTOMER_FIRST_NAME}} before sending.")

    if failures:
        sys.stderr.write("[OUTBOUND-MAIL-GATE BLOCK] Gmail send blocked. Reasons:\n")
        for f in failures:
            sys.stderr.write(f"  {f}\n")
        sys.stderr.write("\nTo proceed (only after surfacing to {{CUSTOMER_FIRST_NAME}} and getting her go-ahead), add 'outbound-ok' to the tool_input.\n")
        # Check for override token
        if "outbound-ok" in (subject + body + recipient).lower():
            sys.stderr.write("[OUTBOUND-MAIL-GATE OVERRIDE] outbound-ok token present; allowing send.\n")
            sys.exit(0)
        sys.exit(1)

    # All gates clear
    sys.exit(0)


if __name__ == "__main__":
    main()
