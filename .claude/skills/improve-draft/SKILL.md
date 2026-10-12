---
name: improve-draft
description: Improve existing drafts in generated/drafts/ before any images or post text are built from them — fix the headline, the VISUALS line, missing or repeated content across the series, simple wording and validator errors. Touches the draft only. Use when the user types /improve-draft, or says "improve the draft", "fix the draft", "mature the draft", "clean up drafts", "improve ai #02", "improve all ai drafts", or gives a draft plus notes and wants a better version of it.
---

# Improve a draft before anything is built from it

The draft in `generated/drafts/<folder>/<prefix>-NN-*.md` is the source of
truth. Images, post text and blog are built from it later by `/create-post`.
This skill makes the draft right first, and changes **nothing else**: no
`posts/` files, no `src/*.html`, no rendering.

## Input

`/improve-draft <series> [#NN | all] [notes...]`

Examples:
- `/improve-draft ai #02`
- `/improve-draft ai all keep every post under 8 images`
- `/improve-draft be #04 the example is too basic, use a payment retry`

Series aliases, folders and roadmap files are the same as in
`.claude/skills/create-post/SKILL.md` (`## Series aliases`). The notes are the
user's extra instructions for this run; they come on top of the rules below.

## Steps

1. Parse series, number (or `all`) and notes. If the series is unclear, ask.
2. Read in full: the draft, the pillar roadmap, `skills/linkedin-content.skill.md`,
   `prompts/master-content-prompt.md`, and the **Rules** section below.
3. Read the drafts of every post listed in this post's `needs`, and the
   roadmap titles of the posts after it, so you know what is taught where.
4. Check the draft against the checklist below and write down every problem.
5. Fix the problems in the draft. Keep the author's hook, examples and voice
   unless a rule says otherwise. Do not add a topic another post teaches; move
   content to the post it belongs in (edit that draft too, and say so).
   Then run the Content Quality Gate from `skills/linkedin-content.skill.md`
   on the revised draft and re-read it against the original: no new error,
   the author's claim and voice kept. The draft stays `STATUS: draft` while
   any marker is left.
6. Run `python3 scripts/validate.py`. Fix every error in this draft and rerun
   until it passes. Errors in other drafts that were there before are not
   yours — leave them and mention the count.
7. Report: a short list of what changed and why, plus anything you chose not
   to change. Then stop. Do not build images, post text or the blog — the user
   approves the draft first, then runs `/create-post`.

For `all`: do one draft at a time, in roadmap order. After each one, report
and wait for the user's approval before starting the next.

## Checklist

- **Headline matches the body.** A count in the headline ("five ideas")
  equals the number of sections that carry an idea.
- **VISUALS line.** One entry per image, no section listed twice, each entry
  is the exact heading of a section in the body, ends with `· rest = text`.
- **One section = one idea = one image.** No two sections teach the same
  thing (e.g. "prediction" and "inference" are one idea — merge them).
- **Right scope for its place in the series.** It covers the basics it is
  meant to cover, and leaves out what earlier or later posts teach. Missing
  basics that no post covers can be added here.
- **Every term is defined** in plain words, with a concrete example, the first
  time it appears.
- **Failure scenario** where the rules require it ("what breaks without it").
- **`Keep in mind …` section** exists, 3–8 do/don't lines, each specific to
  the topic. "When not to", "Common mistake" and "Watch out" content is real —
  cut anything invented to fill a block.
- **Wording fits the level.** Plain, direct sentences; a sentence the
  intended reader would have to read twice gets rewritten. Advanced posts keep
  precise terms and longer reasoning where it is needed.
- **Fact markers** as `[FACT_CHECK: claim → what to check]` on every claim
  about numbers, dates, prices or named products. Remove markers whose claim
  you removed.
- **No markdown headers or `**bold**`** in the body (LinkedIn does not render them).

## Rules

Read `refiner-rules.md` (next to this file) in full on every run. It is the
editing standard: how to diagnose a draft, adapt depth to the topic, check
accuracy, sequence concepts, fix examples and terminology, and preserve the
author's intent. Follow its workflow (section 15) for steps 4–5 above.

Where it meets this repo, these choices apply:

- **Depth follows the draft's `LEVEL:`.** BEGINNER → section 3 "Basic";
  INTERMEDIATE → "Intermediate"; ADVANCED → "Advanced". Plain words never
  replace a term the topic needs — define the term instead.
- **Output.** Its section 17 is replaced by step 7 here: the improved draft is
  saved in place (section A), and the report gives B *What improved*,
  C *Technical corrections* (with every claim still unverified) and
  D *Remaining recommendations* — only meaningful ones.
- **Verification.** Check claims against primary sources when you can. A claim
  you could not verify gets a `[FACT_CHECK: …]` marker; never mark one as
  checked without doing it.
- **Format rules still win.** No markdown headers or `**bold**` in the body,
  the header fields and `VISUALS:` line stay valid, and the validator passes.
- **Too many ideas for one post** (section 11): recommend a split in D; do
  not split or create new drafts without the user's approval.
