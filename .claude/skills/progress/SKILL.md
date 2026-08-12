---
name: progress
description: Show a CCAR-F readiness dashboard - percent correct overall and by domain, coverage of the 30 task statements, weak areas, and what to study next. Use to check where you stand.
---

# Progress

A readiness picture, not a score.

## Gather

Read `progress/state.json`. If it does not exist, say so and suggest starting with
a cold `/mock-exam` to establish a baseline — a number you can name beats a vague
sense of readiness.

Read `wiki/exam/blueprint.md` for the weights and `wiki/exam/preparation-plan.md`
for the readiness signals.

## Report

**1. Headline.** Percent-correct overall across all recorded practice, and the
result of the most recent `/mock-exam` if there is one.

**2. By domain.** A table with, per domain: items seen, percent correct, blueprint
weight, and items on a 60-item form. Order by weight, so Domain 1 leads.

Mark any domain below 70% clearly. Explain the arithmetic if it matters: a strong
average with one weak domain is not readiness, because the weights mean a
collapsed Domain 1 cannot be rescued by a strong Domain 5.

**3. Coverage.** How many of the 30 task statements have been practised at all.
List the untouched ones with links — an unpractised statement is an unknown, not a
strength.

**4. Weakest task statements.** The five lowest by `confidence`, each with its
domain weight and a link to its wiki note.

**5. Distractor families.** If mock exam or quiz history records which families
were missed, rank them. A repeated family is a reasoning habit and is worth more
attention than any single fact — point at the relevant `wiki/heuristics/` note.

**6. Due for review.** Task statements whose `due` date has passed, with a
suggestion to run `/drill`.

**7. What to study next.** Three concrete recommendations, ordered by blueprint
weight × weakness. Name the skill invocation for each, e.g. `/study 2.2`.

## Readiness

Close with an honest judgment against the signals in the preparation plan:
above 80% overall, no domain below 70%, and 60 items comfortably inside 110
minutes. Say plainly if they are not there yet, and name the single biggest gap.

**Never report a scaled score.** See `wiki/exam/format-and-scoring.md`.
