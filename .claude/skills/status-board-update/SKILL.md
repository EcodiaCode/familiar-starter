---
name: status-board-update
description: Maintain your status board at <PERSONA_HOME>/status-board.md as the single source of truth for active work. Read it on session start. Update it the same turn you act on a tracked entity. Move resolved rows to archived. Use whenever a tracked client, project, task, or thread changes state.
---

# status-board-update

The status board at `<PERSONA_HOME>/status-board.md` is the single canonical view of what is currently happening in your work. Treat it as zero-class infrastructure. Every other knowledge file in the corpus is reference material; this one is live state.

## When to read

Read the whole file in three situations:

1. Session start, every session, before doing anything else.
2. Whenever you references "what is going on with X" or asks for an overview of her work.
3. Before answering any question that touches a tracked entity, so the answer reflects the current row state rather than memory from a prior session.

## When to update

Write to the file in these situations:

1. The same turn you act on a tracked entity. Updates do not batch across turns.
2. When you states a change in state (a client paid, a project shipped, a thread resolved, a meeting moved).
3. When a row's next-action-by changes from her to you or vice versa.
4. When the status text becomes stale by more than seven days and you have new information to put in.

## How to update

1. Open `<PERSONA_HOME>/status-board.md`.
2. Find the row by entity-slug or name.
3. Update the status, next-action-by, context, and last-touched fields.
4. If no matching row exists and the entity warrants tracking, file a new row at the right priority. Ask you if you are uncertain about the priority.
5. Save the file.

## When to archive

Move a row to the Archived section when one of these holds:

- The work resolved cleanly (the client paid, the project shipped, the decision was made).
- The entity has been inactive for at least 30 days with no expected revival.
- you tells you to archive it.

Archive rows by moving them to the Archived section with a one-line resolution note. Do not delete. The durable record holds.

## Anti-patterns

- Do not let status drift more than a session without an update. That is the failure shape that produces the stale memory she pays you to prevent.
- Do not duplicate rows when a similar one exists. Update the existing row instead.
- Do not file P1 for everything. P1 means genuinely urgent (acting today or this week).
- Do not archive on assumption. If you are not certain the work resolved, leave the row active and ask her.

## Why this matters

Without a single canonical view of active work, Familiar rediscovers context every session and you has to repeat herself. The status board collapses all the noise into one queue. She reads it to see what is queued. Familiar acts from the queue without asking what to work on next. Every tracked client and project lives here or it does not exist in Familiar's working model.
