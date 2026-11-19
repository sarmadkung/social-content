# Slides spec: Dev Growth #14: Pick the stack for performance, not familiarity

This file is the source for every image in this post: every word, in order, with its layout and colours.
`build-visuals` builds `src/*.html` from it and never changes the wording. To change a slide, edit this
file first, then rebuild.

- **Draft (full text source):** `generated/drafts/dev-growth/growth-14-pick-stack-for-performance.md`
- **LinkedIn PDF title** (`carousel-title.txt`): Choosing a stack with agents: performance, data, native
- **Render:** `./render.sh variant-none` → `0.png … 6.png`, `cover.png`, then `carousel.pdf`

## Global rules (every slide)

| Item | Value |
|---|---|
| Pillar / accent | Dev Growth · `:root{--accent:var(--grow)}` = amber `#FACC15` |
| Theme tokens | `templates/theme.css`: bg `#0A0C10`, panel `#11141B`, code `#0E1117`, line `#1F2530`, ink `#F2F5F9`, ink-2 `#9BA6B7`, ink-3 `#5E6977`, mono `"SF Mono",Menlo,monospace` |
| Series row (top) | `Dev Growth #14` + brand mark (`brand/truelogics-icon.svg` + `brand/truelogics-logo.svg`) on the right |
| Footer left | **Muhammad Sarmad** · Senior Software Engineer |
| Footer right | `swipe →` on slide 0; `N / 6` on slides 1–6; a short topic on the cover |
| Title | One plain question. The part in `*…*` below is the accent `<em>` (amber). Font size 56px on slides |
| "from" cue | Above the title on slides 2–6: `← from 0N: …` (mono, ink-3) |
| "next" cue | Above the footer on slides 1–5: `next → …` (mono, ink-3) |
| Good / costly colours | green `#4ADE80` = good / now; red `#F87171` = old way / costly (panel tint 8%, border 45%) |
| Takeaways | None on the content slides; all of them go on slide 6 |
| Templates | cover: `templates/cover/base.css` · 0: `templates/feed-cover/base.css` · slides 1–6: `templates/variant-b/base.css` |
| Title width | 56px, `max-width:20ch` unless a slide says otherwise |
| Item format | `**Bold**: grey line` = bold title (24px, ink) with a grey line under it (mono 16px, ink-2, line-height 1.4). The split is at the first `: ` after the bold. Later colons belong to the grey line |
| Numbered rows | Panel cards: panel background, 1px line border, radius 12–14px; amber number (mono 28px) in a ~52–56px left column |
| Bold inside a mono sentence | ink (white), weight 500. Amber only when the slide says "amber" |
| Default colours | Mono intro/caption lines: ink-2, centred. Grey lines: ink-2. References ("more in DEV GROWTH #NN"): ink-3 |

---

## cover: daily.dev cover (`src/cover.html` → `cover.png`, 1200×630)

- Template: `templates/cover/base.css`
- Title: Pick the stack for *performance, not familiarity*
- Motif (SVG, 340×250), caption at top in ink-3: "what decides the stack"
  - Two stacked boxes, top to bottom, with an amber `↓` between them:
    1. what the team already knows: red border `#F87171` at 45%, ink-2 text, red 8% tint
    2. **what the job needs to run well**: amber border + amber text (the highlighted box)
- Footer right: `choosing a stack with agents`

---

## 0: Feed cover (`src/0.html` → `0.png`)

- Template: `templates/feed-cover/base.css`. Overrides: h1 56px, max-width 22ch; sub in mono 20px ink-2; toc title 27px, toc line 19px
- Title: Pick the stack for *performance, not familiarity*
- Subtitle: We used to pick the language we knew, because writing code was the hard part. Agents now write the code. What the job needs to run well decides the stack.
- List label: **What we'll explore**
- Numbered list (bold question + one grey line under it):
  1. **What used to decide the stack?**: the four questions teams asked first, and which ones agents made cheap
  2. **Why do performance and native support matter more now?**: apps store more data and do more work, so slow code costs more
  3. **Which stack fits which job?**: seven jobs and the stack that fits each
  4. **What changes in a real job?**: a 2 GB nightly import that took 40 minutes, before and after
  5. **What do you still need to know?**: you still read, measure and run the code the agent writes
  6. **Takeaway: what to remember**: each slide's main point in one line
- Footer right: `swipe →`

---

## 1: What used to decide the stack? (`src/1.html` → `1.png`)

- Template: `templates/variant-b/base.css`
- From cue: none (first content slide)
- Title: What used to *decide the stack?*
- Intro line (mono 18px, ink-2, centred): the questions teams asked, **in this order**:
- Layout: four numbered rows, stacked. Each row: amber number | bold question (24px) with a grey line under it | a status tag on the right (mono 14px, uppercase, pill with 1px border, radius 999px)
  1. **What does the team already know?**: learning a new language took months · tag `AGENTS WRITE ANY LANGUAGE` (green text, green border)
  2. **How fast can we write it?**: writing the code was the slowest, most expensive part · tag `AGENTS WRITE IT FAST` (green text, green border)
  3. **Who can we hire for it?**: it was hard to hire people who knew a rare language · tag `MATTERS LESS NOW` (green text, green border)
  4. **How fast will it run?**: teams asked this last, or never asked it · tag `DID NOT CHANGE` (amber text, amber border)
- Row 4 is **highlighted**: amber 2px border, 9% amber tint, the question in amber
- Bottom line under the rows (mono 18px, ink-2, centred): agents write the code and a person reviews it, so the first three questions matter much less. **how fast it runs now decides the stack.** (all lowercase on purpose; the bold part is ink/white)
- Next cue: next → why performance matters more than it used to
- Footer right: `1 / 6`

---

## 2: Why do performance and native support matter more now? (`src/2.html` → `2.png`)

- From cue: ← from 01: how fast it runs is now the question
- Title: Why do performance and native support *matter more now?* (no max-width, 52px so it fits on two lines)
- Layout: five numbered rows, stacked (same row style as slide 1, no tags)
  1. **More data per user**: apps store messages, files, events and embeddings, and search all of them
  2. **More work per request**: one request may rank results, call an AI model, resize images and sync live
  3. **AI calls are already slow**: a model call can take seconds, so the rest of the request has no time to waste
  4. **The cloud bill follows CPU and memory**: say a runtime needs twice the memory per request: you pay for about twice the servers
  5. **Users feel it**: native apps start faster and scroll smoother (more in DEV GROWTH #13)
- Definition box under the rows (code background, 1px line border, radius 12px, amber left border 4px). Body 20px sans:
  - **Embeddings**: lists of numbers that capture what a piece of text means, so a search can find text with the same meaning.
  - **Example**: "cheap flights" and "low-cost airfare" get numbers that sit close together, so a search for one finds the other.
  - (The words "Embeddings" and "Example" are bold ink; the rest ink-2)
- Next cue: next → which stack fits which job
- Footer right: `2 / 6`

---

## 3: Which stack fits which job? (`src/3.html` → `3.png`)

- From cue: ← from 02: apps do more work on more data
- Title: Which stack fits *which job?*
- Definition line under the title (sans 20px, ink-2, left-aligned, max-width ~30ch per line, 2 lines): **Native**: code that runs straight on the machine or the OS, with no interpreter, embedded browser or framework layer in between. (bold word ink)
- Layout: a table of seven rows, three columns: `JOB` (bold 21px ink, ~250px) | `PICK` (mono 18px, amber, ~250px) | `WHY` (mono 15px, ink-2). Column labels in mono 13px uppercase ink-3. Rows separated by 1px line hairlines; rows 1–6 on panel background
  1. Heavy CPU work (parsing, images, video) | Rust, Go, C++ | compiled to machine code, so it runs fast and uses every CPU core
  2. Many open connections (chat, live updates) | Go, Rust, Elixir | keeps thousands of connections open at once, using little memory
  3. Big data queries | DuckDB, ClickHouse, Polars | stores data by column and works on many rows at once, not one at a time
  4. AI and ML | Python on top of native code | you write Python; PyTorch and NumPy run the heavy maths in C, C++ and CUDA
  5. Phone and desktop apps | Swift, Kotlin | uses the system's own UI and gets new OS features on day one
  6. Heavy work in the browser | WebAssembly, Web Workers | runs close to native performance without freezing the page
  7. Web UI, simple APIs, glue code | TypeScript | still a good pick: here the database or network is the slow part, not the language
- Row 7 has a **green tint** (8%, green border 45%) and its PICK text is green `#4ADE80`, not amber: it shows that a familiar stack is still the right pick for this job
- Next cue: next → one real job, before and after
- Footer right: `3 / 6`

---

## 4: What changes in a real job? (`src/4.html` → `4.png`)

- From cue: ← from 03: pick the stack per job
- Title: What changes in *a real job?*
- Top line (mono 20px, centred): the job: **import a customer's 2 GB CSV file every night**
- Layout: two panels side by side
  - **Left panel, red tint**, label `BEFORE · THE STACK WE KNEW`
    - Bold line: **Node.js reads one row at a time, on one thread**
    - Core diagram: a row of 8 small squares (36px, radius 6px) labelled `8 CPU cores` in ink-3 above them. Square 1 filled red 45% with the label `1 busy` under it; squares 2–8 grey outline `#3A4453` with one shared label `7 idle` under them
    - Bottom line (mono 18px): it takes about **40 minutes**, and longer with every new customer
  - **Right panel, green tint**, label `AFTER · THE ENGINE THE JOB NEEDS`
    - Item A: **Option A: DuckDB**: load the CSV into DuckDB and do the totals in SQL; it reads by column and uses every core
    - Item B: **Option B: Go or Rust**: the agent rewrites only the parser, with one worker on each CPU core
    - Core diagram: the same 8 squares, all 8 filled green 45%, label `all 8 busy` under them
    - Bottom line (mono 16px, ink-2): the rest of the app **stays in TypeScript**
- Strip under the panels (panel background, full width), label `YOUR PART` (mono 14px, amber), three numbered steps in a row (amber number + mono 16px ink text):
  1. Write the spec, with a time target: "a 2 GB file in under 5 minutes"
  2. Give the agent the test file the old version used
  3. Review the diff, then time both versions on a real 2 GB file
- Definition line under the strip (sans 19px, ink-2): **Hot path**: the small part of the code where most of the time goes. Here, the parser that reads the file. (bold word ink)
- Next cue: next → what you still need to know
- Footer right: `4 / 6`

---

## 5: What do you still need to know? (`src/5.html` → `5.png`)

- From cue: ← from 04: move only the hot path
- Title: What do you still *need to know?*
- Intro line (mono 18px, ink-2, centred): familiarity is not the reason to pick a stack. **you still have to own what ships:** (all lowercase on purpose; bold part ink)
- Layout: 2-column grid of four cards (bold title 24px + grey line mono 16px)
  1. **Read it**: review the agent's diff; you can't approve Rust you can't read (more in DEV GROWTH #10)
  2. **Measure it**: run a profiler and a benchmark on data as big as production, to see where the time goes
  3. **Run it**: deploy it, monitor it, debug it when it fails at 2 a.m.
  4. **Know what sits under every language**: memory, threads, disk and network I/O, and how data sits in memory: these carry over to every language (more in DEV GROWTH #07)
- Two stacked bars under the grid (full width, radius 12px), read from bottom to top:
  - Top bar, **green tint**: label `ON TOP OF THAT` (mono 14px, green) · text (22px bold ink): pick what the job needs, not the stack you're used to
  - Bottom bar, panel background, amber left border 4px: label `THE MINIMUM · DEV GROWTH #12` (mono 14px, amber) · text (22px bold ink): only pick tools you can review
- Next cue: next → what to remember from all of this
- Footer right: `5 / 6`

---

## 6: Takeaway: what to remember (`src/6.html` → `6.png`)

- From cue: ← from 05: read, measure and run it
- Title: Takeaway: *what to remember* (no max-width)
- Layout: five numbered rows. Each row has an amber number, then a small uppercase grey label (mono 14px), then the takeaway in bold (22px)
  1. `what used to decide the stack`: Writing code got cheap. Running it didn't.
  2. `why performance matters more now`: More data and more compute make the runtime a product decision.
  3. `which stack fits which job`: Pick per job, not one language for everything.
  4. `a real job`: Move the hot path to the right engine. Leave the rest alone.
  5. `what you still need to know`: You don't need years in a language. You need to read, measure and run it.
- Main box (amber left border, 9% amber tint), label `THE ONE THING` (mono 15px, amber), text 28px bold:
  Agents made code cheap to write, not cheap to run. Pick the stack for what the job needs, then learn enough of it to review, measure and run it.
- Next cue: none (last slide)
- Footer right: `6 / 6`
