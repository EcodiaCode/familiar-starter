---
name: calendar-triage
description: Sweep your person's calendar for clashes, gaps, back-to-backs, and meetings missing a time or a link, and propose fixes. Use when they say "check my calendar", "any clashes this week", or as part of the daily brief when the day is busy.
triggers: ["check my calendar", "my schedule", "any clashes", "double booked", "free time", "gaps in my day", "tidy my calendar", "what's my week look like"]
---

# calendar-triage

A calendar nobody curates fills with clashes, missing links, and no room to breathe. Triage keeps it honest.

## When to use

- They ask you to look over the day, the week, or a specific stretch.
- The daily brief surfaces a double-booking or a back-to-back stack worth flagging.
- Before a heavy day, to catch problems while there is still time to fix them.

## When NOT to use

- For a single "when is my next meeting" question. Just read it and answer.
- To move or cancel events without their go-ahead. Triage proposes; it does not act on the calendar until they say so.

## The sweep

Read the window they named (default: today plus the next seven days) through the calendar connector. Check each event for:

1. **Clashes**: two events overlapping in time. Flag both.
2. **Back-to-backs with no buffer**: meetings touching with no gap, especially across locations. A 2pm in the office and a 2pm video call cannot both happen.
3. **Missing essentials**: no video link on a remote meeting, no location on an in-person one, no agenda where one is clearly needed.
4. **No-breathing-room days**: more than four meetings with no clear lunch or focus block. Worth naming.
5. **Stale holds**: tentative events or blocks from weeks ago that may no longer be real.

## Report shape

One message:

- **Clashes (must fix)**: each clash, both events, and your proposed resolution.
- **Tight spots**: back-to-backs and missing links, with the fix you suggest.
- **Worth a look**: stale holds or an overloaded day, named plainly.

For each fix, propose the specific change ("move the 2pm call to 2:30, I'll send the reschedule note") and wait for their go-ahead before touching the calendar.

## Hard rules

- Never move, cancel, or create an event without explicit approval. The calendar is theirs.
- When they approve a reschedule that needs a message to someone else, draft it; do not send until they confirm, per the email-triage rules.
- After any approved change, read the event back to confirm it took. A narrated reschedule is not a real one.
