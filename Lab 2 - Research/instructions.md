# Lab 2: Research

**Duration:** 30 minutes
**Difficulty:** Beginner–Intermediate
**Prerequisites:** Completed Lab 1

## 🎯 Objectives

By the end of this lab, you will be able to:
- Use Bob to quickly understand unfamiliar business context, documentation, or domain knowledge
- Research a targeted question by pointing Bob at multiple sources simultaneously
- Synthesize findings from several sources into a concise summary or recommendation
- Produce a short written deliverable (briefing, comparison, or decision note) from raw research

## 📋 Setup

Before starting, ensure you have:
- [ ] Completed Lab 1
- [ ] Bob running in your IDE or chat interface
- [ ] Access to the sample data in `Lab 2 - Research/sample-data/` (provided in this lab folder)

> **🔄 Use your own content instead of the samples.** Each exercise below uses a fictional
> research brief and sample source documents so the lab works out of the box. You can substitute
> any real documents, internal pages, or reference materials of your own at any point, either
> by pasting the content directly into the chat or by pointing Bob to your own files.

## 🔨 Exercises

---

### Exercise 1: Getting Up to Speed on Unfamiliar Territory (10 minutes)

**Scenario:** You've been pulled into a new topic area and need to get oriented quickly before
a meeting. Instead of reading every document end-to-end, have Bob extract what matters and
explain it to you.

> **Use your own content (optional):** Swap in any document, policy, internal wiki page, or
> domain reference you'd normally spend time reading end-to-end.

**Tasks:**
1. Point Bob at `Lab 2 - Research/sample-data/source-a.md` and ask it to give you a plain-language overview
2. Ask a follow-up question to dig into a specific area
3. Ask Bob what you'd most need to know before a meeting on this topic

**Example Prompts:**
```
Read sample-data/source-a.md and give me a plain-language overview. What is this about,
what are the key points, and what would I need to understand before a meeting on this topic?
```
```
What's the most important thing I should know about [specific aspect] from what you just read?
```

**Expected Outcome:**
- You understand the key points of an unfamiliar document without reading it yourself
- You can ask targeted follow-up questions to go deeper on specific areas
- You have a short list of things to know before a meeting on the topic

**💡 Real-time Value Indicator:**
Getting up to speed on a new topic typically means reading 10–30 pages before you feel
confident. Bob gets you to the key points in under a minute, leaving the reading time for
the areas that actually need your judgment.

---

### Exercise 2: Researching Across Multiple Sources (10 minutes)

**Scenario:** You need to answer a specific business or technical question, but the answer
is spread across several documents. Instead of reading each one and cross-referencing manually,
have Bob do the synthesis.

> **Use your own content (optional):** Swap in any set of real documents, reports, or reference
> pages that you'd normally cross-reference manually to answer a question.

**Tasks:**
1. Share your research question with Bob (use the sample brief, or bring your own)
2. Point Bob at `sample-data/source-a.md`, `sample-data/source-b.md`, and
   `sample-data/source-c.md` and ask it to answer your question from all three sources
3. Ask Bob to flag where sources agree, where they differ, and where there are gaps

**Example Prompts:**
```
Read sample-data/research-brief.md to understand the question I'm trying to answer.
Then read source-a.md, source-b.md, and source-c.md and answer the question using
all three sources.
```
```
Where do the three sources agree? Where do they differ or contradict each other?
What's missing that I'd need to answer this fully?
```

**Expected Outcome:**
- Bob answers the research question drawing on all three sources
- Agreements and contradictions across sources are surfaced, not hidden
- Gaps are flagged explicitly rather than papered over

**💡 Real-time Value Indicator:**
Manually cross-referencing three documents to answer one targeted question typically takes
30–60 minutes of reading and note-taking. Bob does it in seconds and surfaces contradictions
you'd likely have missed.

---

### Exercise 3: Synthesizing Into a Deliverable (10 minutes)

**Scenario:** You have your research. Now you need to turn it into something you can actually
share, a briefing, a recommendation, a comparison table, or a decision note.

> **Use your own content (optional):** Bring your own research findings, notes, or source
> documents from a real topic you're working on. Describe the deliverable format you need
> and Bob will produce it.

**Tasks:**
1. Ask Bob to produce a short written deliverable based on the research from Exercise 2
2. Specify the audience and format (pick one from the examples below or choose your own)
3. Give Bob one round of feedback and ask it to revise

**Example Prompts — choose one or bring your own:**

*Option A: Executive briefing*
```
Based on the research, write a 3–5 bullet executive briefing for a senior stakeholder
who won't read the source documents. Lead with the key finding, not background.
```

*Option B: Comparison table*
```
Summarize the key differences between the options covered in the three sources as a
comparison table. Include a recommended option with a one-sentence rationale.
```

*Option C: Decision note*
```
Write a short decision note (half a page) recommending an approach based on the research.
State the recommendation first, then the supporting evidence, then any risks or caveats.
```

**Follow-up revision prompt:**
```
Good, but make it shorter. Cut anything that's just restating what the sources said and
keep only what helps the reader decide or act.
```

**Expected Outcome:**
- Bob produces a structured, audience-appropriate deliverable from raw research
- The first draft is substantive, not a generic template with placeholders
- One round of feedback is enough to get to something ready to share

**💡 Real-time Value Indicator:**
Turning research notes into a polished deliverable typically takes 45–90 minutes of
drafting and editing. Bob produces a structured first draft in seconds, leaving you to
review and refine rather than write from scratch.

---

## 🎓 Key Takeaways

After completing this lab, you should understand:

1. **Rapid Orientation**
   - Bob can orient you in unfamiliar territory without requiring you to read everything first
   - Ask targeted follow-up questions to go deeper only where it matters
   - Use Bob before meetings to prepare quickly, not just after the fact

2. **Multi-Source Synthesis**
   - Bob reads and cross-references multiple documents simultaneously
   - Agreements and contradictions across sources are surfaced explicitly
   - Gaps in the available evidence are flagged rather than silently assumed away

3. **Structured Deliverables**
   - Bob can turn raw research into briefings, recommendations, tables, or decision notes
   - Specify the audience and format to get a useful first draft, not a generic summary
   - One clear round of feedback is usually enough to get to something shareable

4. **Going Further: Live Data Sources via MCP**

   The exercises above use static files as sources. Bob can also connect to **live data
   sources** through MCP (Model Context Protocol) servers, so your research doesn't have to
   start with a file you already have.

   **What MCP enables for research:**
   - Pull live data from internal tools (Confluence, SharePoint, Jira, ServiceNow) directly
     into Bob's context, no copy-paste required
   - Query databases, APIs, or dashboards and ask Bob to synthesize what it finds
   - Connect Bob to your organization's own knowledge bases and documentation systems

   **How it works:**
   MCP servers act as bridges between Bob and external systems. An administrator installs and
   configures the server once; after that, Bob can read from (and in some cases write to) the
   connected system just by being asked. IBM and the community publish ready-to-use MCP servers
   for common enterprise tools, and custom ones can be built for internal systems.

   **Example prompts with MCP connected:**
   ```
   Pull the last three sprint retrospectives from Confluence and summarize the recurring themes.
   ```
   ```
   Query the ServiceNow knowledge base for articles related to this incident type and tell me
   what the recommended resolution steps are.
   ```

   > **In this lab:** You used static sample files as a stand-in. In practice, those files could
   > be replaced by a live Confluence page, a SharePoint document, or a database query, with no
   > change to how you interact with Bob.

   See [`resources/bob-differentiators.md`](../resources/bob-differentiators.md) for more on MCP and Bob's extensible architecture.

5. **Best Practices**
   - Give Bob a clear question to answer, not just "summarize this"
   - Specify the audience when asking for a deliverable; it changes the output significantly
   - Use Bob to draft; bring your own judgment to the final review

---

## 💡 Tips for Success

1. **Ask a question, not just for a summary.** "What should I know before this meeting?" gets
   a more useful answer than "summarize this document."
2. **Name the audience.** "Write this for a senior executive who won't read the sources" produces
   a sharper deliverable than "write a summary."
3. **Point Bob at all sources at once.** You get better cross-referencing when Bob reads
   everything together than when you feed it sources one by one.
4. **One clear revision.** Give Bob one specific piece of feedback rather than several vague ones.
5. **Use it on real work.** The sample documents demonstrate the pattern; the real value shows
   when you bring your own questions and materials.

---

## 🐛 Common Issues

### Issue: Bob's summary misses something important
**Solution:** Ask a direct follow-up: "What does [source] say about [specific topic]?"

### Issue: Bob's deliverable is too long or too generic
**Solution:** Be explicit: "Cut to 5 bullets, lead with the recommendation, no background."

### Issue: Sources conflict and Bob picks one without flagging it
**Solution:** Ask directly: "Where do the sources disagree? What's uncertain?"

### Issue: Not sure what format to ask for
**Solution:** Describe who will read it and what they need to do with it. Bob will infer
a suitable format.

---

## 📝 Discussion Questions

1. How does being able to ask targeted questions change the way you'd use a large document?
2. When would you trust Bob's synthesis of sources, and when would you want to verify it yourself?
3. What types of deliverables in your day-to-day work could Bob produce a first draft of?
4. How is this different from a standard internet search?
5. Where in your current workflow would multi-source synthesis save you the most time?

---

## ✅ Completion Checklist

- [ ] Completed Exercise 1: rapid orientation from a single document
- [ ] Completed Exercise 2: multi-source synthesis to answer a research question
- [ ] Completed Exercise 3: structured deliverable from research findings
- [ ] Comfortable asking Bob targeted questions rather than just "summarize"
- [ ] Can point Bob at multiple sources at once and ask it to cross-reference
- [ ] Understand how to specify audience and format to get a useful deliverable

---

## 🚀 Next Steps

Once you've completed this lab:

1. **Claim your badge** — Follow the steps in [`BADGE_GUIDE.md`](../BADGE_GUIDE.md) to earn your IBM Bob Bobathon badge via Credly. Switch Bob to **Badge Issuer Lite** mode, say *"I'd like to claim my bobathon badge"*, and Bob will walk you through the rest. Takes about 5 minutes.

2. **Complete the survey** — your facilitator will share the link at wrap-up. Your feedback helps shape future sessions, so please take a moment to fill it in.

3. **Keep exploring** — still have time? Ask Bob anything you're curious about, revisit an exercise you didn't finish, or try a prompt on something from your own work. There's no better time to experiment than right now with a facilitator nearby.

4. **Questions?** Reach out to Madison Ramsey — madison.ramsey@ibm.com

---

## 📚 Additional Resources

- **Bob Differentiators**: See [`resources/bob-differentiators.md`](../resources/bob-differentiators.md)
- **Bob Documentation**: https://ibm.biz/bob-doc
- **Cheat Sheet**: See [`resources/cheat-sheet.md`](../resources/cheat-sheet.md)

---

**Need Help?** Ask your facilitator or use the dedicated support channel!

---

## 💰 Business Impact

This lab demonstrates how Bob accelerates knowledge work at the research and synthesis layer,
not just at the task execution layer.

### ⏱️ Productivity Gains
- **Rapid Orientation**: Getting up to speed on an unfamiliar document from minutes to seconds
- **Multi-Source Cross-Reference**: 30–60 minutes of manual reading and note-taking replaced by a single prompt
- **Deliverable Drafting**: 45–90 minutes of writing from scratch replaced by a structured first draft in seconds

### 🐛 Quality Improvements
- **Contradiction Detection**: Gaps and conflicts across sources are surfaced rather than missed
- **Audience Fit**: Deliverables are shaped for the actual reader, not a generic audience
- **Completeness**: Bob flags what's missing in the research rather than papering over gaps

### 💵 Cost Savings
- **Based on IBM Client Zero:** The Documentation and Analysis & Insights categories show
  95–100% time savings on synthesis-style tasks at scale
  (see [`resources/bob-productivity-gains-client-zero.md`](../resources/bob-productivity-gains-client-zero.md))
- **Everyday Applicability**: Every knowledge worker who reads documents and produces deliverables
  benefits from this pattern, not just technical roles

**Estimated Weekly Value per Participant**: 1–3 hours saved per research-heavy workday on
orientation, cross-referencing, and first-draft writing

---
