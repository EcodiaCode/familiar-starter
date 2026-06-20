---
name: skill-library
description: Browse and pull skills from your Familiar's wider library. Use when your person says "show me the library", "what skills do you have", "add the meeting-prep skill", "pull in the invoice chaser", or "update the library". Lets you describe everything you can do and switch extra skills on and off on demand.
---

# skill-library

You ship with a small set of always-on skills, and a much larger library you can pull from when the work calls for it. This skill is how you browse that library and switch skills on and off.

## Why it works this way

Claude Code loads every skill in `.claude/skills/` at session start, and each one costs context. So the always-on set stays lean: the handful of skills that earn their place every day. The rest live in `library/skills/`, which is not auto-loaded, and you pull the ones your person actually needs into the active set. The full catalogue is listed in `library/registry.json`, which describes both the active skills and everything pullable.

## The four things you do

### Show the library

When they ask what you can do or to see the library:

1. Read `library/registry.json`.
2. Group the entries by `category` and list each skill's `name` and `summary`, one line each.
3. Mark which are already active (`location: "active"`) and which are pullable (`location: "library"`).
4. Offer to pull in any that fit the kind of work they have described.

### Add a skill

When they say "add <name>" or describe work that a library skill covers:

1. Confirm the skill exists in the registry with `location: "library"`.
2. Copy its whole folder from the library into the active set:
   ```
   cp -R library/skills/<name> .claude/skills/<name>
   ```
3. Update that skill's entry in `library/registry.json` so its `location` reads `"active"`.
4. Tell your person it is added, and that it activates after a window reload: Cmd+Shift+P (Mac) or Ctrl+Shift+P (Windows), then "Developer: Reload Window". Claude Code reads the active skill list at session start, so the new skill is live on the next session.

### Remove a skill

When they say "remove <name>" or an extra skill is no longer earning its context:

1. Confirm it is one you pulled in (it lives in both `.claude/skills/<name>` and `library/skills/<name>`). Never remove one of the core always-on skills.
2. Delete it from the active set:
   ```
   rm -rf .claude/skills/<name>
   ```
   The copy in `library/skills/` stays, so it is always re-addable. Nothing is lost.
3. Update its registry entry back to `location: "library"`.
4. Tell them it is removed and will be gone after the next window reload.

### Update the library

When they say "update the library" or "any new skills":

1. This is the same upstream pull the pack-update skill runs. New catalogue skills ship in `library/skills/` upstream and arrive when you pull.
   ```
   git fetch origin
   git log HEAD..origin/main --oneline -- library/
   ```
2. If there are new commits touching the library, summarise what is new, then `git pull --ff-only` per the pack-update skill's safety rules.
3. After pulling, read the refreshed `library/registry.json` and tell them which new skills are now available to add.

## Keep the registry honest

The registry is the source of truth for what exists and where it lives. Every time you add or remove a skill, update its `location` in `library/registry.json` the same turn. A registry that disagrees with the folders is worse than none, because it makes you describe a library you do not actually have.

## Hard rules

- Never bloat the active set on a whim. Pull a skill in because the work needs it, and offer to remove it when it stops earning its place. A lean active set keeps every session sharp.
- Never remove a core always-on skill. Only ever remove skills your person pulled in from the library.
- The library copy is permanent; removing from active never deletes from the library, so an add is always reversible.
- Adds and removes take effect after a window reload, because Claude Code caches the skill list at session start. Always tell them that, so they are not confused when the skill is not live the same second.
