---
name: connector-setup
description: Walk your person through connecting Gmail, Google Calendar, Google Drive, and other connectors on claude.ai so Familiar can use them. Use during bootstrap section 4, whenever they ask to connect a tool, or whenever a connector you expected is missing.
---

# connector-setup

Connectors are how Familiar reaches your person's mail, calendar, and documents. They are set up on the claude.ai website (not in VS Code, not on the command line), and they sync to this VS Code extension automatically.

## The walkthrough (you guide, they click)

Say it conversationally, one step at a time, waiting for them to confirm each step:

1. "Open your web browser and go to claude.ai. Sign in with the same account you use here."
2. "Click your initials in the bottom-left corner, then Settings."
3. "Find Connectors in the settings menu."
4. "You'll see a list: Google Drive, Gmail, Google Calendar, and others. Click Connect next to the one we want."
5. "A Google window pops up asking you to choose your account and approve access. Pick the account you actually use for work and approve."
6. "Done. Come back here."

Then the part people miss:

7. "Now reload this window so I can see the new connection. Press Cmd+Shift+P (Mac) or Ctrl+Shift+P (Windows), type 'reload window', and press Enter." Without the reload, the connector exists on claude.ai but does not show up here.

## Verify each connector before moving on

After the reload, prove the connection works and show them:
- Mail: read the 3 most recent inbox messages and show the senders + subjects.
- Calendar: read today and tomorrow, show the events.
- Drive: find the most recently edited document, show its name.

If the probe fails: the most common cause is the wrong Google account got approved. Have them disconnect on claude.ai and reconnect with the right account. The second most common cause is the missing window reload.

## Things to know

- Connectors are per-account on claude.ai. If they use Claude on two accounts, the connectors live on the one they connected.
- You cannot set up connectors for them. The Google approval screen needs their click. Your job is the patter and the verify.
- More connectors appear on claude.ai over time. When they ask "can you reach X", check the Connectors page first before saying no.
- Anything with no connector may still be reachable by CDP (see the cdp-usage skill) with their standing permission.
