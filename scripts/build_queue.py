"""Build published/linkedin.md from generated/drafts using the weekly schedule.

Usage: python3 scripts/build_queue.py [START_DATE=YYYY-MM-DD]
One post per pillar per week. When a pillar has no draft left, its slot
is marked "write next" so the gap is visible.
"""
import datetime, glob, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DRAFTS = os.path.join(ROOT, "generated", "drafts")
# weekday (Mon=0) -> pillar folder
SCHEDULE = {0: "dsa", 1: "ai-engineering", 2: "software-engineering",
            3: "system-architecture", 6: "dev-growth"}

start = datetime.date.fromisoformat(sys.argv[1]) if len(sys.argv) > 1 else datetime.date(2026, 9, 28)
start -= datetime.timedelta(days=start.weekday())  # snap to Monday

def num(f):
    return int(re.search(r"-(\d+)-", os.path.basename(f)).group(1))

queue = {p: sorted(glob.glob(os.path.join(DRAFTS, p, "*.md")), key=num) for p in set(SCHEDULE.values())}

out = ["# LinkedIn Posting Queue", "",
       "Five posts a week, one per pillar. Tick the box when posted.",
       "Before posting: fill or delete any [PERSONAL: ...] line, then make the image from HEADLINE + LAYOUT.",
       "Schedule: Mon DSA · Tue AI Engineering · Wed Software Engineering · Thu System Architecture · Sun Dev Growth",
       "", "Already published: DSA #02 · SOFTWARE ENGINEERING #01 · AI ENGINEERING #01 · BUILDING #01"]
day, week = start, 0
while any(queue.values()):
    if day.weekday() == 0:
        week += 1
        out += ["", f"## Week {week} — from {day:%a %d %b}", "",
                "| ✓ | Date | Series | Title | File |", "| --- | --- | --- | --- | --- |"]
    if day.weekday() not in SCHEDULE:
        day += datetime.timedelta(days=1)
        continue
    pillar = SCHEDULE[day.weekday()]
    if not queue[pillar]:
        out.append(f"| ☐ | {day:%a %d %b} | {pillar} | — write next post — | |")
        day += datetime.timedelta(days=1)
        continue
    f = queue[pillar].pop(0)
    text = open(f).read()
    series = re.search(r"SERIES:\s*(.+)", text).group(1).strip()
    title = re.search(r"TITLE:\s*(.+)", text).group(1).strip()
    mark = " ✎" if "[PERSONAL" in text else ""
    rel = os.path.relpath(f, os.path.join(ROOT, "published"))
    out.append(f"| ☐ | {day:%a %d %b} | {series} | {title}{mark} | [{os.path.basename(f)}]({rel}) |")
    day += datetime.timedelta(days=1)

out += ["", "✎ = has a [PERSONAL: ...] line to fill in or delete.", "",
        "## Published log", "", "| Date | Series | Link | Notes |", "| --- | --- | --- | --- |"]
open(os.path.join(ROOT, "published", "linkedin.md"), "w").write("\n".join(out) + "\n")
print(f"{week} weeks written to published/linkedin.md")
