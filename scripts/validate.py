"""Check every post and template against the system's rules.

Usage: python3 scripts/validate.py

Errors break a rule the system depends on and exit non-zero.
Warnings are worth a look but do not fail the run.
"""
import glob, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# pillar folder -> (series label, filename prefix, theme.css accent var)
PILLARS = {
    "dsa": ("DSA SERIES", "dsa", "--dsa"),
    "software-engineering": ("SOFTWARE ENGINEERING", "se", "--swe"),
    "system-architecture": ("SYSTEM ARCHITECTURE", "arch", "--arch"),
    "ai-engineering": ("AI ENGINEERING", "ai", "--ai"),
    "dev-growth": ("DEV GROWTH", "growth", "--grow"),
}
REQUIRED = ["SERIES", "TITLE", "PILLAR", "FORMAT", "STATUS"]
FORMATS = {"TEXT", "VISUAL"}      # TEXT = post the words only; VISUAL = words + image
VISUAL_ONLY = ["HEADLINE", "LAYOUT"]
LAYOUTS = {"STATEMENT", "GRID", "ANATOMY", "FLOW", "COMPARE", "STAT", "CAROUSEL"}
STATUSES = {"draft", "approved", "scheduled", "published"}
LEVELS = {"BEGINNER", "INTERMEDIATE", "ADVANCED"}
BANNED = ["delve", "leverage", "robust", "seamless", "game-changer", "game changer",
          "fast-paced world", "unlock"]
BODY_HARD_MAX = 3000          # LinkedIn's cap
BODY_TARGET = (1400, 2500)    # master prompt target range
TEXT_MAX = 1400               # TEXT posts must be short; longer posts get a visual
FIRST_DSA_PATTERN_POST = 8    # DSA #08 onward teach patterns and need "Spot it when"

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
    return fields, body.strip("\n")


def check_post(path, pillar, series_label, prefix, seen):
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
        if label != series_label:
            err(path, f"SERIES label '{label}' does not match pillar folder (expected '{series_label}')")
        fm = re.match(rf"^{prefix}-(\d+)-", os.path.basename(path))
        if not fm:
            err(path, f"filename should start with '{prefix}-NN-'")
        elif int(fm.group(1)) != n:
            err(path, f"filename number {fm.group(1)} does not match SERIES #{n:02d}")
        key = (label, n)
        if key in seen:
            err(path, f"duplicate {series} (also {rel(seen[key])})")
        seen[key] = path
        if pillar == "dsa" and n >= FIRST_DSA_PATTERN_POST and "Spot it when" not in body:
            err(path, "DSA pattern post is missing the 'Spot it when…' block")
    check_common(path, fields, body)


def check_common(path, fields, body, quiz=False):
    fmt = fields.get("FORMAT", "")
    if fmt and fmt not in FORMATS:
        err(path, f"FORMAT '{fmt}' is not one of {sorted(FORMATS)}")
    for f in VISUAL_ONLY:
        if fmt == "VISUAL" and not fields.get(f):
            err(path, f"VISUAL post is missing {f}:")
        if fmt == "TEXT" and f in fields:
            err(path, f"TEXT post has {f}: — remove it, or set FORMAT: VISUAL")
    headline = fields.get("HEADLINE", "")
    if headline and len(headline.split()) > 8:
        err(path, f"HEADLINE has {len(headline.split())} words (max 8): '{headline}'")
    layout = fields.get("LAYOUT", "")
    if layout and layout not in LAYOUTS:
        err(path, f"LAYOUT '{layout}' is not one of {sorted(LAYOUTS)}")
    status = fields.get("STATUS", "")
    if status and status not in STATUSES:
        err(path, f"STATUS '{status}' is not one of {sorted(STATUSES)}")
    level = fields.get("LEVEL")
    if level is None:
        warn(path, "no LEVEL: line")
    elif level not in LEVELS:
        err(path, f"LEVEL '{level}' is not one of {sorted(LEVELS)}")
    n = len(body)
    if n > BODY_HARD_MAX:
        err(path, f"body is {n} characters (LinkedIn max {BODY_HARD_MAX})")
    elif fmt == "TEXT":
        if n > TEXT_MAX:
            err(path, f"TEXT post is {n} characters (max {TEXT_MAX}) — shorten it or make it VISUAL")
    elif not quiz and not BODY_TARGET[0] <= n <= BODY_TARGET[1]:
        warn(path, f"body is {n} characters (target {BODY_TARGET[0]}–{BODY_TARGET[1]})")
    for i, line in enumerate(body.splitlines(), 1):
        if re.match(r"^#{1,6} ", line):
            err(path, f"body line {i} is a markdown header (LinkedIn does not render it)")
        if re.search(r"\*\*[^*\s][^*]*\*\*", line):
            err(path, f"body line {i} uses **bold** markdown")
    low = body.lower()
    for w in BANNED:
        if re.search(rf"\b{re.escape(w)}\b", low):
            err(path, f"banned word '{w}'")


def check_posts():
    for pillar, (label, prefix, _) in PILLARS.items():
        seen = {}
        files = sorted(glob.glob(os.path.join(ROOT, "generated", "drafts", pillar, "*.md")))
        for f in files:
            check_post(f, pillar, label, prefix, seen)
    known = set(PILLARS) | {".DS_Store"}
    for d in glob.glob(os.path.join(ROOT, "generated", "drafts", "*")):
        if os.path.basename(d) not in known:
            err(d, "unknown pillar folder — pillars are " + ", ".join(PILLARS))
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


def check_visuals():
    theme_path = os.path.join(ROOT, "templates", "theme.css")
    theme = open(theme_path).read()
    defined = set(re.findall(r"(--[a-z0-9-]+)\s*:", theme))
    # theme accents must match the visual skill's accent table
    skill = open(os.path.join(ROOT, "skills", "linkedin-visual.skill.md")).read()
    for pillar, (label, _, var) in PILLARS.items():
        tm = re.search(rf"{var}:(#[0-9A-Fa-f]{{6}})", theme)
        sm = re.search(rf"`{label}`\s*\|\s*`(#[0-9A-Fa-f]{{6}})`", skill)
        if not tm:
            err(theme_path, f"{var} is not defined")
        elif not sm:
            err(os.path.join(ROOT, "skills", "linkedin-visual.skill.md"), f"no accent row for {label}")
        elif tm.group(1).upper() != sm.group(1).upper():
            err(theme_path, f"{var} is {tm.group(1)} but the visual skill says {sm.group(1)} for {label}")
    hexes = re.findall(r"--(?:dsa|swe|arch|ai|grow):(#[0-9A-Fa-f]{6})", theme)
    if len(hexes) != len(set(h.upper() for h in hexes)):
        err(theme_path, "two pillars share an accent colour")
    cards = glob.glob(os.path.join(ROOT, "templates", "variant-*", "*.html")) + \
            glob.glob(os.path.join(ROOT, "visuals", "week-*", "*.html"))
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
        if re.search(r"--(dsa|swe|arch|ai|grow):#", t):
            err(css, "redefines a pillar accent — colours belong in templates/theme.css")


def main():
    check_posts()
    check_visuals()
    for w in warnings:
        print("warn   " + w)
    for e in errors:
        print("ERROR  " + e)
    posts = len(glob.glob(os.path.join(ROOT, "generated", "*", "*", "*.md")))
    print(f"\n{posts} posts checked · {len(errors)} errors · {len(warnings)} warnings")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
