---
name: write-slides
description: Write or update a post's slides spec, posts/<post>/slides.md — every image (daily.dev cover, feed cover, content slides, takeaway slide) with all its text word for word and its layout — from the draft in generated/drafts/. Touches slides.md only; no HTML, no images. Use when the user types /write-slides, or says "write the slides", "make the slides from the draft", "update the slides", "change slide 3", "plan the visuals", or when create-post reaches its image step. Not for rendering (use build-visuals) or for fixing the draft itself (use improve-draft).
---

# Write the slides spec (draft → `slides.md`)

`posts/<post>/slides.md` is the **one source for every image** in a post. It
holds every word that appears on every image, plus layout and colour notes,
so that:
- `build-visuals` can build the HTML and PNGs from it alone, and
- the user or another agent can review or improve all the slides by editing one file.

This skill writes `slides.md` and nothing else. It never writes HTML, never
renders, and never edits the draft (except the two header fixes in step 3).
Reference: `posts/growth-01-hand-written-code-new-assembly/slides.md`.

## Input

`/write-slides <post>`, where `<post>` is a draft basename (`growth-01-hand-written-code-new-assembly`),
a series + number (`growth #01`), or `<post> slide N <change>` for one edit.

## Steps

1. Find the draft `generated/drafts/<pillar>/<post>.md`. No draft: stop and
   say so. If the draft fails the content gate (technical error, missing
   prerequisite, wrong definition), stop and suggest `/improve-draft` first.
   The draft comes first; slides never fix the draft's content.
2. Read, in full: the draft, `skills/linkedin-visual.skill.md`, and
   `skills/linkedin-content.skill.md` (Takeaway rule, titles). If
   `posts/<post>/slides.md` already exists, read it. You are **updating** it:
   keep everything the change does not touch, word for word.
   If it does not exist but `posts/<post>/src/*.html` do, write `slides.md` from
   the HTML first (copy every text, word for word), then apply the change.
3. **Choose the images.** Read the draft's `VISUALS:` line (`1 = <section> ·
   2 = … · rest = text`). If it is missing, choose the sections and add the line
   to the draft header. Adding that line, and a missing `Takeaway:` line on an
   image section, are the only draft edits allowed here.
4. **Write the content of each image** by these rules:
   - **Images explain the content that matters.** One image per idea that needs
     a picture. Every shape is labelled in plain words. Test: a reader who skips
     the text still understands the image. No decorative or cryptic diagrams.
   - **Text or image, per section.** A list of 4+ short items, steps, a
     comparison or a before/after makes a good image. A story or a single
     argument stays in the text.
   - **Define every term fully, with an example** (visual skill section 5d),
     never a fragment.
   - **Titles: one plain question the image answers** ("Who keeps the apps in
     sync now?"). No slogans or clever contrasts. Mark the accent words with
     `*…*`. Test: from the title alone, a reader can guess what the slide shows.
   - **Don't repeat.** No stats or lines from the caption. No idea twice across
     images, or across earlier posts in the series. If an image repeats the
     previous one, merge its new points into that image and drop it.
   - **Link neighbours** (visual skill section 5 rule 8): a `from` cue on slides 2+,
     a `next` cue on every slide but the last. Use the same names, colours and objects for the
     same thing on every image.
   - **Takeaway slide last** (visual skill section 5 rule 9): one row per content
     slide (the section's `Takeaway:` line, word for word from the draft) plus
     `THE ONE THING`, the post's main takeaway. Content slides carry no takeaway box.
   - **Feed cover `0`** when there are 3+ images: the headline, a one-line subtitle, and a numbered
     "What we'll explore" list, one row per image (title + one grey line).
   - **daily.dev cover**: the series label, the `HEADLINE:` with its accent words, one small
     labelled motif for the main idea, and the footer topic. No second idea.
   - **Readable lines, not compressed notes** (visual skill section 5e). Every
     line, grey line and example is a simple phrase a reader understands on
     its own, without the post: keep the subject and the verb, say the "so
     what", and use no arrows, slashes or symbols in place of words.
     Examples are complete and concrete: real names, real numbers, what
     happens. Each line must be worth its space: drop a line that adds
     nothing, never the words that carry the meaning. An item fits on one or
     two lines at slide size. If it doesn't, split it into two items, move
     it to another slide or to the text, or change the layout. Never squeeze
     it into shorthand.
     Test: read each line aloud by itself. If a reader would ask "meaning
     what?", rewrite it.
5. **Write `posts/<post>/slides.md`** in this exact shape:
   ```
   # Slides spec: <Series #NN>: <headline>
   <one paragraph: this file is the source for the images; build-visuals rebuilds src/*.html from it>
   - Draft: <path> · LinkedIn PDF title: <carousel-title.txt text> · Render: ./render.sh variant-none
   ## Global rules        ← table: accent var + hex, theme tokens, series row, footer, cue rules, green/red meaning,
                            template per slide, title size + max-width, item format (`**Bold**: grey line`, split
                            at the first `: `), numbered-row style, colour of bold words inside mono lines
                            (ink unless "amber" is stated), default colours of intro/grey/reference lines
   ## cover: <title> (`src/cover.html` → `cover.png`, 1200×630)
   ## 0: Feed cover (`src/0.html` → `0.png`)
   ## N: <short title> (`src/N.html` → `N.png`)   ← one per slide, in posting order
   ```
   Each slide section lists, in reading order: `Template`, `From cue`, `Title`
   (with `*accent*`), every text element word for word (labels, items with their
   grey second line as `Bold: grey line`, code boxes in fenced blocks with their real
   line breaks), `Next cue`, `Footer right` (`N / total`). Add a `Layout:` line
   for the structure (rows, two panels, grid, which one is highlighted, green or
   red tint), and any size that matters. Every word that will appear on the image must be
   in this file. Nothing appears on an image that is not here.
   **Say every colour and style choice a builder would otherwise guess:** the colour
   of each bold or highlighted word, any lowercase or odd punctuation that is on
   purpose, and anything different from the Global rules defaults. Test: someone
   who never saw the old HTML could rebuild each slide from this file alone and
   get the same image. (Tested on growth-01 slide 4: the only difference was a
   bold colour the spec didn't state.)
6. Run `python3 scripts/build_posts.py <post>` if the folder doesn't exist yet,
   so `posts/<post>/` exists. Write `carousel-title.txt` if it is missing
   (≤ 60 characters, topic + what is inside).
7. **Show and stop.** Show the user `slides.md`: the path, then each slide's
   title with its items. Ask them to check it. Do not build HTML or images until
   they confirm. When they do (or when create-post runs with no review step),
   hand over to `build-visuals`.

## Rules

- `slides.md` is the source. HTML is built from it, never the other way.
  When the user wants a slide changed, change `slides.md` here, then run
  `build-visuals`.
- Big changes (a new section, a different point, a new takeaway) go into the
  draft first (`/improve-draft`), then into the slides. Small slide-only changes
  (shorter wording, layout) go straight into `slides.md`.
- Post rules still apply: work app framing ("the app", no product names), no
  "humans beat AI" claims, no unresolved `[PERSONAL]` / `[FACT_CHECK]` content on an image.
- Do not commit.
