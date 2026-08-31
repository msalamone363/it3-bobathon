# Lab 1: Personal Productivity

**Duration:** 30 minutes
**Difficulty:** Beginner
**Prerequisites:** Bob installed and running

## 🎯 Objectives

By the end of this lab, you will be able to:
- Have Bob create and maintain a running to-do list conversationally
- Extract action items from a meeting transcript and an email thread
- Synthesize action items from multiple sources into one prioritized task list
- (Optional) Personalize Bob's writing style to match your own tone using reference emails
- Draft a follow-up email faster using AI assistance

## 📋 Setup

Before starting, ensure you have:
- [ ] Bob running in your IDE or chat interface
- [ ] Access to the sample data in `Lab 1 - Productivity/sample-data/` (provided in this lab folder)
- [ ] **Optional:** 3–6 of your own past emails saved in `Lab 1 - Productivity/sample-data/tone-reference-emails/`; see that folder's `README.md` for instructions. If you skip this, Bob will use a neutral professional tone instead.


> **💡 Custom skills power this lab.** Exercises 2 and 3 are backed by two custom Bob skills
> (`action-item-sync` and `tone-matched-drafting`). Bob applies them automatically based on what you ask it to do, no slash command needed.

> **🔄 Use your own content instead of the samples.** Every exercise below uses sample files
> (`meeting-notes.md`, `email-chain.md`, `tone-reference-emails/`) so the lab works out of the
> box. If you'd rather use the real thing, just give Bob your own meeting transcript, email chain,
> or past emails instead, either by pasting the content directly into the chat or by pointing Bob
> to your own file(s) in place of the sample path. Nothing else about the exercise changes.

## 🔨 Exercises

### Exercise 1: A To-Do List Bob Maintains For You (10 minutes)

**Scenario:** You have a handful of tasks on your mind. Instead of writing them down yourself, have Bob track them for you, and keep the list updated as things change.

**Tasks:**
1. Tell Bob about 3–4 things you need to get done (real ones, or use the examples below)
2. Ask Bob to mark one as complete
3. Ask Bob to add a new task and reprioritize the list

**Example Prompt:**
```
I need to get a few things done today:
- Send the budget summary to my manager
- Follow up with the vendor about the invoice discrepancy
- Book a conference room for Thursday's planning session

Please track these for me as a to-do list.
```

**Follow-up prompts to try:**
```
I finished the budget summary; mark that one done.
```
```
Add "review Q3 numbers before Thursday's meeting" and make it the top priority.
```

**Expected Outcome:**
- Bob maintains a live, structured task list throughout the conversation
- You can update, complete, and reprioritize items just by talking to Bob
- You never had to open a separate notes app or spreadsheet

**💡 Real-time Value Indicator:**
This is the same underlying capability Bob uses to track its own multi-step work, applied here to *your* day. No formatting, no separate app, no manual reordering.

---

### Exercise 2: Turning Meeting Notes and Emails Into Action Items (10–15 minutes)

**Scenario:** Action items are scattered across your meeting notes and a follow-up email thread. Instead of re-reading both and writing your own list, have Bob do the extraction, and merge the results into the to-do list from Exercise 1.

> **Use your own content (optional):** You can swap in your own real meeting notes and/or email
> thread instead of the samples below (paste them in, or point Bob to your own file).
> Using the provided samples works just as well if you'd rather not.

**Tasks:**
1. Point Bob at `sample-data/meeting-notes.md` (or your own meeting notes) and ask it to pull out action items, owners, and deadlines
2. Point Bob at `sample-data/email-chain.md` (or your own email thread) and do the same
3. Ask Bob to merge both sets of action items into your running to-do list, flagging anything that's just for you

**Example Prompt:**
```
Read sample-data/meeting-notes.md and list the action items, who owns each one, and any deadlines mentioned.
```
```
Now read sample-data/email-chain.md and do the same thing.
```
```
Merge the action items from both into my to-do list from before. Only include the ones that are actually mine to do, and flag anything with an unclear owner.
```

**Expected Outcome:**
- Bob accurately extracts action items, owners, and deadlines from unstructured notes and emails
- Duplicate or overlapping items from the two sources are consolidated
- Your to-do list now reflects real commitments from a meeting and an email thread, not just what you remembered

**💡 Real-time Value Indicator:**
Manually re-reading meeting notes and an email thread to build a task list typically takes 10–15 minutes and things get missed. Bob does the extraction in seconds and catches items you'd likely have missed on a first read.

---

### Exercise 3 (Optional): Drafting Email in Your Own Voice (10 minutes)

**Scenario:** You need to send a follow-up email, but you want it to sound like *you* wrote it, not like generic AI output.

> **Use your own content (optional):** For the strongest result, add 3–6 of your own past emails to
> `sample-data/tone-reference-emails/` (or point Bob to wherever you saved them) so Bob learns your
> actual voice. No reference emails on hand? Bob falls back to a solid neutral, professional tone
> automatically, no extra setup needed.

**Tasks:**
1. If you added 3–6 of your own emails to `sample-data/tone-reference-emails/` (or another folder of your choosing), ask Bob to review them first
2. Ask Bob to draft a follow-up email based on one of the action items from Exercise 2, in your tone
3. Give Bob one round of feedback and ask it to adjust

**Example Prompt (with tone reference emails provided):**
```
Read the emails in sample-data/tone-reference-emails/ and get a sense of how I typically write:
tone, greeting/sign-off style, sentence length, level of formality.

Then draft a follow-up email to the vendor about the invoice discrepancy from the email chain,
using that same voice.
```

**Example Prompt (no tone reference emails, generic tone):**
```
Draft a professional follow-up email to the vendor about the invoice discrepancy from the email chain.
Keep it concise and polite.
```

**Follow-up feedback prompt:**
```
Good, but I'm more direct than that in real emails; trim the pleasantries and get to the ask faster.
```

**Expected Outcome:**
- Bob produces a draft that's ready to send with light editing, not a generic template
- With tone reference emails: the draft sounds recognizably like the participant, not like a generic AI assistant
- Without tone reference emails: Bob still produces a solid professional draft as a fallback

**💡 Real-time Value Indicator:**
Drafting a follow-up email from scratch typically takes 5–10 minutes once you factor in re-reading context and getting the tone right. Bob produces a tone-matched first draft in seconds, leaving you to just review and send.

> **Privacy note:** Only use emails you're comfortable sharing in this lab environment. Reference emails are used to describe writing style only; Bob does not need to see anything confidential to learn tone, sentence length, and phrasing patterns.

---

## 🎓 Key Takeaways

After completing this lab, you should understand:

1. **Conversational Task Tracking**
   - Bob can maintain a running to-do list without a separate app
   - Add, complete, and reprioritize tasks just by describing changes
   - No formatting or manual upkeep required

2. **Multi-Source Synthesis**
   - Bob can extract action items, owners, and deadlines from unstructured text
   - Multiple sources (meetings, emails) can be merged into one clean list
   - Overlaps and unclear ownership get flagged instead of silently duplicated

3. **Tone-Matched Writing**
   - Bob can learn your writing style from a small sample of your own emails
   - Reference material only needs to demonstrate tone, not identical content
   - Without a reference sample, Bob defaults to a solid generic professional tone

4. **Best Practices**
   - Be specific about what's "yours" vs. someone else's when merging tasks
   - Give feedback in one clear round rather than many small tweaks
   - Treat Bob as a first-draft partner; review before sending anything

## 💡 Tips for Success

1. **Start Real:** Use your own actual tasks in Exercise 1 if comfortable; it makes the value obvious
2. **Be Specific:** "Mark the budget summary done" works better than "update my list"
3. **Trust the Merge:** Let Bob do the deduplication in Exercise 2 rather than pre-sorting yourself
4. **One Round of Feedback:** In Exercise 3, give one clear piece of feedback rather than many small edits
5. **Skip Exercise 3 If Needed:** It's optional; Exercises 1 and 2 stand on their own

## 🐛 Common Issues

### Issue: Bob's to-do list doesn't reflect a recent change
**Solution:** Be explicit: "mark X as done" or "remove X" rather than assuming Bob inferred it

### Issue: Merged action items include things that aren't actually yours
**Solution:** Ask Bob to flag ownership explicitly before merging: "tell me who owns each item first"

### Issue: The tone-matched email doesn't sound like you
**Solution:** Add more reference emails (aim for 3–6) or give Bob more specific feedback about what feels off

### Issue: Not sure which tool to use
**Solution:** Ask Bob! "What's the best way to [accomplish task]?"

## 📝 Discussion Questions

1. How does having Bob maintain your to-do list compare to a notes app or task tracker you use today?
2. What's the risk of merging action items from multiple sources without human review?
3. How much of your own writing style could Bob pick up from just 3–6 emails?
4. Where else in your day could "extract action items from this" save you time?
5. What would you *not* want to hand off to Bob, even if it could technically do it?

## ✅ Completion Checklist

- [ ] Completed Exercise 1: Bob-maintained to-do list
- [ ] Completed Exercise 2: Meeting + email action item extraction and merge
- [ ] Completed Exercise 3 (optional): Tone-matched email draft
- [ ] Comfortable asking Bob to track, update, and reprioritize tasks
- [ ] Comfortable asking Bob to synthesize action items across sources
- [ ] Understand how reference material shapes Bob's writing tone

## 🚀 Next Steps

Once you've completed this lab:

1. **Try it with your own content** — feed Bob your actual inbox or a real meeting transcript and see how the patterns from this lab apply to something you work with every day.

2. **Strengthen your voice match** — add more of your own emails to the tone reference folder. The more examples Bob has, the closer the drafts will sound to you.

3. **Continue to your next lab** — choose based on your role and how you spend most of your time:
   - **Lab 2 — Research** (`Lab 2 - Research/instructions.md`) — ideal for analysts, consultants, and anyone whose day-to-day involves reading documents, synthesizing information, and producing written deliverables
   - **Lab 3 — Developer Efficiency** (`Lab 3 - Developer Efficiency/instructions.md`) — ideal for developers, data engineers, and technical practitioners who work in code daily

4. **Bring a real task list** — in your next Bob session, start with your actual recurring to-do list instead of sample data. The workflow is identical; the value is immediate.


## 📚 Additional Resources

- **Bob Differentiators**: See [`resources/bob-differentiators.md`](../resources/bob-differentiators.md) - Learn what makes Bob unique
- **Bob Documentation**: https://ibm.biz/bob-doc
- **Tool Reference Guide**: See [`resources/cheat-sheet.md`](../resources/cheat-sheet.md)
- **Troubleshooting**: See [`resources/troubleshooting.md`](../resources/troubleshooting.md)

### 🌟 Want to Learn More About Bob's Unique Capabilities?

Check out [`resources/bob-differentiators.md`](../resources/bob-differentiators.md) to learn about:
- **Extensible Architecture** - Custom modes, MCP server integrations, and Marketplace
- **Intelligent Optimization** - Automatic model selection and context management
- **Bob Findings** - Automated security and quality analysis
- **Agentic Workflows (v2)** - Sub-tasks, sub-agents, parallel execution, and pre-built workflows
- **Enterprise Modernization** - Java and legacy code transformation

---

**Need Help?** Ask your facilitator or use the dedicated support channel!

## 💰 Business Impact

This lab demonstrates how Bob accelerates everyday knowledge work, not just coding tasks:

### ⏱️ Productivity Gains
- **Task Tracking**: Eliminates manual to-do list upkeep in a separate app
- **Action Item Extraction**: Turns a 10–15 minute re-read of a transcript or email thread into a few seconds
- **Multi-Source Synthesis**: Merges overlapping action items instead of manually cross-checking two sources
- **Email Drafting**: Produces a tone-matched first draft in seconds instead of 5–10 minutes from scratch

### 🐛 Quality Improvements
- **Consistency**: Nothing gets missed when Bob extracts action items from long or messy transcripts
- **Ownership Clarity**: Ambiguous or unassigned action items are flagged rather than silently dropped
- **Tone Accuracy**: Draft emails sound like the participant instead of generic AI output

### 💵 Cost Savings
- **Reduced Manual Effort**: Based on IBM Client Zero's Documentation and Analysis & Insights categories, synthesis-style tasks like this see 95–100% time-savings gains at scale ([`resources/bob-productivity-gains-client-zero.md`](../resources/bob-productivity-gains-client-zero.md))
- **Faster Follow-Through**: Less time between a meeting/email and an action being tracked or acted on
- **Everyday Applicability**: Unlike dev-focused exercises, this lab's time savings apply to any knowledge worker's daily routine

**Estimated Weekly Value per Participant**: 20–30 minutes saved per meeting/email-heavy day on task tracking and follow-up drafting alone

---
