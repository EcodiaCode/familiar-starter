# Installing Familiar

The short version: download the installer from [ecodia.au/familiar/install](https://ecodia.au/familiar/install), double-click it, follow the steps. This file is the long version, for anyone who wants to see what the installer does or run the steps by hand.

## What the installer does

1. Checks for git. On macOS it installs the Xcode Command Line Tools if missing.
2. Checks for Homebrew on macOS and installs it if missing. On Windows it uses winget.
3. Installs Visual Studio Code if missing.
4. Clones this repository to `~/Familiar` (macOS) or `C:\Users\YOU\Familiar` (Windows). If a previous Familiar folder exists, it is backed up first, never overwritten.
5. Opens Visual Studio Code at the folder.

## What you do after the installer finishes

1. In Visual Studio Code, open the Extensions panel (the four-squares icon in the left sidebar).
2. Search for "Claude" and install the Anthropic Claude Code extension.
3. Sign in with your AI provider account when prompted. You need a paid plan on your own account, around twenty US dollars a month, set up directly with the provider.
4. Open the Claude chat panel and say hello. Your Familiar runs a short setup conversation on its first turn to learn who you are and how you work. Give it the time it asks for. Everything you tell it becomes its permanent memory.

## Manual install (technical users)

```bash
git clone https://github.com/EcodiaTate/familiar-starter.git ~/Familiar
cd ~/Familiar
code .
```

Then steps 1 to 4 above.

## Where everything lives

The whole assistant is this folder. Your knowledge corpus grows under `knowledge/`, your working state lives in `status-board.md`, drafts go under `drafts/`. Back the folder up the way you back up documents. Copy it to a new computer and your assistant comes with you.

## If something does not work

Reply on your Familiar welcome email, or write to code@ecodia.au. Say which step you were on and what you saw.
