# Pillar 7 — Pivot (Building Pivot in Public)

Series label: `PIVOT #NN` · Visual accent: Pivot purple `#7C6BFF` · Tag: `PIVOT`

## Purpose

Share the ongoing story of building Pivot: what we ship, the decisions behind
it, what breaks and what we learn. BUILDING covers personal and client
projects; this pillar is only for Pivot, under its real name.

Every post must originate from real work on Pivot. Never manufacture a story
to fit a topic.

## Audience

- Developers curious how a real product is built and run
- Founders and clients evaluating execution ability
- Senior engineers interested in product and architecture decisions
- People who may use Pivot

## Named or anonymous

Decide this per story, before drafting.

- **Named** → this pillar, `PIVOT #NN`. Pivot is mentioned by name.
- **Anonymous** → goes to the BUILDING pillar as `BUILDING #NN`, never here.
  Describe it as "a product I'm building" or by its general category. The
  name Pivot, its features' names, screenshots, and anything that points to
  it stay out.

Never link an anonymous post to a named one ("as I shared in PIVOT #03"),
and never tell the same story both ways. Two versions side by side undo the
anonymity.

## What stays private (both modes)

- Unreleased features and the roadmap, unless announced
- Internal code, repo structure and internal service names
- Business metrics: users, revenue, growth, costs
- Customer names or data
- Security details: how auth, permissions or infrastructure could be attacked
- Anything a teammate or the company has not agreed to share

When in doubt, keep it private or go anonymous.

## Source

Raw notes go in `sources/project-log.md` under `Project: Pivot`. Mark each
entry NAMED or ANON so the draft lands in the right pillar.

Posts must be drafted from this source, not invented, and name their entry
in a `SOURCE:` line (see BUILDING). Missing facts are
written as `[PERSONAL: ...]`, never guessed (see BUILDING, No Invented Facts).

## Quality Bar

Same as BUILDING: every post contains at least 3 of real problem or
constraint, meaningful decision, alternative considered, engineering
trade-off, failure or unexpected result, implementation detail, what changed
because of it, measurable result, generalizable lesson.

A PIVOT post is not a product announcement or a changelog. The engineering
story comes first; the feature is the setting.

## Formats

Same formats and structures as BUILDING (`pillars/06-building.md`), set in
the `TYPE:` line: UPDATE, STORY, DECISION, POSTMORTEM, DEMO, RETRO. Every
PIVOT post uses `MODE: PERSONAL`. There is no roadmap: posts are numbered in
the order they are written.

- **UPDATE** here is the bi-weekly Pivot build log.
- **DEMO** may show Pivot's real UI once the feature is public.

## AI Rule

Same as BUILDING: when AI materially contributed (coding agents, debugging,
review, testing, automation), show how. Never force it in.

## Voice

Default: "we". Pivot is team work.

Use "I" only for work I personally did or decided. Do not claim sole
ownership of team work.

## Cadence

One PIVOT post every two weeks, alternating with BUILDING on the Saturday
slot. Extra posts only when there is meaningful material.

## Principle

PIVOT is not marketing and not a changelog.

It is an honest record of building a real product: decisions, failures,
trade-offs and outcomes.
