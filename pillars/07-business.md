# Pillar 7 — For Business (Products and Solutions)

Series label: `FOR BUSINESS #NN` or `SOLUTIONS #NN` (one shared number sequence)
· Visual accent: lime `#A3E635` · Tag: `FOR BUSINESS` / `SOLUTIONS`

## Purpose

Show business owners and teams what software and AI systems can do for them,
and bring in enquiries. Two post types, set in the `TYPE:` line:

- **PRODUCT**: an app I built and own. Real features, real screens, real links.
- **BLUEPRINT**: a system described as a concept: what it does, how it works,
  what it needs. Not a claim that I built or delivered it.

Pick the series label that fits the post: `FOR BUSINESS` when the post speaks
to a business problem or sells an app; `SOLUTIONS` when it describes a system
that solves a problem. Both labels share one number sequence.

## Audience

Business owners, founders, operations and team leads. Not engineers.
Plain business language. Every technical word gets a one-line meaning.
Talk about outcomes (hours saved, errors avoided, faster answers), never stack
details for their own sake.

## Sources

- **PRODUCT**: only apps listed in `sources/apps.md` (my own apps). The
  `SOURCE:` line names the app's heading there. Missing facts are written as
  `[PERSONAL: ...]`, never guessed.
- **BLUEPRINT**: no source file needed, because it describes a concept. It
  may use a real project as a skeleton (including Pivot) only with nothing
  that identifies it: follow "Pivot and other client products" in
  `pillars/06-building.md`.

Client apps, including Pivot, are never PRODUCT posts.

## Structures

### PRODUCT (`MODE: PERSONAL`)
Hook → Problem (why it costs time or money today) → The app (3–5 "→" lines
of outcomes, not features) → How it works (one real use, screen or steps)
→ Who it's for (one line) → CTA.

### BLUEPRINT (`MODE: TEACH` or `SCENARIO`)
Hook (a business problem, concrete situation) → The system (what it does, in
plain words) → How it works (3–6 steps: data in → processing → AI step →
output → human check) → What it needs (data, tools, people, rough effort,
honest limits) → Where it fits / where it doesn't (one line each) → CTA.

## Call to action

Exactly one CTA line per post, at the end. Use "message me" or "contact us",
whichever fits who is offering: "message me" for my own apps and personal
offers, "contact us" for team or company offers. No "DM for price", no
urgency tricks.

## Honesty rules (hard)

- PRODUCT: only real features and real numbers.
- BLUEPRINT: never say or imply "I built", "we built", "we delivered",
  "our client" or "we helped". No invented results, users, savings or case
  studies. Use "a system like this can…", "here is how it works".
- No guaranteed outcomes ("will double your sales").

`validate.py` enforces the CTA line and the BLUEPRINT phrases.

## Quality bar

Every post teaches something even to a reader who never buys: how the system
works, what it needs, or where it fails. No pure advertising, no hype words
("revolutionary", "10x", "game-changing").

## Format

BLUEPRINT posts are usually VISUAL (one flow diagram) or a CAROUSEL when the
system has 4+ stages that each need their own picture. PRODUCT posts use a
real screenshot, or a carousel of real screens.

## Cadence

One post each time the rotation reaches it (see README). No roadmap: posts are numbered in the
order they are written.
