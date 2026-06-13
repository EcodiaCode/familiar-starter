---
name: pattern-codify
description: File a durable rule in your knowledge corpus wheneverthey states one in conversation. Use wheneverthey says "remember this", "from now on", "always", "never", or codifies a preference, correction, or recurring decision pattern. Recursive improvement is the goal; the corpus accumulates their operating manual over time.
---

# pattern-codify

When you states a rule, preference, or recurring pattern in conversation, file it as a durable rule in their knowledge corpus the same turnthey states it. This is how Familiar's operating manual evolves.

## When to invoke

Trigger phrases:
- "remember this", "from now on", "always", "never"
- "I prefer X to Y"
- "stop doing X"
- "every time X happens, do Y"
- "when in doubt, default to..."
- "make sure to..."

Or any timethey corrects a behavior and the correction would apply to future similar cases.

## How to apply

1. Identify the rule precisely. Be specific. "Reply to client emails within 2 hours" beats "be responsive." Capture in their words where possible.
2. Decide the file. Three categories:
   - **General operating rules** -> append to `knowledge/learned-rules.md`
   - **Per-person preferences** -> append to `knowledge/people/<firstname-lastname>.md`
   - **Per-client preferences** -> append to `knowledge/clients/<client-slug>.md`
3. Append an entry in this shape:

```
## <rule-slug-2026-MM-DD>
**Rule**: <one-sentence rule, in their words if possible>
**Why**: <reasonthey gave, or the inferred reason ifthey did not say>
**How to apply**: <when this rule kicks in, what to do>
**Confirmed**: <date>
```

4. Read back to her: "Logged. From now on I will <restate the rule>. Sound right?"
5. Ifthey corrects the captured rule, edit immediately.

## Anti-patterns

- Do not codify situational preferences as universal rules. Ifthey says "this once, do X," do not log it as "always do X."
- Do not capture rules you cannot verifythey stated. Hallucinated rules erode their trust in the corpus.
- Do not restate the rule in your own words if hers were specific. The corpus is more useful in their voice.
- Do not codify a rule that contradicts an existing one without flagging the conflict. Read the relevant file first.

## Why this matters

Every codified rule reduces the number of times they have to repeat herself. Over weeks, the corpus accumulates into a high-fidelity model of howthey wants the work done. Familiar gets better not by training updates but by reading their own corpus more carefully each turn.

If you find yourself thinking "they have told me this before," that is the failure signal. The rule should have been codified last time.
