# Dark Variant Catalogue

Identity is locked dark. Every variant shares these, and varies only layout:

- Ground `#0A0C10` · panel `#11141B` · border `#1F2530`
- Ink `#F2F5F9` / `#9BA6B7` / `#5E6977`
- Accent per pillar — see "Pillar accents" below; all colours live in `templates/theme.css`
- Correctness takes the card's own accent; green `#4ADE80` is the Software Engineering accent and the diff-mode `+`
- Sans (SF Pro) headline only, mono (SF Mono) for every label and number
- Footer lockup: name left, topic or complexity right, above a hairline
- 1080x1080 logical, rendered at 2x, diagram-first (never a quote card)

## Variant A — Blueprint

`templates/variant-a/` · output `visuals/renders/a-*.png`

Stacked and centred. Full-bleed 60px line grid at 28%, accent wash in the top-left
corner, accent rule before the series label. Title, then the diagram centred in the
remaining space, then one `→` takeaway line.

Diagram runs wide — horizontal rows, side-by-side panels.
Best for: comparisons, wide sequences, anything with two things to set beside each other.

## Variant B — Blueprint, gridless

`templates/variant-b/` · output `visuals/renders/b-*.png`

Variant A with the background line grid removed. Identical layout, type, spacing and
diagram treatment; only the 60px grid is gone. The corner accent wash stays, so the
canvas reads as plain dark rather than technical paper.

Best for: images whose diagram already carries a lot of ruled structure — dense cell
rows, bar charts, stacked blocks — where the grid behind it competes.

(The earlier asymmetric split layout is archived at `templates/_archived-split/`, unrendered.)

## Variant C — Terminal

`templates/variant-c/` · output `visuals/renders/c-*.png`

Series label and title as usual, then an editor window fills the rest: chrome bar with
three muted dots, a filename, and a pillar-coloured tag on the right. Inside, numbered
lines of real code, top-aligned like a real editor.

Syntax colour is deliberately thin — accent for keywords, tertiary ink for comments,
nothing else. The green left-bar highlight marks the correct line; strikethrough in
tertiary ink marks the line that is wrong, struck over the code only, never the indent.
No red: wrong is conveyed by the strike, so the image keeps one accent plus green.

Keep the body under about 12 lines. Empty space below it is fine — terminals have it.

Three content modes share the window, so C is not only for source code:

| Mode | Example | How it reads |
| --- | --- | --- |
| source | `c-01` `c-02` `c-03` | numbered gutter, keywords in accent |
| terminal | `c-04` bench · `c-06` eval run | no gutter, `$` prompt in accent, output rows |
| diff | `c-05` | no gutter, `-` struck, `+` green, `@@` note as comment |

Best for: a post whose whole argument is one line — a bug, a fix, a benchmark, a
regression in a table.

## Variant D — Board

`templates/variant-d/` · output `visuals/renders/d-*.png`

Series label and title as usual, then two bands: a **structure** on top and **three icon
points** underneath. No window, no grid — the objects sit on the bare canvas.

Structure vocabulary, pick one per image:

- **Flow** — boxes joined by `→`, each with a line icon, a name and a metric. The box
  that matters takes an accent border and accent metric (`d-02` latency, `d-03` RAG).
- **Shapes** — array cells with index labels, a stack tower, ghosted dashed boxes for
  popped or discarded items, green for the live top (`d-01` monotonic stack).

Icons are inline stroke SVG at 1.5–1.7, accent-coloured, in a tinted rounded square for
the points and bare inside flow nodes. No icon library, no filled glyphs, no emoji.

Points are always three: mono heading, two lines of body. More than three and the image
stops being readable at thumbnail size.

Best for: a pipeline, an architecture, a data structure in motion, or a post whose shape
is "one picture plus three things to know".

## Pillar accents (v5.2)

Five pillars, five hues, no sharing. Defined once in `templates/theme.css`. Correctness is no longer a colour: the right
answer takes the card's own accent (`--yes` resolves to `var(--accent)`), and the
wrong one is struck in tertiary ink. Only diff mode keeps green — `--add` — for `+`.

| Pillar | Accent | CSS var |
| --- | --- | --- |
| Problem solving | `#FFB86B` amber | `--dsa` |
| Software engineering | `#4ADE80` green | `--swe` |
| System design | `#C084FC` violet | `--arch` |
| AI engineering | `#8AA4FF` indigo | `--ai` |
| Dev growth | `#F2555F` crimson | `--grow` |

## Writing a post card

A post card is not a copy of a template — it *links* to one:

```html
<link rel="stylesheet" href="../../templates/variant-d/base.css">  <!-- imports ../theme.css -->
<style>:root{--accent:var(--arch)}</style>
```

Set `--accent` to the pillar's var and nothing else. Because the card references the
shared stylesheet, a fix to a variant re-renders every card built on it. `./render.sh`
renders `templates/` and every `visuals/week-*/` card.
