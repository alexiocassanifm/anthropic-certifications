# cert-study-kit

A one-skill plugin that installs the [anthropic-certifications](https://github.com/alexiocassanifm/anthropic-certifications)
study kit — a linked wiki, original practice-question banks, and Claude Code skills
that teach, quiz, drill, and sit you a full timed mock exam.

```
/plugin marketplace add alexiocassanifm/anthropic-certifications
/plugin install cert-study-kit@anthropic-certifications
/cert-study-kit:setup
```

`setup` asks where to put the kit, clones it there, checks that the Python scripts
can run, and hands you back with a `cd` and a `claude`.

## What this plugin is for

Discovery, not speed. It is how you find the kit and install it without hunting for
a clone URL; it is not a shortcut. You still end up opening Claude Code inside the
clone, and that is deliberate.

## Why it only bootstraps

The kit is a repository you work *in*, not a tool you install. `/refresh-kb`
rewrites wiki notes when the official documentation moves. `/author-question`
appends to the question bank. Every study session writes your progress. Those edits
are versioned content and personal state: they are worth something only in a
working tree you can commit, back up, and open a pull request from.

Installing a plugin copies it into `~/.claude/plugins/cache/`. Anything written
there is discarded by the next `/plugin update` and can never reach upstream. A
read-only study kit would make a fine plugin payload. This one is not read-only by
design — so the plugin ships the front door and the repository holds the kit.

## Unofficial

Built by a Claude Ambassador — a community role, not an Anthropic one. Not written,
reviewed, endorsed, or sponsored by Anthropic, and it contains no exam content. See
[DISCLAIMER.md](https://github.com/alexiocassanifm/anthropic-certifications/blob/main/DISCLAIMER.md).

## Licence

MIT. The wiki and question content in the cloned repository are CC BY-SA 4.0.
