# Slides spec: Software Engineering · Stack #01: One default stack for every kind of app

This file is the source for every image in this post: every word, in order, with its layout and
colours. `build-visuals` builds `src/*.html` and the PNGs from it alone. To change a slide, edit
this file first, then rebuild. Never edit the text in the HTML.

- **Draft (full text source):** `generated/drafts/software-engineering/stack/stack-01-default-stack-per-app.md`
- **LinkedIn PDF title** (`carousel-title.txt`): Default tech stacks for 7 kinds of apps, in one map
- **Render:** `./render.sh variant-none` → `0.png … 5.png`, `cover.png`, then `carousel.pdf`

## Global rules (every slide)

| Item | Value |
|---|---|
| Pillar / accent | Software Engineering · `:root{--accent:var(--swe)}` = green `#4ADE80` |
| Theme tokens | `templates/theme.css`: bg `#0A0C10`, panel `#11141B`, code `#0E1117`, line `#1F2530`, ink `#F2F5F9`, ink-2 `#9BA6B7`, ink-3 `#5E6977`, mono `"SF Mono",Menlo,monospace` |
| Series row (top) | `Software Engineering · Stack #01` + brand mark (`brand/truelogics-icon.svg` + `brand/truelogics-logo.svg`) on the right |
| Footer left | **Muhammad Sarmad** · Senior Software Engineer |
| Footer right | `swipe →` on slide 0; `N / 5` on slides 1–5; a short topic on the cover |
| Title | One plain question. The part in `*…*` is the accent `<em>` (green). 56px, `max-width:20ch` unless a slide says otherwise |
| "from" cue | Above the title on slides 2–5: `← from 0N: …` (ink-3, mono 16px) |
| "next" cue | Above the footer on slides 1–4: `next → …` (ink-3, mono 16px) |
| Good / costly colours | green `#4ADE80` = the default pick; red `#F87171` = the usual wrong pick (panel tint 8%, border 45%). Green is also the pillar accent here: that is fine, because on these slides green always means "the default" |
| Takeaways | None on the content slides; all of them go on slide 5 |
| Templates | cover: `templates/cover/base.css` · 0: `templates/feed-cover/base.css` · slides 1–5: `templates/variant-b/base.css` |
| Stack row (slides 1–3) | One panel card per row (panel bg, 1px line border, radius 14px), three columns: **job** (220px: bold 24px ink name + grey mono 15px line under it) · **default** (green label `DEFAULT` mono 13px, then the pick in bold 22px ink, then the reason in mono 15px ink-2) · **else** (240px, left hairline: ink-3 label `PICK SOMETHING ELSE WHEN` mono 13px, then mono 15px ink-2 lines; the tool name after `→` is ink, weight 500) |
| Item format | `**Bold**: grey line` = bold title with a grey line under it. Split at the first `: ` after the bold |
| Bold inside a mono sentence | ink (white), weight 500. Green only when the slide says "green" |
| Default colours | Intro lines: mono 18px, ink-2, centred. References ("more in …"): ink-3 |

---

## cover: daily.dev cover (`src/cover.html` → `cover.png`, 1200×630)

- Template: `templates/cover/base.css`
- Title: One default stack for *every kind of app*
- Motif (SVG or HTML, about 340×250), caption at top in ink-3: "start from a default"
  - Four small rows, each `job → pick`, job in ink-2, `→` in ink-3, pick in ink:
    1. web → TypeScript + React
    2. API → Go + Postgres
    3. mobile → Swift + Kotlin
    4. AI → model API + pgvector
  - Row 2 is the highlighted one: green 2px border, green 9% tint, pick in green
- Footer right: `default tech stacks`

---

## 0: Feed cover (`src/0.html` → `0.png`)

- Template: `templates/feed-cover/base.css`. Overrides: h1 56px, max-width 22ch; sub in mono 20px ink-2; toc title 27px, toc line 19px
- Title: One default stack for *every kind of app*
- Subtitle: A web app, an API, two mobile apps, an AI assistant and a dashboard. Start each part from a default, and know when to leave it.
- List label: **What we'll explore**
- Numbered list (bold question + one grey line under it):
  1. **Which stack for web, mobile and desktop?**: the parts users see and touch
  2. **Which stack for the backend and data?**: APIs, app data and analytics
  3. **Which stack for AI and blockchain?**: model features and smart contracts
  4. **Where does the usual pick hurt?**: six wrong picks and what they cost
  5. **Takeaway: what to remember**: every point in one line
- Footer right: `swipe →`

---

## 1: Which stack for web, mobile and desktop? (`src/1.html` → `1.png`)

- Template: `templates/variant-b/base.css`
- From cue: none (first content slide)
- Title: Which stack for *web, mobile and desktop?*
- Intro line: my defaults in 2026: opinions with reasons, not rules
- Layout: three stack rows (see Global rules), top to bottom
  1. Job: **Web app**: SaaS, dashboards
     - Default: **TypeScript + React (Next.js) + Postgres**
     - Why: one language for UI and server, the biggest library and hiring pool
     - Else: mostly content (blog, docs) → **Astro**
  2. Job: **Mobile app**: iOS and Android
     - Default: **Swift (SwiftUI) + Kotlin (Compose)**
     - Why: new OS features on day one, no extra layer between code and phone
     - Else: simple screens, tiny team, no hardware work → **React Native or Flutter**
  3. Job: **Desktop app**: macOS, Windows, Linux
     - Default: **Tauri (Rust core + web UI)**
     - Why: uses the OS's own web view, so the installer is a few MB
     - Else: same rendering everywhere or Node.js libraries → **Electron**
- Reference line under the rows (mono 15px, ink-3, centred): more in WEB #01 and MOBILE #01
- Next cue: next → what runs behind the app
- Footer right: `1 / 5`

---

## 2: Which stack for the backend and data? (`src/2.html` → `2.png`)

- From cue: ← from 01: the parts users see
- Title: Which stack for *the backend and data?*
- Layout: three stack rows (same format as slide 1)
  1. Job: **API and services**: the server code
     - Default: **Go + Postgres**
     - Why: one small binary, cheap concurrency, low memory, easy to review
     - Else: a CPU-heavy hot path → **Rust for that part**; simple CRUD, all-TypeScript team → **Node.js**
  2. Job: **App data**: users, orders, settings
     - Default: **Postgres**
     - Why: transactions, joins, JSON and full-text search in one database
     - Else: a measured pattern Postgres can't serve, like huge key-value → **DynamoDB**
  3. Job: **Analytics**: reports and dashboards
     - Default: **ClickHouse, or DuckDB for files**
     - Why: reads only the columns a query needs, on every core
     - Else: a few million rows → **a Postgres read replica**
- Reference line (mono 15px, ink-3, centred): more in BACKEND #01 and #02
- Next cue: next → AI features and smart contracts
- Footer right: `2 / 5`

---

## 3: Which stack for AI and blockchain? (`src/3.html` → `3.png`)

- From cue: ← from 02: Go and Postgres behind the app
- Title: Which stack for *AI and blockchain?*
- Layout: two stack rows (same format as slide 1, rows taller), then one definition box
  1. Job: **AI features**: chat, search, agents
     - Default: **Model API + your backend + Postgres with pgvector + evals**
     - Why: most AI features are calls, context and evals, not training
     - Else: you train or fine-tune → **Python (PyTorch)**; tens of millions of vectors → **a vector database**
  2. Job: **Smart contracts**: tokens, payments, access rules
     - Default: **Solidity + Foundry + viem (EVM chains)**
     - Why: the most auditors, tools and audited libraries (OpenZeppelin)
     - Else: building on Solana for speed and low fees → **Rust + Anchor**
- Definition box (panel bg, 1px line border, radius 12px; sans 20px ink; the word `Embedding` bold):
  - **Embedding**: a list of numbers that captures what a text means, so similar texts get similar numbers.
  - Example: "refund my order" and "I want my money back" get close numbers, so a search for one finds the other.
- Next cue: next → where the usual pick hurts
- Footer right: `3 / 5`

---

## 4: Where does the usual pick hurt? (`src/4.html` → `4.png`)

- From cue: ← from 03: AI reuses your stack
- Title: Where does *the usual pick hurt?*
- Intro line: numbers are illustrative
- Layout: six rows, top to bottom. Each row is one red-tinted card (red 8% tint, red border 45%) with three columns: **the usual pick** (bold 20px ink, 260px) · **what happens** (mono 15px ink-2) · **default instead** (180px, small green label `INSTEAD` mono 12px, then the pick in mono 15px green)
  1. **Cross-platform for a hardware-heavy app** · camera, Bluetooth and widgets need native modules anyway: now three languages · instead: Swift + Kotlin
  2. **Electron for a tray utility** · say a 150 MB download and 200 MB of RAM to show a menu · instead: Tauri
  3. **Rust for a CRUD API** · it waits on the database 90% of the time: slower to change, fewer reviewers · instead: Go
  4. **Dashboards on the main Postgres** · a 90-day revenue query scans 50M rows and slows checkout · instead: ClickHouse
  5. **A vector database on day one** · 50,000 docs in a second store: a deleted contract still shows up in answers · instead: pgvector
  6. **Your own token contract** · one missed check and funds are lost; deployed code can't be patched like a server · instead: OpenZeppelin
- Next cue: next → what to remember
- Footer right: `4 / 5`

---

## 5: Takeaway: what to remember (`src/5.html` → `5.png`)

- From cue: ← from 04: the wrong pick fails later
- Title: Takeaway: *what to remember* (no max-width)
- Layout: four numbered rows. Each row has a green number (mono 28px), then a small uppercase grey label (mono 14px), then the takeaway in bold (22px, ink)
  1. `web, mobile and desktop`: The product side goes native where users feel it, web where reach matters.
  2. `backend and data`: Go and Postgres cover most backends. Add engines only for a measured need.
  3. `AI and blockchain`: AI reuses your stack. Blockchain needs audited tools, because deployed bugs stay.
  4. `where the usual pick hurts`: The wrong pick rarely fails on day one. It fails at scale or in review.
- Main box (green 4px left border, 9% green tint), label `THE ONE THING` (mono 15px, green), text 28px bold:
  Start every part of the app from a default you can defend, and know the one signal that would make you leave it.
- Next cue: none (last slide)
- Footer right: `5 / 5`
