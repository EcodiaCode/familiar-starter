---
name: invoice-chase
description: Track what your person is owed and chase overdue invoices at the right cadence with the right tone. Use when they say "who owes me money", "chase that invoice", or to run a standing receivables sweep.
triggers: ["who owes me", "chase that invoice", "overdue invoice", "unpaid invoices", "outstanding payments", "follow up on payment", "receivables", "money owed to me"]
---

# invoice-chase

Money owed and not chased is money lost. invoice-chase makes sure every invoice gets followed up, firmly and on time, without your person having to be the one to nag.

## When to use

- They ask who owes them or want a specific invoice chased.
- A standing weekly or fortnightly sweep of receivables, if they want one.
- An invoice has passed its due date.

## When NOT to use

- To send anything before they confirm the amounts and the recipients. Money messages are gated until they set a standing rule.
- To chase a client they have told you to handle gently or not at all. Check `knowledge/clients/` and the hard-stops first.

## Find what is owed

1. Pull outstanding invoices from wherever they live: the accounting tool (drive it per the cdp-usage skill if there is no API), a spreadsheet, or their own notes.
2. Sort by how overdue each one is. Anything past its terms is in scope.
3. Read the client file for each before drafting; the right tone for a chase depends entirely on the relationship.

## The chase ladder

Match firmness to lateness:

- **Just overdue (a few days)**: a warm reminder. Assume it was missed, not refused.
- **Properly late (past a couple of weeks)**: clearer, naming the invoice number, the amount, the due date, and the new date you would like it settled by.
- **Seriously late**: firm and specific about next steps, drafted for your person to review carefully. This is a judgement call, so surface it rather than auto-drafting a hard line.

## Keep the loop alive

- After each chase, set a reminder for the next check per the contact-followup pattern. Do not rely on memory.
- When a payment lands, close the loop: mark it paid in their records and update the status board the same turn.

## Hard rules

- Confirm the amount and the recipient before any chase goes out. A chase for the wrong amount damages the relationship and the credibility.
- Nothing sends without their go-ahead until they grant a standing rule for routine reminders.
- Read the client file before drafting; a tone-deaf chase costs more than the invoice.
- Never assert an invoice is paid without reading it back from the source of truth.
