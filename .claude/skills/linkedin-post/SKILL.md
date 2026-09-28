---
name: linkedin-post
description: Write one LinkedIn post for this repo — the draft text plus its rendered cover image — from a series + post number and an optional one-line angle. Use when the user types /linkedin-post, or says "write DSA #18", "generate backend #04", "make post web #05 about ...", or gives a pillar, a number and a line and wants the post.
---

# LinkedIn post from a number and a line

Turns `<series> #<NN> [keyword] [angle]` into a finished post: the draft in
`generated/drafts/` **and** its cover image in `visuals/week-NN/`, following the
repo's content system. Every run ends with both files on disk.

## Input

`/linkedin-post <series> #<NN> [COPY|FULL|VISUAL] [angle...]`

Examples:
- `/linkedin-post BE #04 we cached the wrong thing and Redis made it worse`
- `/linkedin-post dsa 18`
- `/linkedin-post web #05 FULL memo made our table slower`

The angle is the user's line: the story, opinion or example to build the post
around. It is optional. When given, it shapes the hook and example; it never
overrides the roadmap title, mode or the rules.

Keyword default is `FULL` (post text + cover image). `COPY` makes the post
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
   (Software Engineering), FORMAT/CAROUSEL choice, banned words, length.
   Add `[PERSONAL: ...]` and `[FACT_CHECK: ...]` markers where the rules say.
6. Save to `generated/drafts/<folder>/<prefix>-NN-<short-kebab-title>.md`.
7. Run `python3 scripts/validate.py`. Fix every error in this post and rerun
   until it passes. Report warnings for this post.
8. Run `python3 scripts/build_queue.py` so the queue includes it.
9. `FULL`/`VISUAL`: build the image(s) per the visual skill from the draft's
   `HEADLINE:` and `LAYOUT:`.
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
   - Extra images use the same basename with `-2`, `-3` … and are listed in the
     reply in posting order.
   - Path: `visuals/week-NN/<same basename as the draft>.html`, where `NN` is
     the week the post sits in within `published/queue.md` (two digits). If an
     old card exists there, replace it when it no longer matches the draft's
     HEADLINE/LAYOUT.
   - Link `../../templates/variant-<x>/base.css`; set `:root{--accent:...}`
     for the pillar; include the brand mark in the series row as the templates do.
   - Render with `./render.sh variant-none` (renders post cards only), then
     open the PNG and check it against the visual skill's review checklist.
     Fix and re-render until it passes.
10. Reply with: the draft path, the image path(s) (PNG), the post body, and a list
    of any `[PERSONAL]` / `[FACT_CHECK]` markers the user must resolve.
    Do not commit.
