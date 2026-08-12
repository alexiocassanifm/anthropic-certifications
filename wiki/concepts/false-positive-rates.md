---
title: False positive rates and category disabling
domain: 4
tasks: ["4.1"]
verified: "2026-08-12"
---

# False positive rates and category disabling

**Trust is per-category, and one noisy category poisons the rest.**

A single high-false-positive category undermines developer confidence in the accurate categories too. Trust is not averaged across a system; it collapses.

## The counterintuitive move

**Temporarily disable the high-false-positive category** to restore trust, while you improve its prompts. Then re-enable.

This feels like giving up, which is why it is testable. The reasoning: developer trust is the scarce resource. A category producing 40% noise is actively destroying the value of the four categories that work. Turning it off is a net gain until it is fixed.

## Why not a global threshold

Lowering a confidence threshold across all categories degrades the good ones to fix the bad one. The problem is localised; the fix should be too.

## The `detected_pattern` field

Add it to structured findings so you can analyse **which code constructs trigger dismissals**. That turns "developers keep dismissing these" into a specific, fixable pattern. See [4.4](../tasks/4-4.md).

See [explicit criteria](explicit-criteria.md) · [4.1](../tasks/4-1.md)
