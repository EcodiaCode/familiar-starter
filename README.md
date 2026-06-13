# Familiar

Your personal AI assistant, set up on your computer.

This is the open template that the Familiar installer clones into your home directory. EcodiaOS keeps shipping updates here; your local copy pulls them on its own schedule.

## Install

Go to [ecodia.au/familiar](https://ecodia.au/familiar) and start a subscription. The install link arrives by email immediately.

## Manual install (technical users)

```bash
git clone https://github.com/EcodiaTate/familiar-starter.git ~/Familiar
cd ~/Familiar
open .  # macOS - or open the folder in VS Code
```

Open VS Code in `~/Familiar`, install the Claude Code extension if you have not already, and sign into your AI provider.

## What is in here

- `CLAUDE.md` - the assistant identity that takes shape with you on first run.
- `BOOTSTRAP.md` - the conversation your assistant runs with you the first time you talk to it.
- `INSTALL.md` - the long-form install guide.
- `.claude/skills/` - the operations the assistant can run.
- `.claude/hooks/` - the rules that keep the assistant aligned with you over time.
- `knowledge/` - the corpus the assistant grows about you, your work, the people in it.

## License

MIT. The pack is yours.