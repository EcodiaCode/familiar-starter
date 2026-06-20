---
name: meeting-prep
description: Build a tight prep pack before a meeting - who is in the room, what it is about, the history, and the three things your person needs at hand. Use when they say "prep me for", "what do I need for the meeting with", or the morning of a day with meetings.
triggers: ["prep me for", "prep for my meeting", "meeting with", "who am i meeting", "before the call with", "get me ready for"]
---

# meeting-prep

A meeting your person walks into cold is a meeting half-wasted. The prep pack makes them the most prepared person in the room.

## When to use

- They name a meeting and ask to be prepped.
- The daily brief shows a meeting today with someone who has a file in `knowledge/people/`.
- A first meeting with someone new, where you do the research they would not have time for.

## When NOT to use

- A standing internal sync with no agenda and no stakes. A one-line reminder is enough.
- Anything you cannot research without sending external messages. Prep is read-only until they say otherwise.

## Build the pack

1. Read the calendar event through the mail/calendar connector: time, attendees, location or link, any agenda in the description.
2. For every attendee with a file in `knowledge/people/`, read it. Pull their role, your person's relationship with them, communication-style notes, and any pitfalls.
3. For attendees with no file, research what you honestly can: their public role, the org they are with. Drive the browser per the cdp-usage skill if it lives behind a login. Cite each fact inline or mark it `UNVERIFIED:`.
4. Read `status-board.md` for any row tied to this person or org, so the prep reflects the live state of the work, not last month's.
5. Scan recent mail with these attendees for the last thread and any open question.

## The pack shape

One message, scannable in thirty seconds:

- **Who and what**: the meeting, the time, who is in the room and their role in one line each.
- **Where we are**: the live state from the status board, one line.
- **Last exchange**: the most recent thread and any question left hanging.
- **Three things to have ready**: the specific facts, numbers, or decisions your person will likely need. This is the part that earns the prep.
- **One open risk or opportunity**: the thing worth them knowing before they walk in.

## Hard rules

- Every claim about a person or org carries its source or an `UNVERIFIED:` flag. A prep pack that asserts a wrong role is worse than no prep.
- Read the person file before writing a word about them.
- Do not contact attendees to "confirm" anything. Prep is silent.
- After the meeting, if they tell you what happened, update the person files and the status board the same turn.
