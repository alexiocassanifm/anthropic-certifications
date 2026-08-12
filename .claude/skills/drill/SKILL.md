---
name: drill
description: Spaced-repetition practice on the CCAR-F task statements that are due or weakest, using an SM-2-lite schedule. Use for daily review between study sessions.
argument-hint: [--count N] [--due-only]
---

# Drill

Short spaced-repetition review. `/quiz` is for a topic you choose; `drill` chooses
for you, based on what you are forgetting.

## Read the schedule

Load `progress/state.json` (create from `progress/state.example.json` if absent).
Each task statement entry carries `confidence` (0–5), `ease`, `interval_days`,
`due`, `seen`, `correct`, and `seen_ids`.

Build the queue in this order:

1. **Overdue** — `due` before today, oldest first.
2. **Due today.**
3. **Never seen** — any of the 30 task statements with no entry.
4. **Weakest** — lowest `confidence`, tie-broken by domain blueprint weight so
   Domain 1 gaps surface before Domain 5 gaps.

With `--due-only`, stop after step 2 and say the queue is empty if it is. That is
a good outcome, not a failure — say so.

Default to 10 items. Draw from `questions/bank/`, preferring ids not in that task
statement's `seen_ids`.

## Run

One item at a time, same presentation as `/quiz`. Feedback immediately after each
answer, naming the `distractor_family` when they miss.

Because this is review rather than first exposure, keep explanations shorter — but
when they miss a task statement they have previously scored well on, stop and ask
what changed. A regression on known material usually means the underlying
distinction was never solid.

## Reschedule

After each task statement's items, update its entry with an SM-2-lite step:

| Result | Change |
|---|---|
| All correct | `ease` += 0.1 (cap 2.8); `interval_days` = round(`interval_days` × `ease`), min 1; `confidence` += 1 (cap 5) |
| Partially correct | `interval_days` unchanged; `confidence` unchanged |
| All wrong | `ease` −= 0.2 (floor 1.3); `interval_days` = 1; `confidence` −= 1 (floor 0) |

New entries start at `ease` 2.5, `interval_days` 1. Set `due` to today +
`interval_days`, and update `last_reviewed`, `seen`, `correct`, `seen_ids`.

## Report

Close with what was drilled, what moved, and what is due next — with the date.
If a task statement has now failed twice in a row, say plainly that drilling is
not working for it and recommend `/study <id>` instead. Repetition does not fix a
misunderstanding.
