# Familiar full install playbook (you, 2026-06-11)

One path: the actual install. 3-4 hours from cold to working back-office EA + voice samples captured. Voice profile lands end of week 1 via async EcodiaOS extraction. Persona-core MCP server delivered week 1 for background work.

## Prereqs (verify before starting)

- macOS Mac (you's, 8GB+, Apple Silicon preferred)
- VSCode installed
- Claude Pro or Claude Max account active on her Anthropic email
- Google Workspace account on resonaverde.com with super-admin access (she is the principal so this should be a yes; confirm before booking install)
- Tailscale account for Tate (or whoever drives the install)
- Existing file tree she wants Familiar to slot into; if no preference, default to `~/Documents/resonaverde/familiar/`

## Phase 1: Tailscale + SSH (10-15 min)

1. She installs Tailscale from tailscale.com, signs in with her resonaverde.com Google account
2. She shares her Mac with Tate's tailnet via Tailscale settings
3. Tate accepts the share, verifies `ssh angelica@<her-tailnet-name>` works
4. Tate verifies write access to her home directory
5. Tate confirms `<PERSONA_HOME>` location with you and exports the path: `export PERSONA_HOME=~/Documents/resonaverde/familiar` (or whatever path she picked)

## Phase 2: File tree (10-15 min)

1. SSH in, `mkdir -p $PERSONA_HOME/{knowledge/{people,docs,clients},voice/samples,episodes,routines,onboarding,familiar-core,.creds}`
2. `chmod 700 $PERSONA_HOME/.creds` (credentials directory)
3. Rsync the familiar-starter contents:
   ```
   rsync -av --exclude='familiar-core/' --exclude='.creds/' \
     /Users/ecodia/.code/ecodiaos/backend/products/persona-pack/templates/familiar-starter/ \
     angelica@<her-tailnet>:$PERSONA_HOME/
   ```
4. Patch CLAUDE.md, BOOTSTRAP.md, INSTALL.md to replace `<PERSONA_HOME>` placeholder with her actual path:
   ```
   ssh angelica@<her-tailnet> "cd $PERSONA_HOME && find . -name '*.md' -exec sed -i '' \"s|<PERSONA_HOME>|$PERSONA_HOME|g\" {} +"
   ```
5. Drop `.gitignore` covering `.creds/`, `episodes/`, `voice/samples/`, `onboarding/`

## Phase 3: Google Workspace Service Account + DWD (30-45 min)

This is the credential setup that lets Familiar act on your behalf without her sitting at the keyboard. Needed for Routines (background work).

1. Start CDP on her Chrome with her your work admin account logged in
2. Navigate to console.cloud.google.com - either use her existing your work GCP project or create `resonaverde-familiar`
3. Enable APIs: Gmail, Calendar, Drive, Contacts (People API)
4. Create Service Account: `familiar-persona-sa` with display name "Familiar Persona Agent"
5. Generate JSON key, download to `$PERSONA_HOME/.creds/google-sa.json`, chmod 600
6. Note the SA client_id from the JSON
7. Navigate to admin.google.com (super-admin required) → Security → Access and data control → API controls → Domain-wide delegation
8. Add new client: client_id from step 6
9. Grant OAuth scopes:
   ```
   https://www.googleapis.com/auth/gmail.modify
   https://www.googleapis.com/auth/gmail.send
   https://www.googleapis.com/auth/calendar
   https://www.googleapis.com/auth/drive
   https://www.googleapis.com/auth/contacts
   https://www.googleapis.com/auth/contacts.readonly
   ```
10. Save. Note: propagation takes 1-5 minutes.
11. Test: run a quick Node script with the SA acting as angelica@resonaverde.com listing Gmail messages. Confirm 200 OK.

If she is NOT super-admin, this phase blocks until her workspace admin can be looped in. Phase 4-7 can still proceed; Routines just will not work until DWD is in place.

## Phase 4: VSCode + Claude Code (10 min)

1. She installs Claude Code extension from VSCode marketplace
2. She signs into Claude in the extension with her Pro/Max account
3. She authenticates the claude.ai Gmail, Calendar, Drive connectors via OAuth in the side panel (these give Familiar interactive access; the DWD-SA gives her background access)
4. She opens `$PERSONA_HOME` as a folder in VSCode
5. Claude Code picks up CLAUDE.md automatically
6. Verify: she opens the chat, types "Hi", confirms Familiar reads CLAUDE.md and recognizes the bootstrap-pending state

## Phase 5: First conversation (60-90 min)

This is the bootstrap. Familiar reads BOOTSTRAP.md, runs the 9-section interview with you, captures everything to `$PERSONA_HOME/knowledge/` as the conversation goes. Tate sits in for the first 15 minutes to make sure the setup is holding, then leaves you and Familiar to it.

Sections (covered in BOOTSTRAP.md):
1. You + your work (10 min)
2. The persona (5 min)
3. A typical week (15 min)
4. Systems + integrations + live probes (10 min)
5. Authority (10 min)
6. Voice samples (10 min - she pastes/drags 50+ samples)
7. Knowledge corpus (15 min)
8. Routines (5 min)
9. Pilot success (5 min)
+ closing smoke test (5 min)

Total: ~90 min.

At the end of bootstrap, you has a working Familiar who knows her, has her tool stack live, has the knowledge corpus seeded, and has the voice samples ready for extraction.

## Phase 6: Routines + backup (20-30 min, Tate does while you finishes bootstrap)

While you works through the bootstrap interview with Familiar, Tate sets up the scheduled background work on his side.

1. claude.ai Routines on your account:
   - Morning brief: 7am AEST daily, scheduled prompt: "You are Familiar. Read $PERSONA_HOME/knowledge/. Check angelica@resonaverde.com's inbox via DWD-SA for new mail since last check, check her calendar for today and tomorrow, compile a morning brief and email it to her at 7am. Include: priority items in inbox, calendar for today, any reminders from $PERSONA_HOME/routines/reminders.md, anything else load-bearing."
   - End-of-day wrap: 6pm AEST daily, similar shape, what got done / what's pending / what tomorrow looks like
   - Weekly recap: Sunday 7pm AEST, looking back at the week + forecasting the next
   - Any custom routines she added in bootstrap section 8
2. Nightly Drive backup: rsync `$PERSONA_HOME/` to her Drive at 11pm AEST via launchd plist
3. Install launchd plist `com.ecodia.familiar.drive-backup.plist` (template in `templates/familiar-starter/launchd/`)

## Phase 7: familiar-core MCP scaffold (15 min today, full build async this week)

Drop the scaffold for the familiar-core MCP server. Full implementation lands during week 1 via EcodiaOS push.

MCP config lives at `~/.claude.json` (user-global), NOT a project-level `.mcp.json`. User-global keeps Familiar's tools available regardless of which folder VSCode opens, and avoids the project-discovery confusion that hit the pilot. Customer does not have Node.js, npx, or the Claude CLI; never tell her to run `claude mcp add`. Either we SSH in via Tailscale to edit `~/.claude.json` directly, or we hand her a JSON snippet to paste via Cmd+Shift+P → "Claude: Open Settings".

1. Scaffold lives at `$PERSONA_HOME/familiar-core/`:
   - `package.json` - dependencies (sqlite3, googleapis, MCP server SDK)
   - `index.js` - MCP server entry point (stub: registers tool names, returns "not implemented yet")
   - `README.md` - what this server does and what's pending
2. `npm install` in `$PERSONA_HOME/familiar-core/`
3. Add launchd plist to auto-start on login (not active until full implementation lands)
4. Wire the familiar-core entry into `~/.claude.json` mcpServers block (commented out until full implementation lands)

Full server delivers in week 1:
- Read/write tools for `$PERSONA_HOME/knowledge/` with sqlite-backed search
- Google DWD-SA tools (Gmail, Calendar, Drive, Contacts) as MCP-callable functions
- CDP helpers wrapping cdp.findVisible / clickByTag / nativeFill for web automation
- Scheduled task primitives for background work invoked by Routines

## Phase 8: Walkthrough + close (15 min)

Tate or Familiar walks you through the active surfaces:
- How to talk to Familiar in the VSCode side panel
- How to ask Familiar to remember something ("Familiar, save this: X")
- How to ask Familiar to look something up ("Familiar, what do I know about Y?")
- How to invoke a CDP action ("Familiar, open LinkedIn and find me replies pending")
- How the morning brief will land tomorrow
- Where the hard-stops live and how to update them

Tell her: "Voice profile lands tomorrow. Until then I draft, you send. Routines start firing tomorrow morning. Tate is one message away if anything feels wrong. The 30-day review is on the calendar."

## Week 1 follow-ups (async, EcodiaOS does)

- Voice extraction: 50+ samples through scorer-builder
- Voice profile review: you reviews 10 sample outputs before lock
- Voice profile locked, outbound gate flipped on
- familiar-core MCP server full implementation delivered
- Any setup issues from `$PERSONA_HOME/onboarding/setup-issues.md` resolved

## Gotchas

- Claude Code extension may prompt for Bash + file write permissions in `$PERSONA_HOME` on first use. Expected.
- 8GB RAM: with VSCode + Chrome (CDP) + Claude Code + familiar-core (week 2), expect ~6GB used. Do not add local Postgres or Neo4j desktop.
- DWD propagation can take 1-5 minutes after scope grant. If smoke test fails immediately, wait 5 min and retry.
- Routines on claude.ai are per-account. They run from her Anthropic account, not Tate's.
- The `.creds/` directory is gitignored and chmod 700. If she ever zips up `$PERSONA_HOME` to share, exclude that directory.

## Escalation

Anything weird: tate@ecodia.au or SMS to Tate's known number. Familiar knows EcodiaOS maintains her.
