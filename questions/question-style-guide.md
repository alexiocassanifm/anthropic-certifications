# Question style guide

How CCAR-F items are built, and how to write ones that train the right reflexes.

This is original analysis of the item *style* — derived from the published objectives, the scenario descriptions, and the exam's stated emphasis on tradeoff judgment. It contains no exam content. See [`../DISCLAIMER.md`](../DISCLAIMER.md).

---

## The item shape

A good item on this exam is a **production symptom plus four defensible responses**, exactly one of which is best.

> Production data shows that in 12% of cases, your agent skips the verification step and processes the action using only the customer's stated name, occasionally leading to misidentified accounts. What change would most effectively address this reliability issue?

Three things make that work:

1. **A measured symptom.** "12% of cases" is falsifiable and gives the reader something to reason against. "Sometimes it makes mistakes" does not.
2. **A stated consequence.** Misidentified accounts, incorrect refunds — the stakes decide whether a prompt fix is acceptable.
3. **Four options a competent engineer might actually ship.** If a distractor is obviously silly, the item tests nothing.

## What not to write

| Bad | Why |
|---|---|
| "What is a `PostToolUse` hook?" | Definition recall. The exam tests judgment, not vocabulary. |
| "Which of these is NOT a valid `tool_choice` value?" | Negative-form trivia. |
| "What is the best practice for tool descriptions?" | No situation, so no tradeoff. |
| Options of obviously different quality | One plausible answer and three straw men measures nothing. |

Write the symptom first, then ask what you would actually do about it, then write the three next-best things you considered.

---

## The seven distractor families

Every wrong option should be one of these, and be tagged with it in the YAML. If you cannot classify a distractor, it is probably a straw man — rewrite it.

### `prompt-instead-of-enforcement`
Prompt or few-shot guidance where **deterministic enforcement** is required.

> *"Enhance the system prompt to state that customer verification is mandatory before any order operation."*

Fails because prompt instructions have a non-zero failure rate. When money moves or identity must be verified, "usually complies" is a production incident waiting. See [deterministic vs probabilistic](../wiki/heuristics/deterministic-vs-probabilistic.md).

### `over-engineered`
A classifier, routing layer, trained model, or new infrastructure component when a description, prompt, or configuration change would address the stated cause.

> *"Deploy a separate classifier model trained on historical tickets to predict which requests need escalation."*

Fails on proportionality. Especially wrong when the stem says **"first step"**. See [cheapest fix at the root cause](../wiki/heuristics/cheapest-fix-at-root-cause.md).

### `solves-different-problem`
A plausible, competent fix aimed at something other than the root cause the stem describes.

> Stem: tool *ordering* is violated. Option: *"Implement a routing classifier that enables only the subset of tools appropriate for that request type."* — that is tool *availability*.

Fails because it would not change the reported symptom. The hardest family to spot, and the most valuable to practise.

### `blames-wrong-component`
In a pipeline, faults a downstream component that is working correctly within the scope it was given.

> Stem: the coordinator decomposed the topic too narrowly. Option: *"The web search agent's queries are not comprehensive enough."*

Fails because the named component did its job. When every component succeeds and the whole fails, look **upstream**.

### `unreliable-proxy`
Routes or decides on a signal that correlates poorly with the thing that matters.

> *"Have the agent self-report a confidence score (1–10) before each response and automatically route to humans when confidence falls below a threshold."*
> *"Implement sentiment analysis to detect customer frustration and escalate when negative sentiment exceeds a threshold."*

Fails because LLM self-reported confidence is poorly calibrated (the agent is confident *and* wrong on hard cases) and sentiment measures annoyance, not complexity. Also covers keyword-matching routers and iteration caps used as loop control.

**Exception:** field-level confidence **calibrated against a labelled validation set** is legitimate ([5.5](../wiki/tasks/5-5.md)). The labelled set is the difference.

### `suppresses-signal`
Consensus voting, error swallowing, or filtering that hides real findings.

> *"Run three independent review passes and only flag issues that appear in at least two of the three runs."*
> *"Catch the timeout within the subagent and return an empty result set marked as successful."*

Fails because the findings you most need are the ones caught intermittently, and a suppressed error cannot be recovered from.

### `shifts-burden`
Pushes work onto humans instead of improving the system.

> *"Require developers to split large PRs into smaller submissions of 3–4 files before the automated review runs."*

Fails because the system is unchanged; you have only moved the cost.

---

## Stem archetypes

| Phrasing | What it asks | Reading |
|---|---|---|
| *"most effective **first step**"* | Proportionality | The elaborate options are wrong **because premature**, not because they would not work |
| *"most likely **root cause**"* | Diagnosis | Do not fix anything — identify which component is actually broken |
| *"most effectively address"* | Both | Right target, right size |
| *"how should you **evaluate** this proposal"* | Constraint matching | The proposal is usually **half** right; the answer splits it |

**"First step" is the strongest signal on the exam.** When you see it, the answer almost never adds infrastructure.

---

## Writing the `why` fields

The `why` is the study material; the item is the delivery mechanism. Aim for one or two sentences that would teach the point even without the question.

- **On the correct option:** name the principle, not just the mechanic. *"Programmatic enforcement provides a deterministic guarantee that prompt-based approaches cannot, which is required when errors have financial consequences."*
- **On wrong options:** say what it *would* fix, then why that is not the stated problem. *"This addresses tool availability rather than tool ordering, which is the actual failure."*

Avoid "this is incorrect" as a `why`. It teaches nothing.

---

## Coverage targets

The bank aims for **three items per task statement**, giving per-domain totals of 21 / 15 / 18 / 18 / 18. That guarantees every objective is exercised and leaves enough pool that a 60-item mock exam is not memorised after one run.

Within each task statement's three items, vary the shape: one diagnostic, one "first step" proportionality item, one applied-configuration item where possible.

---

## Before you open a PR

```bash
python scripts/validate_questions.py
```

It must exit 0. And confirm in the PR description that your items are original — see [`../CONTRIBUTING.md`](../CONTRIBUTING.md).
