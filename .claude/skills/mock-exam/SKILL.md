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

It returns the seed, the selected scenarios, the item ids in presentation order, a
per-item `items` map giving `domain`, `task_statement`, `select_count` and
`scenario`, the option order for each item, the correct slots for each item, any
off-scenario fills, and any shortfalls. Read the item text from `questions/bank/`.

**Record the `seed` before item 1 and put it in the report.** It is emitted whether
or not you passed `--seed`, and it is the only way to rebuild the form afterwards.

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

1. Read out all four scenario descriptions from `wiki/scenarios/` **before item 1**,
   not before each scenario's items. The builder shuffles the form, so items from
   the four scenarios are interleaved and there are no blocks to introduce. Tell the
   candidate the context will switch item to item, and that every item names its own
   scenario.

   **Read out the `## The situation` section and nothing else.** Everything below it
   in those files is written for post-exam study and states the answers: the
   *Failure modes to expect* table maps each symptom to the correct fix, and *The
   traps* / *Task statements most likely to be tested here* name the rest. Scenario 6
   gives away `tool_choice: "any"`; scenario 1 gives away the prerequisite gate;
   scenario 5 gives away the independent review instance. Quoting any of it turns
   the mock into an open-book test and destroys the diagnostic the run exists to
   produce. `## The situation` is the framing the real exam gives, and it is enough.
2. Note the start time. Target pace is **two minutes per item**.
3. Say once, before item 1, how flagging works — see step 6. Nobody discovers it
   mid-exam otherwise.
4. Present items one at a time with **`AskUserQuestion`**, one call per item:
   - `questions`: a single entry.
   - `question`: the item's scenario, then a blank line, then the stem verbatim.

     ```
     Scenario 3 — Multi-Agent Research System

     A web search subagent times out mid-task. You are designing what it
     reports back to the coordinator. …
     ```

     **The scenario line is load-bearing, not a label.** Stems refer back to their
     scenario with definite articles — *the* coordinator, *the* extraction pipeline
     — and an interleaved form gives the candidate no other way to know which cast
     is meant. Name both when `scenario` lists two. When `scenario` is `null`, open
     with `No scenario — general` rather than guessing one.

     Do not trim the stem — reading a dense stem under time pressure is part of
     what the exam measures.
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
4. **Distractor families** they fell for, ranked **by rate, never by count**. For
   each family compute `chosen ÷ present`, where `present` is how many times that
   family appeared as a wrong option *on this form* — count it from the bank entries
   of the 60 items served, not from the bank as a whole. Report both numbers and the
   rate.

   Ranking by raw count inverts the finding. `solves-different-problem` is roughly
   half the wrong options, so it collects the most picks on almost any form while
   sitting at its base rate — which means the general skill of matching a fix to the
   stated cause is *intact*, and it should be reported as carrying no signal. The
   family to name is whichever one is most over-represented against its own
   availability, even at two or three picks: that is what identifies a specific
   reasoning habit. Link to the matching `wiki/heuristics/` note.
5. **Readiness, in words.** Use the signals in `wiki/exam/preparation-plan.md`:
   above 80% overall with no domain below 70% is the target. A strong average with
   one collapsed domain is not ready — say so plainly.
6. **What to study next**, ordered by blueprint weight × weakness, **with the command
   to run beside each entry**. A diagnosis the candidate has to translate into actions
   is half a report. Give the per-task-statement table a `/study N.N` and
   `/quiz --task N.N` column, and turn the domain ordering into a numbered sequence of
   runnable phases.

   Only emit forms these skills actually document: `/quiz` takes **one** filter per
   invocation (`--domain N` | `--task N.N` | `--scenario N` | `--weak`) plus optional
   `--count N` — never two filters of the same kind. `/study` takes one task
   statement, concept, heuristic phrase, or domain. `/drill` takes `--count N` and
   `--due-only`. `/progress` takes nothing. Check the target skill's `argument-hint`
   before writing a flag into a report; a command that does not parse is worse than a
   prose instruction.

   Sequence teaching before testing where a whole domain has collapsed — quizzing a
   model the candidate does not have yet just reproduces the same wrong picks. Where
   the gap is one statement, quiz first. When a distractor family clusters, point at
   the `wiki/heuristics/` note by phrase (`/study deterministic vs probabilistic`),
   because no single task statement contains a cross-domain habit.

   Close on re-measurement, and separate the two mock runs: `/mock-exam --seed <seed>`
   re-grades the same form and is a diagnostic re-check only; a bare `/mock-exam`
   draws a fresh form and is the one that can support a readiness claim.

Then walk through every missed item: its scenario, the stem, what they chose, why
it fails, and why the correct answer is correct. Restate the scenario for the same
reason it appears during the exam — a stem that says "the coordinator" is as
unanchored in the report as it would be on the item.

**Use the slot letters the candidate saw, not the bank's.** The options were
permuted for this form, so an item stored with `correct: [A]` may have been
answered in slot D. Read the `why` text by bank id via `option_order`, then refer
to it by its slot. Telling someone "the answer was A" when they saw it as D
teaches them nothing and makes them distrust the report.

**Never emit a scaled score.** The 720/1000 cut comes from a standard-setting
study that cannot be reproduced, and a fabricated number invites someone to stop
studying at the wrong moment. `wiki/exam/format-and-scoring.md` explains this — say
so if the user asks for one.

**"Would this have passed?" has no honest answer, and the question will be asked.**
Say plainly that it is not computable, in one sentence, with the reason: the raw
percentage that maps to 720 varies by form. Then give what *is* available — the
readiness bar in `wiki/exam/preparation-plan.md` — and rule against it. A result
in the low-to-mid 70s is the trap case: it looks like it clears "720 must be 72%",
which is the exact inference `format-and-scoring.md` warns against. Name that trap
when the result lands there.

## Offer a durable copy

The report is long and a chat transcript is a poor place to keep it. After the
walkthrough, ask with a single **`AskUserQuestion`** whether to publish it — options
`HTML artifact` (recommended), `Markdown artifact`, and `No, chat is fine`.

Ask once, at the end, and never in place of the in-chat report — the artifact is a
copy, not the delivery. If they accept, **load the `artifact-design` skill before
writing the file**, then publish with the `Artifact` tool.

Carry the whole diagnostic across, not a summary: the overall and per-domain
percentages, the pass/fail field marked as not computable, the per-task-statement
table, the distractor families with their rates, the study plan **including its
commands**, and every missed item with its scenario, stem, chosen slot, correct slot,
and both `why` texts. Put the form's provenance — date, seed, scenarios, off-scenario
fills, elapsed time — in the header, so a form can be rebuilt from the report alone.

The commands matter most here: an artifact is read days later, away from this
conversation, and it is the only place the candidate can pick the thread back up.

Append the result to `mock_exams` in `progress/state.json`, and update the
per-task-statement entries. `progress/` ships without a `state.json`; create it from
the shape in `progress/README.md` on first run rather than failing. It is gitignored
— never stage it.
