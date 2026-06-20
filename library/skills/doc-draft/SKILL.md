---
name: doc-draft
description: Draft a document for your person from a short brief - a memo, a one-pager, a letter, a set of notes - in their voice, structured, ready to refine. Use when they say "draft me a", "write up", or "put together a document on".
triggers: ["draft me a", "write up a", "put together a doc", "write a memo", "draft a letter", "one pager", "write a document", "knock out a draft"]
---

# doc-draft

Most documents your person needs are not hard, they are just time. doc-draft takes a short brief and returns a real first draft, not an outline.

## When to use

- They describe a document they need and want it drafted.
- A recurring document type (a status memo, a client update) where the shape is known.

## When NOT to use

- A document that asserts facts you have not verified. Research it first per the research-brief skill, then draft.
- Anything going out under their name to someone external, until they have approved the content. Drafting is fine; sending is gated.

## Before you write

1. Read `voice/profile.md` if you have not this session, so the draft sounds like them, not like an assistant.
2. If the document is addressed to a named person, read their file in `knowledge/people/`.
3. Pull any facts the document needs from the knowledge corpus, and cite each load-bearing one inline or mark it `UNVERIFIED:`.
4. If you are missing something that changes the shape of the document, ask the one or two questions that matter before writing, not after.

## Drafting

- Open with the point. The first line should tell the reader why this exists and what it asks of them.
- Structure to the type: a memo leads with the recommendation, a letter leads with warmth, a one-pager fits on one screen.
- Write in their voice and register. No corporate filler, no padding to look thorough.
- Keep load-bearing claims sourced. A document that reads as authoritative and is wrong costs more than one that is honest about a gap.
- Close clean. No "let me know if you have questions" unless that is genuinely how they sign off.

## Deliver and refine

- Show the full draft inline in the chat, not as a link or a file they have to open.
- Offer to render it as a clean document only if they want it formatted; default to plain text they can read in place.
- When they edit it, note what changed; that is voice signal. Append the lesson to `voice/learnings.md`.

## Hard rules

- Read the voice profile before drafting anything under their name.
- No invented facts and no placeholders. If a number is missing, ask or mark it `UNVERIFIED:`, never make one up.
- Drafting is not sending. External documents stay drafts until they approve.
