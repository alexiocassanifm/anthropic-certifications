---
title: Least-privilege tooling and scoped context
type: heuristic
---

# Least-privilege tooling and scoped context

> **Give each agent exactly the tools and context its role requires. Reliability degrades with breadth, not just with quality.**

The third cross-domain pattern. It shows up in tool distribution, subagent design, skill configuration, and context management — anywhere the question is "how much should this component have access to?"

## Why breadth hurts

Every additional tool is another candidate the model must discriminate among at selection time. Going from 4–5 tools to 18 does not add capability; it adds **decision complexity**, and tool-selection reliability falls. The same logic applies to context: a subagent handed the coordinator's entire conversation history has more to sift and more ways to be distracted than one handed the three findings it needs.

There is a second effect, subtler and more testable: **agents with tools outside their specialisation misuse them.** A synthesis agent given web search will search the web — badly, because searching is not what it was designed and prompted to do, and because doing so quietly bypasses the agent you built for that job. The failure is not "the tool did not work." It is "the architecture stopped being the architecture."

## The scoped-exception pattern

Least privilege does not mean zero cross-role access. The exam rewards a specific, more nuanced shape:

> Give the agent a **narrow, purpose-built tool** for the high-frequency simple case; route the complex cases through the coordinator as before.

Concretely: a synthesis agent that needs to check facts constantly gets `verify_fact` — one scoped tool for simple lookups. It does **not** get the full web-search toolset. Complex verification still delegates through the coordinator.

This beats both extremes. Full access over-provisions and breaks separation of concerns. Pure delegation adds round trips for the 85% case that did not need them. The scoped tool is the proportionate middle — which is [cheapest fix at the root cause](cheapest-fix-at-root-cause.md) applied to tool topology.

## Where the pattern appears

| Context | Least-privilege move | Task |
|---|---|---|
| Multi-agent tool distribution | Restrict each subagent's tool set to its role; add scoped cross-role tools only for proven high-frequency needs | [2.3](../tasks/2-3.md) |
| Generic vs constrained tools | Replace `fetch_url` with `load_document`, which validates that the URL is a document | [2.3](../tasks/2-3.md) |
| Tool granularity | Split a generic `analyze_document` into `extract_data_points`, `summarize_content`, `verify_claim_against_source` — each with a defined input/output contract | [2.1](../tasks/2-1.md) |
| Skills | `allowed-tools` in SKILL.md frontmatter, restricting tool access during skill execution | [3.2](../tasks/3-2.md) |
| Subagent context | Pass the specific findings the subagent needs, not the whole history — subagents do not inherit context automatically anyway | [1.3](../tasks/1-3.md) |
| Context isolation | `context: fork` for skills producing verbose output; the Explore subagent for verbose discovery | [3.2](../tasks/3-2.md), [3.4](../tasks/3-4.md) |
| Rules loading | Path-scoped `.claude/rules/` files that load only when editing matching files, instead of one monolithic always-loaded CLAUDE.md | [3.3](../tasks/3-3.md) |
| Tool output | Trim verbose results to the relevant fields before they accumulate in context — 40+ fields per order lookup when 5 matter | [5.1](../tasks/5-1.md) |

Notice how many domains that spans. The same idea — *narrow the surface to what the role needs* — is being tested as tool design in Domain 2, as configuration in Domain 3, and as context management in Domain 5.

## The one place breadth is correct

Coordinator agents need `Task` in `allowedTools` in order to spawn subagents at all, and they need enough visibility to route, aggregate, and recover. Routing **all** subagent communication through the coordinator is deliberately centralising — it buys observability, consistent error handling, and controlled information flow. See [1.2](../tasks/1-2.md).

Least privilege applies to the specialists, not to the hub. Do not "simplify" a coordinator by letting subagents talk to each other directly; that is a hub-and-spoke violation and a reliably wrong answer.

## Applying it to an item

When an option proposes giving a component *more* — more tools, more context, more history, more permissions — ask:

1. Does the component's **role** require it, or is this convenience?
2. Is there a **narrower** version of the same capability? (A scoped tool instead of a toolset. A summary instead of a transcript.)
3. Does it **break separation of concerns** — will this component now do a job another component exists to do?

If the answer to 3 is yes, it is a distractor, however reasonable it sounds.

## Related

- [Cheapest fix at the root cause](cheapest-fix-at-root-cause.md)
- [Deterministic vs probabilistic](deterministic-vs-probabilistic.md)
- [2.3](../tasks/2-3.md) tool distribution · [1.3](../tasks/1-3.md) subagent context · [3.2](../tasks/3-2.md) skills
