---
name: study
description: Teach one certification task statement or concept from the wiki, then check recall with a few questions. Use when the user wants to learn or review exam material.
argument-hint: [task-statement-or-topic]
---

# Study

Teach one piece of CCAR-F material properly, then verify it landed.

## Resolve the certification first

This repository holds several certification study kits under `certifications/`.
Before reading anything, decide which one you are working in:

- If the user names one (`ccar-f`), use `certifications/<slug>/`.
- If only one directory exists under `certifications/`, use it without asking.
- If several exist and the request is ambiguous, ask which.

Everything below is relative to that certification directory — `wiki/`,
`questions/`, and `progress/` all live inside it.

## Resolve the target

The argument may be a task statement id (`1.4`), a domain (`domain 3`), a concept
name (`tool_choice`), or a plain-language topic (`escalation`).

1. Read `wiki/exam/out-of-scope.md` **first**.
2. If the topic is on the out-of-scope list, say so plainly, name the nearest
   in-scope task statement, and offer to study that instead. Only proceed with an
   out-of-scope topic if the user explicitly asks — and say clearly that it is not
   exam material.
3. Otherwise map the request to a file:
   - task statement → `wiki/tasks/<d>-<n>.md`
   - concept → `wiki/concepts/<slug>.md`
   - heuristic → `wiki/heuristics/<slug>.md`
   - domain → `wiki/domains/<n>-*.md`, then work through its task statements
   - ambiguous → use `wiki/README.md` to pick, and say which you chose

   The heuristics are cross-domain reasoning patterns, so they are named by phrase
   rather than by id — "deterministic vs probabilistic", "cheapest fix at the root
   cause", "least-privilege tooling". A `/mock-exam` report points at them by name
   when a distractor family clusters, and that pointer has to resolve to a lesson.

## Teach

Read the note in full, plus its linked concepts, before saying anything.

Then, in your own words:

1. **What it tests** — one short paragraph.
2. **The knowledge** — the conceptual points, with the *why*. Do not paste the
   note back; explain it.
3. **Anti-patterns** — what the guide flags as wrong, and why each fails. This is
   where most exam items get their distractors, so give it real weight.
4. **Exam angle** — how it is likely framed, and which distractor families apply.
5. **Drift** — if the note has an "In production, beyond the guide" section, say
   what the guide expects versus what current docs say, and make clear the guide
   is the exam answer.

Keep it conversational. If the user seems to know part of it already, skip ahead.

## Check

Ask **2–3** questions drawn from `questions/bank/` for that task statement. Present
one at a time. After each answer:

- If correct, confirm briefly and say *why* the distractors fail — that is the
  transferable part.
- If wrong, do not just give the answer. Ask what made the chosen option
  attractive, then explain the distinction.

If the bank has no items for the topic, write questions in the style of
`questions/question-style-guide.md`. Do not save them unless the user asks — that
is what `/author-question` is for.

## Record

After the checks, update `progress/state.json` (create it from
`progress/state.example.json` if absent) for the task statement covered:
`confidence` (0–5, your read of how solid they are), `seen`, `correct`,
`last_reviewed` (today), `seen_ids`, and a one-line `notes`.

Close by naming the next thing worth studying, based on the blueprint weights and
what `progress/state.json` shows is weak.
