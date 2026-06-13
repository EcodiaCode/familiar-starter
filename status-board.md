# your status board

This is the single source of truth for what is currently happening in your work. Familiar reads it on every session start. Familiar updates it the same turn she acts on a tracked entity. you reads it whenever she wants to see what is on her plate without asking.

Stale memory is worse than no memory. The status board IS the live memory.

## P1 - Urgent (acting today or this week)

(empty - rows here get attention first)

## P2 - This sprint (next 2 weeks)

(empty)

## P3 - Tracked (longer arc)

(empty)

## Archived

(empty - resolved or stale rows move here with a resolution note; never deleted, so the durable record holds)

---

## Row format

Each row is a level-3 subsection with these fields:

```
### <entity-slug-YYYY-MM-DD>
**Type**: client | project | task | thread | infrastructure | opportunity | personal | legal
**Name**: <human-readable name>
**Status**: <one-line state>
**Next action by**: angelica | familiar | external
**Context**: <2 to 4 lines, enough that Familiar opening this cold knows what to do>
**Last touched**: <YYYY-MM-DD>
```

## How Familiar maintains this file

- On session start, read the whole file. Surface P1 and P2 to you in the opening response if anything material has changed.
- When acting on a tracked entity, update the row's status and last_touched in the same turn. Do not batch updates across turns.
- When work resolves, move the row to Archived with a one-line resolution note. Do not delete.
- When something new emerges that warrants tracking, ask you whether to add it and at what priority before filing the row.
- Never duplicate a row. If a similar one exists, update it.

## Why this exists

Without a single canonical view, Familiar rediscovers context every session and you has to repeat herself. The status board collapses the noise into one queue. She sees what is queued by reading the file. Familiar acts from the queue rather than guessing what to work on next. Every tracked client and project lives here or it does not exist in Familiar's working model.
