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
| LinkedIn | `post.md` | `1.png`, `2.png` … (or `carousel.pdf`) |
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
   exists and no angle was given, keep it as is and go straight to the image
   (step 9), then report. Only when an angle *was* given, show the draft and ask
   whether to rewrite it. If any earlier number in the
   series has no draft, warn — the validator fails on skipped numbers.
4. Read, in full: `skills/linkedin-content.skill.md`,
   `prompts/master-content-prompt.md`, the pillar file, and every draft listed
   in `needs` (so the post builds on them and does not repeat them). For
   `FULL`/`VISUAL` (the default) also read `skills/linkedin-visual.skill.md`
   and the base CSS of the variant you will use.
5. Write the post in the skill's output format, with `SERIES: <label> #NN`,
   `MODE:` exactly as the roadmap says, `STATUS: draft`. Apply every rule:
   Senior Interest Test, teaching order, mode structure, failure scenario rule
   (Software Engineering), Keep in mind rule (every post), Watch out section
   (when the topic has real drawbacks), FORMAT/CAROUSEL choice, banned words, length.
   Add `[PERSONAL: ...]` and `[FACT_CHECK: ...]` markers where the rules say.
6. Save to `generated/drafts/<folder>/<prefix>-NN-<short-kebab-title>.md`.
7. Run `python3 scripts/validate.py`. Fix every error in this post and rerun
   until it passes. Report warnings for this post.
8. Run `python3 scripts/build_queue.py` so the queue includes it, then
   `python3 scripts/build_posts.py <draft basename>` to create this post's
   folder (`posts/<post>/post.md`) and add it to `posts/README.md`. Folders are
   made only for posts the user asks for — never for every draft.
9. `FULL`/`VISUAL`: build the image(s) per the visual skill from the draft's
   `HEADLINE:` and `LAYOUT:`.
   - **Read or write the draft's `VISUALS:` line first.** It names the
     sections that become images (`1 = <section heading> · 2 = … · rest =
     text`). If the draft has none, choose the sections and add the line to the
     header — adding this header line, and a missing `Keep in mind …`
     section, are the only changes allowed to an existing draft. Make one image per listed section, in that order.
   - **Text or image, per section.** Any section — including `Keep in mind`
     and `Watch out` — can stay in the text or become an image. Decide per
     post: a list of 4+ short items or anything with a shape (steps,
     comparison, before/after) reads better as an image; a story or a single
     argument stays in the text.
   - **Images explain the content that matters.** First list the 1–3 ideas the
     post is really about. Make one image per idea that needs a picture — more
     than one image is fine (LinkedIn multi-image post). Every shape is labelled
     in plain words. Test: would a reader who skips the text understand the
     image on its own? If not, redraw. Never a decorative or cryptic diagram
     (unlabelled dots, symbol-only graphs, tiny icons standing in for ideas).
   - **Don't repeat the text.** Stats, counts and lines already in the post body
     (e.g. "23 technique write-ups") do not go on the image — not in the
     diagram, not in the footer. The image adds what the text can't show; the
     footer's right side is the topic, complexity, or `1 / 2` page number.
   - Images are numbered in posting order: `1.png` is the first image shown.
   - **Feed cover for 3+ images.** When the post has 3 or more images, also
     write `src/0.html` → `0.png` per the visual skill's section 5c: the
     headline plus a numbered "In this post" list, one row per image. It is
     shown first everywhere: attach it first on LinkedIn and Instagram, and
     put `0` first in post 1's `[images: …]` line in `x.md`. 1–2 images: no
     feed cover.
   - **Then cut from `post.md` what the images show — never from the draft.**
     The draft in `generated/drafts/` is the full source and is never trimmed.
     `posts/<post>/post.md` is the text that gets posted: remove from it every
     section listed in `VISUALS:` and leave one short line pointing to the images.
     Keep only what the images can't carry: the story, the detail and
     examples, the close. `build_posts.py` never overwrites an existing
     `post.md`; to start over from the draft, delete `post.md` and re-run it.
   - Path: `posts/<draft basename>/src/1.html`, `2.html` … in posting order
     (carousel: `src/slide-01.html` …). If old sources exist there, replace
     them when they no longer match the draft.
   - Link `../../../templates/variant-<x>/base.css` and
     `../../../brand/…`; set `:root{--accent:...}` for the pillar; include the
     brand mark in the series row as the templates do.
   - Render with `./render.sh variant-none` (renders post images only, into
     `posts/<post>/1.png` …), then open each PNG and check it against the
     visual skill's review checklist. Fix and re-render until it passes.
   - **daily.dev cover** (every `FULL`/`VISUAL` run, `TEXT` posts too): write
     `posts/<post>/src/cover.html` using `../../../templates/cover/base.css`
     (1200×630). Only the series label + brand mark, the draft's `HEADLINE:`
     with the `<em>` accent, one small labelled motif for the post's main idea,
     and the footer (name lockup · topic). No stats, no grids, no second idea —
     the cover gets the click; the post images explain. `render.sh` renders
     it to `posts/<post>/cover.png`. Check it at 300px wide: the headline must
     still read. See the visual skill's cover rules.
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
     shows>](1.png)`). **Easy to understand comes first; aim for a 1–5 minute
     read (220–1100 words; the blog shows "N min read" from the word count
     at 220 words a minute).** Plain words and short sentences; one simple
     example per idea, the same one the images use; define a term once, in
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
   - Run `python3 scripts/build_posts.py <draft basename>` again so the index
     counts the images, cover and platform texts.
10. Reply with: the draft path, the `posts/<post>/` folder and its image(s),
    `cover.png`, `dailydev.md`, `instagram.md`, `x.md` and `blog.md`, the post body, and a list
    of any `[PERSONAL]` / `[FACT_CHECK]` markers the user must resolve.
    Do not commit.
