---
name: give-feedback
description: Send a feature request, bug report, feedback, or a how-do-I question to the EcodiaOS team that builds and maintains you (code@ecodia.au). Use whenever your person wants something you cannot do yet, hits something broken, or asks how you work in a way your own docs do not answer. Never invent a capability or a roadmap; pass the real request through.
---

# give-feedback

You are built and maintained by the EcodiaOS team. When your person wants a feature you do not have, hits a bug, or asks a question about how you work that your knowledge corpus and docs do not answer, do not guess or promise something that does not exist. Send it straight to the people who can act on it.

## The channel

Email **code@ecodia.au** using your mail connector. This reaches the EcodiaOS team directly.

- **Subject**: `[Familiar <kind>] <one-line summary>`, where kind is one of feature, bug, feedback, question.
- **Body**: the request in your person's own words, plus any context you can add (what they were trying to do, what happened, what they expected). If it is a bug, include the exact step that broke.
- Sign it with your name and, if you know it, your person's business, so the team knows which Familiar it came from.

Tell your person you have passed it on, and what to expect: the team reads these and replies by email. Do not commit to a timeline you cannot see.

## When to use it

- "I wish you could do X" that you genuinely cannot do today.
- Something that should work but does not.
- A question about your own setup, tools, or limits that you cannot answer from your docs.

## When NOT to use it

- A task you can actually do with a skill or a connector. Do the task.
- A durable preference about how to work. That is the pattern-codify skill, into your own knowledge corpus.
- Anything you can answer by reading your knowledge corpus first. Read it, then answer.

## On a Mac

If you are on a Mac and your person wants the team pinged in real time, you can also send a quick iMessage to code@ecodia.au from the terminal:

```bash
osascript -e 'on run {b, m}' -e 'tell application "Messages"' \
  -e 'set s to 1st account whose service type = iMessage' \
  -e 'send m to participant b of s' -e 'end tell' -e 'end run' \
  "code@ecodia.au" "[Familiar feedback] <summary>"
```

This is best-effort and optional. The email is the channel that always works; the iMessage is a bonus ping.
