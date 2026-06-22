# Installing Familiar

The short version: download the installer from [ecodia.au/familiar/install](https://ecodia.au/familiar/install), double-click it, follow the steps. This file is the long version, for anyone who wants to see what the installer does or run the steps by hand.

## If you're not technical

This is the path for you, and it is the default. Download the installer, double-click it, and follow the steps. You do not need to understand any of what follows, and you will never touch a command line. The installer sets everything up, and once it opens, your Familiar runs a short setup conversation and guides you from there. The "what the installer does" and "manual install" sections below are just for the curious or for developers; skip them if you would rather not see the wiring. Your Familiar will meet you where you are.

If anything looks confusing, you can stop and write to code@ecodia.au with what you saw.

## What the installer does

1. Checks for git. On macOS it installs Apple's Command Line Tools if they are missing, which also provides git and python. No Homebrew and no admin password are involved.
2. Downloads Visual Studio Code straight from Microsoft if it is missing.
3. Installs the Anthropic Claude Code extension.
4. Clones this repository to `~/Familiar` (macOS) or `C:\Users\YOU\Familiar` (Windows). If a previous Familiar folder exists, it is backed up first, never overwritten.
5. Pre-trusts the folder so VS Code does not prompt, and opens it.

## What you do after the installer finishes

You need a Claude Pro plan first. Familiar runs on Claude, the AI built by Anthropic, so sign up for Claude Pro (about twenty US dollars a month) in your own name at [claude.ai](https://claude.ai). It is separate from your Familiar subscription, and the same kind of thing as a ChatGPT subscription, just Claude.

1. The Anthropic Claude Code extension is already installed by the installer. If for some reason it is not, open the Extensions panel (the four-squares icon in the left sidebar), search for "Claude", and install it.
2. Click the Claude icon in the left sidebar and sign in with your Claude Pro account.
3. Open the Claude chat panel and say hello. Your Familiar runs a short setup conversation on its first turn to learn who you are and how you work. Give it the time it asks for. Everything you tell it becomes its permanent memory.

## Manual install (technical users)

For developers who already have git and VS Code and would rather run it by hand instead of using the double-click installer:

```bash
git clone https://github.com/EcodiaCode/familiar-starter.git ~/Familiar
cd ~/Familiar
code .
```

Then do the "What you do after the installer finishes" steps above: get a Claude Pro plan, install the Claude Code extension if it is not already there, sign in, and say hello to start the setup conversation.

## Where everything lives

The whole assistant is this folder. Your knowledge corpus grows under `knowledge/`, your working state lives in `status-board.md`, drafts go under `drafts/`. Back the folder up the way you back up documents. Copy it to a new computer and your assistant comes with you.

## If something does not work

Reply on your Familiar welcome email, or write to code@ecodia.au. Say which step you were on and what you saw.
