---
name: quiz
description: Run a short targeted CCAR-F quiz filtered by domain, task statement, scenario, or weak areas, with immediate per-item feedback. Use for practice between full mock exams.
argument-hint: [--domain N | --task N.N | --scenario N | --weak] [--count N]
---

# Quiz

A short, focused practice set — not a full exam. For that, use `/mock-exam`.

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

Present **one item at a time**. Show the stem and all four options. If
`select_count > 1`, state how many to select — exactly as the exam does.

Wait for the answer. Do not reveal anything early.

After each answer:

- **Correct** — confirm, then give the `why` for the correct option *and* for at
  least the most tempting distractor. Name its `distractor_family`.
- **Wrong** — give the `why` for what they chose and for the correct option. Then
  name the distractor family and connect it to the relevant heuristic in
  `wiki/heuristics/`. The family is the transferable lesson; the item is not.

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
