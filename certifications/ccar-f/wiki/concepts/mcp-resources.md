---
title: MCP resources
domain: 2
tasks: ["2.4"]
verified: "2026-08-12"
---

# MCP resources

**Tools are for actions. Resources are for knowing what exists.**

An MCP **resource** exposes a content catalogue — issue summaries, documentation hierarchies, database schemas — giving the agent visibility into available data **without spending exploratory tool calls to discover it**.

## The problem it solves

Without a catalogue, an agent that needs to know what data is available has to go looking: call a tool, see what comes back, call another. Each call costs tokens and latency, and the agent may never find something it did not think to ask for.

With a resource, the catalogue is simply visible.

## The exam shape

*"The agent burns tool calls discovering what data even exists"* → expose the catalogue as an MCP resource.

Easy to miss because "resource" and "tool" are both things an MCP server provides, and the guide's phrasing is brief. The distinction — **actions versus catalogues** — is the whole of it.

See [MCP server configuration](mcp-configuration.md) · [2.4](../tasks/2-4.md)
