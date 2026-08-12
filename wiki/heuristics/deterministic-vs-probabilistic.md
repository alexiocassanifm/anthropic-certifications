---
title: Deterministic enforcement vs probabilistic compliance
type: heuristic
---

# Deterministic enforcement vs probabilistic compliance

> **A prompt instruction has a non-zero failure rate. When the requirement is that something must *never* happen, put it in code.**

This is the second great divider on the exam, and it overrides [cheapest fix at the root cause](cheapest-fix-at-root-cause.md) whenever guaranteed compliance is at stake.

## The two mechanisms

| | Probabilistic | Deterministic |
|---|---|---|
| **How** | System prompt instructions, few-shot examples, tool descriptions | Hooks, prerequisite gates, `tool_choice` forcing, schema constraints |
| **Guarantee** | None. Compliance is high but not 100%. | Absolute, for the rule encoded. |
| **Cost** | Low — text | Higher — code, testing, maintenance |
| **Flexibility** | Adapts to situations you did not anticipate | Only enforces what you wrote down |
| **Failure mode** | Silent, intermittent, load-bearing at exactly the wrong moment | Blocks a legitimate edge case you did not foresee |

Both are correct in their place. The exam tests whether you know which place you are in.

## The test

Ask: **what happens the 1% of the time the model does not comply?**

- *A slightly worse answer.* → prompt is fine. Prefer it; it is cheaper and more adaptable.
- *Money moves incorrectly. An unverified identity gets account access. A policy is violated. A regulated action happens without its prerequisite.* → prompt is **not** fine, no matter how well written.

"12% of the time it skips `get_customer` and refunds the wrong account" is not a prompting problem you can prompt your way out of. Rewriting the instruction to say *mandatory* moves 12% to maybe 3%. Three percent of refunds going to the wrong customer is still a production incident.

## What deterministic enforcement looks like

**Prerequisite gates** — block a tool call until an earlier step has completed successfully. `process_refund` is unavailable until `get_customer` has returned a verified customer ID. The model cannot skip the step because the step is not skippable. See [1.4](../tasks/1-4.md).

**Tool call interception hooks** — inspect an outgoing call and block or redirect it. A refund above $500 never reaches the payment system; it is rerouted to human escalation. See [1.5](../tasks/1-5.md).

**`PostToolUse` hooks** — transform results before the model sees them. Normalising Unix timestamps, ISO 8601 strings, and numeric status codes into one format is not something to ask a model to do reliably every time — it is a transformation, so write the transformation. See [1.5](../tasks/1-5.md).

**`tool_choice`** — `"any"` guarantees the model calls *a* tool rather than replying in prose; forced selection (`{"type": "tool", "name": "..."}`) guarantees it calls a *specific* one. This is how you make structured output non-optional. See [4.3](../tasks/4-3.md).

**Schema constraints** — a strict JSON schema via tool use eliminates malformed JSON *entirely*. Note the boundary: it eliminates **syntax** errors, not **semantic** ones. Line items that do not sum to the stated total still pass schema validation. See [4.3](../tasks/4-3.md) and [4.4](../tasks/4-4.md).

## Where prompts are genuinely the right answer

The exam is not "always choose the hook." Prompt-level fixes win when the problem is **judgment**, not **guarantee**:

- Unclear decision boundaries — when to escalate versus resolve. You cannot enumerate every case in code; explicit criteria plus few-shot examples are the correct fix. See [5.2](../tasks/5-2.md).
- Inconsistent output format — few-shot examples are the most effective technique when detailed instructions alone produce variation. See [4.2](../tasks/4-2.md).
- Wrong tool selection caused by weak descriptions — fix the descriptions. See [2.1](../tasks/2-1.md).
- False positives in review — explicit categorical criteria, not confidence thresholds. See [4.1](../tasks/4-1.md).

The pattern: **prompts shape judgment; code enforces invariants.** Using a prompt for an invariant is the classic error. Using a hook where you needed judgment is the less common but equally real error — you end up with a rigid system that blocks legitimate cases.

## The related trap: unreliable proxies

Adjacent to this heuristic is a family of wrong answers that *look* deterministic but are not:

- **Self-reported confidence scores** — an LLM's own confidence is poorly calibrated. An agent that is wrong on a hard case is typically wrong *and confident*. Routing on self-reported confidence routes exactly the wrong cases. (Field-level confidence calibrated against a **labelled validation set** is different and legitimate — see [5.5](../tasks/5-5.md).)
- **Sentiment analysis** as an escalation trigger — sentiment measures how annoyed the customer is, which does not correlate with case complexity. See [5.2](../tasks/5-2.md).
- **Keyword or pattern matching** in a routing layer — brittle, and it discards the language understanding you are already paying for.
- **Iteration caps** as the primary loop-termination mechanism — a safety net, not a control-flow decision. The loop terminates on `stop_reason`. See [1.1](../tasks/1-1.md).
- **Consensus across multiple runs** ("flag only issues appearing in 2 of 3 passes") — suppresses real findings that are only caught intermittently. See [4.6](../tasks/4-6.md).

If an option's mechanism is a proxy for the thing you care about rather than the thing itself, it is almost certainly a distractor.

## Related

- [Cheapest fix at the root cause](cheapest-fix-at-root-cause.md) — the default rule this one overrides
- [1.4](../tasks/1-4.md) enforcement and handoff · [1.5](../tasks/1-5.md) hooks · [4.3](../tasks/4-3.md) structured output
- [`questions/question-style-guide.md`](../../questions/question-style-guide.md) — distractor families `prompt-instead-of-enforcement` and `unreliable-proxy`
