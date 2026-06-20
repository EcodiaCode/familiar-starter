---
name: crm-update
description: Keep your person's contacts and deal records current - log the call that just happened, update the stage, add the new contact, so the CRM reflects reality instead of last month. Use when they say "update my CRM", "log this in the pipeline", or after a client interaction.
triggers: ["update my crm", "log this in the pipeline", "add a contact", "update the deal", "log the call", "move this to", "pipeline update", "record this interaction"]
---

# crm-update

A CRM is only worth anything if it is current, and it goes stale the instant updating it becomes a chore. crm-update keeps the record honest by logging interactions as they happen.

## When to use

- After a call, meeting, or exchange that should be logged against a contact or deal.
- A new contact to add, a deal to move stages, a note to attach.
- A standing tidy of the pipeline, if they want one.

## When NOT to use

- To send anything to a contact from the CRM. Updating the record is yours; outbound messages are gated.
- To delete records or contacts without their go-ahead.

## Make the update

1. Find the record. Drive the CRM per the cdp-usage skill if it has no API, in their session.
2. For an interaction: log it against the right contact and deal with the date, what happened, and the next step. Keep the note factual and short.
3. For a stage change: move the deal only when the real-world state actually changed, and record why.
4. For a new contact: add them with the details you hold, and create a matching `knowledge/people/<firstname-lastname>.md` file so your own corpus and the CRM stay in step.
5. Mirror anything load-bearing back into the status board so your working model and the CRM agree.

## Keep both sides honest

- The CRM and your `knowledge/people/` files are two views of the same truth. When one changes, update the other the same turn so they never drift.
- Log what happened, not what you hope happened. A pipeline full of optimistic stages is a lie that costs decisions.

## Hard rules

- Update only on a real state change. Do not advance a deal stage to look busy.
- Record facts, not guesses. If a next step is unconfirmed, note it as unconfirmed.
- Reading and updating records is yours; messaging contacts and deleting records is gated to their approval.
- After any update, read the record back to confirm it saved. A narrated CRM update is not a saved one.
