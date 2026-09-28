# Pillar 6 — Building (Real Projects)

Series label: `BUILDING #NN` · Visual accent: teal `#2DD4BF` · Tag: `BUILDING`

## Purpose

Show how real engineering work happens under real constraints.

This pillar demonstrates practical execution: shipping products,
making technical decisions, debugging failures, changing direction,
working with trade-offs, and learning from real projects.

Every post must originate from real project work, real observations,
or real decisions. Never manufacture a project story to fit a topic.

Scope: personal and client projects, including Pivot. Pivot is a client's
product, so it is always anonymous here (see "Pivot and other client
products" below).

## Audience

- Developers learning how real projects work
- Founders and clients evaluating execution ability
- Senior engineers interested in practical decisions and trade-offs

## Source

Raw notes go in `sources/project-log.md`.

Every two weeks capture:
- What shipped
- What broke
- What was decided
- What changed
- Important technical details
- Numbers/results where safe
- What we learned
- What I would do differently

Posts must be drafted from this source, not invented. Each post's `SOURCE:`
line names the entry it came from (its heading, e.g. `2026-10-02 — Pivot`,
which never appears in the post itself);
`validate.py` rejects a post whose entry is missing.

## No Invented Facts

If a draft needs a fact that is not in the source (a number, a date, a
tool, what happened, who decided), write it as `[PERSONAL: one line
describing what is needed]`. Never guess or fill the gap. The author
replaces every marker before posting.

## Quality Bar

Every BUILDING post must contain at least 3 of:

- Real problem or constraint
- Meaningful decision
- Alternative considered
- Engineering trade-off
- Failure or unexpected result
- Implementation detail
- What changed because of it (impact)
- Measurable result
- Generalizable lesson

Never turn a BUILDING post into a task/status report.

## Core Formats

Set the format in the post's `TYPE:` line (shown in brackets). Every
BUILDING post uses `MODE: PERSONAL`. There is no roadmap: posts are
numbered in the order they are written.

### Bi-weekly Update [UPDATE]
One main story: Problem → Decision → Result → Lesson.
Then 2–3 short "Also shipped" lines (one line each, no detail).
Then one "Next:" line.
The main story carries the post; the extra lines only show momentum.

### Project Story [STORY]
Problem → What we tried → What happened → What changed → Lesson

### Decision Log [DECISION]
Context → Options → Decision → Trade-off → Result

### Postmortem [POSTMORTEM]
What broke → Impact → Root cause → Fix → Prevention

### Demo / Walkthrough [DEMO]
VISUAL: Show the actual product, architecture, workflow,
or implementation with concise project-specific explanation.
Use personal projects. Client work only with explicit permission.

### What I'd Do Differently [RETRO]
For looking back at an older or finished project, not recent work.
Original decision → What we learned → What I'd change now → Why

## AI Rule

When AI materially contributed to the work, show how it was used.

Examples:
- AI coding agents
- Debugging
- Research
- Architecture
- Testing
- Automation
- AI-assisted workflows

Never force AI into a project where it wasn't relevant.

## Engineering Detail Rule

Do not turn BUILDING posts into generic tutorials.

The engineering lesson should emerge from the real project context.

## Client Work

- No client names, data, screenshots, architecture, or metrics without permission.
- Anonymize domains when necessary.
- Never expose information that could identify the client or reveal confidential business information.
- When in doubt, anonymize more.

## Pivot and other client products

Pivot is a client's product. Never name it, and never use its brand colour,
logo or screenshots. Describe it by category ("a real-time collaboration
product I work on").

Also keep out, for Pivot and any client product:
- Feature names, unreleased features and the roadmap
- Internal code, repo structure and internal service names
- Business metrics: users, revenue, growth, costs
- Customer names or data
- Security details: how auth, permissions or infrastructure could be attacked

Never tell the same story twice in a way that links it back to the client.
`validate.py` warns when a BUILDING post mentions "pivot".

## Voice

Default: "I"

Use "we" when describing genuine team decisions or team execution.

Do not claim sole ownership of team work.

## Cadence

One BUILDING post each time the rotation reaches it (about every 1.5 weeks at
5 posts a week; see README). Alternate the bi-weekly update with a story,
decision, postmortem, demo or retro when there is real material.

Additional BUILDING posts only when there is meaningful material.

## Principle

BUILDING is not a project diary.

It is a record of real engineering decisions, failures,
trade-offs, and outcomes.
