---
name: git-sync
description: Use when the user wants to sync, pull, update, or push changes with the shared repo — including phrases like "pull down any changes", "get the latest", "sync up", "push my changes", or "update the repo". Walks through each step in plain English and pauses for human confirmation before any destructive action.
---

# Git Sync

Your audience includes non-technical users, so explain every action in plain English before running it. Never assume the user knows git terminology — always say what you're doing and why.

## Repository Facts

- All changes go directly to **main**. There are no branches, no pull requests, no forks.
- All content files are **Markdown (`.md`)**. Binary files will never need merging.
- Remote: `origin`, branch: `main`.

## Workflow — follow these steps in order

<Steps>

<Step>

### Step 1 — Check current state
Run `git status` and `git log --oneline -5` to understand what local changes exist and where HEAD is. Report back in plain English:
- "You have X changed files not yet saved to the shared repo."
- "Your copy is Y commits behind the shared version." (or "up to date")

</Step>

<Step>

### Step 2 — Fetch remote changes
Run `git fetch origin main`. This downloads the latest state without touching any files yet. Tell the user you are "checking for updates" — do not use the word "fetch".

</Step>

<Step>

### Step 3 — Identify conflicts before merging
Run `git diff HEAD origin/main --name-only` to list files that differ. Read each changed file locally and from the remote diff. Flag any file where the same section was edited on both sides.

</Step>

<Step>

### Step 4 — Pause for confirmation
Before doing anything destructive, summarise in a short bullet list:
- Files you will update locally (remote changes only)
- Files with conflicts (both sides changed the same section)

Then ask: **"Ready to bring in the latest updates? (yes / no)"**

Do not proceed until the user says yes (or equivalent).

</Step>

<Step>

### Step 5 — Pull and merge
Run `git pull origin main`. If git exits with a zero status (no conflicts), skip to Step 7.

</Step>

<Step>

### Step 6 — Resolve merge conflicts (conservative strategy)
For every file that has conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`):

1. Read the file.
2. For each conflict block, **keep BOTH versions** — do not discard either side.
3. Replace the raw git conflict markers with a clean Markdown notation:

```
<!-- MERGE CONFLICT: review and reconcile the two versions below -->

**Version from main (incoming):**
[incoming text]

**Your local version:**
[local text]

<!-- END MERGE CONFLICT -->
```

4. Save the file.
5. Stage it: `git add <file>`.

After resolving all conflicts, report each file resolved and what sections were flagged. Use plain language:
- "I kept both versions of the 'Summary' section in `customers/acme/overview.md` and marked it for your review."

</Step>

<Step>

### Step 7 — Commit (if there were conflicts to resolve)
If you wrote any conflict-notation blocks, commit with a clear message:

```
git commit -m "Merge main: conflict sections flagged for review in [list files]"
```

If the pull was clean, no additional commit is needed.

</Step>

<Step>

### Step 8 — Pause before pushing
Show the user a final summary:
- Files changed
- Any conflict markers still in place that they should review

Then ask: **"Everything looks good. Ready to push to the shared repo? (yes / no)"**

Do not push until the user explicitly says yes.

</Step>

<Step>

### Step 9 — Push
Run `git push origin main`. Report success or failure in plain English.

If the push fails due to a new remote update that arrived while you were working, restart from Step 2 and tell the user: "Someone else made a change while we were working. I'll pull that in first — this only takes a moment."

</Step>

</Steps>

## Error handling
- If `git pull` fails for a reason other than merge conflicts (e.g. network error, authentication), stop and report the exact error message in a clearly labelled block, then ask the user to let a technical colleague know.
- Never force-push (`--force`). Never rebase. Never delete any file as part of conflict resolution.
- If uncertain about any file, stop and ask the user before proceeding.

## Output style
- Short paragraphs. No jargon without explanation.
- Use ✅ for completed steps and ⚠️ for items needing the user's attention.
- Never dump raw git output at the user — summarise it, then offer "Want to see the full details?" if relevant.
