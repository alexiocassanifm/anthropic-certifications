---
title: MCP server configuration
domain: 2
tasks: ["2.4"]
verified: "2026-08-12"
sources:
  - "https://code.claude.com/docs/en/mcp"
---

# MCP server configuration

## Scoping

| Scope | File | For |
|---|---|---|
| **Project** | `.mcp.json` | Shared team tooling, committed to version control |
| **User** | `~/.claude.json` | Personal and experimental servers |

## Environment variable expansion

`${GITHUB_TOKEN}` in `.mcp.json` lets you commit the configuration without committing the credential. This is what makes project scope viable at all — without it, sharing the config means sharing the secret.

## All configured servers are active at once

Tools from **every** configured server are discovered at connection time and available simultaneously. Project and personal servers coexist; adding one does not displace another.

## Description quality still decides selection

An MCP tool with a thin description loses to a built-in like `Grep`, no matter how much more capable it is. Same root cause as [2.1](../tasks/2-1.md), different surface.

## Build versus adopt

Prefer **existing community MCP servers** for standard integrations (Jira, GitHub). Reserve custom servers for team-specific workflows.

## In production

Current docs define **three** scopes — local (default), project, user — with precedence local > project > user, and support `${VAR:-default}`. See the [drift log](../exam/drift-log.md#mcp-scopes--changed).

See [MCP resources](mcp-resources.md) · [2.4](../tasks/2-4.md)
