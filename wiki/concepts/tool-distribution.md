---
title: Tool distribution across agents
domain: 2
tasks: ["2.3"]
verified: "2026-08-12"
---

# Tool distribution across agents

## Breadth degrades selection

**18 tools instead of 4–5 measurably reduces tool-selection reliability** by increasing decision complexity. Breadth is not capability.

## Agents misuse tools outside their specialisation

A synthesis agent given web search will search the web — badly, because searching is not what it was designed and prompted for, and doing so bypasses the agent built for that job. The failure is not "the tool broke"; it is "the architecture stopped being the architecture".

## The scoped-exception pattern

Least privilege here is not zero cross-role access. The shape the exam rewards:

> Give the agent a **narrow, purpose-built tool** for the high-frequency simple case; route complex cases through the coordinator as before.

A synthesis agent that constantly checks facts gets `verify_fact` — one scoped tool for simple lookups. It does **not** get the full web-search toolset. Complex verification still delegates.

This beats both extremes: full access over-provisions and breaks separation of concerns; pure delegation adds round trips for the 85% case that did not need them.

See [least-privilege tooling](../heuristics/least-privilege-tooling.md) · [tool_choice](tool-choice.md) · [2.3](../tasks/2-3.md)
