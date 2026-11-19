# Slides spec: Dev Growth #01: Writing code by hand is the new assembly

This file lists every image in this post: every word, in order, with its layout and colours.
It matches `src/*.html` word for word. Rebuild the HTML from this file, or edit this file
first and then the HTML. When either one changes, update the other so they match.

- **Draft (full text source):** `generated/drafts/dev-growth/growth-01-hand-written-code-new-assembly.md`
- **LinkedIn PDF title** (`carousel-title.txt`): Hand-written code as the new assembly, in 5 visuals
- **Render:** `./render.sh variant-none` → `0.png … 6.png`, `cover.png`, then `carousel.pdf`

## Global rules (every slide)

| Item | Value |
|---|---|
| Pillar / accent | Dev Growth · `:root{--accent:var(--grow)}` = amber `#FACC15` |
| Theme tokens | `templates/theme.css`: bg `#0A0C10`, panel `#11141B`, code `#0E1117`, line `#1F2530`, ink `#F2F5F9`, ink-2 `#9BA6B7`, ink-3 `#5E6977`, mono `"SF Mono",Menlo,monospace` |
| Series row (top) | `Dev Growth #01` + brand mark (`brand/truelogics-icon.svg` + `brand/truelogics-logo.svg`) on the right |
| Footer left | **Muhammad Sarmad** · Senior Software Engineer |
| Footer right | `swipe →` on slide 0; `N / 6` on slides 1–6; a short topic on the cover |
| Title | One plain question. The part in `*…*` below is the accent `<em>` (amber). Font size 56px on slides |
| "from" cue | Above the title on slides 2–6: `← from 0N: …` |
| "next" cue | Above the footer on slides 1–5: `next → …` |
| Good / costly colours | green `#4ADE80` = good / now; red `#F87171` = old way / costly (panel tint 8%, border 45%) |
| Takeaways | None on the content slides; all of them go on slide 6 |
| Templates | cover: `templates/cover/base.css` · 0: `templates/feed-cover/base.css` · slides 1–6: `templates/variant-b/base.css` |
| Title width | 56px, `max-width:20ch` unless a slide says otherwise |
| Item format | `**Bold**: grey line` = bold title (24px, ink) with a grey line under it (mono, ink-2, line-height 1.4). The split is at the first `: ` after the bold. Later colons belong to the grey line |
| Numbered rows | Panel cards: panel background, 1px line border, radius 12–14px; amber number (mono) in a ~52–56px left column |
| Bold inside a mono sentence | ink (white), weight 500. Amber only when the slide says "amber" |
| Default colours | Mono intro/caption lines: ink-2, centred. Grey lines: ink-2. References ("coming in …"): ink-3 |

---

## cover: daily.dev cover (`src/cover.html` → `cover.png`, 1200×630)

- Template: `templates/cover/base.css`
- Title: Writing code by hand is *the new assembly*
- Motif (SVG, 340×250), caption at top in ink-3: "the level we work at moves up"
  - Three stacked boxes, top to bottom, with a `↑` between each:
    1. **agents write the code**: amber border + amber text (the highlighted level)
    2. you type the code: grey border `#3A4453`, ink text
    3. assembly: grey border, ink-2 text
- Footer right: `agents and hand-written code`

---

## 0: Feed cover (`src/0.html` → `0.png`)

- Template: `templates/feed-cover/base.css`. Overrides: h1 56px, max-width 22ch; sub in mono 20px ink-2; toc title 27px, toc line 19px
- Title: Writing code by hand is *the new assembly*
- Subtitle: In 1999, a hit PC game was written almost entirely in assembly. Today almost nobody writes a whole app that way. Hand-written code is heading the same way.
- List label: **What we'll explore**
- Numbered list (bold question + one grey line under it):
  1. **How has the level we write code at moved up?**: machine code → assembly → languages → agents
  2. **What changes in a normal day?**: one feature, before and after agents
  3. **Where does the comparison break?**: a compiler you trust, an agent you check
  4. **What do we still write by hand?**: the five places it still pays off
  5. **Which skills matter more now?**: less typing, more judgment
  6. **Takeaway: what to remember**: every point in one line
- Footer right: `swipe →`

---

## 1: How has the level moved up? (`src/1.html` → `1.png`)

- Template: `templates/variant-b/base.css`
- From cue: none (first content slide)
- Title: How has the level we write code at *moved up?* (no max-width)
- Layout: four rows stacked from top to bottom with a small grey `↑ …` line between each row. Each row has 3 columns: name (200px) | description (mono 16px, ink-2) | code box (300px, mono 15px, code background, keeps line breaks)
  - Row 1, **highlighted** (amber 2px border, 9% amber tint, amber name):
    - **Agents** | you describe the rules and tests; the agent writes the code | code:
      ```
      "Mute a chat for 8 hours.
      Test: hour 9 notifies."
      ```
  - `↑ hides the code itself`
  - Row 2: **High-level languages** | C, Java, Python: a compiler turns readable code into instructions | `total = price + tax;`
  - `↑ hides registers`
  - Row 3: **Assembly** | short names for CPU instructions; you manage registers, the CPU's few tiny fast storage slots | code:
    ```
    MOV eax, [price]
    ADD eax, [tax]
    ```
  - `↑ hides raw numbers`
  - Row 4: **Machine code** | the raw numbers the CPU runs | `8B 45 F8 03 45 FC`
- Next cue: next → what this looks like in a normal day
- Footer right: `1 / 6`

---

## 2: What changes in a normal day? (`src/2.html` → `2.png`)

- From cue: ← from 01: agents are the new level
- Title: What changes in *a normal day?* (max-width 20ch)
- Top line (mono 20px, centred): one feature: **"users can mute a chat for 8 hours"**
- Layout: two panels side by side
  - **Left panel, red tint**, label `BEFORE · YOU TYPE IT`. Items (bold line + small grey line):
    1. The data change: store when the mute ends
    2. The API endpoint: mute and unmute a chat
    3. The UI toggle: the mute switch and its menu
    4. The tests: every rule, by hand
    - Bottom line: **~300 lines** · most of a day
  - **Right panel, green tint**, label `NOW · YOU SAY WHAT IT MUST DO`
    - Spec box (mono 16px, code background), three lines:
      - → A mute lasts 8 hours, then turns off by itself.
      - → Muted chats send no notifications, but still show unread counts.
      - → Test: a message at hour 7 is silent; at hour 9 it notifies.
    - Items:
      1. The agent writes the code: the same ~300 lines
      2. You read the diff and run the tests: then fix what is wrong
- Next cue: next → an agent is not a compiler
- Footer right: `2 / 6`

---

## 3: Where does the comparison break? (`src/3.html` → `3.png`)

- From cue: ← from 02: the agent writes the 300 lines
- Title: Where does *the comparison break?*
- Layout: two panels side by side, each with: label, big title (30px), 3 items, then a bottom line under a thin border
  - **Left panel, green tint**, label `COMPILER · C → ASSEMBLY`, title **Fixed rules**
    1. Same input, same output: every time, on every run
    2. Almost never the bug: proven over decades of use
    3. You rarely read its output: most developers never read the machine code
    - Bottom: so you **trust** the output (*trust* in green)
  - **Right panel, red tint**, label `AGENT · REQUEST → CODE`, title **A best guess**
    1. Same request, different code: it can change on every run
    2. Can be confidently wrong: the code looks right and still breaks a rule
    3. You must read its output: review is now the main part of the job
    - Bottom: so you **check** the output (*check* in red)
- Reference line under the panels (mono 16px, ink-3, centred): coming in DEV GROWTH #07: how to review a PR an agent wrote
- Next cue: next → where we still type the code ourselves
- Footer right: `3 / 6`

---

## 4: What do we still write by hand? (`src/4.html` → `4.png`)

- From cue: ← from 03: you check what the agent writes
- Title: What do we still *write by hand?*
- Intro line (mono 18px, ink-2, centred, all lowercase on purpose; the bold part is ink/white, not amber): assembly survived in **boot code, drivers and tight loops**. hand-written code survives the same way:
- Layout: five numbered rows. Each row has an amber number (mono 28px) on the left, then a bold title (24px) and a grey line under it (mono 16px)
  1. **The risky core**: money, security checks, concurrency (code that runs at the same time): one wrong line costs a lot
  2. **Hot paths**: code that runs millions of times, where you tune every line
  3. **The first example of a new pattern**: so the agent has a good example to copy
  4. **Learning**: you write it yourself while you learn a new idea (more in DEV GROWTH #05)
  5. **The bug the agent loops on**: when it tries the same broken fix again and again, you take over
- Next cue: next → the skills that matter more now
- Footer right: `4 / 6`

---

## 5: Which skills matter more now? (`src/5.html` → `5.png`)

- From cue: ← from 04: hand-written code moves to where it pays off
- Title: Which skills *matter more now?*
- Section label (mono 16px, ink-3): `THE SKILL MOVES UP, AGAIN`
- Two "shift" rows: red box `→` (amber arrow) green box
  1. compilers: managing registers → designing programs
  2. agents: typing every line → saying what it must do, and checking it
- Section label: `WHAT TO GET GOOD AT`
- Skill cards, 2-column grid (bold title 22px + grey line 15px); the last card spans both columns:
  1. **Clear specs**: say exactly what you want, edge cases included
  2. **Small steps**: break a feature into pieces you can test
  3. **Tests first**: they pin the behaviour the agent must meet
  4. **Reading code fast**: spot what is wrong in a diff (more in DEV GROWTH #07)
  5. **Architecture** (full width): know where code should live, and why
- Next cue: next → what to remember from all of this
- Footer right: `5 / 6`

---

## 6: Takeaway: what to remember (`src/6.html` → `6.png`)

- From cue: ← from 05: judgment matters more
- Title: Takeaway: *what to remember* (no max-width)
- Layout: five numbered rows. Each row has an amber number, then a small uppercase grey label (mono 14px), then the takeaway in bold (22px)
  1. `the level moved up`: Each new level hides detail. The old level never dies; it moves to where it still pays off.
  2. `a normal day`: The code still exists. Your job moved from typing it to describing it and checking it.
  3. `where the comparison breaks`: You can trust a compiler. You must check an agent.
  4. `what we still write by hand`: Type code by hand where one wrong line costs the most.
  5. `the skills that matter`: Typing speed matters less. Judgment matters more.
- Main box (amber left border, 9% amber tint), label `THE ONE THING` (mono 15px, amber), text 28px bold:
  Typing code is becoming the new assembly. Your job: say what the code must do, and prove that it does.
- Next cue: none (last slide)
- Footer right: `6 / 6`
