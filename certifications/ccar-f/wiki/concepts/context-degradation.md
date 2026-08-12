---
title: Context degradation
domain: 5
tasks: ["5.4"]
verified: "2026-08-12"
---

# Context degradation

**Context degrades before it runs out.**

## The signature

In extended sessions the model starts giving **inconsistent answers** and referring to **"typical patterns"** rather than the specific classes it discovered earlier. That phrasing is the tell: it has lost the specifics and fallen back on priors. It will keep answering fluently; it has stopped being right.

## The countermeasures

| Technique | What it does |
|---|---|
| **Scratchpad files** | Persist key findings across context boundaries; reference them for later questions |
| **Subagent delegation** | Keep verbose exploration out of the main thread while the main agent coordinates |
| **Summary injection** | Summarise phase N's findings before spawning agents for phase N+1 |
| **`/compact`** | Reduce context usage when it fills with verbose discovery output |
| **State manifests** | Each agent exports state to a known location; the coordinator loads a manifest on resume for crash recovery |

## Not a capacity problem

A bigger model or a larger window does not fix degradation, any more than it fixes [attention dilution](multi-pass-review.md). The fix is keeping the coherent thread small.

See [Explore subagent](explore-subagent.md) · [tool output trimming](tool-output-trimming.md) · [5.4](../tasks/5-4.md)
