---
name: skill-creator
description: Build a new skill (and its keyword trigger) when your person has a workflow they want to make repeatable. Use when they say "make a skill for this", "set this up so you can do it again", "turn this into a routine", or "remember how to do this", or after the two of you finish a task by hand that they will clearly want to repeat. A skill is just a good prompt plus the agentic loop you already run; this skill is the one that writes the others.
---

# skill-creator

This is the skill that makes other skills. When your person has a workflow they want you to own (a reconciliation, a recurring report, a weekly email shape), capture it as a skill so it runs the same reliable way every time, instead of being re-figured-out from scratch each session.

A skill is not magic and not code. It is a folder with one Markdown file, `SKILL.md`, that holds a clear description and a set of steps. Claude Code reads the description at session start and pulls in the full file when the work matches. That is the whole mechanism: a good prompt plus the agentic loop you already run.

## When to invoke

- Your person says "make a skill for this", "set this up so you can do it again", "turn this into a routine", or "remember how to do this".
- The two of you just finished a multi-step task by hand that they will obviously repeat (a reconciliation, a report, a recurring email shape).
- A `[SKILL-TRIGGER]` reminder fired for a workflow that has no skill yet (`built: false` in keyword-triggers.json) and they want it built.

## When NOT to invoke

- For a one-off task they will not repeat. A skill is for recurring work. Just do the task.
- For a single durable rule or preference ("always cc me on client mail"). That is the pattern-codify skill, not a new skill.
- Mid-way through a time-sensitive task. Finish the task, then offer to capture it as a skill.

## The one rule that protects your work: name it so a pack update will not clobber it

`.claude/skills/` is git-tracked and refreshed from the upstream EcodiaOS template by the pack-update skill (`git pull --ff-only`). A skill you author with a name EcodiaOS later ships under would be overwritten by an update, and your version lost. So every skill you write here MUST use a name EcodiaOS will not ship.

- Prefix self-authored skills with `my-`, or name them after your person's specific tools and workflow: `my-xero-rec`, `acme-weekly-report`, `studio-invoice-run`. Never reuse a shipped skill's name (`email-triage`, `daily-brief`, `cdp-usage`, and the rest of the active set), and avoid plausible future-shipped generic names like `bookkeeping` or `crm`.
- Keep a writable backup. The pack's `origin` is the shared template you only ever pull from. To back up the skills your person owns, fork the pack to their own GitHub account and commit there, or just back up the whole Familiar folder the way they back up documents. The unique name is what survives a pull; the fork is what survives a lost laptop.

If you ever do want a skill shipped to every Familiar, do not push it upstream yourself. Note it in `knowledge/pack-feedback.md` and the give-feedback skill carries it to EcodiaOS, who lift it into the template.

## What a skill is made of

Every skill lives at `.claude/skills/<skill-name>/SKILL.md` and has two parts:

1. **Frontmatter** (the block between the `---` lines at the top):
   - `name`: the skill's folder name, lowercase with dashes, unique per the rule above, e.g. `my-xero-rec`.
   - `description`: one or two sentences. This is the most important field, because Claude Code decides whether to load the skill from this line alone. Say plainly what the skill does AND when to use it, including the words your person actually says when they want it.
   - `allowed-tools` (optional): leave it off unless you want to restrict the skill to specific tools.

2. **Body** (the Markdown under the frontmatter): the steps. Write them like instructions to a sharp new assistant who has never seen this workflow: what to do, in what order, what to check, what to never do.

Look at the skills already in the pack for the shape: `pattern-codify`, `pack-update`, `cdp-usage`, `status-board-update`, `troubleshoot`. Copy the one closest to the new workflow and adapt it.

## How to create a skill (step by step)

1. **Name it** per the protect-your-work rule above. A unique, specific name, not a generic one EcodiaOS might ship.

2. **Make the folder and file.**
   ```
   mkdir -p ".claude/skills/<skill-name>"
   ```
   Then write `.claude/skills/<skill-name>/SKILL.md`.

3. **Write the frontmatter first.** Get the `description` right. Read it back to your person and confirm it matches when they would want this skill.

4. **Write the body as numbered steps.** Capture exactly what the two of you did by hand. Be specific. Name the tools, the URLs, the fields, the order. Add a "never do" section for the traps you hit while figuring it out (a wrong button, a step that must come first, a thing that breaks the flow).

5. **Add a keyword trigger** so the skill surfaces on its own (see the next section).

6. **Reload so Claude Code sees it.** New skills register at session start. Tell your person: open the command palette with Cmd+Shift+P (Mac) or Ctrl+Shift+P (Windows), run "Developer: Reload Window".

7. **Test it.** On the next message, run the new skill on a real example and watch it work end to end. Fix any step that was vague or wrong, then reload again.

8. **Back it up.** Commit the Familiar folder so the skill is safe (to their own fork if they made one, otherwise it lives in the folder backup).

## How to add a keyword trigger

A trigger makes you remember a skill exists the moment your person mentions the right words, even if they do not name the skill. Triggers live in one data file, no code:

`.claude/hooks/keyword-triggers.json`

Add an entry to the `triggers` list:
```json
{
  "skill": "<skill-name>",
  "built": true,
  "keywords": ["word", "another word", "short phrase"],
  "reminder": "One line you see when a keyword matches. Name the skill to use and why."
}
```
- `keywords` are lowercase. Multi-word entries like `bank rec` match as a contiguous run.
- Set `built` to `true` once the skill actually exists. A `built: false` entry is a placeholder reminding the two of you that the skill is still worth making.
- When you finish building a skill that already had a `built: false` placeholder, flip it to `true` and point the `reminder` at the real skill instead of at skill-creator.

Save the file, reload the window, and the trigger is live.

## Anti-patterns

- Do not write a skill so vague it could mean anything. "Handle the finances" is not a skill. "Pull the receipts, code them in Xero, then drive the bank rec in the browser" is.
- Do not leave the `description` generic. A weak description means Claude Code never loads the skill when it is needed, and the skill is dead weight.
- Do not name a self-authored skill anything EcodiaOS might ship. A pull overwrites it and the work is gone. Unique, specific names only.
- Do not put secrets (passwords, API keys, tokens) inside a SKILL.md. Skills are committed to git. Credentials live outside the corpus, referenced by path, never pasted.
- Do not skip the test. A skill that was never run on a real example is a guess, not a skill.

## Why this matters

This is how you stop needing EcodiaOS for every new workflow. The two of you hit a task, do it once together carefully, and capture it. After that you own it. The pack is not a fixed product handed down; it is a starting kit that your person and you grow yourselves, one captured workflow at a time, each one named so an update never takes it away.
