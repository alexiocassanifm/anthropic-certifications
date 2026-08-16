---
name: quiz
description: Run a short targeted quiz filtered by domain, task statement, scenario, or weak areas, with immediate per-item feedback. Use for practice between full mock exams.
argument-hint: [--domain N | --task N.N | --scenario N | --weak] [--count N]
---

# Quiz

A short, focused practice set — not a full exam. For that, use `/mock-exam`.

## Resolve the certification first

This repository holds several certification study kits under `certifications/`.
Before reading anything, decide which one you are working in:

- If the user names one (`ccar-f`), use `certifications/<slug>/`.
- If only one directory exists under `certifications/`, use it without asking.
- If several exist and the request is ambiguous, ask which.

Everything below is relative to that certification directory — `wiki/`,
`questions/`, and `progress/` all live inside it.

## Select items

Default: 10 items. Accept `--count`.

Filters:

| Argument | Behaviour |
|---|---|
| `--domain N` | Items from that domain |
| `--task N.N` | Items for one task statement |
| `--scenario N` | Items tagged with that exam scenario |
| `--weak` | Read `progress/state.json`; draw from the lowest-`confidence` task statements, weighted by domain blueprint weight |
| none | Spread across all five domains in blueprint proportion |

Prefer items whose id is **not** in that task statement's `seen_ids`. If the pool
is exhausted, reuse and say so.

## Run

Present **one item at a time** with **`AskUserQuestion`**, one call per item:

- `questions`: a single entry.
- `question`: the item's scenario, then a blank line, then the stem verbatim —
  `Scenario 3 — Multi-Agent Research System`, naming both when `scenario` lists two,
  and `No scenario — general` when it is `null`. Stems refer back to their scenario
  with definite articles (*the* coordinator, *the* extraction pipeline), so without
  the line the candidate cannot tell which cast is meant. This matters even under
  `--scenario N`, where every item shares one scenario: name it once when the quiz
  starts and still tag each item.
- `header`: `Q1`, `Q2`, … — the position in this quiz, not the bank id.
- `options`: exactly four, in the order they appear in the bank. `label` is the
  option's letter `A`, `B`, `C`, `D`; `description` is its full `text`.
- `multiSelect`: `true` when `select_count > 1`, `false` otherwise. The tool does
  not enforce a count, so if the number selected does not match `select_count`,
  say what was required and re-ask the same item once before scoring it.
- No `preview`.

Do not reveal anything early: no hints in the `question` text, no ordering of the
options that telegraphs the answer, nothing in `header`.

The tool always adds an **Other** choice. If it is used, read the free text as the
answer when it plainly names an option, and otherwise treat the item as unanswered
and move on.

After each answer:

- **Correct** — confirm, then give the `why` for the correct option *and* for at
  least the most tempting distractor, naming its family.
- **Wrong** — give the `why` for what they chose and for the correct option. Then
  name the family and connect it to the relevant heuristic in `wiki/heuristics/`.
  The family is the transferable lesson; the item is not.

Name a family the way `/study` does — see its **Name things the way a learner can
use them** section. Describe the trap first and give the canonical name once, and
keep bank item ids out of anything the learner reads, here and in the report.

Keep feedback tight — two or three sentences unless they ask for more.

## Report

At the end:

- Score, and **percent-correct by domain**
- Task statements that were missed, with links to their wiki notes
- Distractor families they fell for. `solves-different-problem` is the broadest
  family and about half the bank, so treat it as the base rate: a few misses there
  means the general skill of matching a fix to the *stated* cause needs work. A
  repeat in any of the other six is sharper — it points at one specific reasoning
  habit, and is worth calling out with the matching `wiki/heuristics/` note

Then update `progress/state.json`: per task statement, increment `seen` and
`correct`, append the item ids to `seen_ids`, set `last_reviewed`, and adjust
`confidence`.

Do **not** report a scaled score. See `wiki/exam/format-and-scoring.md`.
