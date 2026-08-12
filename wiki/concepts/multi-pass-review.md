---
title: Multi-pass review and attention dilution
domain: 4
tasks: ["1.6", "4.6"]
verified: "2026-08-12"
---

# Multi-pass review and attention dilution

**Attention dilutes across a large pass.** One review of fourteen files produces detailed feedback on some, superficial comments on others, missed bugs, and **contradictory findings** — flagging a pattern as problematic in one file while approving identical code elsewhere in the same PR.

**"Contradictory feedback within one PR" is the signature symptom.**

## The fix

Split into **per-file local analysis passes** plus a **separate cross-file integration pass**. The integration pass is not optional — it is where cross-file data flow issues live.

## Why the distractors fail

| Wrong answer | Why |
|---|---|
| Require developers to split large PRs | **Shifts the burden** to humans without improving the system |
| Switch to a larger context window | Misunderstands the cause — attention **quality**, not capacity |
| Run three passes; flag issues appearing in ≥2 | **Suppresses** real bugs that are only caught intermittently |

That third one is the most instructive on the exam. Consensus voting feels like rigour and is actively harmful: the bugs you most need are exactly the ones a single pass catches inconsistently.

## Confidence for routing

Running verification passes where the model **self-reports confidence alongside each finding** is endorsed here for calibrated review routing — in contrast to [unreliable proxies](unreliable-proxies.md), where confidence as a proxy for case complexity is rejected. Scope and calibration are what separate them.

See [task decomposition](task-decomposition.md) · [session context isolation](session-context-isolation.md) · [4.6](../tasks/4-6.md)
