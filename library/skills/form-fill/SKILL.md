---
name: form-fill
description: Fill out a web form, application, or portal field-by-field from what your person already gave you, then show it for a final check before submit. Use when they say "fill out this form", "do this application", or "enter this for me".
triggers: ["fill out this form", "do this application", "enter this for me", "complete the form", "fill in the", "submit this form", "register me on", "sign up for"]
---

# form-fill

Forms are pure grind: the same details typed into yet another box. form-fill does the typing in your person's own browser session and hands them a filled form to check before it goes.

## When to use

- A web form, application, or portal that wants details you already hold about your person.
- A repeat form where the answers are known and only need re-entering.

## When NOT to use

- A form that commits money, a legal agreement, or anything irreversible at submit. Fill it, but the final submit is theirs.
- Anything asking for credentials or secrets you should not handle. Surface it; do not enter passwords on their behalf beyond their own logged-in session.

## Fill the form

1. Read the form first. Drive the browser per the cdp-usage skill, in their logged-in session. List every field and what it wants.
2. Pull the answers from the knowledge corpus: their details, their org, the standard answers they have given before. Save a reusable answer set to `knowledge/form-answers.md` so the next form is faster.
3. Fill each field with real key events (`nativeFill`, not a value setter, since most forms run frameworks that ignore a raw value set). Descend into same-origin iframes as the cdp-usage skill describes.
4. For any field you cannot answer from what you hold, stop and ask. Do not guess on a form; a wrong answer on an application is worse than a pause.

## Before submit

- Screenshot or read back the completed form and show your person every field as filled.
- Walk anything you were unsure about explicitly.
- Wait for their go-ahead, then submit, then confirm the submission registered with a discriminating probe (the confirmation page or a follow-up read). A narrated submit is not a real one.

## Hard rules

- Never invent an answer to fill a field. Ask, or leave it for them.
- The final submit on anything binding, paid, or irreversible is theirs, after they have seen every field.
- Never enter passwords or secrets beyond driving their own already-signed-in session.
- Confirm the submit took; do not claim it went through on faith.
