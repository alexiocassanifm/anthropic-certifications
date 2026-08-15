---
name: mock-exam
description: Run a full timed mock exam with blueprint-weighted domain allocation and scenario framing, then produce a diagnostic report. Use to measure readiness.
argument-hint: [--seed N] [--untimed]
---

# Mock exam

A full simulation. Read the certification's `wiki/exam/blueprint.md` for its
format — for CCAR-F that is **60 items, 120 minutes, 4 scenarios drawn from 6**.

## Resolve the certification first

This repository holds several certification study kits under `certifications/`.
Before reading anything, decide which one you are working in:

- If the user names one (`ccar-f`), use `certifications/<slug>/`.
- If only one directory exists under `certifications/`, use it without asking.
- If several exist and the request is ambiguous, ask which.

Everything below is relative to that certification directory — `wiki/`,
`questions/`, and `progress/` all live inside it.

## Build the form

Run the builder rather than selecting items yourself:

```bash
python scripts/build_exam.py --cert <slug> --json          # add --seed N to reproduce
```

It returns the selected scenarios, the item ids in presentation order, the option
order for each item, the correct slots for each item, any off-scenario fills, and
any shortfalls. Read the item text from `questions/bank/`.

**Option order comes from the builder, not from the bank.** The bank stores options
in a fixed order; the builder permutes them per form so that repeat runs cannot be
answered from position. For each item the JSON gives:

```json
"option_order": { "d1-1.1-001": ["C", "A", "D", "B"] },
"correct":      { "d1-1.1-001": ["B"] }
```

`option_order` reads left to right as slots A, B, C, D — so slot A shows the bank's
option C, slot B shows the bank's option A, and so on. `correct` is already in slot
letters. **Grade against `correct` from the JSON, never against the `correct` field
in the bank** — that one refers to bank ids and will be wrong once the options move.
When you later quote an item's `why` text in the report, look it up by bank id and
refer to it by the slot the candidate actually saw.

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
3. Say once, before item 1, how flagging works — see step 6. Nobody discovers it
   mid-exam otherwise.
4. Present items one at a time with **`AskUserQuestion`**, one call per item:
   - `questions`: a single entry.
   - `question`: the stem, verbatim. Do not trim it — reading a dense stem under
     time pressure is part of what the exam measures.
   - `header`: `Item N` (the position in the form, not the bank id).
   - `options`: exactly four, in the builder's `option_order`. `label` is the slot
     letter `A`, `B`, `C`, `D`; `description` is that option's full text from the
     bank. Never put the bank id in the label.
   - `multiSelect`: `true` when `select_count > 1`, `false` otherwise.
   - No `preview`.
5. **Give no feedback during the exam.** Record the slot letter and move on. Do not
   acknowledge whether it was right, and do not vary your wording in a way that
   leaks it.
6. `AskUserQuestion` always offers **Other** alongside the four options. That is the
   flag/skip channel: the candidate picks Other and types `flag` to mark an item for
   review, or `skip` to defer it. Treat any other free text as a written answer and
   record it as unanswered unless it plainly names one option. Return to flagged and
   skipped items at the end, re-asking them the same way.
7. On a `multiSelect` item, if the number selected does not equal `select_count`,
   re-ask the same item once, restating the required count. Record the second answer
   whatever it is — the real exam does not negotiate either.
8. Unless `--untimed`, warn at 60 minutes elapsed and at 15 minutes remaining.

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

**Use the slot letters the candidate saw, not the bank's.** The options were
permuted for this form, so an item stored with `correct: [A]` may have been
answered in slot D. Read the `why` text by bank id via `option_order`, then refer
to it by its slot. Telling someone "the answer was A" when they saw it as D
teaches them nothing and makes them distrust the report.

**Never emit a scaled score.** The 720/1000 cut comes from a standard-setting
study that cannot be reproduced, and a fabricated number invites someone to stop
studying at the wrong moment. `wiki/exam/format-and-scoring.md` explains this — say
so if the user asks for one.

Append the result to `mock_exams` in `progress/state.json`, and update the
per-task-statement entries.
