# IT^3 Bob-a-thon — Participant Guide
### Developer Efficiency Lab · September 24, 2026

Welcome to the Women in Technology Bob-a-thon! This guide has everything you need
to get started and get the most out of the 90-minute workshop.

---

## 🗓 Event details

| | |
|---|---|
| **Date** | Wednesday, September 24, 2026 |
| **Locations** | Charlotte, NC · Atlanta, GA |
| **Duration** | 90 minutes |
| **Format** | Hands-on lab — work at your own pace |
| **IBM Contact** | Madison Ramsey — madison.ramsey@ibm.com |

---

## 💻 What you'll need

Everything runs in your **TechZone VM** — no local installation required.

- Your TechZone VM access will be provisioned before the event
- Bob V2 is pre-installed in the VM
- Python 3.9.21 is pre-installed in the VM

**If you have trouble accessing your VM:** Find an IBM facilitator at your location
or email madison.ramsey@ibm.com.

---

## 🚀 Getting started

This workshop includes **three labs**. Everyone begins with **Lab 1**, then continues with a second lab based on your role and interests.

> 💬 **All labs are driven from the Bob chat interface.** You'll type prompts, review responses, and approve actions directly in the Bob chat panel — you won't need to run scripts or use the terminal yourself. To open the chat panel if it isn't already visible, click the **Bob icon** in the sidebar, or use the keyboard shortcut **`⌥ ⌘ B`** (Mac) / **`Ctrl + Alt + B`** (Windows). The panel has three parts: the conversation history at the top, a text input at the bottom where you type your prompts, and a Send button (or press **Enter**) to submit.

1. Log in to your TechZone VM
2. Open Bob and ensure the chat panel is visible (see note above)
3. Start with **Lab 1 — Personal Productivity** (`Lab 1 - Productivity/instructions.md`) — this lab is for everyone
4. When you finish Lab 1, choose your next lab:
   - **Lab 2 — Research** (`Lab 2 - Research/instructions.md`) — ideal for analysts, consultants, and anyone whose day-to-day involves reading documents, synthesizing information, and producing written deliverables
   - **Lab 3 — Developer Efficiency** (`Lab 3 - Developer Efficiency/instructions.md`) — ideal for developers, data engineers, and technical practitioners who work in code daily

Work at your own pace. You don't need to complete every exercise in each lab — focus on what's most relevant to you.

---

## 🎯 Lab overview

### Lab 1 — Personal Productivity *(Everyone · ~30 min · Beginner)*

Applies to every knowledge worker regardless of technical background. You'll use Bob to manage a running to-do list conversationally, extract action items from meeting notes and email threads, merge them into a single prioritized list, and optionally draft a follow-up email in your own writing voice.

| Exercise | Focus |
|---|---|
| 1 — To-Do List | Have Bob maintain and update a task list through natural conversation |
| 2 — Action Item Extraction | Pull action items, owners, and deadlines from meeting notes and an email thread |
| 3 — Email Drafting *(optional)* | Draft a tone-matched follow-up email using your own emails as reference |

---

### Lab 2 — Research *(~30 min · Beginner–Intermediate)*

Focused on knowledge work that involves reading, synthesizing, and producing deliverables from multiple sources. No coding required.

| Exercise | Focus |
|---|---|
| 1 — Rapid Orientation | Get up to speed on an unfamiliar document without reading it end-to-end |
| 2 — Multi-Source Synthesis | Answer a research question by having Bob cross-reference several sources simultaneously |
| 3 — Structured Deliverable | Turn research findings into a briefing, comparison table, or decision note |

---

### Lab 3 — Developer Efficiency *(~90 min · Progressive)*

A hands-on coding lab built around a realistic Python data-engineering project (`data-pipeline`). Seven incremental checkpoints — each harder than the last. Work at your own pace; aim for checkpoints 1–4 at minimum.

| Checkpoint | Focus | Difficulty |
|---|---|---|
| 1 — Orient in the Codebase | Understand the project without reading every file | Entry |
| 2 — Read and Explain Code | Trace execution paths, generate documentation | Easy |
| 3 — Search and Pattern Recognition | TODOs, design patterns, security scan | Medium |
| 4 — Debug and Troubleshoot | Diagnose and fix a real pre-planted bug | Medium–Hard |
| 5 — Make and Validate Code Changes | Implement a feature and write a unit test | Hard |
| 6 — Bob Findings *(stretch)* | Surface and fix ML code quality issues | Stretch |
| 7 — Build Something New *(stretch)* | Scaffold a complete feature end-to-end | Open-ended |

Checkpoints 6 and 7 have no finish line — keep going if you have time.

---

## 💡 Tips for using Bob

- **Ask broad questions first.** Bob understands your entire codebase — not just the current file.
- **Be direct.** "Find the bug in normalize_amounts" works better than "help me with the code."
- **Review before applying.** Bob shows you diffs — always read what's changing before accepting.
- **Use follow-up prompts.** If Bob's first answer isn't quite right, correct it in the same conversation.
- **Watch for mode switching.** In complex tasks, Bob shifts between Ask, Plan, and Agent modes automatically.

### 🔐 Permissions and approvals

By default, Bob asks for your confirmation before taking any action that affects your system. You can either approve each action individually as it comes up, or enable **auto-approve** to let Bob work uninterrupted.

**How to approve during the lab:**
When Bob proposes an action (reading a file, editing code, running a command), **Approve** and **Reject** buttons appear above the chat input. Click **Approve** to proceed or **Reject** to cancel.

**Auto-approve — available permissions:**

| Permission | What it allows | Risk level |
|---|---|---|
| **Read** | View files and directory contents | Medium |
| **Edit** | Create, edit, and save files | High |
| **Execute** | Run commands in your terminal | High |
| **MCP** | Use configured MCP servers | Medium–High |
| **Skill** | Activate custom skills | Medium |
| **Todo** | Update the to-do list | Low |
| **Subtask** | Create and complete subtasks | Low |
| **Subagent** | Spawn subagents for focused tasks | Low |
| **Mode** | Switch modes during a task | Low |

To enable auto-approve: hover over the **Auto-Approve toolbar** above the chat input and toggle the permissions you want.

> **Recommended for these labs:** Enable **Read**, **Edit**, and **Execute** auto-approve so Bob can run tests, apply fixes, and read files without pausing for each step. Because you're working in a pre-provisioned TechZone VM, this is a safe and controlled environment. On your own machine, review each permission carefully before enabling it — **Edit** and **Execute** in particular carry high risk outside a sandbox.

---

## 📊 Business value table

| What you'll do in the lab | Time without Bob | Time with Bob |
|---|---|---|
| Orient in unfamiliar codebase | 30–60 min | ~5 min |
| Trace execution path across files | 15–30 min | Instant |
| Find a hardcoded credential | Manual review / security tooling | Seconds |
| Debug division-by-zero bug | 20–45 min | Directed in one conversation |
| Write a unit test | 15–20 min | Generated + explained quickly |
| Surface ML code quality issues | Requires profiling knowledge | Bob Findings |

---

## 📝 After the labs

1. **Claim your badge** — Follow the steps in [`BADGE_GUIDE.md`](BADGE_GUIDE.md) to earn your IBM Bob Bobathon badge via Credly. Switch Bob to **Badge Issuer Lite** mode, say *"I'd like to claim my bobathon badge"*, and Bob will walk you through the rest. Takes about 5 minutes.

2. **Complete the survey** — your facilitator will share the link at wrap-up. Your feedback helps shape future sessions, so please take a moment to fill it in.

3. **Keep exploring** — still have time? Ask Bob anything you're curious about, revisit a checkpoint you didn't finish, or try a prompt on something from your own work. There's no better time to experiment than right now with a facilitator nearby.

4. **Questions?** Reach out to Madison Ramsey — madison.ramsey@ibm.com

---

## 🔗 Resources

| Resource | Location |
|---|---|
| Lab 1 instructions | `Lab 1 - Productivity/instructions.md` |
| Lab 2 instructions | `Lab 2 - Research/instructions.md` |
| Lab 3 instructions | `Lab 3 - Developer Efficiency/instructions.md` |
| Badge guide | `BADGE_GUIDE.md` |
| Bob cheat sheet | Contact your IBM facilitator |
| Bob installation (outside TechZone) | Contact Madison Ramsey |
| IBM Bob documentation | [To be confirmed — check with IBM facilitator] |

---

*IBM Technology Sales · madison.ramsey@ibm.com*  
*Made with Bob · Opportunity: 006gR000004t4ezQAA*
