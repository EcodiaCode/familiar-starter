---
name: pattern-codify
description: File a durable rule in your knowledge corpus whenever she states one in conversation. Use whenever she says "remember this", "from now on", "always", "never", or codifies a preference, correction, or recurring decision pattern. Recursive improvement is the goal; the corpus accumulates her operating manual over time.
---

# pattern-codify

When you states a rule, preference, or recurring pattern in conversation, file it as a durable rule in her knowledge corpus the same turn she states it. This is how Familiar's operating manual evolves.

## When to invoke

Trigger phrases:
- "remember this", "from now on", "always", "never"
- "I prefer X to Y"
- "stop doing X"
- "every time X happens, do Y"
- "when in doubt, default to..."
- "make sure to..."

Or any time she corrects a behavior and the correction would apply to future similar cases.

## How to apply

1. Identify the rule precisely. Be specific. "Reply to client emails within 2 hours" beats "be responsive." Capture in her words where possible.
2. Decide the file. Three categories:
   - **General operating rules** -> append to `<PERSONA_HOME>/knowledge/learned-rules.md`
   - **Per-person preferences** -> append to `<PERSONA_HOME>/knowledge/people/<firstname-lastname>.md`
   - **Per-client preferences** -> append to `<PERSONA_HOME>/knowledge/clients/<client-slug>.md`
3. Append an entry in this shape:

```
## <rule-slug-2026-MM-DD>
**Rule**: <one-sentence rule, in her words if possible>
**Why**: <reason she gave, or the inferred reason if she did not say>
**How to apply**: <when this rule kicks in, what to do>
**Confirmed**: <date>
```

4. Read back to her: "Logged. From now on I will <restate the rule>. Sound right?"
5. If she corrects the captured rule, edit immediately.

## Anti-patterns

- Do not codify situational preferences as universal rules. If she says "this once, do X," do not log it as "always do X."
- Do not capture rules you cannot verify she stated. Hallucinated rules erode her trust in the corpus.
- Do not restate the rule in your own words if hers were specific. The corpus is more useful in her voice.
- Do not codify a rule that contradicts an existing one without flagging the conflict. Read the relevant file first.

## Why this matters

Every codified rule reduces the number of times she has to repeat herself. Over weeks, the corpus accumulates into a high-fidelity model of how she wants the work done. Familiar gets better not by training updates but by reading her own corpus more carefully each turn.

If you find yourself thinking "she has told me this before," that is the failure signal. The rule should have been codified last time.
