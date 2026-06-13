---
name: voice-capture
description: Collect your person's writing samples and distil how they actually write into a working voice profile. Use during bootstrap section 6, when they share new writing, or when a draft of yours gets heavily edited.
---

# voice-capture

You write FOR your person, so you have to write LIKE your person. The voice profile is a living document, not a one-time setup.

## Collecting samples

Ask for real writing: sent emails, posts, documents. Aim for 20 to 50 pieces. They can drag files into the chat or point you at a folder. Save everything to `voice/samples/` with descriptive names (`email-to-client-pricing.txt`, `linkedin-post-launch.txt`).

## Building the profile

Read every sample, then write `voice/profile.md` with these sections:

- **Register**: formal or loose, warm or dry, first-name or title. Quote two samples as evidence.
- **Sentence shape**: short and punchy, or long and flowing. Average length. Fragments allowed or not.
- **Openers and closers**: how they actually start and end emails. Quote the real ones.
- **Vocabulary fingerprint**: words and phrases they reach for repeatedly. Words they never use.
- **Punctuation habits**: exclamation marks, ellipses, dashes, emoji. Observed, not assumed.
- **Banned list**: anything they said never to write, plus anything in the samples they marked as not-them. Mirror to `voice/banned-vocab.md` (the outbound hook reads that file).

## Keeping it alive

Every time they edit one of your drafts, diff what changed and ask yourself what rule the edit implies. Append the rule to `voice/learnings.md` with the example. When three learnings point the same way, fold them into `voice/profile.md`.

## The test

Before any outbound draft, reread `voice/profile.md` if you have not this session. A draft that sounds like an assistant instead of like them is a failed draft, however correct its content.
