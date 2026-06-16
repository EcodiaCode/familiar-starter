---
name: pack-update
description: Safely pull doctrine updates from the shared EcodiaOS familiar-starter upstream repo. Use when you says "Familiar, pull updates" or "check for updates", or when the weekly pack-update Routine fires. Wraps git fetch + pull + reload + smoke test in one workflow with safety gates.
---

# pack-update

Familiar's self-update workflow. Pulls doctrine updates from `upstream/main` while preserving your knowledge corpus, voice profile, status board state, and accumulated episodes.

## When to invoke

- you says "Familiar, pull updates", "check for updates", "any new doctrine", or similar
- The weekly pack-update Routine fires (Sunday 6pm AEST)
- After Tate signals out-of-band that a pack version has shipped

## When NOT to invoke

- During an active outbound mail draft or any time-sensitive task. Finish the task first.
- When `git status` shows a dirty tree with uncommitted changes you has not seen yet. Commit those first.
- When the network is offline or GitHub is unreachable. Defer and surface to her.

## The workflow

### Step 1: Pre-flight check

```
cd the Familiar folder
git status
```

If output shows uncommitted changes:
- Read the changed files. Identify whether they are accumulated knowledge or genuine work-in-progress.
- If accumulated knowledge (additions to knowledge/, status-board.md updates, new episodes): commit to `origin` with a one-line message describing what was added, then proceed.
- If genuine work-in-progress that should not be backed up yet: surface to you, ask whether to commit or stash, do not proceed without their go-ahead.

### Step 2: Fetch + pull

```
git fetch upstream
git log HEAD..upstream/main --oneline
```

If there are new commits, summarize them for you before pulling. One line per commit, focus on what changed.

```
git pull upstream main
```

### Step 3: Handle conflicts

If pull surfaces a merge conflict, STOP. Do NOT auto-resolve. Output:
- The list of conflicted files
- A one-line description of what changed upstream vs locally
- A recommendation: "Tate needs to resolve this before I continue. The pull is paused. Your current working state is intact."

Leave the tree in conflicted state until a human (Tate, usually) resolves. Do not run `git checkout` or `git reset` to escape the conflict.

### Step 4: Reload the extension

After a clean pull, tell you:

```
Pulled cleanly. To pick up the new skills and hooks, hit Cmd+Shift+P then type "Developer: Reload Window".
```

The reload is required because Claude Code caches the loaded skills list at session start.

### Step 5: Smoke test

After the reload, on their next message, run:
- Read `status-board.md` and confirm it still parses
- List the skills you can see (count vs the new INDEX.md entries)
- Check `.claude/hooks/` matches what `.claude/settings.json` references

If anything looks broken, surface immediately. Tate may need to push a fix to upstream.

### Step 6: Write the Episode

Append to `episodes/<YYYY-MM-DD>.md`:

```
## pack-update <time>
Pulled upstream/main at <commit-sha>.
New: <list new skills, hooks, doctrine sections>
Removed: <list any removed items>
Smoke test: <pass | fail with detail>
```

This becomes the durable record. Tomorrow's session knows what version of the pack is in play.

## Hard rules

- NEVER push to `upstream`. Tate's side only. Her `origin` is the only push target Familiar has.
- NEVER auto-resolve merge conflicts. Conflicts mean upstream changed a file you also changed; human judgment required.
- NEVER discard their uncommitted work to make the pull clean. Stash or commit, never reset hard.
- Doctrine improvements Familiar wants to propose go to `knowledge/pilot-feedback.md`, not into a push to upstream.

## Why this matters

The familiar-pack evolves continuously at EcodiaOS. New skills, refined hooks, doctrine patches land on the template repo weekly. Without a self-update mechanism, your Familiar falls behind and the pack they paid for stops being the pack we ship. The git-pull-from-upstream model lets them stay current with one command, without losing the knowledge corpus they have accumulated.

Her data is hers and stays in `origin`. The pack is shared and flows from `upstream`. The two never collide because of the gitignore boundary.
