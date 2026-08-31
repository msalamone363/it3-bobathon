---
name: action-item-sync
description: Use when extracting action items, owners, and deadlines from a meeting transcript and/or email thread, and merging them into a running to-do list. Flags duplicate items and unclear ownership rather than merging silently.
---

# Action Item Sync

Turn unstructured meeting and email content into a clean, merged to-do list.

## Step 1 — Extract from each source separately

For each source provided (meeting transcript, email thread, or similar), read the full file before
extracting anything. For each source, produce:
- The action item itself, stated as a concrete task
- The owner (who said they'd do it, or who it was assigned to)
- Any deadline or timing mentioned
- The source it came from

Do not skip items that seem minor. Do not paraphrase away specifics (names, dates, numbers) that
were stated explicitly.

## Step 2 — Flag unclear ownership

If a source doesn't make ownership explicit, don't guess. Mark the item as "owner unclear" rather
than assigning it to whoever seems likely. Surface these to the user rather than silently deciding.

## Step 3 — Merge across sources

When multiple sources are provided:
- Identify items that refer to the same underlying task (even if worded differently) and merge them
  into one entry rather than listing duplicates
- If two sources give conflicting details for what looks like the same item (different deadline,
  different owner), keep both details visible and flag the conflict rather than picking one silently
- Preserve items that are unique to a single source

## Step 4 — Filter to what's actually the user's

If the user has an existing to-do list (from this conversation or otherwise), merge the new items
into it. Ask which items are actually theirs to do if it isn't obvious from context, rather than
assuming every extracted item belongs to the user.

## Step 5 — Present the result

Present the merged list as a clean to-do list (use `update_todo_list` if this is being tracked as a
live list in the conversation). For each item, note the source it came from if the user might want to
verify it later. List any ownership or deadline conflicts flagged in Steps 2–3 separately at the end
so they're easy to review.
