---
name: setup
description: Clone the anthropic-certifications study kit into a repository you own, and check that its scripts can run. Use once, to get set up.
disable-model-invocation: true
---

# Set up the study kit

This plugin does not contain the study kit. It clones it.

The kit is a repository you work *in*: `/refresh-kb` rewrites wiki notes when the
official documentation moves, `/author-question` appends to the question bank, and
every session writes your progress. Those edits are only worth something in a
working tree you can commit and open a pull request from. A plugin is copied into
`~/.claude/plugins/cache/`, where the next `/plugin update` discards whatever you
wrote. So the kit lives in a clone, and this skill puts one where you want it.

## 1. Check you are not already there

If the current directory contains both `certifications/` and `.claude/skills/study/`,
the user is already inside a clone. Say so, tell them to run `/study 1.1` or
`/progress`, and stop. Do not clone again.

## 2. Check git

Run `git --version`. If git is missing, say so and stop — point them at
<https://git-scm.com/downloads>. Everything below needs it.

## 3. Say what is about to be cloned

Two sentences, before asking for a path — nobody can choose where to put something
they have not been told the shape of:

> An unofficial, open-source study repository for the Anthropic certification
> programme: a linked wiki covering every task statement, a bank of original
> practice questions where each wrong answer explains why it is wrong, and seven
> skills that teach, quiz, drill, and sit you a full timed mock exam. Under 2 MB and
> about 135 files, no build step — a git repository you study in and can contribute
> back from.

Add that it is not written, reviewed, or endorsed by Anthropic and contains no exam
content. That belongs *before* the download, not after it.

Do not recite which certifications are covered — that list grows, and the table in
the repository's `README.md` is the copy that stays true. Point at it in step 7.

## 4. Agree on a location

Offer `./anthropic-certifications` — a folder in the directory this session started
in, exactly where `git clone <url>` with no path argument would put it — and say
they can accept it or name another path. This will be a git repository they own and
study in, so somewhere they will find it again.

The kit always lands in a folder of its own, never in the current directory itself:
`git clone` refuses a destination that already has contents, and the kit brings a
`.claude/` of its own that would collide with whatever is already there.

Before cloning, check the target path and the current directory. Each check below
is a warning with a suggested alternative, not a refusal — say what the risk is,
offer the alternative, and clone where they choose:

- **Target exists and is not empty** → the one hard stop. Say so and ask for a
  different path. Never clone into or over an existing directory's contents.
- **Current directory is inside a git work tree** (`git rev-parse
  --is-inside-work-tree` succeeds) → the clone would nest a repository inside
  theirs, which is easy to commit by accident as a gitlink. Offer
  `~/anthropic-certifications` instead.
- **Target resolves under a sync folder** — `~/Library/Mobile Documents` (iCloud
  Drive), `~/Dropbox`, `~/Google Drive`, `~/OneDrive` → a `.git` directory under
  continuous file sync can be corrupted mid-operation, and paths there often carry
  spaces and non-ASCII characters that scripts handle badly. Offer a path outside
  it, such as `~/Projects/anthropic-certifications`.
- Otherwise → fine, proceed.

## 5. Clone

```bash
git clone https://github.com/alexiocassanifm/anthropic-certifications.git <path>
```

If the clone fails, report the actual error rather than guessing — no network, no
proxy, and a full disk all look different.

## 6. Check the Python scripts can run

Two skills shell out to Python: `/mock-exam` builds a form with
`scripts/build_exam.py`, and `/author-question` validates with
`scripts/validate_questions.py`. Both need PyYAML. Nothing else does — the wiki,
`/study`, `/quiz`, `/drill`, and `/progress` need no dependencies at all.

Check it:

```bash
python3 -c "import yaml; print(yaml.__version__)"
```

If that fails, offer to install it, and say which command you are about to run:

```bash
python3 -m pip install -r <path>/requirements.txt
```

Mention that a virtual environment is the tidier option if they prefer one, and
that declining is fine — five of the seven skills work without it, and they can
install it later.

## 7. Hand over

Print the next step plainly. They must open Claude Code *in the clone*, because the
seven study skills are project-scoped under the repo's `.claude/` and load only
when the repo is the working directory:

```bash
cd <path>
claude
```

Then, in that session:

```
/study 1.1          # learn one task statement, then get checked on it
/mock-exam          # 60-item timed simulation and a diagnostic report
/progress           # readiness dashboard
```

Tell them two more things:

- The first launch in the clone asks them to trust the folder, because the repo
  ships a `SessionStart` hook that checks how long ago the wiki was verified.
  Declining is fine — everything still works, they just run `/refresh-kb`
  themselves.
- The skills are `/study`, not `/cert-study-kit:study`. This plugin's only skill is
  the one they just ran; the study skills come from the clone.

Finally, point at the repository's `README.md` — its table lists every certification
covered — and `CONTRIBUTING.md` for how to add practice items. The unofficial
standing was already said in step 3; here just name `DISCLAIMER.md` in the clone as
the full version, without repeating it.
