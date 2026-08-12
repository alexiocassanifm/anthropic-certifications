---
title: Structured handoff
domain: 1
tasks: ["1.3", "1.4"]
verified: "2026-08-12"
---

# Structured handoff

Passing information across a boundary — agent to agent, or agent to human — in a form that survives the crossing.

## Agent to agent

Use **structured formats that separate content from metadata**. Source URLs, document names, and page numbers travel *alongside* the content, not embedded in prose. This is what makes attribution survive summarisation later ([5.6](../tasks/5-6.md)).

Pass **complete findings**, not references to them — subagents share no memory ([subagent context isolation](subagent-context-isolation.md)).

## Agent to human (escalation)

The human receiving an escalation **does not have your conversation transcript**. A structured handoff summary carries:

- Customer ID
- Root cause analysis
- Refund amount (or the relevant figures)
- Recommended action

"Customer needs help with a refund" wastes the human's first five minutes and is a recognisable wrong answer.

See [escalation triggers](escalation-triggers.md) · [provenance](provenance.md) · [1.4](../tasks/1-4.md)
