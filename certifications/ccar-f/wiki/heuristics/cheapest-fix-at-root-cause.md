---
title: The cheapest fix at the root cause
type: heuristic
---

# The cheapest fix at the root cause

If you learn one thing from this kit, learn this. It decides more items than any single domain fact.

> **Choose the least elaborate intervention that addresses the root cause actually stated in the stem.**

Two conditions, and both must hold. An answer that is cheap but aimed at the wrong problem loses. An answer that hits the right problem with a machine-learning pipeline, when a rewritten tool description would have done it, also loses.

## Why the exam is built this way

The exam tests **architectural judgment in production**, and the judgment that separates a good architect from a merely knowledgeable one is proportionality. Anyone can propose adding a classifier. Knowing that you do not need one yet — and being able to say *why* — is the skill being measured.

So the item writers construct options along two axes:

|  | Addresses the stated root cause | Addresses something else |
|---|---|---|
| **Proportionate** | ✅ the answer | plausible, wrong |
| **Elaborate** | tempting, wrong | obviously wrong |

The wrong answers are rarely stupid. They are usually things a competent engineer might actually do. That is the difficulty.

## How to apply it under time pressure

**Step 1 — Name the root cause in one sentence, before reading the options.**

The stem almost always states it or hands you the evidence for it. "Both tools have minimal descriptions" *is* the root cause. "The coordinator's logs show it decomposed the topic into three visual-arts subtasks" *is* the root cause. If you can name it, half the options eliminate themselves.

**Step 2 — Check each option against that sentence.** Not against "would this help?" — nearly all of them would help a bit. Against "does this fix *that*?"

**Step 3 — Among the survivors, take the cheapest.**

Rough cost ordering, from cheapest to most expensive:

1. Rewrite a description, a prompt, or a criterion
2. Add few-shot examples
3. Change configuration (`tool_choice`, scoping, allowed tools, rules files)
4. Restructure the workflow (split passes, add a stage, re-partition)
5. Add programmatic enforcement (a hook, a prerequisite gate)
6. Add a new component (a routing layer, a cache, a classifier)
7. Train or deploy a model

**The exception that matters:** cost ordering is overridden when the requirement is *guaranteed* compliance. If the stem involves money, identity verification, or a policy that must never be violated, a level-5 hook beats a level-1 prompt even though it is more expensive — because the cheap option does not actually solve the problem. See [deterministic vs probabilistic](deterministic-vs-probabilistic.md).

## The tell in the stem

Watch the question's verb phrase. It tells you which axis is being tested:

| Stem phrasing | What it is asking |
|---|---|
| "most effective **first step**" | Proportionality. The elaborate options are wrong *because* they are premature, not because they would not work. |
| "**most likely root cause**" | Diagnosis. Do not fix anything — identify which component is actually broken. |
| "**most effectively** address this" | Both. Right target, right size. |
| "how should you **evaluate** this proposal" | Constraint matching. Some part of the proposal fits and some does not; the answer usually splits it. |

"First step" is the strongest signal in the whole exam. When you see it, the answer is almost never the one that adds infrastructure.

## Worked pattern

*Symptom: an agent picks the wrong one of two similar tools 12% of the time. Both tool descriptions are one line.*

- Add a routing layer that parses input and pre-selects the tool → level 6. Also bypasses the model's language understanding, which is the thing you are paying for.
- Add 5–8 few-shot examples of correct routing → level 2. Would help, but it papers over a description problem with token overhead, and it does not generalise to the next similar tool you add.
- Merge both tools into one that figures it out internally → level 4. A defensible architecture, but it is a redesign, not a first step.
- **Expand both descriptions with input formats, example queries, edge cases, and explicit "use this instead of that when…" boundaries → level 1, and it hits the stated cause exactly.** ✅

The trap is that three of those four are things you might genuinely ship. Cheapness is what breaks the tie.

## The inverse trap

Do not over-rotate. "Cheapest" does not mean "smallest text change regardless of the problem." A vague instruction like *"be conservative"* or *"only report high-confidence findings"* is extremely cheap and reliably **wrong** on this exam, because it does not address anything — it just asks the model to try harder. See [4.1](../tasks/4-1.md).

Cheap and *specific* wins. Cheap and vague loses to everything.

## Related

- [Deterministic vs probabilistic](deterministic-vs-probabilistic.md) — when the cheap option is disqualified
- [Least-privilege tooling](least-privilege-tooling.md) — the proportionality rule applied to tool access
- [`questions/question-style-guide.md`](../../questions/question-style-guide.md) — the distractor families this heuristic defeats: `over-engineered`, `solves-different-problem`, `shifts-burden`
