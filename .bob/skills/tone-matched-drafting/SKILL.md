---
name: tone-matched-drafting
description: Use when drafting an email or message that should sound like the user's own writing voice. Reads reference emails from a designated folder to learn tone before drafting; falls back to a neutral professional tone if no reference emails are provided.
---

# Tone-Matched Drafting

Draft correspondence that sounds like the user wrote it, using a small sample of their own emails
as a style reference.

## Step 1 — Check for reference emails

Look for a folder of reference emails. By default, use `sample-data/tone-reference-emails/` if it
exists in the current workspace; if the user points to a different folder, use that instead.
Treat anything in that folder other than its own `README.md` as a reference sample.

- **If reference emails exist:** read all of them before drafting anything.
- **If none exist (only a README, or the folder is empty/missing):** skip to Step 3 and use a
  neutral, professional tone. Mention once that adding 3–6 of the user's own emails to that folder
  would let future drafts match their voice more closely.

## Step 2 — Learn the tone from the reference emails

From the reference emails, identify:
- Sentence length and rhythm (short and direct vs. longer and explanatory)
- Greeting and sign-off habits
- Level of formality
- Characteristic phrases or word choices
- How directly the writer makes requests (blunt ask vs. softened lead-in)

Use these patterns to draft in that voice. Don't imitate the *content* of the reference emails,
only the *style*.

## Step 3 — Draft the requested email

Produce the first draft already in the target tone (from Step 2, or the neutral fallback). Don't
produce a generic draft and then offer to "adjust the tone" afterward; get it right the first time.

Keep the same style discipline regardless of which tone is used:
- Get to the point in the first sentence; no throat-clearing openers
- No em dashes (—); use a comma, parentheses, or a separate sentence instead
- No tidy summary sentence that just restates what was already said
- One clear ask beats several soft, hedged ones

## Step 4 — Apply feedback in one pass

If the user gives feedback (e.g. "more direct," "less formal"), apply it directly to the full draft
rather than asking clarifying questions first. Treat one clear round of feedback as enough; don't
require multiple back-and-forth exchanges to converge on the right tone.

## Step 5 — Final check before presenting

Before presenting the draft, confirm:
1. No em dashes remain
2. The opening sentence gets to the point without a throat-clearing lead-in
3. The tone matches the reference emails (or the neutral fallback, if none were provided)
4. The draft is ready to send with light editing, not a placeholder-filled template
