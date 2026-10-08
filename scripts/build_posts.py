"""Build posts/ — a ready-to-post folder for each post you chose to prepare.

Usage: python3 scripts/build_posts.py              refresh existing folders + index
       python3 scripts/build_posts.py <post>       also create posts/<post>/
                                                   (<post> = draft basename, e.g. dsa-01-reclaiming-dsa)

Folders are made only on request (the create-post skill does it), never for
every draft. The draft in generated/drafts/ is the source and is never changed.

posts/<post>/post.md is the text to paste. On creation it is the draft body
(no SERIES/MODE header); the create-post skill then cuts from post.md the
sections the images already show. This script never overwrites an existing
post.md — delete it to start again from the draft. If the text still has
[PERSONAL: ...] or [FACT_CHECK: ...] markers, a "not ready" block lists them;
if the draft was edited after post.md, the index says so.

Images live next to it and are made by render.sh from posts/<post>/src/:
  src/0.html                     → 0.png            (feed cover, posts with 3+ images)
  src/1.html, src/2.html …       → 1.png, 2.png …   (feed images, posting order)
  src/slide-01.html …            → slide-01.png … + carousel.pdf
  src/cover.html                 → cover.png        (1200x630, daily.dev cover)

posts/<post>/dailydev.md, instagram.md and x.md are the daily.dev, Instagram
and X versions of the text, and blog.md is the full article for the portfolio
blog (all written by the create-post skill, never by this script).
Every platform uses the same images.

posts/README.md is the index: every prepared post, its queue date, status,
image count and whether it is ready. build_queue.py re-runs this for you.
"""
import glob, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
POSTS = os.path.join(ROOT, "posts")
QUEUE = os.path.join(ROOT, "published", "queue.md")
MARKER = re.compile(r"\[(PERSONAL|FACT_CHECK):[^\]]*\]")


def drafts():
    files = glob.glob(os.path.join(ROOT, "generated", "drafts", "**", "*.md"), recursive=True) + \
            glob.glob(os.path.join(ROOT, "generated", "quiz", "**", "*.md"), recursive=True)
    return sorted(files)


def split(path):
    text = open(path).read()
    head, _, body = text.partition("\n---\n")
    fields = dict(re.findall(r"^([A-Z]+):[ \t]*(.*)$", head, re.M))
    return fields, body.strip() + "\n"


def queue_dates():
    """{draft basename: 'Mon 28 Sep'} from published/queue.md."""
    if not os.path.exists(QUEUE):
        return {}
    return {name: date for date, name in
            re.findall(r"^\| (\w{3} \d{2} \w{3}) \|.*\[([^\]]+)\.md\]", open(QUEUE).read(), re.M)}


def images(folder):
    pngs = [os.path.basename(p) for p in glob.glob(os.path.join(folder, "*.png"))]
    feed = sorted((p for p in pngs if re.fullmatch(r"\d+\.png", p)), key=lambda p: int(p[:-4]))
    slides = sorted(p for p in pngs if p.startswith("slide-"))
    return feed, slides


def main(create=()):
    os.makedirs(POSTS, exist_ok=True)
    dates = queue_dates()
    by_name = {os.path.basename(p)[:-3]: p for p in drafts()}
    for name in create:
        if name not in by_name:
            sys.exit(f"build_posts: no draft named {name}.md")
        os.makedirs(os.path.join(POSTS, name), exist_ok=True)
    rows, names = [], set()
    for folder in sorted(glob.glob(os.path.join(POSTS, "*/"))):
        name = os.path.basename(folder.rstrip("/"))
        if name not in by_name:
            continue
        names.add(name)
        fields, body = split(by_name[name])
        folder = os.path.join(POSTS, name)
        post = os.path.join(folder, "post.md")
        if not os.path.exists(post):
            full = [m.group(0) for m in MARKER.finditer(body)]
            out = body
            if full:
                out = "> ⚠ NOT READY — resolve these, then delete this block:\n" + \
                      "".join(f"> - {m}\n" for m in full) + "\n---\n\n" + body
            open(post, "w").write(out)
        text = open(post).read()
        markers = MARKER.findall(text.split("\n---\n", 1)[-1] if text.startswith("> ⚠") else text)

        feed, slides = images(folder)
        fmt = fields.get("FORMAT", "")
        carousel = fields.get("LAYOUT", "") == "CAROUSEL"
        todo = []
        if os.path.getmtime(by_name[name]) > os.path.getmtime(post):
            todo.append("draft changed since post.md")
        if markers:
            todo.append(f"{len(markers)} marker{'s' * (len(markers) > 1)}")
        if fmt == "VISUAL" and carousel and not slides:
            todo.append("needs slides")
        elif fmt == "VISUAL" and not carousel and not feed:
            todo.append("needs image")
        pics = f"{len(slides)} slides" if slides else (str(len(feed)) if feed else "—")
        if os.path.exists(os.path.join(folder, "cover.png")):
            pics += " + cover"
        extra = " · ".join(n for n, f in (("daily.dev", "dailydev.md"), ("Instagram", "instagram.md"), ("X", "x.md"), ("Blog", "blog.md"))
                           if os.path.exists(os.path.join(folder, f))) or "—"
        rows.append((dates.get(name, ""), fields.get("SERIES", ""), fields.get("TITLE", name),
                     fields.get("STATUS", ""), pics, extra, "✅ ready" if not todo else ", ".join(todo), name))

    for folder in sorted(glob.glob(os.path.join(POSTS, "*/"))):
        name = os.path.basename(folder.rstrip("/"))
        if name in names:
            continue
        leftovers = [f for f in os.listdir(folder) if f != "post.md"]
        if leftovers:
            print(f"build_posts: posts/{name}/ has no draft any more — kept (has {', '.join(leftovers)})")
        else:
            os.remove(os.path.join(folder, "post.md"))
            os.rmdir(folder)

    # queued posts first, in posting order; the rest after, by series
    def order(r):
        return (0, list(dates.values()).index(r[0])) if r[0] else (1, r[1])
    rows.sort(key=order)
    ready = sum(r[6] == "✅ ready" for r in rows)
    lines = ["# Posts", "",
             "Generated by `python3 scripts/build_posts.py` — do not edit by hand.",
             "Each folder holds `post.md` (the text to paste) and the images to attach, in order,",
             "plus `dailydev.md` + `cover.png` (daily.dev), `instagram.md` (Instagram), `x.md` (X thread) and `blog.md` (blog article), same images.",
             "Edit the draft in `generated/drafts/`, never `post.md`.", "",
             f"**{len(rows)} post{"s" * (len(rows) != 1)} prepared · {ready} ready to post · "
             f"{len(by_name) - len(rows)} more drafts not prepared yet** "
             "(prepare one with `/create-post <series> <NN>`)", "",
             "| Date | Series | Title | Status | Images | Also for | Ready | Folder |",
             "| --- | --- | --- | --- | --- | --- | --- | --- |"]
    lines += [f"| {d} | {s} | {t} | {st} | {p} | {dd} | {rd} | [{n}/]({n}/) |" for d, s, t, st, p, dd, rd, n in rows]
    open(os.path.join(POSTS, "README.md"), "w").write("\n".join(lines) + "\n")
    print(f"{len(rows)} posts in posts/ ({ready} ready)")


if __name__ == "__main__":
    main(sys.argv[1:])
