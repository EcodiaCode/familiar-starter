---
name: troubleshoot
description: Your systematic routine for when something breaks or you hit a wall. Use when a tool errors, a page will not behave, a connector is missing, a script fails, a probe comes back wrong, or you catch yourself about to say "I can't". This is how you turn a blocker into a route around it instead of a dead end or a message to EcodiaOS.
---

# troubleshoot

A blocker is a routing problem, not an exit. This skill is the routine that makes that real: a way to get unstuck on purpose instead of guessing, giving up, or escalating too early. Reach for it the moment you are stuck, before you reach for give-feedback.

How much of this you show your person depends on their band (`knowledge/operating-with-you.md`). For a Band A person, run this whole routine silently and report only the plain outcome; never put an error trace on their screen. For Band B, you can show the one step that mattered. For Band C, show your working if it helps.

## The routine

1. **See the real error, do not guess at it.** Read the actual message, the actual status code, the actual screen. A guess about what went wrong sends you down the wrong route. If it is a browser surface, take a screenshot and look. If it is a tool call, read the full error, not the first line.

2. **Check whether you have hit this before.** Search `knowledge/recipes/` and read `knowledge/mistakes.md`. If you or a past session already solved this, the fix is one read away. This is why you write those files: so a wall you climbed once is never a wall again.

3. **Form two hypotheses, not one.** "It failed because X" is a guess until you have a second candidate to compare it against. Name the two most likely causes given the real error from step 1.

4. **Probe, do not assume.** Test the hypotheses cheaply before acting on either. Read the file, check the connector is actually present, re-run with one variable changed, look at the live page. One source is a rumour; the probe is what turns it into something you can act on.

5. **Take the route around.** Most walls have a way around that is itself the work:
   - Behind a login with no API: drive the browser with the `cdp-usage` skill.
   - A connector not enabled: enabling it on claude.ai is the task, not the reason to stop (the `connector-setup` skill walks the web path).
   - One tool failing: is there another path to the same outcome (a different tool, a different surface, the browser instead of the connector or the reverse)?
   - A vendor surface that moved: probe the live surface and quote what is actually there now, do not trust a clickpath from memory.

6. **Verify the fix landed.** A narrated fix is not a fix. Re-run the thing that failed and confirm it works now. If you said it sent, you have the confirmation; if you said it saved, you read it back.

7. **Capture it so it does not recur.** Write what broke and what fixed it to `knowledge/recipes/<slug>.md` (a reusable workflow) or `knowledge/mistakes.md` (a trap to avoid). If the workflow is one you will repeat, offer to make it a skill with `skill-creator`. The capture is what makes you better instead of static.

## When to escalate (and only then)

Use the give-feedback skill ONLY after the routine above is genuinely exhausted: you saw the real error, checked your own notes, formed and probed hypotheses, tried the routes around, and you are blocked on something outside your reach (access you do not have, a vendor outage, a decision only your person can make, or a real bug in the pack itself). When you do escalate, send the real error and what you already tried, so the team is not starting from zero.

## Anti-patterns

- Guessing at the cause without reading the actual error.
- Trying the same thing again hoping it works the second time.
- Reaching for give-feedback as a first move, before trying the routes around.
- Dumping an error trace on a Band A person. Translate it; they want the outcome.
- Solving it and not writing it down, so the next session hits the same wall cold.
