---
title: Few-shot prompting
domain: 4
tasks: ["4.2"]
verified: "2026-08-12"
---

# Few-shot prompting

**The most effective technique when detailed instructions alone produce inconsistent results.** The trigger is: *"we already wrote detailed instructions and it still varies."*

## What examples do that instructions cannot

- Carry **judgment on ambiguous cases** — tool selection for ambiguous requests, branch-level coverage gaps
- Enable **generalisation to novel patterns**, rather than matching only what you enumerated
- **Reduce hallucination** in extraction — informal measurements, varied document structures

## The count matters

**2–4 targeted examples**, each showing the *reasoning* for why one action was chosen over a plausible alternative.

When a distractor proposes "5–8 examples showing…", the number is itself a signal. Volume is not the mechanism — in the guide's own sample question, a many-examples option loses to a better tool description.

## When few-shot is the *wrong* answer

Few-shot is a strong technique that is also this exam's most common wrong answer, because it plausibly helps almost anything. Ask whether it addresses the **stated cause**:

| Symptom | Right fix |
|---|---|
| Two tools with thin descriptions get confused | [Tool descriptions](tool-descriptions.md) |
| An ordering invariant is sometimes violated | [Prerequisite gate](deterministic-enforcement.md) |
| Output format varies despite detailed instructions | **Few-shot** ✅ |

See [explicit criteria](explicit-criteria.md) · [4.2](../tasks/4-2.md)
