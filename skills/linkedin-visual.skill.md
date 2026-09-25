---
name: linkedin-visual
description: Use when generating any LinkedIn image, carousel, or code graphic for Muhammad Sarmad — renders the image directly, locking one dark visual identity and varying only the pillar accent and the rendering variant.
version: 5.2
owner: Muhammad Sarmad
works-with: any (Claude, ChatGPT, Gemini, local, any HTML renderer)
---

# LinkedIn Visual System Skill

The visual half of the LinkedIn system. `linkedin-content.skill.md` decides what
a post says; this decides what it looks like. Use both together.

## Use this when

- Generating a post image, cover, or code graphic.
- Generating a carousel (multi-slide) deck.
- Reviewing a generated image for brand consistency.
- Building an HTML/CSS template that renders post images.

## Do not use this when

- Writing post copy only, with no image — use `linkedin-content.skill.md`.
- Designing a product UI, a site, or a slide deck for a talk. This system is
  tuned for a 200px-wide thumbnail in a feed, and nothing else.

## Output format

When asked for an image, return:

1. Self-contained HTML/CSS that renders it, or the rendered PNG.
2. A one-line note naming the pillar, the accent hex, and the variant used.
3. The headline text as plain text, so it can be checked against the word limit.

---

## 0. Request keywords

The request keywords — `COPY`, `VISUAL`, `FULL` — are defined once, in
`linkedin-content.skill.md` section 0. For this skill: `VISUAL` returns the image
(the HTML/CSS that renders it, or the rendered PNG) and nothing else; `FULL`
returns the post text first, then the image. There is no separate HTML keyword —
HTML is how every image is made (section 0b).

`VISUAL` still needs a headline — if the request has no post text to draw the
headline from, ask for it rather than inventing one.

## 0b. How to produce the image

**Write HTML and CSS, then screenshot it.** This system draws real diagrams,
real code and real numbers, and an image model cannot be trusted with any of
them — it will produce plausible-looking nonsense code, invented axis labels and
misspelled headlines. HTML is the system, not a fallback.

Render at 1080×1080 logical pixels, screenshotted at 2× (2160×2160) so mono type
stays crisp. Headless Chrome does this in one command:

```
chrome --headless --force-device-scale-factor=2 --window-size=1080,1080 \
       --screenshot=out.png file://card.html
```

Use system fonts only — `-apple-system`/`SF Pro Display` for the headline,
`SF Mono`/`Menlo` for everything else — so a card renders identically with no
network access.

If no renderer is available at all, say so and return the HTML. Do not
substitute an image model and do not describe the picture in words.

## 1. The governing rule

**One identity, one variable, four variants.**

Five pillars must not mean five designs. Five designs means no recognizable
design, and a reader scrolling a feed never builds recall. Section 2 is fixed
forever. What changes per post is the accent colour and the variant — and the
variant is chosen by the content's shape, never at random.

If a request asks to change a locked element for a single post, refuse and
offer the accent or the variant as the place to express the difference.

## 1a. The variants

All four share section 2 exactly. They differ only in how the middle of the
canvas is arranged.

| Variant | Name | Middle of the canvas | Reach for it when |
| --- | --- | --- | --- |
| **A** | Blueprint | Stacked and centred on a 60px line grid at 28% opacity. Diagram runs wide. | A comparison, a wide sequence, two things set side by side. |
| **B** | Blueprint, gridless | Variant A with the background grid removed. | The diagram already has heavy ruled structure — dense cells, bars, stacked blocks — and the grid competes. |
| **C** | Terminal | An editor window fills the lower canvas: chrome bar with three muted dots, a filename, an accent tag. | The whole argument is one line — of code, of output, or of a diff. |
| **D** | Board | A structure band (flow of icon nodes, or shapes) over exactly three icon points. | A pipeline, an architecture, a data structure in motion, or "one picture plus three things to know". |

**Variant C has three content modes**, all inside the same window:

| Mode | Shows | Treatment |
| --- | --- | --- |
| source | a function, a loop | numbered gutter, keywords in accent |
| terminal | a benchmark, an eval run, a log | no gutter, `$` prompt in accent, output rows |
| diff | a fix, a migration | no gutter, `-` struck in tertiary, `+` in green |

**Variant D has two structure forms**, one per image:

- **Flow** — boxes joined by `→`, each with a line icon, a name and a metric.
  The box that matters takes the accent border and accent metric.
- **Shapes** — array cells with index labels, a stack tower, ghosted dashed
  boxes for popped or discarded items, green for the live top.

D's points are always three: mono heading, two lines of body. More than three
and the image stops being readable at thumbnail size.

## 1b. Layout routing — the content picks the arrangement

Read the content's shape first, then pick. The pillar colours never change.

**STATEMENT** — one idea, ≤8-word headline, one diagram or code block. Variant
A, B or C.

**COMPARE** — two panels, naive on the left, better on the right with the accent
border. One shared line underneath names what was *spent*, not just what was
gained. Variant A (side by side) or C (diff mode).

**FLOW** — one chain of steps. Horizontal when ≤5 steps; vertical when 5+ and
each step needs a sentence. A loop-back is a dashed panel under the chain, not a
curved arrow — curved arrows across a flex row do not survive rendering.
Variant D, flow form.

**ANATOMY** — one subject taken apart: a structure, then labelled points.
Variant D.

**STAT** — one very large mono number in the ink colour, its unit beside the
baseline, up to three supporting tiles, one closing line. The number must be
real and checkable. Variant B.

**GRID** — a title band, then N equal cards (4 → 2×2, 6 → 3×2, 9 → 3×3), each
with a number, a name, a small diagram and a 4–8 word caption. Variant B.

### Block vocabulary

Every diagram is assembled from these. Do not invent new primitives; combine
these instead.

- `box` — a labelled rounded rectangle. The `hero` variant takes the accent
  border and accent fill, and marks the one step that matters.
- `cells` — a row of array cells with index labels beneath; the active cell
  takes the accent.
- `stack` — a vertical tower; ghosted dashed boxes are popped, green is the
  live top.
- `arrow` — `→`, always left to right or top to bottom.
- `fan` — two or three boxes stacked after one arrow, for a branch. Each branch
  row carries its own continuation — never run one arrow out of a whole fan.
- `bars` — a bar chart with a labelled baseline and a named peak.
- `point` — an icon tile, a mono heading and two lines of body.

Rules: at most 6 blocks in one diagram; never two hero boxes; labels are 1–3
words; every chart has a scale.

## 2. Locked elements — never vary these

**Canvas**

| Use | Size | Notes |
| --- | --- | --- |
| Feed image | 1080 × 1080 @2× | Default. Square wins the most feed height. |
| Carousel slide | 1080 × 1350 @2× | 4:5, exported as PDF for LinkedIn documents. |

Padding: 68–76px on all sides. Nothing but the background crosses it.

**Surface — dark, one ground for every pillar**

| Use | Hex |
| --- | --- |
| Ground | `#0A0C10` |
| Panel / card | `#11141B` |
| Code panel | `#0E1117` |
| Window chrome | `#141821` |
| Border, hairline | `#1F2530` |
| Primary ink | `#F2F5F9` |
| Secondary ink | `#9BA6B7` |
| Tertiary ink | `#5E6977` |

A soft radial wash of the pillar accent sits in the top-left corner at about
12–13% and fades by 60%. That wash is the only place the accent touches the
background. There is no left-edge rule and no full-bleed tint.

**Correctness is marked structurally, not by colour.** The right answer, the
fixed line, the "after" state — all take the card's own accent: a raised row with
an accent left-bar. The wrong one is struck through in tertiary ink. No colour is
reserved for "good", which is what frees green to be a pillar.

Two consequences worth stating, because they are easy to get wrong:

- On a card whose accent marks a *problem* — a bottleneck, an outage, a slow
  query — the accent is still correct usage. It marks the thing to look at, not
  the thing to approve of. Muted grey `#3A4453` marks the losing side of a
  comparison; the accent marks the side that matters.
- **Diff mode is the one exception.** Inside variant C's diff mode, `+` keeps the
  universal green `#4ADE80` and `−` stays struck, whatever the pillar accent is.
  The plus/minus convention is older and stronger than this brand, and a crimson
  `+` would read as a deletion.

**Type**

- Headline: `-apple-system`, `SF Pro Display`. 50–58px, line-height 1.1,
  letter-spacing −0.022em, weight 700. Max 19 characters per line.
- Everything else: `SF Mono`, `Menlo` — series label, all diagram labels, the
  takeaway line, the footer. The sans/mono split is the brand signature: the
  headline is human, the data is machine.
- Nothing smaller than 15px at 1080 width.

**Furniture, in this order, on every card**

1. Series label — mono, 18–19px, uppercase, 0.20–0.22em tracking, accent, after
   a 32px accent rule.
2. Headline — sans, with the phrase carrying the argument in the accent. Colour
   the phrase that makes the point, never a random noun.
3. The middle — per the variant.
4. Footer — hairline rule, then `Muhammad Sarmad · Senior Software Engineer`
   left and the topic or complexity right, mono, tertiary ink.

## 3. The one variable — pillar accent

The hexes below live in one file, `templates/theme.css`; every variant imports it.
Change a colour there, never in a variant's `base.css`.

| Pillar (from the content skill) | Tag text | Accent |
| --- | --- | --- |
| Problem solving | `DSA SERIES` | `#FFB86B` amber |
| Software engineering | `SOFTWARE ENGINEERING` | `#4ADE80` green |
| System design | `SYSTEM ARCHITECTURE` | `#C084FC` violet |
| AI engineering | `AI ENGINEERING` | `#8AA4FF` indigo |
| Dev growth | `DEV GROWTH` | `#F2555F` crimson |

One accent per pillar, five pillars, no sharing. If a sixth pillar ever appears it
gets its own hue — never a second pillar on an existing accent, which is what makes
two different posts look like the same series.

The accent appears in exactly five places, and nowhere else:

1. The corner wash, at 12–13%.
2. The series rule and series label.
3. The one phrase in the headline that carries the argument.
4. The hero element of the diagram — one border, one metric, one keyword set.
5. Icon strokes and icon tiles in variant D.

Never use the accent as a gradient, and never give one card two accents.

## 4. Content rules for the image itself

1. **Draw the mechanism, not a quote.** A pull-quote on a dark background
   teaches nothing. Before designing, answer: *what should a reader understand
   from this image with the caption collapsed?* If the answer is "that the post
   sounds smart", start over.
2. The image carries **one** idea. The headline is 8 words or fewer.
3. Never put a paragraph on an image. If it needs a paragraph, it needs a
   carousel.
4. Code and terminal bodies: **12 lines maximum**. Keywords in accent,
   comments in tertiary, nothing else — never full multi-colour syntax
   highlighting, which destroys the identity.
5. One visual per image: a diagram, *or* a window, *or* a structure band with
   points. Never two.
6. **Every number must be defensible.** If a chart says 240 rps, it must
   reconcile with the other numbers on the card. Invented figures destroy the
   credibility the content is built on. Label every axis and unit.
7. Greyed-out or struck-through text must still be readable, or the point lands
   as a rendering bug.
8. No stock photography, no 3D renders, no AI-generated illustration, no emoji
   on the canvas. Icons are inline stroke SVG at 1.5–1.7 weight — no icon
   library, no filled glyphs.
9. No drop shadows, no glows, no glassmorphism, no gradient meshes. One focus
   ring at most, the hairline colour for separation.

## 5. Carousel rules

1. 6–10 slides. Below 6 it should have been a single image; above 10 it is an
   article.
2. Slide 1 is the cover: series label, headline, name lockup, nothing else.
3. Slides 2..n−1 each carry exactly one point, with the point as a 56px
   headline at top and supporting detail below.
4. One variant for the whole deck. Mixing variants inside a carousel breaks it.
5. Slide numbers in tertiary ink, bottom-right, `03 / 08` format.
6. Final slide is a single question or takeaway plus the name lockup. No
   "follow me" graphics, no like-and-share instructions.

## 6. Review checklist

Before returning any image, verify each:

1. Headline is 8 words or fewer.
2. Ground is `#0A0C10`; no light variant slipped in.
3. Exactly one accent on the canvas, and green only where it means correct.
4. The accent appears in no more than the five permitted places.
5. Name lockup bottom-left, topic or complexity bottom-right, above a hairline.
6. Every number on the card reconciles with every other number on the card.
7. Nothing crosses the padding.
8. Legible when the image is scaled to 200px wide — check by shrinking it.
9. Code or terminal body is 12 lines or fewer.
10. Whitespace is balanced between headline and footer — a void at the bottom
    means the diagram is too small, not the padding too large.

## 7. Examples

Illustrative only — these describe the template cards in `templates/variant-*/`,
whose series labels read `· Example`. They are not posts in the queue; real posts
live in `generated/drafts/` and their cards in `visuals/week-*/`.

**Variant A, problem solving.** Series `DSA SERIES #03`. Headline "Binary search
is not about *sorted arrays*", the last two words amber. Thirteen cells labelled
1–13: the first six read NO in tertiary, the rest YES in the amber accent, cell 7
ringed in amber with a tick reading "the flip — first YES is the answer". Takeaway:
nothing here is sorted — you are searching the answer space. Footer right:
`O(n log R)`.

**Variant C, terminal mode, AI engineering.** Series `AI ENGINEERING #04`.
Headline "The prompt got better. Something else got *worse.*" Window titled
`evals — zsh`, tag `120 CASES`. A `$ eval run --suite all --vs main` prompt, then
a four-row table; the improved rows stay in plain ink, and the regressed
`tool-calling 20 61% -23` row is marked in the indigo accent. Closing line
`overall 86% (+2) — ship? no.`

**Variant D, flow, software engineering.** Series `SOFTWARE ENGINEERING #03`.
Headline "You optimised the code. The time was *never there.*" Four nodes —
client 12 ms, CDN 8 ms, API 31 ms, postgres 240 ms — the last with the green
accent border and accent metric. Three points beneath: measure first, p99 not average,
usually an N+1. Footer right: `291 ms total`.

