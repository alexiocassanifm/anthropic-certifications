---
name: author-question
description: Interview the user and draft a new CCAR-F practice item conforming to the schema and style guide, validate it, and append it to the question bank. Use to contribute or extend coverage.
argument-hint: [task-statement]
---

# Author a question

Turn a real production situation into a bank item that trains the right reflex.

## Ground rules first

Before anything else, state plainly: **do not contribute anything seen on the real
exam.** Candidates are under NDA, and the guide's own sample questions are
Anthropic's. Items must be original, written from the published objectives and
from production experience. See `DISCLAIMER.md` and `CONTRIBUTING.md`.

If the user's description sounds like recall of a real item, stop and say so.

## Read the standard

Read `questions/schema.md` and `questions/question-style-guide.md` in full. They
are short and they are the contract.

## Interview

Establish, by asking rather than assuming:

1. **The task statement** it tests. If not given, propose one from `wiki/tasks/`
   and confirm.
2. **The production symptom.** Push for something measured and falsifiable — "12%
   of cases", "40% latency increase" — not "sometimes it fails". The number is what
   gives the reader something to reason against.
3. **The consequence.** Whether money moves, whether a human is waiting. This
   decides whether a prompt-level fix is acceptable.
4. **The correct answer**, and why it is best rather than merely good.
5. **Three things a competent engineer might do instead.** Ask for real
   alternatives the user has considered or seen. If they cannot produce three,
   suggest candidates from the distractor families and check each is genuinely
   plausible.

## Draft

Write the item to the schema. Then check it against the style guide:

- Is the stem a **situation**, not a definition lookup?
- Would a competent engineer plausibly ship each distractor? If one is a straw
  man, rewrite it.
- Can every wrong option be classified into one of the seven families? If not, it
  is probably a straw man.
- Does every option have a `why` that teaches something? "This is incorrect" is
  not acceptable.
- If `select_count > 1`, does the stem say so — "Select TWO."?
- Does the correct answer's `why` name the *principle*, not just the mechanic?

Show the draft and ask for corrections before writing anything.

## Commit

Assign an id: `d<domain>-<task>-<NNN>`, taking the next free sequence number for
that task statement. Append to the matching `questions/bank/d<N>-*.yaml`.

Then run:

```bash
python scripts/validate_questions.py
```

If it fails, fix and re-run. Do not leave the bank invalid.

Finally, report the new per-task-statement count and whether the domain totals
still line up against the blueprint.
