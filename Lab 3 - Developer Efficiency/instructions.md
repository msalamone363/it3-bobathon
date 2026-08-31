# Lab 3 — Developer Efficiency
### IT^3 Bob-a-thon · Sep 24, 2026

**Duration:** 90 minutes  
**Language:** Python  
**Repo:** `Lab 3 - Developer Efficiency/data-pipeline/`  
**Difficulty:** Progressive — 7 incremental checkpoints, each harder than the last  
**Questions?** Madison Ramsey — madison.ramsey@ibm.com

---

## 🎯 Objectives

Work through a realistic Python data engineering codebase (`data-pipeline`) using Bob as your AI coding partner. Each checkpoint builds on the last. You don't need to finish all seven — work at your own pace. Checkpoints 6 and 7 are intentionally open-ended stretch goals.

**By the end you'll be able to:**
- Navigate and understand an unfamiliar Python project with Bob in minutes
- Use Bob's literate coding to read and explain non-trivial code
- Search for patterns, TODOs, and security issues across a codebase
- Debug a real bug using Bob's diagnostic capabilities
- Make, review, and test a code change with Bob as your pair programmer
- Use Bob Findings to surface ML code quality issues
- Scaffold a complete new feature end-to-end with Bob

---

## 📋 Setup

Before starting, ensure you have:
- [ ] Completed Lab 1
- [ ] Bob running in your IDE or chat interface

### 🗂 Repository overview

```
data-pipeline/
├── config/settings.py          ← Pipeline configuration (environment, credentials)
├── pipeline/
│   ├── ingest.py               ← Load raw CSV transactions
│   ├── transform.py            ← Clean and enrich data
│   ├── validate.py             ← Data quality checks
│   └── loader.py               ← Write to data warehouse
├── models/
│   ├── feature_engineering.py ← Feature extraction for ML
│   └── risk_scorer.py          ← Credit risk scoring model
├── utils/
│   ├── logger.py               ← Logging setup
│   └── db.py                   ← Database helpers
└── tests/
    ├── test_transform.py
    └── test_validate.py
```

---

> 💬 **How to get the most out of each checkpoint:** Don't just run the suggested prompts and
> move on — take a moment to **read Bob's response**. If something is unclear, surprising, or
> you want to go deeper, ask a follow-up question before continuing. Bob holds the full context
> of your conversation, so questions like *"Why did it do that?"*, *"What would happen if…?"*,
> or *"Explain that last part in simpler terms"* are always fair game. The prompts in each
> checkpoint are starting points, not scripts.

> 🔧 **The pipeline is intentionally incomplete.** As you work through the checkpoints, Bob may
> flag missing error handling, unimplemented stubs, TODOs, or other gaps in the codebase. This
> is by design — the pipeline was built with deliberate imperfections to give you realistic
> material to explore, debug, and improve. Treat anything Bob surfaces as an opportunity to
> dig in further, not as something that's broken or wrong with your setup.

---

## ✅ Checkpoint 1 — Orient in the Codebase
*Goal: Use Bob to understand this project without reading every file. (~10 min)*

> 💡 **Bob differentiator:** Bob has context over the entire repo — it doesn't just see the
> current file. Ask broad questions and Bob will synthesize across all files at once.

**Tasks:**

1. Ask Bob to explain the project structure:
   ```
   Explain the structure of the Python project @Lab\ 3\ -\ Developer\ Efficiency/data-pipeline/  . What does each top-level directory contain and what is each module responsible for?
   ```

2. Ask Bob to identify the entry point and describe what it does:
   ```
   What is the main entry point of this pipeline? Walk me through the end-to-end data flow from ingestion to loading.
   ```

3. Navigate to a file by description (without knowing its name):
   ```
   Which file is responsible for removing duplicate records and parsing timestamps? Open it.
   ```

4. Confirm your understanding: ask Bob which module would need to change if the data source
   switched from CSV files to an S3 bucket.

**✅ You're done when:** You can describe in one sentence what each module does without opening them yourself.

---

## ✅ Checkpoint 2 — Read and Explain Code
*Goal: Use Bob's literate coding capability to understand non-trivial Python. (~12 min)*

> 💡 **Bob differentiator:** Bob can trace execution paths through multiple functions across
> multiple files — something grep and manual reading can't do efficiently.

**Tasks:**

1. Ask Bob to explain a function in plain English:
   ```
   Explain what the compute_account_features function in models/feature_engineering.py does. Use plain English — no jargon.
   ```

2. Trace an execution path:
   ```
   Trace what happens when run_transformations is called with a raw DataFrame. Show me every function that gets called in order and what each one does to the data.
   ```

3. Identify dependencies:
   ```
   What does pipeline/loader.py depend on? List every import and external service it relies on.
   ```

4. Generate inline documentation for an undocumented function:
   ```
   The scale_features function in models/feature_engineering.py has no docstring. Write a complete docstring for it including Args, Returns, and Raises sections.
   ```

**✅ You're done when:** You've traced the full transformation pipeline and Bob has documented `scale_features`.

---

## ✅ Checkpoint 3 — Search and Pattern Recognition
*Goal: Use Bob to find patterns across the codebase quickly. (~12 min)*

> 💡 **Bob differentiator:** Bob can interpret intent, not just match strings. Ask "find all
> places where we ignore errors" and Bob understands that — not just `except: pass`.

**Tasks:**

1. Find all uses of a specific function:
   ```
   Find every place in this codebase where the logger object is used. Which modules log at ERROR level?
   ```

2. Surface all TODOs and FIXMEs and summarize them:
   ```
   Find all TODO and FIXME comments in the repo. Summarize them as a prioritized list — which are most important to address before production?
   ```

3. Identify a design pattern:
   ```
   Does this codebase follow a pipeline / chain-of-responsibility pattern? Where does that pattern appear?
   ```

4. Find the security issue (there is one deliberately planted):
   ```
   Scan this codebase for security-sensitive patterns — hardcoded credentials, secrets in source code, or insecure environment variable fallbacks. Report anything suspicious.
   ```

   > **Expected finding:** `config/settings.py` line 16 — hardcoded password fallback `"B0nk@Pipeline2024!"`.  
   > Ask Bob to explain why this is a risk and suggest a fix.

**✅ You're done when:** Bob has found the hardcoded credential and you've discussed how to remediate it.

---

## ✅ Checkpoint 4 — Debug and Troubleshoot
*Goal: Use Bob to diagnose and fix a pre-planted bug. (~15 min)*

> 💡 **Bob differentiator:** Bob can run tests, read the failure output, trace the root cause
> through the code, and propose a fix — all in one conversation without you switching context.

> 📺 **Viewing command output:** When Bob runs a terminal command, the output is displayed
> directly in the chat. If it appears collapsed, click the output block to expand it and see
> the full result. You can also type `@terminal` in the chat at any point to pull in the most
> recent terminal output as context for your next question.

**The bug:** `normalize_amounts` in `pipeline/transform.py` silently produces `NaN` values
when all transaction amounts in a batch are identical. There is already a failing test for it.

**Tasks:**

1. Run the tests and observe the failure:
   ```
   Run pytest tests/test_transform.py and show me the output.
   ```

2. Ask Bob to diagnose the failure:
   ```
   The test test_normalize_amounts_all_identical_values is failing. Read the test, read the normalize_amounts function, and explain the root cause of the bug.
   ```

3. Ask Bob to suggest a fix:
   ```
   Suggest a fix for the normalize_amounts bug. Explain why your fix is correct and what edge cases it handles.
   ```

4. Apply the fix and re-run the tests:
   ```
   Apply your suggested fix to pipeline/transform.py. Then run the tests again to confirm they pass.
   ```

**✅ You're done when:** All tests in `test_transform.py` pass including `test_normalize_amounts_all_identical_values`.

---

## ✅ Checkpoint 5 — Make and Validate Code Changes
*Goal: Use Bob as a coding assistant to implement a small feature. (~18 min)*

> 💡 **Bob differentiator:** Bob uses `apply_diff` to make surgical, reviewable changes.
> You see exactly what's changing before it's applied — just like a code review diff.

**The feature:** Add a new transformation function `add_weekend_flag` that adds a boolean
column `is_weekend` to the DataFrame — `True` when the transaction occurred on a Saturday or Sunday.

**Tasks:**

1. Ask Bob to implement the function:
   ```
   Add a new function called add_weekend_flag to pipeline/transform.py. It should add a boolean column 'is_weekend' that is True when the transaction_date falls on a Saturday or Sunday. Follow the same style as the existing transformation functions.
   ```

2. Review the proposed diff before accepting:
   - Look at what Bob proposes to change
   - Verify the logic is correct for weekend detection
   - Ask Bob to explain any part you're unsure about

3. Also add `add_weekend_flag` to the `run_transformations` function:
   ```
   Update run_transformations in pipeline/transform.py to call add_weekend_flag after add_high_value_flag.
   ```

4. Ask Bob to write a unit test:
   ```
   Write a pytest test for add_weekend_flag in tests/test_transform.py. Include a test case for a Saturday, a Sunday, and a weekday.
   ```

5. Run the new test to confirm it passes:
   ```
   Run pytest tests/test_transform.py -k "weekend" and show me the output.
   ```

**✅ You're done when:** The new function is in place, called in the pipeline, and the test passes.

---

## ✅ Checkpoint 6 — Bob Findings and ML Code Improvements *(Stretch)*
*Goal: Use Bob Findings to surface actionable improvements in ML code. (~13 min)*

> 💡 **Bob differentiator:** Bob Findings runs automated analysis across your code and surfaces
> security, quality, and performance issues that aren't obvious from manual review.

**Tasks:**

1. Point Bob at the risk scorer and run Findings:
   ```
   Run Bob Findings on models/risk_scorer.py and models/feature_engineering.py. Show me all findings.
   ```

2. Review the findings output — expected issues include:
   - Model loaded from disk on every call (no caching)
   - No input validation on feature array shape
   - No logging of prediction distribution for model monitoring
   - Hardcoded `magic number` threshold with no explanation

3. Select one finding and ask Bob to explain the impact:
   ```
   Explain the performance impact of loading the model from disk on every call to score_accounts. How much overhead does this add at scale?
   ```

4. Apply the improvement:
   ```
   Refactor risk_scorer.py to cache the loaded model using a module-level variable so it is only loaded once per process. Explain the change.
   ```

**✅ You're done when:** At least one Finding is understood and its improvement applied.

---

## ✅ Checkpoint 7 — Build Something New *(Stretch)*
*Goal: Use Bob to scaffold and deliver a complete small feature end-to-end.*

> 💡 **Bob differentiator:** Bob V2 can use sub-tasks and mode switching automatically —
> shifting from Ask → Plan → Agent as the work progresses and delegating focused subtasks
> to keep the main conversation clean. **This only happens if the Subtask permission is
> enabled in Bob's auto-approve settings.** Enable it by hovering over the Auto-Approve
> toolbar above the chat input and toggling **Subtask** on. If it's off, Bob will still
> complete the work but won't break it into sub-tasks or switch modes automatically.
> Watch for Bob switching modes during this checkpoint if Subtask is enabled.

**The feature:** `pipeline/report.py` does **not exist yet** — you will create it from scratch
using Bob. Add a `ReportGenerator` class to this new file that takes a validated, transformed
DataFrame and produces a simple summary report:
- Total transaction count
- Total and average transaction amount
- Count and percentage of high-value transactions
- Count and percentage of flagged high-risk accounts (if scores are provided)

**Tasks:**

1. Write a spec with Bob's help:
   ```
   Help me write a spec for a ReportGenerator class in pipeline/report.py. It should take a transformed DataFrame and optional risk scores array and generate a summary report. Capture the requirements, method signatures, and acceptance criteria before we write any code.
   ```

2. Generate an implementation plan:
   ```
   Generate an implementation plan for ReportGenerator before writing code. What methods should it have? What should each return?
   ```

3. Scaffold the implementation:
   ```
   Implement ReportGenerator in pipeline/report.py based on the plan. Follow the same style as the existing pipeline modules.
   ```

4. Write tests:
   ```
   Write pytest tests for ReportGenerator in tests/test_report.py. Cover: basic summary generation, correct handling of missing risk scores, and edge case of empty DataFrame.
   ```

5. Generate documentation:
   ```
   Add a docstring to the ReportGenerator class and each of its public methods. Also add a section to README.md describing the report module.
   ```

6. Reflect:
   ```
   Where in this feature did Bob save the most time?
   ```

**✅ There is no finish line.** Keep going as long as you have time. If you've exhausted this checkpoint and still have time remaining, head back to Checkpoint 6 and apply the other Bob Findings you didn't act on — each one is a self-contained improvement worth exploring.

---

## 📊 Business value — what did Bob just help you do?

| Activity | Without Bob | With Bob |
|---|---|---|
| Orient in unfamiliar codebase | 30–60 min reading files manually | ~5 min conversational exploration |
| Trace execution path through modules | Manual cross-file reading | Instant with one prompt |
| Find hardcoded credential | Manual code review / security scan tooling | Seconds |
| Debug division-by-zero bug | Read code + Google + trial and error | Directed diagnosis in one conversation |
| Write a unit test | Manual authoring | Generated + explained in seconds |
| ML code improvement (caching) | Requires profiling + architecture knowledge | Surfaced by Findings, explained, applied |

**For a team of 10 data engineers:** even 30 minutes saved per developer per day = **~130 hours/month** returned to the team.

---

## 📝 Reflection

After the lab:
1. Which checkpoint surprised you most?
2. Where did Bob behave differently than you expected?
3. What would you use Bob for first in your actual work?
4. What would you still do manually — and why?

---

## 🚀 Next steps

1. **Claim your badge** — Follow the steps in [`BADGE_GUIDE.md`](../BADGE_GUIDE.md) to earn your IBM Bob Bobathon badge via Credly. Switch Bob to **Badge Issuer Lite** mode, say *"I'd like to claim my bobathon badge"*, and Bob will walk you through the rest. Takes about 5 minutes.

2. **Complete the survey** — your facilitator will share the link at wrap-up. Your feedback helps shape future sessions, so please take a moment to fill it in.

3. **Keep exploring** — still have time? Ask Bob anything you're curious about, revisit a checkpoint you didn't finish, or try a prompt on something from your own work. There's no better time to experiment than right now with a facilitator nearby.

4. **Questions?** Reach out to Madison Ramsey — madison.ramsey@ibm.com
