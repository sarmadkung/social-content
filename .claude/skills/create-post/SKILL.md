---
name: create-post
description: Create one post for every platform — LinkedIn, daily.dev, Instagram, X and the blog — from a series + post number and an optional one-line angle: the draft, the shared images, a daily.dev cover, and each platform's text. Use when the user types /create-post (or the old /linkedin-post), or says "create post", "generate post", "write DSA #18", "generate backend #04", "make post web #05 about ...", or gives a pillar, a number and a line and wants the post.
---

# Create a post (LinkedIn, daily.dev, Instagram, X, blog) from a number and a line

Turns `<series> #<NN> [keyword] [angle]` into a finished post: the draft in
`generated/drafts/` **and** a ready-to-post folder `posts/<post>/` holding
the images (shared by every platform) and one text file per platform,
following the repo's content system. Every run ends with both on disk.

| Platform | Text | Images |
| --- | --- | --- |
| LinkedIn | `post.md` (caption) + `carousel-title.txt` (the PDF's title) | `carousel.pdf` — every image in order, posted as a document so it swipes |
| daily.dev | `dailydev.md` | `cover.png` |
| Instagram | `instagram.md` | `1.png`, `2.png` … as a carousel (or the `slide-NN.png` files) |
| X | `x.md` (a thread) | up to 4 images per post, as `x.md` says |
| Blog (portfolio) | `blog.md` (the full article) | `1.png`, `2.png` … inline, `cover.png` as the header |

The images are made once and reused everywhere; only the text changes per
platform. The blog is the full, canonical version; the social texts are the
short versions of it.

## Input

`/create-post <series> #<NN> [COPY|FULL|VISUAL] [angle...]`

Examples:
- `/create-post BE #04 we cached the wrong thing and Redis made it worse`
- `/create-post dsa 18`
- `/create-post web #05 FULL memo made our table slower`

The angle is the user's line: the story, opinion or example to build the post
around. It is optional. When given, it shapes the hook and example; it never
overrides the roadmap title, mode or the rules.

Keyword default is `FULL` (all platform texts + blog article + images + daily.dev cover). `COPY` makes the post
text only, `VISUAL` makes only the image for an existing draft. A post whose
`FORMAT:` is `TEXT` gets no image even under `FULL`; a `CAROUSEL` post gets its
slide deck instead of a single cover.

## Series aliases

| User types | Pillar folder | Series label | File prefix | Roadmap |
| --- | --- | --- | --- | --- |
| dsa | `dsa` | `DSA SERIES` | `dsa` | `pillars/01-dsa-problem-solving.md` |
| be, backend | `software-engineering/backend` | `SOFTWARE ENGINEERING · BACKEND` | `be` | `pillars/02-software-engineering.md` → `## Backend roadmap` |
| web | `software-engineering/web` | `SOFTWARE ENGINEERING · WEB` | `web` | same file → `## Web roadmap` |
| mob, mobile | `software-engineering/mobile` | `SOFTWARE ENGINEERING · MOBILE` | `mob` | same file → `## Mobile roadmap` |
| stack | `software-engineering/stack` | `SOFTWARE ENGINEERING · STACK` | `stack` | same file → `## Stack roadmap` |
| arch, sd, system | `system-architecture` | `SYSTEM ARCHITECTURE` | `arch` | `pillars/03-system-design.md` |
| ai | `ai-engineering` | `AI ENGINEERING` | `ai` | `pillars/04-ai-engineering.md` |
| growth, dev | `dev-growth` | `DEV GROWTH` | `growth` | `pillars/05-dev-growth.md` |
| build, building | `building` | `BUILDING` | `build` | none — source is `sources/project-log.md` |
| biz, business | `business` | `FOR BUSINESS` / `SOLUTIONS` | `biz` | none — source is `sources/apps.md` |

If the series is ambiguous or missing, ask. If the number is missing, use the
next unwritten number for that series.

## Steps

1. Parse series, number, keyword and angle.
2. Read the roadmap line `#NN Title · MODE · needs ...` for that number. If it
   does not exist, stop and say so (offer to add a roadmap line first).
   BUILDING / FOR BUSINESS: find the matching entry in the source file instead;
   if the angle has no real source entry, stop and ask — never invent one.
3. Check drafts: if `generated/drafts/<folder>/<prefix>-NN-*.md` already
   exists and no angle was given, keep it as is: read it and run the Content
   Quality Gate on it read-only (step 6). If the gate finds a technical error,
   a missing prerequisite or a wrong definition, stop before building anything,
   list the problems and suggest `/improve-draft` — do not rewrite the draft
   here. Otherwise go straight to the image (step 10), then report. Only when
   an angle *was* given, show the draft and ask
   whether to rewrite it. If any earlier number in the
   series has no draft, warn — the validator fails on skipped numbers.
   **No duplicates.** Before writing a new draft or post folder, search
   `generated/drafts/`, `posts/` and every pillar roadmap for the same topic
   under another number or title. If one already covers it, stop and name it —
   never make a second draft, folder or roadmap line for the same idea.
4. Read, in full: `skills/linkedin-content.skill.md`,
   `prompts/master-content-prompt.md`, the pillar file, and every draft listed
   in `needs` (so the post builds on them and does not repeat them). For
   `FULL`/`VISUAL` (the default) also read `skills/linkedin-visual.skill.md`
   and the base CSS of the variant you will use.
5. Write the post in the skill's output format, with `SERIES: <label> #NN`,
   `MODE:` exactly as the roadmap says, `STATUS: draft`. First write down the
   reader, the learning outcome in one sentence and why it matters (Senior
   Interest and Learning Value Test). Then apply every rule: adaptive teaching
   order for the `LEVEL:`, mode structure, real-or-nothing examples, limits and
   mistakes, failure scenario rule (Software Engineering), Takeaway rule
   (a closing takeaway plus one `Takeaway:` line per image section), Keep in mind rule
   (every post), Watch out section (when the topic has real drawbacks),
   FORMAT/CAROUSEL choice, banned words, length.
   Add `[PERSONAL: ...]` and `[FACT_CHECK: ...]` markers where the rules say.
6. **Content Quality Gate.** Run the gate defined in the content skill on the
   finished draft: technical correctness, depth and learning value, teaching,
   language, completeness, author intent, markers. Fix what fails, then re-read
   the revised draft to confirm the fixes added no new error and kept the
   intended claim. Do not add sections, caveats or facts just to satisfy the
   gate. Keep a short note of any substantive correction for the reply. Do not
   go on to images or platform texts until the draft passes.
7. Save to `generated/drafts/<folder>/<prefix>-NN-<short-kebab-title>.md`
   with `STATUS: draft` — never a later status while a marker is left.
8. Run `python3 scripts/validate.py`. Fix every error in this post and rerun
   until it passes. Report warnings for this post.
9. Run `python3 scripts/build_queue.py` so the queue includes it, then
   `python3 scripts/build_posts.py <draft basename>` to create this post's
   folder (`posts/<post>/post.md`) and add it to `posts/README.md`. Folders are
   made only for posts the user asks for — never for every draft.
10. `FULL`/`VISUAL`: make the images in two skills, in this order.
   - **Slides first: run `write-slides`.** It writes `posts/<post>/slides.md`
     from the draft: every image (daily.dev cover, feed cover `0`, content
     slides, takeaway slide) with all its words and layout. All the rules on
     what goes on an image live there: the `VISUALS:` line, one idea per image,
     question titles, from/next cues, the takeaway slide, the feed cover, and
     the cover content. Show `slides.md` to the user and wait for their OK
     before building anything, unless they asked for the whole post in one go.
   - **Then run `build-visuals`.** It builds `src/*.html` from `slides.md`,
     renders the PNGs, `cover.png` and `carousel.pdf`, and checks them. It never
     changes wording. If text doesn't fit, it proposes a change to `slides.md`.
   - **To change a slide later:** edit `slides.md` (via `write-slides`), then
     run `build-visuals`. Never edit `src/*.html` text directly: `validate.py`
     fails when HTML text is missing from `slides.md`.
   - **The image list in the captions comes from `slides.md`.** Use the slide
     titles as they are written there, so captions and images always match.
   - **LinkedIn caption (`post.md`): select, don't compress.** The draft in
     `generated/drafts/` is the full source and is never trimmed.
     `posts/<post>/post.md` is the LinkedIn caption; with images it is short
     (about 700–1,200 characters, 1,400 soft ceiling — content skill
     **Length**). These rules are for LinkedIn only; the other platform texts
     below keep their own. Build it from:
     1. the hook, in short lines;
     2. one or two sentences on why it matters;
     3. a pointer to the images — a numbered list of their titles is fine as
        a table of contents (one short line each), but never re-explain what
        an image shows;
     4. one takeaway, said once;
     5. optionally one closing question or a `Next:` line — not both.
     Leave out by default: `Keep in mind`, a separate `Takeaway:` label when
     the last line already says it, side explanations (they stay in the draft
     and blog), and any second summary. Keep a section only if the post is
     misleading without it. No markdown (`**bold**`, headers): LinkedIn shows
     it as plain symbols. No `[PERSONAL]` / `[FACT_CHECK]` content in the
     caption; the NOT READY block `build_posts.py` adds stays on top until
     the markers are resolved. Then read it once as an editor: one main
     message, nothing said twice, every sentence natural — and still accurate.
     `build_posts.py` never overwrites an existing `post.md`; to start over
     from the draft, delete `post.md` and re-run it.
     Reference for length and tone (AI #01, approved by the user — a guide,
     not a template):
     ```
     You correct an AI model. It says, "Thanks, noted."
     Tomorrow, in a new chat, it makes the same mistake.
     It didn't forget. It never learned from your correction.
     To understand why, you need a few fundamentals before diving into LLMs.
     I put these 9 fundamental AI concepts into one visual guide:
     1. AI vs. ML vs. Deep Learning
     … (one line per image)
     9. Training vs. inference
     The key takeaway: A model is a function with learned weights. Training
     adjusts those weights; inference uses them to generate outputs.
     And every inference call comes with a cost.
     What fundamental concept would you add to this list?
     ```
   - **Carousel PDF title.** LinkedIn asks for a descriptive title when you
     upload `carousel.pdf`. Write it to `posts/<post>/carousel-title.txt`:
     one line, nothing else — never in `post.md`, so it can't be pasted into
     the caption by mistake. `build_posts.py` seeds it from the draft's
     `TITLE:` and never overwrites it; rewrite it to say what the document
     contains: topic + what is inside, ≤ 60 characters, no hashtags, no
     series label, not the hook (e.g. `AI Foundations: 9 core ideas,
     explained visually`). `carousel_pdf.sh` also writes it into the PDF's
     title metadata. `validate.py` errors when a post with images has no
     title file or a title over 60 characters. **Always end a run by showing
     the title on its own line**, labelled `LinkedIn PDF title:`, so the user
     can copy it.
   - **daily.dev text**: write `posts/<post>/dailydev.md` — a `TITLE:` line
     (a clear claim, ≤ 70 characters, not the series label), `COVER: cover.png`,
     `---`, then 150–250 words of Markdown from the draft: the hook, the key
     points as a short bold-led list, one close line. daily.dev readers are
     developers who click through from a feed card, so drop the personal
     diary parts and hashtags, keep the technical substance, and leave out any
     unresolved `[PERSONAL]` / `[FACT_CHECK]` content. Never overwrite an
     existing `dailydev.md` unless the user asks.
   - **Instagram text**: write `posts/<post>/instagram.md` — the caption only;
     the images carry the post. A hook line (the headline idea, not the
     series label), 2–4 short lines saying what the images show and one
     takeaway, a `Swipe →` line when there are 2+ images, then 3–5 hashtags on
     the last line. 300–700 characters, plain text (Instagram shows no
     markdown and links in captions don't click). No unresolved `[PERSONAL]` /
     `[FACT_CHECK]` content. Never overwrite an existing `instagram.md` unless
     the user asks.
   - **X thread**: write `posts/<post>/x.md` — 3–6 posts separated by a line
     holding only `---`. Each post is 280 characters or fewer (the free-account
     limit). Post 1 is the hook and stands alone (most people only see it);
     the middle posts carry one point each; the last post is the takeaway
     and the `Next:` line. Put `[images: 1, 2]` on its own line at the end of
     a post to attach images — at most 4 per post, each image once, usually
     all on post 1 or spread next to the point they show. 0–2 hashtags in the
     whole thread, plain text, no markdown. No unresolved `[PERSONAL]` /
     `[FACT_CHECK]` content. Never overwrite an existing `x.md` unless the
     user asks.
   - **Blog article**: write `posts/<post>/blog.md` — the full, canonical
     version for the portfolio blog. Start with YAML front-matter:
     ```
     ---
     title: "<a clear claim, ≤ 70 characters — may match dailydev.md's TITLE>"
     description: "<one sentence for search results, ≤ 160 characters>"
     date: <the post's queue date from published/queue.md, else today, YYYY-MM-DD>
     series: "<series label in title case, e.g. AI Engineering>"
     seriesNumber: <NN as a number>
     slug: <draft basename>
     tags: [<3–5 lowercase tags>]
     cover: cover.png
     lab: <optimallab.dev URL, only if the post has a Lab page — else omit>
     ---
     ```
     Then the article in Markdown, built from the **full draft** (never from the
     trimmed `post.md`): the hook as the opening paragraph, each draft section
     as a `##` heading with its content written as prose and lists, and each
     image placed inline under the section it shows (`![<what the image
     shows>](1.png)`). If the post has a feed cover (`0.png`), put it right
     after the hook under `## What we'll cover`, with a numbered list of the
     sections, one line each. **Easy to understand comes first; aim for a 1–5 minute
     read (220–1100 words; the blog shows "N min read" from the word count
     at 220 words a minute).** Plain words and short sentences; one simple
     example per idea, the same one the images use; define a term once, in a full plain sentence with a
     simple example, in
     a few words, when it first appears. Let the images carry the detail.
     Leave out what the reader doesn't need to get the idea: side topics,
     history, extra techniques, long glossaries, repeated points. The length
     is a guide, not a cap: if a topic needs 7 minutes to explain properly,
     write 7 minutes — never cut something the learner needs just to fit. Every claim must
     already be in the draft or be common, checkable knowledge — no new
     numbers, dates or versions.
     If `lab:` is set, add a line linking to the interactive version. End with a
     `## Next in the series` line naming the next post. No hashtags, no
     `→` arrows (use `-` lists), no unresolved `[PERSONAL]` / `[FACT_CHECK]`
     content. Never overwrite an existing `blog.md` unless the user asks.
   - **Publish the blog when the post goes live** (or when the user asks).
     Copy `blog.md` to the site repo as
     `~/Documents/personal/muhammadsarmad/content/blog/<site-slug>.mdx`. Use a
     short site slug (e.g. `one-codebase-to-native`). The front-matter is
     `title`, `description`, `date`, `tags` (Title Case) and `draft: false`.
     Copy the images used to `public/blog/<site-slug>/` and change image paths
     to `/blog/<site-slug>/N.png`. Run `pnpm build` there; the page must appear
     as `/blog/<site-slug>`. Then commit and push to `main`, which deploys it.
     Example: `content/blog/one-codebase-to-native.mdx`. A post that is
     live on social media must not be missing from the blog.
   - **Blog link** (rule in `skills/linkedin-content.skill.md`, **Blog
     links**): only when the matching article is live on
     muhammadsarmad.com — check the site repo for `<slug>.mdx` with `draft:
     false`; otherwise add no link and say so in the reply. When it is live:
     LinkedIn (`post.md`) — one line before the hashtags, "Read the full
     explanation on my blog: <url>"; X (`x.md`) — the URL on the last post;
     daily.dev (`dailydev.md`) — a last line linking the article; Instagram
     (`instagram.md`) — no URL (it won't click), one line such as "Full
     explanation on my blog, link in bio". Never link other social profiles
     or ask readers to follow elsewhere.
   - Run `python3 scripts/build_posts.py <draft basename>` again so the index
     counts the images, cover and platform texts.
11. Reply with: the draft path, the `posts/<post>/` folder and its image(s),
    `cover.png`, `dailydev.md`, `instagram.md`, `x.md` and `blog.md`, the post body, the
    learning outcome, any substantive corrections the gate made, and a list
    of any `[PERSONAL]` / `[FACT_CHECK]` markers the user must resolve.
    Do not commit.
