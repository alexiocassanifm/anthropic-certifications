---
title: Tool use for structured output
domain: 4
tasks: ["4.3"]
verified: "2026-08-12"
---

# Tool use for structured output

**Define the extraction schema as a tool's input schema; read the result from the `tool_use` response.** Per the guide, this is the most reliable approach for guaranteed schema-compliant output, and it eliminates JSON syntax errors.

## Schema design

- **Required vs optional** fields — see [nullable fields](nullable-fields.md)
- **Enum with `"other"` + a detail string** for extensible categories
- **`"unclear"`** as an enum value for genuinely ambiguous cases
- **Format normalisation rules in the prompt**, alongside the strict schema, to handle inconsistent source formatting

## Pair it with `tool_choice`

A schema does nothing if the model replies in prose instead of calling the tool. `"any"` guarantees a call; forced selection pins a specific one. See [tool_choice](tool-choice.md).

## The guarantee boundary

Schemas eliminate **syntax** errors, not **semantic** ones. That boundary is the most testable fact in the domain — see [semantic vs syntax errors](semantic-vs-syntax-errors.md).

## In production

Native structured outputs (`output_config.format`) and `strict: true` on tool definitions now exist alongside this technique. **The exam tests tool use + JSON schema.** See the [drift log](../exam/drift-log.md#structured-output--changed-).

See [4.3](../tasks/4-3.md)
