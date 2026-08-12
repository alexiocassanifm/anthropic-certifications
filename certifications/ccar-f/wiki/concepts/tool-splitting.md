---
title: Tool splitting and constrained tools
domain: 2
tasks: ["2.1", "2.3"]
verified: "2026-08-12"
---

# Tool splitting and constrained tools

## Splitting

Break a generic tool into purpose-specific ones with defined input/output contracts. The guide's example: a generic `analyze_document` becomes

- `extract_data_points`
- `summarize_content`
- `verify_claim_against_source`

Each has a clear purpose, which makes each description sharp, which makes selection reliable.

## Renaming to eliminate overlap

`analyze_content` → `extract_web_results`, with a web-specific description. The rename and the description change go together; renaming alone does not fix selection.

## Constrained alternatives

Replace a generic tool with one that validates its own domain: `fetch_url` becomes `load_document`, which checks that the URL actually points at a document. The constraint moves a class of errors out of the model's judgment and into the tool.

See [tool descriptions](tool-descriptions.md) · [tool distribution](tool-distribution.md) · [2.1](../tasks/2-1.md)
