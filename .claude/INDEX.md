# Familiar `.claude/` bundle v1 - scope + ship state

This is Familiar's project-scoped skills + hooks substrate. Mirrors EcodiaOS's own `.claude/` shape, scaled down for a single-principal EA pack. Lives at `<PERSONA_HOME>/.claude/` and gets discovered the moment you opens the folder in VSCode.

## Skills planned (11)

| skill                  | status      | purpose                                                       |
|------------------------|-------------|---------------------------------------------------------------|
| pattern-codify         | shipped v1  | file durable rules when you states one                   |
| cdp-usage              | shipped v1  | drive Chrome via CDP for browser-only surfaces                |
| status-board-update    | shipped v1  | maintain status-board.md as single source of truth            |
| voice-drift-correct    | planned     | periodic check of recent outbound vs locked voice profile     |
| inbox-triage           | planned     | sort morning Gmail by Familiar heuristics + flag what needs eyes  |
| outbound-draft         | planned     | draft outbound mail with recipient + voice + spend gates      |
| client-prep            | planned     | CRM + recent thread + calendar to one-page brief              |
| memory-write           | planned     | structured writes to her knowledge corpus                     |
| routine-add            | planned     | schedule new claude.ai Routines from chat                     |
| graphic-generate       | planned     | brand graphics in her voice                                   |
| outbound-mail-gate     | planned     | composite check on recipient + voice + topic before send      |

## Hooks planned (7)

| hook                       | status      | purpose                                                |
|----------------------------|-------------|--------------------------------------------------------|
| voice-score-outbound       | shipped v1  | PostToolUse, score outbound drafts vs voice profile    |
| session-start-surface      | planned     | SessionStart, surface P1/P2 + cal + inbox flags        |
| knowledge-corpus-surface   | planned     | UserPromptSubmit, surface relevant corpus slice        |
| outbound-mail-gate         | planned     | PreToolUse on gmail_send, recipient + voice + topics   |
| spend-cap-gate             | planned     | PreToolUse on spend-bearing ops, dollar threshold check|
| end-of-session-episode     | planned     | Stop, write episodes/<date>.md if session substantive  |
| pre-compact-checkpoint     | planned     | PreCompact, defensive episode before context compress  |

## Authoring conventions

- **Skills**: SKILL.md frontmatter + markdown body. Frontmatter: `name`, `description`. Optional: `allowed-tools`.
- **Hooks**: pure-Python stdlib only. No venv on the customer Mac. Read input from stdin as JSON.
- **Both**: reference `<PERSONA_HOME>` via the `PERSONA_HOME` env var or `${CLAUDE_PROJECT_DIR}` in command strings.

## Iteration

Pack iteration happens from your actual usage friction over the next 7 days. As she hits a use case the v1 bundle does not cover, the relevant skill or hook gets built from the v1 template, tested, and rsynced to her `<PERSONA_HOME>/.claude/` via the Tailscale upgrade mechanism.

The full bundle does NOT ship on day 1. The 2 shipped skills + 1 shipped hook are the canonical templates from which the rest are forked when use cases justify them.

## Why project-scoped, not global

Global skills at `~/.claude/skills/` would apply to every Claude Code session on your Mac, even ones unrelated to Familiar. Project-scoped keeps the pack self-contained, prevents collision with any other Claude Code use she has, and means a Tailscale rsync to her `<PERSONA_HOME>/.claude/` propagates updates cleanly with zero global-state mutation.
