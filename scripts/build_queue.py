"""Build published/queue.md — the upcoming posting plan — from post headers.

Usage: python3 scripts/build_queue.py [START_DATE=YYYY-MM-DD] [--per-week N]

- Reads every post in generated/drafts/<pillar>/ and its STATUS: line.
- Posts with STATUS: published are skipped; draft, approved and scheduled are queued.
- Starts on the Monday of the given date, default the next Monday from today
  (today, if today is Monday).
- Posts go out POSTS_PER_WEEK times a week (default 5, Mon-Fri; change it
  here or pass --per-week 3..7). Each posting day takes the next pillar in
  ROTATION, so all seven pillars keep moving at a pace one person can hold.
  When a pillar has nothing left, its slot is marked "write next".

Writes published/queue.md, then rebuilds posts/ (scripts/build_posts.py). published/linkedin.md is the hand-kept
published log and is never touched by this script.
"""
import datetime, glob, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DRAFTS = os.path.join(ROOT, "generated", "drafts")
QUEUE = os.path.join(ROOT, "published", "queue.md")
# seven pillars are the inventory; POSTS_PER_WEEK is what actually goes out
POSTS_PER_WEEK = 5
POST_DAYS = {3: (0, 2, 4), 4: (0, 1, 2, 3), 5: (0, 1, 2, 3, 4),   # Mon=0
             6: (0, 1, 2, 3, 4, 5), 7: (0, 1, 2, 3, 4, 5, 6)}
# technical and story pillars alternate so the feed never runs one kind
ROTATION = ["dsa", "ai-engineering", "software-engineering", "building",
            "system-architecture", "business", "dev-growth"]
NAMES = {"dsa": "DSA", "ai-engineering": "AI Engineering", "software-engineering": "Software Engineering",
         "building": "Building", "system-architecture": "System Architecture",
         "business": "For Business", "dev-growth": "Dev Growth"}
# a pillar with subsections gives its rotation slot to each subsection in turn
TRACKS = {"software-engineering": ["software-engineering/backend", "software-engineering/web",
                                   "software-engineering/mobile"]}
QUEUED = {"draft", "approved", "scheduled"}
# pillar folder -> series label, so empty slots read like filled ones
LABELS = {"dsa": "DSA SERIES", "software-engineering/backend": "SOFTWARE ENGINEERING · BACKEND",
          "software-engineering/web": "SOFTWARE ENGINEERING · WEB",
          "software-engineering/mobile": "SOFTWARE ENGINEERING · MOBILE",
          "system-architecture": "SYSTEM ARCHITECTURE", "ai-engineering": "AI ENGINEERING",
          "dev-growth": "DEV GROWTH", "building": "BUILDING",
          "business": "FOR BUSINESS / SOLUTIONS"}
SE_ROAD = "02-software-engineering.md"
ROADMAPS = {"dsa": "01-dsa-problem-solving.md",
            # (file, section): the subsection's roadmap is under "## <section>"
            "software-engineering/backend": (SE_ROAD, "Backend roadmap"),
            "software-engineering/web": (SE_ROAD, "Web roadmap"),
            "software-engineering/mobile": (SE_ROAD, "Mobile roadmap"),
            "system-architecture": "03-system-design.md", "ai-engineering": "04-ai-engineering.md",
            "dev-growth": "05-dev-growth.md",
            # no roadmap: BUILDING from sources/project-log.md, FOR BUSINESS from
            # sources/apps.md (PRODUCT) or a system idea (BLUEPRINT)
            "building": None, "business": None}


def roadmap(pillar):
    """{n: 'Title · MODE'} from the pillar's roadmap lines ({} for story pillars)."""
    if ROADMAPS[pillar] is None:
        return {}
    name, section = ROADMAPS[pillar] if isinstance(ROADMAPS[pillar], tuple) else (ROADMAPS[pillar], None)
    text = open(os.path.join(ROOT, "pillars", name)).read()
    if section:
        text = re.split(r"^## ", text.split(f"\n## {section}\n", 1)[1], maxsplit=1, flags=re.M)[0]
    return {int(n): f"{t} · {m}" for n, t, m in re.findall(r"^- #(\d+) (.+?) · ([A-Z]+) · needs", text, re.M)}


def field(text, name):
    m = re.search(rf"^{name}:\s*(.+)$", text, re.M)
    return m.group(1).strip() if m else None


def num(path):
    return int(re.search(r"-(\d+)-", os.path.basename(path)).group(1))


def main():
    args = sys.argv[1:]
    per_week = POSTS_PER_WEEK
    if "--per-week" in args:
        i = args.index("--per-week")
        per_week = int(args[i + 1])
        del args[i:i + 2]
    if per_week not in POST_DAYS:
        sys.exit(f"--per-week must be one of {sorted(POST_DAYS)}")
    days = POST_DAYS[per_week]
    if args:
        start = datetime.date.fromisoformat(args[0])
        start -= datetime.timedelta(days=start.weekday())
    else:
        today = datetime.date.today()
        start = today + datetime.timedelta(days=(7 - today.weekday()) % 7)

    queue, skipped, upcoming = {}, 0, {}
    for pillar in (t for p in ROTATION for t in TRACKS.get(p, [p])):
        posts = []
        files = sorted(glob.glob(os.path.join(DRAFTS, pillar, "*.md")), key=num)
        last = num(files[-1]) if files else 0
        road = roadmap(pillar)
        upcoming[pillar] = [f"#{n:02d} {road[n]}" for n in sorted(road) if n > last]
        if ROADMAPS[pillar] is None:
            upcoming[pillar] = None  # never runs out: always "write from the project log"
        for f in files:
            text = open(f).read()
            status = (field(text, "STATUS") or "draft").lower()
            if status not in QUEUED:
                skipped += 1
                continue
            posts.append((f, text, status))
        queue[pillar] = posts

    out = ["# Posting Queue", "",
           "Generated by `python3 scripts/build_queue.py` — do not edit by hand.",
           "Change a post's STATUS: line instead, then re-run the script.",
           "The record of what went live is `published/linkedin.md`.", "",
           f"Schedule: {per_week} posts a week ({', '.join(datetime.date(2024, 1, 1 + d).strftime('%a') for d in days)}), "
           "pillars in rotation: " + " → ".join(NAMES[p] for p in ROTATION)
           + "".join(f" ({NAMES[p]} takes " + " → ".join(t.split("/")[1].title() for t in ts) + " in turn)"
                     for p, ts in TRACKS.items()),
           "Before posting: fill or delete any [PERSONAL: ...] line and verify or cut any [FACT_CHECK: ...] claim. 🖼 posts need an image made from HEADLINE + LAYOUT; 🎞 posts need one slide per SLIDES line (PDF for LinkedIn, images for Instagram); ✍ posts go out as text only."]
    day, week, turn = start, 0, 0
    track_turn = dict.fromkeys(TRACKS, 0)
    while any(queue.values()):  # after the last draft, open slots name the next roadmap post
        if day.weekday() == 0:
            week += 1
            out += ["", f"## Week {week} — from {day:%a %d %b %Y}", "",
                    "| Date | Series | Title | Mode | Format | Status | File |", "| --- | --- | --- | --- | --- | --- | --- |"]
        pillar = None
        if day.weekday() in days:
            pillar = ROTATION[turn % len(ROTATION)]
            turn += 1
            if pillar in TRACKS:
                pillar = TRACKS[pillar][track_turn[pillar] % len(TRACKS[pillar])]
                track_turn[pillar.split("/")[0]] += 1
        if pillar:
            if queue[pillar]:
                f, text, status = queue[pillar].pop(0)
                mark = (" ✎" if "[PERSONAL" in text else "") + (" 🔎" if "[FACT_CHECK" in text else "")
                rel = os.path.relpath(f, os.path.dirname(QUEUE))
                fmt = "🖼 visual" if field(text, "FORMAT") == "VISUAL" else "✍ text"
                if field(text, "LAYOUT") == "CAROUSEL":
                    n = len(re.findall(r"^\s+\d{2} · ", text.split("\n---\n")[0], re.M)) + 1
                    fmt = f"🎞 carousel ({n} slides)"
                out.append(f"| {day:%a %d %b} | {field(text, 'SERIES')} | {field(text, 'TITLE')}{mark} "
                           f"| {field(text, 'MODE')} | {fmt} | {status} | [{os.path.basename(f)}]({rel}) |")
            else:
                if upcoming[pillar] is None:
                    nxt = ("a PRODUCT (sources/apps.md) or a BLUEPRINT post" if pillar == "business"
                           else "next post from sources/project-log.md")
                else:
                    nxt = upcoming[pillar].pop(0) if upcoming[pillar] else "roadmap finished"
                out.append(f"| {day:%a %d %b} | {LABELS[pillar]} | — write: {nxt} — | | | | |")
        day += datetime.timedelta(days=1)

    out += ["", "✎ = has a [PERSONAL: ...] line to fill in or delete.",
            "🔎 = has a [FACT_CHECK: ...] claim to verify (fix or cut it if it is wrong), then delete the marker."]
    open(QUEUE, "w").write("\n".join(out) + "\n")
    print(f"{week} weeks written to published/queue.md ({skipped} published posts skipped)")
    # posts/ reads the queue dates, so rebuild it now
    import build_posts
    build_posts.main()


if __name__ == "__main__":
    main()
