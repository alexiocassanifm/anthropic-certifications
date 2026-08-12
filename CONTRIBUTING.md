# Contributing

Thanks for helping. These study kits get better mainly through **more and better practice items** and through **corrections** when the underlying tooling changes.

Everything below applies to any certification in `certifications/`. Paths are written relative to a certification directory — substitute the one you are working on, e.g. `certifications/ccar-f/`.

## The one hard rule

**Never contribute real exam content.**

If you have sat CCAR-F, you are under an NDA. Do not contribute questions you saw, paraphrases of them, or observations about what your form emphasised. Do not reproduce the sample questions printed in the official exam guide either — they are Anthropic's.

Write from the **published objectives** (the task statements) and from your own production experience. Every item in `questions/bank/` carries `source: original` and must genuinely be so.

Pull requests that appear to contain exam content will be closed without merge. See [DISCLAIMER.md](DISCLAIMER.md).

---

## Ways to contribute

### 1. Add practice items

The highest-value contribution. Items live in `<cert>/questions/bank/d<N>-*.yaml`, one file per domain.

Read these two files first — they are short and they are the standard:

- [`schema.md`](certifications/ccar-f/questions/schema.md) — the required shape of an item
- [`question-style-guide.md`](certifications/ccar-f/questions/question-style-guide.md) — how a good item is built, and the seven distractor families

The fastest path is to let the kit do it with you:

```
/author-question 3.4
```

It interviews you, drafts an item against the schema and style guide, runs the validator, and appends it to the right bank file.

Before opening a PR:

```bash
python scripts/validate_questions.py --cert ccar-f
```

It must exit 0.

**What makes an item good here:**

- A realistic production symptom, not a definition lookup. "Production logs show X" beats "What is X?"
- One clearly best answer, with the others *defensible but worse* — over-engineered, aimed at a different problem, or reliant on an unreliable proxy.
- Every option carries a `why`. The explanation is the study material; the item is just the delivery mechanism.
- Every wrong option is tagged with a `distractor_family`.
- Tie it to exactly one `task_statement`. If it spans two, it is probably two items.
- **Vary the answer position.** Do not put the correct option first out of habit —
  the validator fails the build if any single letter is correct on more than 40% of
  single-answer items.
- Reach for a specific `distractor_family` before falling back to
  `solves-different-problem`, which is already about half the bank.

### 2. Fix or extend the wiki

Each certification's `wiki/` is plain Markdown with **relative links only** — no `[[wikilinks]]`, so pages render on GitHub and resolve in Obsidian alike.

- Task statement notes (`wiki/tasks/`) follow a fixed section order. Keep it.
- New concepts go in `wiki/concepts/` as one focused note per concept, and get linked from the task statements that need them.
- Keep the reproduced task statement **titles** verbatim. Write everything else in your own words.

### 3. Report drift

Claude Code, the Agent SDK, and MCP all move. If a concept note describes a flag, path, or behaviour that no longer matches reality, open an issue with a link to current documentation — or a PR. Note that **the exam is written against a specific guide version**, so if current tooling has diverged from what the guide describes, say so in the note rather than silently rewriting it.

### 4. Add a new certification

Open an issue first. A new certification is a directory under `certifications/` with the same shape — `wiki/`, `questions/bank/`, `progress/` — plus a `README.md` and a blueprint note recording the guide version it was written against. The shared skills and scripts pick it up automatically once the directory exists; see [`certifications/README.md`](certifications/README.md).

### 5. Update for a new guide version

If Anthropic publishes a new exam guide version with a changed blueprint or new task statements, open an issue first so we can agree the migration before anyone rewrites 30 notes. The version in force is recorded in each certification's `wiki/exam/blueprint.md` — for CCAR-F, [here](certifications/ccar-f/wiki/exam/blueprint.md).

---

## Style

- **English only**, for everything: prose, comments, commit messages, item text.
- Prefer concrete over abstract. The exam tests judgment in production situations; so should the material.
- Explain the *why*, including why the tempting-but-wrong approach is wrong. That is the part that transfers.
- No marketing tone. No emoji in wiki content.

## Development

```bash
pip install -r requirements.txt
python scripts/validate_questions.py --cert ccar-f     # schema + coverage checks
python scripts/build_exam.py --cert ccar-f --seed 1    # deterministic form, for inspection
```

`<cert>/progress/state.json` is personal and gitignored. Never commit it.

## Pull requests

- One topic per PR. A batch of items for one domain is fine; items plus a wiki refactor is not.
- Say in the description which task statements you touched.
- Confirm in the description that your contribution contains no exam content.
