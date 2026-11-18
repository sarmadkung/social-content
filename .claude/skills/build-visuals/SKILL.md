---
name: build-visuals
description: Build a post's images from its slides spec: posts/<post>/slides.md → src/*.html → PNGs → carousel.pdf and the daily.dev cover, without changing any wording. Use when the user types /build-visuals, or says "build the visuals", "render the slides", "generate the images from the slides", "regenerate visuals", "re-render", or when write-slides is confirmed inside create-post. Not for changing what a slide says (use write-slides).
---

# Build the visuals (`slides.md` → HTML → PNG → PDF)

Turns `posts/<post>/slides.md` into the post's images. The words come only
from `slides.md`. This skill decides how the slides look (HTML, CSS, sizes,
spacing) and never what they say.

## Input

`/build-visuals <post> [slide N …]`: a draft basename or series + number;
optionally only some slides.

## Steps

1. Read `posts/<post>/slides.md`. If it is missing, stop and run `write-slides`
   first. Never build slides from the draft directly.
2. **Regenerate = re-render.** If the user asked to regenerate or re-render and
   `src/*.html` already match `slides.md` (`python3 scripts/validate.py`
   shows no "text not in slides.md" error for this post), skip to step 5.
3. Read `skills/linkedin-visual.skill.md` (sections 5–5d and the review
   checklist), `templates/theme.css` and the base CSS of every template
   `slides.md` names. Look at one existing post's `src/*.html` for the markup
   pattern (e.g. `posts/growth-01-hand-written-code-new-assembly/src/`).
4. **Write the HTML**, one file per slide section: `src/cover.html`,
   `src/0.html`, `src/1.html` … (carousel: `src/slide-01.html` …). Remove any old
   `src/` file that `slides.md` no longer lists.
   - Link `../../../templates/<template>/base.css` and the brand files under
     `../../../brand/`. Set `:root{--accent:var(--<pillar>)}` as `slides.md`'s
     Global rules say.
   - Use the text exactly as written: same words, order, case and punctuation.
     `*accent*` in a title becomes `<em>`. `**bold**` becomes `<b>`. Code blocks
     keep their line breaks (`white-space:pre` or `<br>`).
   - Follow every `Layout:` note: rows, panels, grids, highlighted rows, green
     (`#4ADE80`, good/now) and red (`#F87171`, old/costly) tints.
5. **Render:** `./render.sh variant-none`. It renders post images to
   `posts/<post>/*.png` and `cover.png`, then builds `carousel.pdf` with
   `scripts/carousel_pdf.sh`. After a render by hand, run
   `scripts/carousel_pdf.sh posts/<post>`.
6. **Check every PNG** (open it) against the visual skill's review checklist:
   nothing cut off or overlapping, text readable at phone size, the cover readable at
   300px wide, cues and footers right. Fix layout problems in the HTML/CSS
   (sizes, spacing, columns) and re-render.
   **If text does not fit even after layout fixes, stop.** Name the slide and
   the item, and propose shorter wording for `slides.md`. Never shorten or
   reword text in the HTML yourself.
7. Run `python3 scripts/validate.py`. There must be no "text not in slides.md"
   error for this post. If there is one, the HTML drifted: fix the HTML to match
   `slides.md`, never the other way round.
8. Reply with: the PNGs built, `carousel.pdf`, `cover.png`, any wording you
   propose to change in `slides.md`, and the PDF title on its own line, labelled
   `LinkedIn PDF title:` (from `carousel-title.txt`). PNGs and `carousel.pdf`
   are build output: never commit them. Do not commit.
