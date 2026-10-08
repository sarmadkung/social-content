"""Check every post and template against the system's rules.

Usage: python3 scripts/validate.py

Errors break a rule the system depends on and exit non-zero.
Warnings are worth a look but do not fail the run.
"""
import glob, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# pillar folder -> roadmap file, or (file, "## section") for a subsection
SE_ROAD = "02-software-engineering.md"
ROADMAPS = {
    "dsa": "01-dsa-problem-solving.md",
    # Software Engineering has three subsections, each its own series
    "software-engineering/backend": (SE_ROAD, "Backend roadmap"),
    "software-engineering/web": (SE_ROAD, "Web roadmap"),
    "software-engineering/mobile": (SE_ROAD, "Mobile roadmap"),
    "system-architecture": "03-system-design.md",
    "ai-engineering": "04-ai-engineering.md",
    "dev-growth": "05-dev-growth.md",
    # no roadmap: BUILDING follows real work, FOR BUSINESS follows apps and ideas
    "building": None,
    "business": None,
}
# pillar folder -> (series label, filename prefix, theme.css accent var)
PILLARS = {
    "dsa": ("DSA SERIES", "dsa", "--dsa"),
    "software-engineering/backend": ("SOFTWARE ENGINEERING · BACKEND", "be", "--swe"),
    "software-engineering/web": ("SOFTWARE ENGINEERING · WEB", "web", "--swe"),
    "software-engineering/mobile": ("SOFTWARE ENGINEERING · MOBILE", "mob", "--swe"),
    "system-architecture": ("SYSTEM ARCHITECTURE", "arch", "--arch"),
    "ai-engineering": ("AI ENGINEERING", "ai", "--ai"),
    "dev-growth": ("DEV GROWTH", "growth", "--grow"),
    "building": ("BUILDING", "build", "--build"),
    "business": (("FOR BUSINESS", "SOLUTIONS"), "biz", "--biz"),   # either label, one sequence
}
BUSINESS_TYPES = {"PRODUCT": {"PERSONAL"}, "BLUEPRINT": {"TEACH", "SCENARIO"}}
APPS = os.path.join(ROOT, "sources", "apps.md")
CTA = re.compile(r"message me|contact us", re.I)
# a BLUEPRINT describes a concept; these phrases claim it was built or sold
CLAIMS = ["i built", "we built", "we delivered", "i delivered", "our client", "we helped", "i helped"]
STORY_TYPES = {"UPDATE", "STORY", "DECISION", "POSTMORTEM", "DEMO", "RETRO"}
PROJECT_LOG = os.path.join(ROOT, "sources", "project-log.md")
READY = {"approved", "scheduled", "published"}   # past draft: no [PERSONAL: ...] left
REQUIRED = ["SERIES", "TITLE", "PILLAR", "MODE", "FORMAT", "STATUS"]
MODES = {"TEACH", "WHY", "COMPARE", "LIST", "SCENARIO", "QUIZ", "PERSONAL"}
MAX_TEACH_RUN = 4             # mix rule: never more than 4 TEACH posts in a row
FORMATS = {"TEXT", "VISUAL"}      # TEXT = post the words only; VISUAL = words + image
VISUAL_ONLY = ["HEADLINE", "LAYOUT"]
LAYOUTS = {"STATEMENT", "GRID", "ANATOMY", "FLOW", "COMPARE", "STAT", "CAROUSEL"}
SLIDE_LINE = re.compile(r"^\s+(\d{2}) · ([A-Z]+) · (.+?)(?: · (.+))?$")
CAROUSEL_SLIDES = (6, 10)     # cover + one per stage + END
MAX_CAROUSEL_SHARE = 0.25     # carousels are for real sequences only
STATUSES = {"draft", "approved", "scheduled", "published"}
LEVELS = {"BEGINNER", "INTERMEDIATE", "ADVANCED"}
BANNED = ["delve", "leverage", "robust", "seamless", "game-changer", "game changer",
          "fast-paced world", "unlock"]
BODY_HARD_MAX = 3000          # LinkedIn's cap
BODY_TARGET = (1400, 2500)    # master prompt target range — checked on posts/<post>/post.md,
                              # the text that gets posted. The draft is the full source: no limit.
KEEP_IN_MIND = "Keep in mind"  # every prepared post (posts/<post>/) has this section
TEXT_MAX = 1400               # TEXT posts must be short; longer posts get a visual
FIRST_DSA_PATTERN_POST = 9    # DSA TEACH posts from #09 (Two Pointers) on need "Spot it when"

errors, warnings = [], []


def rel(p):
    return os.path.relpath(p, ROOT)


def err(p, msg):
    errors.append(f"{rel(p)}: {msg}")


def warn(p, msg):
    warnings.append(f"{rel(p)}: {msg}")


def parse(path):
    text = open(path).read()
    if "\n---\n" not in text:
        err(path, "no '---' line between header and body")
        return None, None
    head, body = text.split("\n---\n", 1)
    fields = {}
    for line in head.splitlines():
        m = re.match(r"^([A-Z][A-Z ]*?):\s*(.*)$", line)
        if m:
            fields[m.group(1)] = m.group(2).strip()
    fields["_SLIDES"] = [SLIDE_LINE.match(l) for l in head.splitlines() if re.match(r"^\s+\d{2} · ", l)]
    return fields, body.strip("\n")


ROAD_LINE = re.compile(r"^- #(\d+) (.+?) · ([A-Z]+) · needs (.+)$")


def read_roadmap(pillar):
    """Roadmap lines '- #NN Title · MODE · needs #a, #b' -> {n: (mode, title)}.
    Story pillars have no roadmap and return None."""
    if ROADMAPS[pillar] is None:
        return None
    name, section = ROADMAPS[pillar] if isinstance(ROADMAPS[pillar], tuple) else (ROADMAPS[pillar], None)
    path = os.path.join(ROOT, "pillars", name)
    road, run, inside = {}, 0, section is None
    for i, line in enumerate(open(path).read().splitlines(), 1):
        if section and line.startswith("## "):
            inside = line[3:].strip() == section
        if not inside or not re.match(r"^- #\d+ ", line):
            continue
        m = ROAD_LINE.match(line)
        if not m:
            err(path, f"line {i} is not '- #NN Title · MODE · needs ...'")
            continue
        n, title, mode, needs = int(m.group(1)), m.group(2), m.group(3), m.group(4)
        if mode not in MODES:
            err(path, f"#{n:02d} MODE '{mode}' is not one of {sorted(MODES)}")
        if n in road:
            err(path, f"#{n:02d} appears twice")
        if n != len(road) + 1:
            err(path, f"#{n:02d} is out of order (expected #{len(road) + 1:02d})")
        for a, b in re.findall(r"#(\d+)(?:–#(\d+))?", needs):
            if int(b or a) >= n:
                err(path, f"#{n:02d} needs #{int(b or a):02d}, which comes later or is itself")
        run = run + 1 if mode == "TEACH" else 0
        if run > MAX_TEACH_RUN:
            err(path, f"#{n:02d} is the {run}th TEACH post in a row (max {MAX_TEACH_RUN})")
        road[n] = (mode, title)
    if section and not road:
        err(path, f"no '## {section}' section with roadmap lines")
    return road


def check_post(path, pillar, series_label, prefix, seen, road):
    fields, body = parse(path)
    if fields is None:
        return
    for f in REQUIRED:
        if not fields.get(f):
            err(path, f"missing {f}:")
    series = fields.get("SERIES", "")
    m = re.match(r"^(.+?) #(\d+)$", series)
    if not m:
        err(path, f"SERIES '{series}' is not '<LABEL> #NN'")
    else:
        label, n = m.group(1), int(m.group(2))
        labels = series_label if isinstance(series_label, tuple) else (series_label,)
        if label not in labels:
            err(path, f"SERIES label '{label}' does not match pillar folder (expected {' or '.join(labels)})")
        fm = re.match(rf"^{prefix}-(\d+)-", os.path.basename(path))
        if not fm:
            err(path, f"filename should start with '{prefix}-NN-'")
        elif int(fm.group(1)) != n:
            err(path, f"filename number {fm.group(1)} does not match SERIES #{n:02d}")
        key = n   # per pillar; FOR BUSINESS and SOLUTIONS share one sequence
        if key in seen:
            err(path, f"duplicate {series} (also {rel(seen[key])})")
        seen[key] = path
        if pillar == "business":
            check_business(path, fields, body)
        elif road is None:
            if fields.get("MODE") != "PERSONAL":
                err(path, f"{label} posts use MODE: PERSONAL (got '{fields.get('MODE')}')")
            if fields.get("TYPE") not in STORY_TYPES:
                err(path, f"TYPE '{fields.get('TYPE')}' is not one of {sorted(STORY_TYPES)}")
            # story posts come from the project log, never from nowhere
            src = fields.get("SOURCE", "")
            if not re.match(r"^\d{4}-\d{2}-\d{2} — .+", src):
                err(path, "SOURCE: must name a project-log entry, e.g. '2026-10-02 — Pivot'")
            elif f"## {src}" not in open(PROJECT_LOG).read():
                err(path, f"SOURCE '{src}' has no matching '## {src}' entry in sources/project-log.md")
            # Pivot is a client product: its name must never reach a post
            if re.search(r"\bpivot\b", body, re.I):
                warn(path, "mentions 'pivot' — Pivot is a client product and is never named")
        elif n not in road:
            err(path, f"{series} is not in the roadmap")
        elif fields.get("MODE") != road[n][0]:
            err(path, f"MODE '{fields.get('MODE')}' does not match the roadmap ({road[n][0]})")
        if pillar == "dsa" and n >= FIRST_DSA_PATTERN_POST and fields.get("MODE") == "TEACH" \
                and "Spot it when" not in body:
            err(path, "DSA pattern post is missing the 'Spot it when…' block")
    check_common(path, fields, body)


def check_business(path, fields, body):
    kind, mode = fields.get("TYPE"), fields.get("MODE")
    if kind not in BUSINESS_TYPES:
        err(path, f"TYPE '{kind}' is not one of {sorted(BUSINESS_TYPES)}")
        return
    if mode not in BUSINESS_TYPES[kind]:
        err(path, f"{kind} posts use MODE {' or '.join(sorted(BUSINESS_TYPES[kind]))} (got '{mode}')")
    if not CTA.search(body):
        err(path, "needs one call to action: 'message me' or 'contact us'")
    elif len(CTA.findall(body)) > 1:
        warn(path, "has more than one call to action — keep one")
    if re.search(r"\bpivot\b", body, re.I):
        warn(path, "mentions 'pivot' — Pivot is a client product and is never named")
    if kind == "PRODUCT":
        src = fields.get("SOURCE", "")
        if not src:
            err(path, "PRODUCT posts need SOURCE: <app heading in sources/apps.md>")
        elif f"## {src}\n" not in open(APPS).read() + "\n":
            err(path, f"SOURCE '{src}' has no '## {src}' entry in sources/apps.md")
    else:
        low = body.lower()
        for c in CLAIMS:
            if re.search(rf"\b{c}\b", low):
                err(path, f"BLUEPRINT says '{c}' — a blueprint never claims it was built or delivered")


MARKER_LINE = re.compile(r"^\[(PERSONAL|FACT_CHECK):.*\]\s*$", re.M)


def posted(body):
    """The body as it goes to LinkedIn: marker lines are removed before posting."""
    return re.sub(r"\n{3,}", "\n\n", MARKER_LINE.sub("", body)).strip()


def check_common(path, fields, body, quiz=False):
    mode = fields.get("MODE", "")
    if mode and mode not in MODES:
        err(path, f"MODE '{mode}' is not one of {sorted(MODES)}")
    fmt = fields.get("FORMAT", "")
    if fmt and fmt not in FORMATS:
        err(path, f"FORMAT '{fmt}' is not one of {sorted(FORMATS)}")
    for f in VISUAL_ONLY:
        if fmt == "VISUAL" and not fields.get(f):
            err(path, f"VISUAL post is missing {f}:")
        if fmt == "TEXT" and f in fields:
            err(path, f"TEXT post has {f}: — remove it, or set FORMAT: VISUAL")
    visuals = fields.get("VISUALS", "")
    if visuals:
        if fmt == "TEXT":
            err(path, "TEXT post has VISUALS: — remove it, or set FORMAT: VISUAL")
        parts = [p.strip() for p in visuals.split(" · ")]
        if not parts or parts[-1] != "rest = text":
            err(path, "VISUALS: must end with '· rest = text'")
        lines = {l.strip() for l in body.splitlines()}
        for i, part in enumerate(parts[:-1], 1):
            m = re.match(r"^(\d+) = (.+)$", part)
            if not m or int(m.group(1)) != i:
                err(path, f"VISUALS: item '{part}' is not '{i} = <section heading>'")
            else:
                # a section heading exactly, or several paragraph starts joined by " + "
                for piece in m.group(2).split(" + "):
                    if piece not in lines and not any(l.startswith(piece) for l in lines):
                        err(path, f"VISUALS: no line '{piece}' in the body — name a section heading or a paragraph's opening words exactly")
    headline = fields.get("HEADLINE", "")
    if headline and len(headline.split()) > 8:
        err(path, f"HEADLINE has {len(headline.split())} words (max 8): '{headline}'")
    layout = fields.get("LAYOUT", "")
    if layout and layout not in LAYOUTS:
        err(path, f"LAYOUT '{layout}' is not one of {sorted(LAYOUTS)}")
    check_slides(path, fields, layout)
    status = fields.get("STATUS", "")
    if status and status not in STATUSES:
        err(path, f"STATUS '{status}' is not one of {sorted(STATUSES)}")
    for marker in ("PERSONAL", "FACT_CHECK"):
        if status in READY and f"[{marker}" in body:
            err(path, f"STATUS is {status} but the body still has a [{marker}: ...] marker — clear it first")
    if any(m.group() != "[FACT_CHECK:" for m in re.finditer(r"\[fact[ _-]?check\s*:?", body, re.I)):
        err(path, "write fact markers exactly as [FACT_CHECK: claim → what to check]")
    level = fields.get("LEVEL")
    if level is None:
        warn(path, "no LEVEL: line")
    elif level not in LEVELS:
        err(path, f"LEVEL '{level}' is not one of {sorted(LEVELS)}")
    n = len(posted(body))
    name = os.path.basename(path)[:-3]
    if not quiz and os.path.isdir(os.path.join(ROOT, "posts", name)) and \
            not any(l.startswith(KEEP_IN_MIND) for l in body.splitlines()):
        err(path, f"prepared post has no '{KEEP_IN_MIND}' section — add 3–8 do/don't lines for this topic")
    # no length limit on the draft — it is the full source; post.md is limited (check_post_text)
    if fmt == "TEXT" and n > TEXT_MAX:
        err(path, f"TEXT post is {n} characters (max {TEXT_MAX}) — shorten it or make it VISUAL")
    for i, line in enumerate(body.splitlines(), 1):
        if re.match(r"^#{1,6} ", line):
            err(path, f"body line {i} is a markdown header (LinkedIn does not render it)")
        if re.search(r"\*\*[^*\s][^*]*\*\*", line):
            err(path, f"body line {i} uses **bold** markdown")
    low = body.lower()
    for w in BANNED:
        if re.search(rf"\b{re.escape(w)}(s|d|ed|ing)?\b", low):
            err(path, f"banned word '{w}'")


def check_slides(path, fields, layout):
    slides = fields["_SLIDES"]
    if layout != "CAROUSEL":
        if "SLIDES" in fields or slides:
            err(path, "has SLIDES: but LAYOUT is not CAROUSEL")
        return
    if not slides:
        err(path, "CAROUSEL post is missing its SLIDES: block")
        return
    if None in slides:
        err(path, "a SLIDES line is not '  NN · LAYOUT · headline · what it draws'")
        return
    total = len(slides) + 1   # + the cover, which is HEADLINE
    if not CAROUSEL_SLIDES[0] <= total <= CAROUSEL_SLIDES[1]:
        err(path, f"carousel has {total} slides (need {CAROUSEL_SLIDES[0]}–{CAROUSEL_SLIDES[1]} incl. cover)")
    for i, m in enumerate(slides, 2):
        n, lay, headline = int(m.group(1)), m.group(2), m.group(3)
        if n != i:
            err(path, f"slide {m.group(1)} is out of order (expected {i:02d})")
        last = i == len(slides) + 1
        if last and lay != "END":
            err(path, f"last slide {n:02d} should be END")
        elif not last and lay not in LAYOUTS - {"CAROUSEL"}:
            err(path, f"slide {n:02d} layout '{lay}' is not a single-image layout")
        if len(headline.split()) > 8:
            err(path, f"slide {n:02d} headline has {len(headline.split())} words (max 8)")


def check_posts():
    for pillar, (label, prefix, _) in PILLARS.items():
        seen, road = {}, read_roadmap(pillar)
        files = sorted(glob.glob(os.path.join(ROOT, "generated", "drafts", pillar, "*.md")))
        for f in files:
            check_post(f, pillar, label, prefix, seen, road)
        # the queue posts drafts in number order, so a hole means a post goes out
        # before something it builds on
        carousels = sum("LAYOUT:    CAROUSEL" in open(f).read() for f in files)
        if files and carousels / len(files) > MAX_CAROUSEL_SHARE:
            warn(os.path.join(ROOT, "generated", "drafts", pillar),
                 f"{carousels} of {len(files)} posts are carousels — keep them for real sequences")
        drafted = sorted(seen)
        for n in range(1, (drafted[-1] if drafted else 0) + 1):
            if n not in drafted and (road is None or n in road):
                err(os.path.join(ROOT, "generated", "drafts", pillar),
                    f"#{n:02d} {repr(road[n][1]) + ' ' if road else ''}has no draft, but later posts do")
    known = {p.split("/")[0] for p in PILLARS} | {".DS_Store"}
    for d in glob.glob(os.path.join(ROOT, "generated", "drafts", "*")):
        if os.path.basename(d) not in known:
            err(d, "unknown pillar folder — pillars are " + ", ".join(sorted(known - {".DS_Store"})))
    # a pillar with subsections keeps its posts only inside them
    for parent in {p.split("/")[0] for p in PILLARS if "/" in p}:
        subs = sorted(p.split("/")[1] for p in PILLARS if p.startswith(parent + "/"))
        for f in glob.glob(os.path.join(ROOT, "generated", "drafts", parent, "*")):
            name = os.path.basename(f)
            if name != ".DS_Store" and name not in subs:
                err(f, f"{parent} posts go in one of its subsections: {', '.join(subs)}")
    for f in sorted(glob.glob(os.path.join(ROOT, "generated", "quiz", "*", "*.md"))):
        fields, body = parse(f)
        if fields is None:
            continue
        for k in REQUIRED:
            if not fields.get(k):
                err(f, f"missing {k}:")
        if not re.match(r"^DSA QUIZ #\d+$", fields.get("SERIES", "")):
            err(f, f"quiz SERIES should be 'DSA QUIZ #NN', got '{fields.get('SERIES')}'")
        check_common(f, fields, body, quiz=True)


def check_post_text():
    """posts/<post>/post.md is what gets posted, so the length limit lives here."""
    for p in glob.glob(os.path.join(ROOT, "posts", "*", "post.md")):
        text = open(p).read()
        if text.startswith("> ⚠"):
            text = text.split("\n---\n", 1)[-1]   # the NOT READY block is not posted
        n = len(posted(text))
        has_images = bool(glob.glob(os.path.join(os.path.dirname(p), "*.png")))
        if n > BODY_HARD_MAX:
            err(p, f"{n} characters (LinkedIn max {BODY_HARD_MAX}) — move a section into an image")
        elif n > BODY_TARGET[1]:
            warn(p, f"{n} characters (target up to {BODY_TARGET[1]}) — move a section into an image")
        elif n < BODY_TARGET[0] and not has_images:
            warn(p, f"{n} characters (target {BODY_TARGET[0]}–{BODY_TARGET[1]})")


IG_CAPTION_MAX = 2200            # Instagram's caption cap
X_POST_MAX = 280                 # X free-account post cap


def check_platform_texts():
    """The other platforms' texts in posts/<post>/: Instagram and X limits, markers."""
    for p in glob.glob(os.path.join(ROOT, "posts", "*", "instagram.md")):
        text = open(p).read()
        if len(text) > IG_CAPTION_MAX:
            err(p, f"{len(text)} characters (Instagram max {IG_CAPTION_MAX})")
        tags = re.findall(r"(?<!\w)#\w+", text)
        if len(tags) > 5:
            warn(p, f"{len(tags)} hashtags — keep 3–5")
    for p in glob.glob(os.path.join(ROOT, "posts", "*", "x.md")):
        folder = os.path.dirname(p)
        used = []
        for i, tweet in enumerate(re.split(r"^---\s*$", open(p).read(), flags=re.M), 1):
            m = re.search(r"^\[images:\s*([\d,\s]+)\]\s*$", tweet, re.M)
            nums = [int(x) for x in re.findall(r"\d+", m.group(1))] if m else []
            text = re.sub(r"^\[images:.*\]\s*$", "", tweet, flags=re.M).strip()
            if len(text) > X_POST_MAX:
                err(p, f"post {i} is {len(text)} characters (X max {X_POST_MAX})")
            if len(nums) > 4:
                err(p, f"post {i} attaches {len(nums)} images (X max 4)")
            for n in nums:
                if not os.path.exists(os.path.join(folder, f"{n}.png")):
                    err(p, f"post {i} attaches image {n}, but {n}.png does not exist")
            used += nums
        if len(re.findall(r"(?<!\w)#\w+", open(p).read())) > 2:
            warn(p, "more than 2 hashtags — X threads use 0–2")
    for p in glob.glob(os.path.join(ROOT, "posts", "*", "instagram.md")) + \
             glob.glob(os.path.join(ROOT, "posts", "*", "dailydev.md")) + \
             glob.glob(os.path.join(ROOT, "posts", "*", "x.md")) + \
             glob.glob(os.path.join(ROOT, "posts", "*", "blog.md")):
        if re.search(r"\[(PERSONAL|FACT_CHECK):", open(p).read()):
            err(p, "has a [PERSONAL]/[FACT_CHECK] marker — platform texts go out as written")


BLOG_KEYS = ("title", "description", "date", "series", "seriesNumber", "slug", "tags", "cover")
BLOG_WORDS = (600, 2000)


def check_blog():
    """posts/<post>/blog.md: front-matter, image links, length, no social leftovers."""
    for p in glob.glob(os.path.join(ROOT, "posts", "*", "blog.md")):
        folder = os.path.dirname(p)
        text = open(p).read()
        m = re.match(r"---\n(.*?)\n---\n(.*)", text, re.S)
        if not m:
            err(p, "no YAML front-matter (--- ... ---) at the top")
            continue
        front = dict(re.findall(r"^(\w+):\s*(.*)$", m.group(1), re.M))
        body = m.group(2)
        for key in BLOG_KEYS:
            if not front.get(key, "").strip():
                err(p, f"front-matter is missing {key}")
        if len(front.get("title", "").strip('"')) > 70:
            warn(p, "title over 70 characters")
        if len(front.get("description", "").strip('"')) > 160:
            warn(p, "description over 160 characters (search results cut it)")
        if front.get("slug") and front["slug"] != os.path.basename(folder):
            err(p, f"slug {front['slug']} does not match the folder {os.path.basename(folder)}")
        if front.get("date") and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", front["date"]):
            err(p, "date must be YYYY-MM-DD")
        for img in re.findall(r"!\[[^\]]*\]\(([^)\s]+)\)", body) + [front.get("cover", "")]:
            if img and not img.startswith("http") and not os.path.exists(os.path.join(folder, img)):
                err(p, f"links {img}, but it does not exist in the folder")
        words = len(re.findall(r"\w+", body))
        if not BLOG_WORDS[0] <= words <= BLOG_WORDS[1]:
            warn(p, f"{words} words (target {BLOG_WORDS[0]}–{BLOG_WORDS[1]})")
        if re.search(r"(?<![\w#(])#[A-Za-z]\w*", re.sub(r"```.*?```", "", body, flags=re.S)):
            warn(p, "has hashtags — the blog uses front-matter tags instead")


def check_visuals():
    theme_path = os.path.join(ROOT, "templates", "theme.css")
    theme = open(theme_path).read()
    defined = set(re.findall(r"(--[a-z0-9-]+)\s*:", theme))
    # theme accents must match the visual skill's accent table
    skill = open(os.path.join(ROOT, "skills", "linkedin-visual.skill.md")).read()
    checked = set()
    for pillar, (label, _, var) in PILLARS.items():
        label = label[0] if isinstance(label, tuple) else label
        label = label.split(" · ")[0]   # subsections share their pillar's accent
        if var in checked:
            continue
        checked.add(var)
        tm = re.search(rf"{var}:(#[0-9A-Fa-f]{{6}})", theme)
        sm = re.search(rf"`{label}`(?:\s*/\s*`[^`]+`)*\s*\|\s*`(#[0-9A-Fa-f]{{6}})`", skill)
        if not tm:
            err(theme_path, f"{var} is not defined")
        elif not sm:
            err(os.path.join(ROOT, "skills", "linkedin-visual.skill.md"), f"no accent row for {label}")
        elif tm.group(1).upper() != sm.group(1).upper():
            err(theme_path, f"{var} is {tm.group(1)} but the visual skill says {sm.group(1)} for {label}")
    hexes = re.findall(r"--(?:dsa|swe|arch|ai|grow|build|biz):(#[0-9A-Fa-f]{6})", theme)
    if len(hexes) != len(set(h.upper() for h in hexes)):
        err(theme_path, "two pillars share an accent colour")
    cards = glob.glob(os.path.join(ROOT, "templates", "variant-*", "*.html")) + \
            glob.glob(os.path.join(ROOT, "posts", "*", "src", "*.html"))
    names = {os.path.basename(f)[:-3] for f in
             glob.glob(os.path.join(ROOT, "generated", "**", "*.md"), recursive=True)}
    for src in glob.glob(os.path.join(ROOT, "posts", "*", "src")):
        post = os.path.basename(os.path.dirname(src))
        if post not in names:
            err(src, f"no draft named {post}.md — post folders must match a draft's file name")
        for f in glob.glob(os.path.join(src, "*.html")):
            if not re.fullmatch(r"\d+\.html|slide-\d\d\.html|cover\.html", os.path.basename(f)):
                err(f, "image sources are named 1.html, 2.html …, slide-01.html … or cover.html")
    for f in cards:
        t = open(f).read()
        for href in re.findall(r'href="([^"]+\.css)"', t):
            if not href.startswith("http") and not os.path.exists(os.path.join(os.path.dirname(f), href)):
                err(f, f"stylesheet '{href}' does not exist")
        for var in re.findall(r"var\((--[a-z0-9-]+)\)", t):
            if var not in defined and var not in re.findall(r"(--[a-z0-9-]+)\s*:", t):
                err(f, f"uses {var}, which templates/theme.css does not define")
    for css in glob.glob(os.path.join(ROOT, "templates", "variant-*", "base.css")):
        t = open(css).read()
        if '@import url("../theme.css")' not in t:
            err(css, "does not import ../theme.css")
        if re.search(r"--(dsa|swe|arch|ai|grow|build|biz):#", t):
            err(css, "redefines a pillar accent — colours belong in templates/theme.css")


def main():
    check_posts()
    check_post_text()
    check_platform_texts()
    check_blog()
    check_visuals()
    for w in warnings:
        print("warn   " + w)
    for e in errors:
        print("ERROR  " + e)
    posts = len(glob.glob(os.path.join(ROOT, "generated", "**", "*.md"), recursive=True))
    print(f"\n{posts} posts checked · {len(errors)} errors · {len(warnings)} warnings")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
