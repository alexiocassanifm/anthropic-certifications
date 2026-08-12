#!/usr/bin/env python3
"""SessionStart hook: nudge a re-verification when a wiki's checks have gone stale.

Each certification's `wiki/exam/drift-log.md` carries a `last_verified` date in
its frontmatter. This script compares that date to today and, when it is more
than a day old, prints JSON on stdout asking Claude to run `/refresh-kb`.

Claude Code adds a SessionStart hook's stdout to the session as context, so the
refresh happens on the first interaction of the day without the user asking.

Deliberately conservative:

- **Reads only.** No network calls, no writes to the wiki. The actual
  verification is `/refresh-kb`, which reports before it edits anything.
- **Once per day.** A stamp file stops it from re-prompting in every session.
- **Silent when fresh.** No output, so it costs nothing on a normal day.
- **Never fails the session.** Any error exits 0 with no output; a broken
  staleness check must not get between you and your work.

Run it by hand to see what it would say:

    python scripts/check_verification_age.py --force
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CERTS = ROOT / "certifications"
STAMP = ROOT / ".claude" / ".refresh-prompted"

STALE_AFTER_DAYS = 1        # the user's ask: at least once a day
FULL_SWEEP_AFTER_DAYS = 7   # below this, the fast-moving domains are enough

DATE_RE = re.compile(r'^last_verified:\s*["\']?(\d{4}-\d{2}-\d{2})["\']?\s*$', re.M)


def last_verified(drift_log: Path) -> date | None:
    """Read `last_verified` from the drift log's frontmatter."""
    try:
        head = drift_log.read_text()[:800]
    except OSError:
        return None
    m = DATE_RE.search(head)
    if not m:
        return None
    try:
        return datetime.strptime(m.group(1), "%Y-%m-%d").date()
    except ValueError:
        return None


def already_prompted_today(today: date) -> bool:
    try:
        return STAMP.read_text().strip() == today.isoformat()
    except OSError:
        return False


def stamp(today: date) -> None:
    try:
        STAMP.parent.mkdir(parents=True, exist_ok=True)
        STAMP.write_text(today.isoformat() + "\n")
    except OSError:
        pass  # a read-only checkout should still start cleanly


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--force", action="store_true",
                    help="ignore the once-a-day stamp and report regardless")
    args = ap.parse_args()

    today = date.today()

    if not args.force and already_prompted_today(today):
        return 0

    stale: list[tuple[str, int]] = []
    unknown: list[str] = []

    if not CERTS.is_dir():
        return 0

    for cert in sorted(p for p in CERTS.iterdir() if p.is_dir()):
        log = cert / "wiki" / "exam" / "drift-log.md"
        if not log.exists():
            continue
        seen = last_verified(log)
        if seen is None:
            unknown.append(cert.name)
            continue
        age = (today - seen).days
        if age >= STALE_AFTER_DAYS:
            stale.append((cert.name, age))

    if not stale and not unknown:
        return 0

    lines = [
        "Scheduled check: this repository's wiki claims are verified against "
        "official documentation, and that verification has gone stale.",
        "",
    ]
    for name, age in stale:
        scope = "--all" if age >= FULL_SWEEP_AFTER_DAYS else "--domain 3"
        lines.append(
            f"- **{name}** — last verified {age} day{'s' if age != 1 else ''} ago. "
            f"Suggested scope: `/refresh-kb {scope}`"
            + ("  (a week or more, so sweep everything)" if age >= FULL_SWEEP_AFTER_DAYS
               else "  (Domain 3 is where the tooling actually moves)")
        )
    for name in unknown:
        lines.append(f"- **{name}** — no `last_verified` date recorded in its drift log.")

    lines += [
        "",
        "Offer to run `/refresh-kb` now, before the user relies on this material. "
        "Keep it to one short sentence — do not restate this notice. If they "
        "decline, or they are clearly mid-task, drop it and carry on; do not ask "
        "again this session.",
        "",
        "`/refresh-kb` reports its findings before changing any file, so running it "
        "is safe. It must not write without the user's approval.",
    ]

    json.dump({"additionalContext": "\n".join(lines)}, sys.stdout)
    if not args.force:
        stamp(today)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        # A staleness reminder is never worth failing a session over.
        sys.exit(0)
