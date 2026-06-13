# Familiar's knowledge corpus

This is Familiar's persistent memory. Everything in this folder is read at session start (or for relevant subsets via lookup) and becomes context Familiar uses to act.

## What goes here

- `client-roster.md` - active your work clients, what they're working on, when last contact was
- `brand-guidelines.md` - your work brand voice, visual rules, banned vocab
- `vendor-list.md` - suppliers, freelancers, agencies Familiar may need to contact
- `voice-samples/` - 50+ samples of you writing, used for voice extraction (week 1)
- `sops/` - standard operating procedures (how you handles common situations)
- `episodes/` - daily session logs Familiar writes at end-of-day
- `decisions/` - durable decisions about how Familiar works (authored by you or Tate)
- `people/` - one file per person Familiar may interact with on your behalf, with relationship context

## How Familiar updates it

When you tells Familiar something new ("the Acme contract starts next month", "Sarah prefers email over Slack"), Familiar writes it to the right topic file the same session. Stale memory is worse than no memory.

## Seeding day 1

Tate or you adds: client-roster.md, brand-guidelines.md, voice-samples/ (drag-drop 50 writing samples - emails, posts, docs, whatever feels representative).

The rest grows organically over week 1 as Familiar works.

## What does NOT go here

- Credentials (those live in `~/familiar/.creds/`, chmod 600, never committed)
- Personal-not-business documents (Familiar has hard-stops on the personal sphere)
- Anything you would not want a future Familiar session to see
