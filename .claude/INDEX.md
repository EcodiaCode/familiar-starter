# Familiar `.claude/` bundle - what is in here

This is Familiar's project-scoped skills and hooks substrate. It mirrors the shape EcodiaOS runs on itself, scaled for a single-person assistant pack. Claude Code discovers it the moment the Familiar folder opens in VS Code.

## Skills (10 shipped)

| skill               | purpose                                                                |
|---------------------|------------------------------------------------------------------------|
| connector-setup     | walk your person through claude.ai connectors (mail, calendar, drive)  |
| daily-brief         | open the day: status board + calendar + inbox in one tight message     |
| email-triage        | sort the inbox: needs-them / drafted / noise, never send unapproved    |
| voice-capture       | collect writing samples, build and maintain the voice profile          |
| weekly-review       | sweep the board weekly, name what moved, set next week                 |
| self-improve        | capture friction, codify learnings, feed pack gaps upstream            |
| pattern-codify      | file durable rules the moment your person states one                   |
| status-board-update | maintain status-board.md as the single source of truth                 |
| pack-update         | pull upstream improvements safely, never touching their files          |
| cdp-usage           | drive Chrome for browser-only surfaces, with standing permission       |

## Hooks (8 shipped, registered in settings.json)

| hook                   | event                      | purpose                                            |
|------------------------|----------------------------|----------------------------------------------------|
| session-start-surface  | SessionStart               | surface P1/P2 + today's calendar + inbox flags     |
| skill-trigger-surface  | UserPromptSubmit           | keyword to skill reminders from keyword-triggers.json |
| sidecar-surface        | UserPromptSubmit           | surface and clear one-shot scorer sidecars (voice drift) |
| outbound-mail-gate     | PreToolUse on mail send    | recipient + voice + hard-stop check before send    |
| voice-score-outbound   | PostToolUse on Write/Edit  | score outbound drafts against the voice profile    |
| claim-verify-surface   | Stop                       | block once if a deliverable asserts an uncited load-bearing claim |
| status-board-nudge     | Stop                       | block once if a state-changing turn left the board stale |
| end-of-session-episode | Stop                       | write episodes/<date>.md when a session mattered   |

## Authoring conventions

- **Skills**: SKILL.md with frontmatter (`name`, `description`) + a markdown body one page or less.
- **Hooks**: pure-Python stdlib only. No venv on the customer machine. Read input from stdin as JSON.
- **Paths**: hooks resolve the pack folder via `CLAUDE_PROJECT_DIR`, falling back to `~/Familiar`.

## How this evolves

EcodiaOS ships improvements to the upstream template (`EcodiaCode/familiar-starter`); your pack pulls them via the pack-update skill. Gaps you hit go to `knowledge/pack-feedback.md` (see self-improve) and the fix arrives upstream for every Familiar at once.

## Why project-scoped, not global

Global skills at `~/.claude/skills/` would apply to every Claude Code session on the machine, even ones unrelated to Familiar. Project-scoped keeps the pack self-contained, avoids collisions, and means a clean `git pull` propagates updates with zero global-state mutation.
