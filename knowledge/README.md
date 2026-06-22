# Familiar's knowledge corpus

This is Familiar's persistent memory. Everything in this folder is read at session start (or for relevant subsets via lookup) and becomes context Familiar uses to act.

## What goes here

- `operating-with-you.md` - your tech-comfort band and how you want Familiar to talk and work. Holds a `Band: A` (or B / C) line that the session-start hook reads to calibrate its register, plus a short note in your words on what to show and what to keep off screen. Captured in the first setup chat; change it any time by saying "too technical" or "show me how".
- `client-roster.md` - active your work clients, what they're working on, when last contact was
- `brand-guidelines.md` - your work brand voice, visual rules, banned vocab
- `vendor-list.md` - suppliers, freelancers, agencies Familiar may need to contact
- `recipes/` - one file per workflow Familiar figured out, written down so next time is one read instead of re-figuring it from scratch
- `mistakes.md` - what went wrong and how to avoid the shape next time, so a wall climbed once is never a wall again
- `learned-rules.md` - durable preferences and rules you have stated ("never schedule before 10am", "always bcc the office account")
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
