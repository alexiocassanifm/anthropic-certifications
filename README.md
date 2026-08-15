# Anthropic Certifications

**Study kits for the Anthropic certification program that re-verify their own claims against current documentation — and quiz you on what you got wrong, not what you already know.**

![Practice items](https://img.shields.io/badge/practice_items-90-2F5D7C)
![Wiki notes](https://img.shields.io/badge/wiki_notes-98-2F5D7C)
![Certifications](https://img.shields.io/badge/certifications-1_of_many-B07A16)
![Licence](https://img.shields.io/badge/licence-MIT_%2B_CC_BY--SA_4.0-2E7D62)

Certification material goes stale faster than anyone updates it. A guide written in July describes flags that were renamed in August, and you memorise the wrong thing. So this kit keeps a **drift log** — a running record of where the official documentation has moved since the exam guide was written — and a `/refresh-kb` command that re-checks it. When the tooling changes, the kit says so instead of quietly teaching you a dead flag.

The rest is what you would hope for: a linked wiki covering every task statement, a bank of original practice items where **every wrong answer explains why it is wrong**, and a set of Claude Code skills that teach, quiz, drill, and sit you a full timed mock exam.

---

## See it before you install anything

A real 60-item mock exam produces this:

**→ [examples/mock-exam-report.md](examples/mock-exam-report.md)** — percent correct by domain, which task statements you missed with the command to fix each, the reasoning habits you fell for ranked against their base rate, and a walkthrough of every item you got wrong.

The same report also publishes as a styled HTML page — [`examples/mock-exam-report.html`](examples/mock-exam-report.html) (open it locally; GitHub shows HTML as source).

The sample has a domain sitting at 55% under a 77% average. That is left in deliberately. A strong average hiding one collapsed domain is the exact failure the report exists to catch, and a sample where everything went well would demonstrate nothing.

---

## Unofficial — and specific about it

Built by a **Claude Ambassador**, a member of Anthropic's official community program. That is a *community* role, not an Anthropic one. Concretely:

- **Not** written, reviewed, endorsed, or sponsored by Anthropic
- Contains **no exam content** — no live questions, and not even the sample questions printed in the official guide
- Every practice item is original, written from the published objectives

If you have sat the exam, you are under an NDA. Do not contribute anything you saw on it. See [DISCLAIMER.md](DISCLAIMER.md) — it is short and it is the honest version.

---

## Certifications

| Slug | Certification | Exam code | Status |
|---|---|---|---|
| [`ccar-f`](certifications/ccar-f/) | Claude Certified Architect – Foundations | `CCAR-F` | **Complete** — 30 task statements, 90 practice items |

**One today. The goal is all of them.** The repo is built as a monorepo precisely so that the second certification is *content*, not plumbing: the skills, the scripts, the schema, and the validator are already shared and certification-aware. Adding one means writing a wiki and a question bank, not rebuilding the machinery.

If you are studying a certification that is not here yet, that is the single most valuable thing you could contribute — and you would be building it with the same tools you study with. See [Adding a certification](certifications/README.md).

---

## Quick start

```bash
git clone https://github.com/alexiocassanifm/anthropic-certifications.git
cd anthropic-certifications
pip install -r requirements.txt      # PyYAML, for the scripts
claude                               # open Claude Code at the repo root
```

Then:

```
/study 1.4          # learn one task statement, then get checked on it
/quiz --domain 2    # short targeted quiz, feedback per item
/mock-exam          # full 60-item timed simulation + diagnostic report
/progress           # readiness dashboard
/drill              # spaced repetition on what you are forgetting
/refresh-kb         # re-verify the wiki against current official docs
/author-question    # draft a new practice item, schema-checked
```

Run them from the **repo root**. The skills resolve which certification you mean — the only one present, or the one you name.

`/mock-exam` ends by offering to publish its diagnostic as an HTML or Markdown artifact, so a sixty-item report does not evaporate with your terminal scrollback.

---

## What makes it different

**The explanations are the study material.** Every option in the bank carries a `why`. Getting an item right without knowing why teaches you nothing, so the report tells you why the distractor was tempting as well as why the answer was right.

**Wrong answers are taxonomised.** Seven named [distractor families](certifications/ccar-f/questions/question-style-guide.md) — `prompt-instead-of-enforcement`, `blames-wrong-component`, `unreliable-proxy`, and four more. Reports rank the ones you fall for **by rate against how often each appeared**, not by raw count, because the most common family collects the most misses on any form and tells you nothing. The rate is what names a real reasoning habit.

**It knows when it is out of date.** A `SessionStart` hook checks how long ago each wiki was verified and offers `/refresh-kb`. No network calls, prompts at most once a day, prints nothing when fresh, and never fails a session.

**It admits what it cannot know.** The exam passes at a scaled 720 out of 1,000, and the raw percentage that maps to 720 varies by form. So this kit **never emits a scaled score** — a fabricated "you scored 743" invites you to stop studying at exactly the wrong moment. You get percent-correct by domain, which is what the real score report gives you anyway.

---

## Contributing

Practice items, corrections, and **new certifications** are all welcome — see [CONTRIBUTING.md](CONTRIBUTING.md).

The fastest way in is to let the kit write with you:

```
/author-question 3.4
```

It interviews you, drafts an item against the schema and style guide, validates it, and appends it to the right bank file. You supply the production experience; it handles the shape.

The one hard rule: **never contribute real exam content.** Write from the published objectives and from what you have actually built.

---

## Layout

```
├── certifications/
│   ├── README.md            conventions + how to add one
│   └── ccar-f/
│       ├── wiki/            98 linked notes — tasks, concepts, scenarios, heuristics
│       ├── questions/       schema, style guide, item bank
│       └── progress/        your local state (gitignored)
├── examples/                sample mock exam report
├── .claude/skills/          seven shared, certification-aware skills
├── scripts/                 validator + mock exam builder
├── DISCLAIMER.md            applies to every kit here
├── CONTRIBUTING.md
└── LICENSE                  MIT (code) + CC BY-SA 4.0 (content)
```

**Shared at the root:** skills, scripts, licence, disclaimer, contributing guide.
**Per certification:** wiki, questions, progress.

### Why this is not a plugin

A plugin would ship the wiki, the question bank, and your `progress/state.json` into `~/.claude/plugins/cache/`, where an update overwrites them. Your study history is not tool configuration; it belongs in a repo you clone and own. Clone it, work in it, commit your notes if you want them backed up.

Hooks require workspace trust, so the first `claude` in a fresh clone asks you to approve the folder. Declining is fine — everything still works, you just run `/refresh-kb` yourself.

---

## Scripts

```bash
python scripts/validate_questions.py --cert ccar-f     # schema + style checks
python scripts/build_exam.py --cert ccar-f --seed 1    # assemble a form
python scripts/check_verification_age.py --force       # see what the hook would say
```

With one certification present it is the default; with several, `--cert` is required — guessing would silently validate the wrong bank. `build_exam.py` always reports the seed it used, with or without `--seed`, so any form can be rebuilt afterwards to re-grade an exam or check a report against the form it came from.

## Reading the wiki without Claude

Everything under `certifications/<slug>/wiki/` is plain Markdown with relative links, so it renders on GitHub and navigates in Obsidian. To use an existing vault:

```bash
ln -s "$(pwd)/certifications/ccar-f/wiki" /path/to/vault/ccar-f
```

## Licence

Code is MIT. Wiki and question content are CC BY-SA 4.0. See [LICENSE](LICENSE).

---

<sub>If this saved you time, a ⭐ helps other people studying the same exam find it.</sub>
