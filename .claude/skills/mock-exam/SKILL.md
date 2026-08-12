---
name: mock-exam
description: Run a full 60-item timed CCAR-F mock exam with blueprint-weighted domain allocation and 4 of 6 scenarios, then produce a diagnostic report. Use to measure readiness.
argument-hint: [--seed N] [--untimed]
---

# Mock exam

A full simulation: **60 items, 120 minutes, 4 scenarios drawn from 6**.

## Build the form

Run the builder rather than selecting items yourself:

```bash
python scripts/build_exam.py --json          # add --seed N to reproduce
```

It returns the selected scenarios, the item ids in presentation order, any
off-scenario fills, and any shortfalls. Read the items from `questions/bank/`.

**The allocation rule** (implemented in the script, stated here so you can explain
it): each exam scenario declares only 2–3 primary domains — scenario 2 covers
domains 3 and 5 only — so a form cannot be both scenario-pure and weight-exact.
The blueprint weights win. Per domain, prefer items tagged to one of the four
selected scenarios, then domain-generic items, then any remaining item in that
domain, recorded as an off-scenario fill.

**If the script reports shortfalls or fills, tell the user.** Never present a form
as blueprint-faithful when it is not.

## Administer

1. Announce the four scenarios and read out each scenario description from
   `wiki/scenarios/` before its items — the real exam frames items this way, and
   the details are load-bearing.
2. Note the start time. Target pace is **two minutes per item**.
3. Present items one at a time. Show the stem and four options. State
   `select_count` when it is greater than 1.
4. **Give no feedback during the exam.** Record the answer and move on.
5. Accept "flag" to mark an item for review, and "skip" to defer it. Return to
   flagged and skipped items at the end.
6. Unless `--untimed`, warn at 60 minutes elapsed and at 15 minutes remaining.

## Report

Only after all 60:

1. **Percent-correct overall.**
2. **Percent-correct by domain**, against the blueprint weights — this is what the
   real score report gives you, and it is the actionable part.
3. **Per-task-statement misses**, linked to their wiki notes.
4. **Distractor families** they fell for, ranked — but read them against the base
   rate. `solves-different-problem` is roughly half the bank, so several misses
   there indicate the general skill of matching a fix to the stated cause. A
   cluster in one of the other six families is the sharper signal: it names a
   specific reasoning habit. Link to the matching `wiki/heuristics/` note.
5. **Readiness, in words.** Use the signals in `wiki/exam/preparation-plan.md`:
   above 80% overall with no domain below 70% is the target. A strong average with
   one collapsed domain is not ready — say so plainly.
6. **What to study next**, ordered by blueprint weight × weakness.

Then walk through every missed item: the stem, what they chose, why it fails, and
why the correct answer is correct.

**Never emit a scaled score.** The 720/1000 cut comes from a standard-setting
study that cannot be reproduced, and a fabricated number invites someone to stop
studying at the wrong moment. `wiki/exam/format-and-scoring.md` explains this — say
so if the user asks for one.

Append the result to `mock_exams` in `progress/state.json`, and update the
per-task-statement entries.
