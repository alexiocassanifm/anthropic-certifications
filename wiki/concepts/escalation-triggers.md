---
title: Escalation triggers
domain: 5
tasks: ["5.2"]
verified: "2026-08-12"
---

# Escalation triggers

## The three legitimate triggers

1. The customer **requests a human**
2. A **policy exception or gap** — *not merely a complex case*
3. **Inability to make meaningful progress**

Note what is absent: difficulty. Complexity alone is not a trigger; a policy **gap** is.

## The fine distinctions the exam tests

| Situation | Do this |
|---|---|
| Customer explicitly demands a human | **Escalate immediately** — do not investigate first "to be helpful" |
| Customer is frustrated, issue is straightforward | **Acknowledge the frustration and offer to resolve**; escalate only if they reiterate |
| Policy is silent or ambiguous on their request (competitor price matching, when policy covers only own-site adjustments) | **Escalate** — this is a policy gap |
| Tool returns multiple customer matches | **Ask for another identifier** — do not select on heuristics |

## The fix when calibration is wrong

**Explicit escalation criteria with few-shot examples** in the system prompt, demonstrating when to escalate versus resolve. The root cause of miscalibration is unclear decision boundaries, and this is the proportionate first response before adding infrastructure.

See [unreliable proxies](unreliable-proxies.md) · [structured handoff](structured-handoff.md) · [5.2](../tasks/5-2.md)
