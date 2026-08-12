---
title: Out of Scope
---

# Out of Scope

The exam guide publishes an explicit list of related topics that **will not appear** on the exam. This note exists so you can stop studying them — and so the `/study` and `/quiz` skills can decline to drill them.

Knowing the boundary is worth real time. Several of these are things a Claude architect legitimately cares about in production, which is exactly why candidates waste hours on them.

## Not tested

**Model internals and training**
- Fine-tuning Claude models or training custom models
- Claude's internal architecture, training process, or model weights
- Constitutional AI, RLHF, or safety training methodologies

**API mechanics that are not about building agents**
- Claude API authentication, billing, or account management
- Streaming API implementation or server-sent events
- Rate limiting, quotas, or API pricing calculations
- OAuth, API key rotation, or authentication protocol details
- Token counting algorithms or tokenization specifics
- Prompt caching implementation details — *beyond knowing that it exists*

**Capabilities outside the tested surface**
- Computer use (browser automation, desktop interaction)
- Vision / image analysis capabilities
- Embedding models or vector database implementation details

**Infrastructure and platform**
- Deploying or hosting MCP servers (infrastructure, networking, container orchestration)
- Specific cloud provider configurations (AWS, GCP, Azure)

**Adjacent engineering**
- Detailed implementation of specific programming languages or frameworks, beyond what is needed for tool and schema configuration
- Performance benchmarking or model comparison metrics

## The distinctions that catch people

Several out-of-scope items sit next to something that **is** tested. The line matters:

| Out of scope | In scope |
|---|---|
| Prompt caching implementation details | *That prompt caching exists* |
| Deploying and hosting MCP servers | Configuring MCP servers in `.mcp.json` / `~/.claude.json`, scoping, env var expansion — see [2.4](../tasks/2-4.md) |
| Rate limits, quotas, pricing calculations | The Message Batches API trade-off: 50% cost saving, up to 24h window, no latency SLA — see [4.5](../tasks/4-5.md) |
| Token counting algorithms | Context window *management*: trimming tool output, lost-in-the-middle, structured fact extraction — see [5.1](../tasks/5-1.md) |
| Embedding models and vector DB internals | Nothing. Retrieval internals are simply not on this exam. |
| Framework-specific implementation detail | Pydantic as a *schema validation* mechanism in a validation-retry loop — see [4.4](../tasks/4-4.md) |
| Streaming and SSE | `stop_reason` values and agentic loop control flow — see [1.1](../tasks/1-1.md) |
| Model comparison metrics | Choosing an *architecture*: multi-pass review, independent review instances — see [4.6](../tasks/4-6.md) |

The pattern: **configuration and architectural judgment are tested; implementation, infrastructure, and cost mechanics are not.** When you are unsure whether something is in scope, ask "is this a decision an architect makes about how to assemble the system, or is it an operational detail of running it?"

## How the skills use this

`/study` and `/quiz` read this file. If you ask them to drill an out-of-scope topic, they will say so and redirect you to the nearest in-scope task statement rather than generating material you will never be tested on.

If you *want* to study an out-of-scope topic anyway — perfectly reasonable, you have a job to do besides passing an exam — say so explicitly and they will proceed, with a note that it is not exam material.

## See also

- [blueprint.md](blueprint.md) — what *is* tested
- [`../concepts/`](../concepts/) — the in-scope technology surface, one note per concept
