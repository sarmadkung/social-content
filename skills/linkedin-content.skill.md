
---
name: linkedin-content
description: Use when writing, planning, or reviewing LinkedIn content for Muhammad Sarmad — enforces positioning, the seven content pillars, series labels, and tone.
version: 1.7
owner: Muhammad Sarmad
works-with: any (Claude, ChatGPT, Gemini, local)
---

# LinkedIn Content Skill

A reusable content system for creating consistent, technically credible LinkedIn
content from Muhammad Sarmad's personal profile.

**Companion skill:** `linkedin-visual.skill.md` covers the visual half — canvas
sizes, locked layout, type, and the per-pillar accent colors. Load it whenever a
post needs an image or carousel; this skill decides what a post says, that one
decides what it looks like.

## Use this when

- Drafting a LinkedIn post, carousel, or comment.
- Planning a content series or a batch of posts.
- Reviewing a draft for positioning, tone, or pillar fit.
- Turning a technical topic (a bug, a design decision, an algorithm) into a post.

## Do not use this when

- Writing for another person's profile or another platform's native voice.
- Writing resumes, cover letters, or client proposals.

## Output format

For a `COPY` or `FULL` request (see section 0), return each post in exactly this
shape. It is the one post format for the whole system — the master prompt, the
drafts in `generated/`, `scripts/build_queue.py` and `scripts/validate.py` all
use it.

```
SERIES:    <series label and number, e.g. DSA SERIES #04>
TITLE:     <title>
PILLAR:    <pillar> — for <who benefits most>
LEVEL:     <BEGINNER | INTERMEDIATE | ADVANCED>
MODE:      <TEACH | WHY | COMPARE | LIST | SCENARIO | QUIZ | PERSONAL>
TYPE:      <UPDATE | STORY | DECISION | POSTMORTEM | DEMO | RETRO>   (BUILDING)
           <PRODUCT | BLUEPRINT>   (FOR BUSINESS)
SOURCE:    <project-log entry heading>   (BUILDING) · <app heading in sources/apps.md>   (PRODUCT)
FORMAT:    <TEXT | VISUAL>   (TEXT = words only; VISUAL = words + image)
HEADLINE:  <image headline, 8 words or fewer>          (VISUAL only)
LAYOUT:    <STATEMENT | GRID | ANATOMY | FLOW | COMPARE | STAT | CAROUSEL>   (VISUAL only)
SLIDES:    <one line per slide: NN · LAYOUT · headline · what it draws>   (CAROUSEL only)
VISUALS:   <1 = <section heading> · 2 = <section heading> · rest = text>   (VISUAL, optional)
STATUS:    <draft | approved | scheduled | published>
---
<post body, ready to paste — no markdown headers, short paragraphs>
```

New posts start as `STATUS: draft`. Only the text below `---` goes into LinkedIn.

**VISUALS:** says which sections of the body become images and which stay
text. Each item names a section by its heading line exactly as it appears in
the body — or, for paragraphs with no heading, their opening words joined by
` + ` (`3 = Search: + Traversal: + In-place:`) — in posting order (`1 = …` is `1.png`); `rest = text` closes the line.
The draft keeps every section in full — the posted text
(`posts/<post>/post.md`) leaves out the sections listed here and points to the
images instead.

**Choosing MODE:** the roadmap line in `pillars/` gives each post its mode
(`#NN Title · MODE · needs #..`). TEACH explains what X is; WHY explains a
reason; COMPARE weighs options; LIST is a specific top-N, mistakes or
checklist post; SCENARIO walks through a realistic situation; QUIZ asks the
reader; PERSONAL is the author's own experience. Each mode's structure lives
in `prompts/master-content-prompt.md`. Never more than 4 TEACH posts in a row
within a pillar, and a post only relies on the posts in its `needs` list.

**Markers:** `[PERSONAL: ...]` marks a personal fact to fill in.
`[FACT_CHECK: claim → what to check it against]` marks an outside claim to
verify (history, dates, "X uses Y", benchmarks, specific library or runtime
behaviour). Each goes on its own line after the paragraph. `validate.py` stops a
post from moving past draft while either is left.

**Senior Interest and Learning Value Test:** before writing or refining, answer
four things: who the reader is (the `LEVEL:` and the posts in `needs`), what
they already know, the learning outcome in one sentence, and why it matters to
them. A post earns its place when it delivers that outcome — more than a bare
definition. Valid outcomes: understand a foundation concept accurately; see how
or why a mechanism works; learn a technique or mental model; spot a non-obvious
insight, trade-off, failure mode or limitation; separate two concepts people
mix up; learn to choose, build, debug or evaluate something; see a production
or architecture consequence.
- **Foundation posts the roadmap plans are welcome.** A roadmap line like AI
  #01 or DSA #01 exists because later posts depend on it; do not reject it
  because seniors know it. Judge it by its outcome: accurate definitions, a
  complete example, and the one idea a learner needs next.
- **Unplanned basics are not.** Do not add a post on what every working
  developer knows (variables, loops, client vs server) outside a roadmap
  foundation slot, and never in Software Engineering, which targets mid-level
  and senior readers. When a pillar runs out of topics, go sideways (mistakes,
  COMPARE, SCENARIO), never more basic.
- **"Beginner-friendly" never excuses a wrong or empty explanation.**
Simple language, professional depth: juniors follow the words, seniors trust
the accuracy. Never a beginner post with a senior footnote.

**Depth by LEVEL** (guidance, not boxes — follow the post's actual goal):
- BEGINNER — build intuition, define every term, familiar examples, no jargon
  the reader doesn't need yet.
- INTERMEDIATE — explain the mechanism, the implementation choices, a realistic
  example and the trade-offs that matter.
- ADVANCED — be precise about assumptions, system boundaries, mechanisms, edge
  cases and failure modes; use the formal terms early when they help.

**Choosing FORMAT:** `VISUAL` is the default. A post is `TEXT` only when both
are true: it is short (body 1,400 characters or fewer) and the words explain it
fully, so an image would only repeat them. Anything longer, or anything with a
flow, comparison, structure or idea a picture explains better, is `VISUAL`.
`TEXT` posts leave out `HEADLINE:` and `LAYOUT:`.

**Choosing CAROUSEL:** only when it is really needed. `LAYOUT: CAROUSEL` needs
all three: the idea is an ordered sequence; it has 4+ stages that each need
their own picture (numbers, code or a diagram, not a one-line label); and one
image would be unreadable or lose the order. Otherwise one image. A carousel is
the cover (HEADLINE) + one slide per stage + an END slide, 6–10 slides, listed
in a `SLIDES:` block (full rule in `prompts/master-content-prompt.md`).

**Adaptive teaching order:** pick the order that makes the idea easiest to
understand at the post's level. These are starting points, not templates:
- BEGINNER: familiar problem → plain idea → "this is called X" → concrete
  example → what it means in practice.
- INTERMEDIATE: problem or question → key term → how the mechanism works →
  demonstration → trade-offs and when to use it.
- ADVANCED: precise claim or problem → terms and assumptions → mechanism or
  reasoning → evidence or example → edge cases, trade-offs, implications.
Whatever the order: prerequisites are present or covered by `needs`; terms
the reader may not know are defined when they first appear; the post shows how
or why when the outcome needs it; the example demonstrates the idea instead of
restating the definition; the ending gives an implication, decision rule or
takeaway. The block order per mode lives in `prompts/master-content-prompt.md`.

**Examples, limits and mistakes — real or not at all:** every post has a
concrete example (code, numbers, a text diagram or before/after). A "when not
to use it" line, a common mistake with its fix, a failure mode and a trade-off
go in whenever the topic has a real one — most TEACH and COMPARE topics do.
Never invent one to fill a slot: no made-up drawback, no straw-man mistake, no
caveat the topic doesn't have. If a block has nothing true to say, leave it
out.

**Keep in mind rule (every pillar):** every post except a QUIZ question has a
section whose heading starts with `Keep in mind`, then a tail worded for the
post: `Keep in mind: how to learn DSA without wasting time`, `Keep in mind
before you add a cache`, `Keep in mind when you ship a RAG feature`, `Keep in
mind before you hire a developer`. 3–8 short `→` lines (about 60 characters
each), each a do or a don't with its reason. Examples per pillar are in
`prompts/master-content-prompt.md`. `validate.py` fails a prepared post
without it, so it stays required — but every line must be specific to this
topic and say something the body doesn't already say word for word. Use 3
strong lines rather than 8 with filler; no generic advice ("practice daily",
"keep learning") and no summary of the post.

**Watch out section (optional):** when the topic has real drawbacks, add a
section whose heading starts with `Watch out`, worded for the topic: `Watch
out: what caching breaks`, `Watch out: where RAG fails`, `Watch out: what
microservices cost you`. 2–5 `→` lines, each `problem → where you see it → how
to prevent or catch it`. "Keep in mind" is how to do the thing well; "Watch
out" is what the thing costs even when done well. Skip it when there are no
real drawbacks. Text or image, decided per post. Examples per pillar are in
`prompts/master-content-prompt.md`.

**Length:** the draft in `generated/drafts/` is the skeleton — the full
source that the images and the posted text are made from — so it has no length
limit. The limit is on `posts/<post>/post.md`, the LinkedIn text that gets
posted. With images it is a short caption: about 700–1,200 characters
(hashtags not counted), 1,400 as a soft ceiling, no minimum — shorter is better
when the point is clear; go over only when the user asks or the post truly
needs it. Without images (TEXT): 1,400 max. 3,000 is LinkedIn's hard cap. These
numbers are for LinkedIn only; daily.dev, Instagram, X and the blog keep their
own rules in `create-post`. Never cut content from the draft to fit; the
caption is an editorial selection from it (rule in `create-post`).

**Blog links (every platform):** the blog is the one place social posts send
readers for the full explanation: https://www.muhammadsarmad.com. Link only
when a matching article is live there — its file exists in the site repo
(`~/Documents/personal/muhammadsarmad/content/blog/<slug>.mdx`, `draft:
false`) and the URL is `https://www.muhammadsarmad.com/blog/<slug>`, using the
site's slug, which can differ from the draft basename. Never invent a URL,
never link to an unrelated page; no matching article → no link. Never link
one social profile from another or ask readers to follow on another platform.
The call to action is one natural line, e.g. "Read the full explanation on my
blog: <url>" or "The detailed guide is on my blog: <url>". Placement per
platform is in `create-post`.

**Failure scenario rule (Software Engineering):** every concept, tool or
feature comes with a concrete production scenario showing what breaks without
it, then why we adopt it. Model: a payment call times out, the client retries,
the customer is charged twice → that is why payment APIs need idempotency
keys. In COMPARE posts, give each option its own "where it hurts" scenario.
The scenario must be technically plausible; numbers are illustrative unless
sourced, and are worded that way ("say 2,000 requests").

**Content Quality Gate (before a draft is saved or moves past draft):** this
is the one definition of the gate; `create-post`, `improve-draft` and the
master prompt's self-check all run it. Read the finished draft — not the plan
for it — as both the intended reader and a technical reviewer, fix what fails,
then read the fixed version again.
1. **Technical correctness.** Definitions and terms are accurate. Mechanisms,
   causal claims, comparisons and conclusions are sound. Code, numbers,
   examples and analogies actually support the point (and the maths is
   right). Related concepts are not confused. A simplification is not stated
   as always true; needed assumptions, scope and qualifications are there.
   Every checkable outside claim has a `[FACT_CHECK: …]` marker unless you
   really checked it. Never say a source, benchmark or spec was verified when
   it wasn't. If a claim can't be supported, qualify it, mark it, or cut it.
2. **Depth and learning value.** The post delivers the one-sentence learning
   outcome at its `LEVEL:`. It teaches the idea, not just names it. Nothing a
   reader needs for the central claim is missing; no advanced detail pulls
   away from it.
3. **Teaching.** The order is logical for the level; prerequisites are present
   or in `needs`; jargon and abbreviations are handled; the example shows the
   concept; analogies are bounded and not misleading. After reading, the
   reader could explain the main idea.
4. **Language and structure.** No repetition, filler, vague claims, needless
   hedging or generic AI phrasing. Direct, specific, natural sentences. Every
   section earns its heading — none exists only because a template has it.
   Shorter is not a reason to cut correctness or needed depth.
5. **Completeness and relevance.** It says why the concept matters; examples,
   failure modes, limits and trade-offs are there when they matter; no
   important distinction or caveat is missing; nothing is said twice; the
   ending fits the outcome.
6. **Author intent.** Topic, argument, stance, audience and real experience are
   kept. No invented anecdotes, incidents, metrics, credentials, client
   results, benchmarks or quotes — a gap is a `[PERSONAL: …]` marker. No
   complexity added to sound senior; no needed detail removed to sound
   simple. A good draft gets only the changes that add real value. When a
   factual or logical fix changes what the draft claims, say so in the reply.
7. **Markers and status.** Every `[PERSONAL: …]` and `[FACT_CHECK: …]` is on
   its own line in the right form. A draft with any marker left stays
   `STATUS: draft` (`validate.py` enforces this), and platform texts never
   carry one.
The gate is a review, not a list of things to add: it never licenses an extra
section, an invented caveat or an unsupported fact.

---

## 0. Request keywords

Every request begins with one keyword that sets what to return. Honor it
exactly — do not return more than asked, and do not return less. This table is
the only definition of the keywords; the visual skill refers back to it.

| Keyword | Return | Skills to apply |
| --- | --- | --- |
| `COPY` | Post text only, in the format above. No image. | content skill only |
| `VISUAL` | The image: the HTML/CSS that renders it, or the rendered PNG (visual skill §0b). No post text. | visual skill only |
| `FULL` | Post text **and** the image, in that order. | both skills |

If no keyword is given, assume `FULL`.

`VISUAL` still needs a headline — if the request has no post text to draw the
headline from, ask for it rather than inventing one.


## 1. Personal positioning

Muhammad Sarmad is a **Senior Software Engineer, Product Engineer, Full-Stack
Engineer, System Architect, and AI Engineer** with broad experience building
real-world software products and systems.

**Software engineering** — React, React Native, Next.js, TypeScript, Node.js,
Go, Rust, backend/API architecture, distributed systems, databases, web, mobile
and desktop applications.

**System architecture** — system design, scalable backend architecture,
distributed systems, API design, event-driven architecture, real-time systems,
database architecture, cloud infrastructure, performance and scalability,
reliability and observability, architecture trade-offs.

**AI engineering** — LLM applications, AI agents, agent orchestration, agent
harnesses, AI pipelines, AI memory, context engineering, RAG, AI application
architecture, AI evaluation, production AI systems.

**Engineering fundamentals** — data structures and algorithms, problem solving,
complexity analysis, software design, testing, debugging, performance
optimization, engineering principles.

Position him as:

> An experienced software and product engineer with strong engineering
> fundamentals, system architecture expertise, and hands-on experience across
> multiple technology domains — while actively working with modern engineering
> approaches and the latest developments in AI engineering.

Communicate both **established expertise** and **continuous engagement with
modern technology**.

Do **not** present him as someone merely learning modern engineering or AI. The
narrative is:

> Strong engineering fundamentals + extensive practical experience + modern
> engineering practices + continuous learning and adoption of emerging
> technologies.

## 2. Content philosophy

The goal is not to post for engagement. Content should:

1. Demonstrate genuine technical expertise.
2. Teach something useful.
3. Share practical engineering experience.
4. Help junior and mid-level developers grow.
5. Help developers preparing for technical interviews.
6. Explain complex concepts simply.
7. Show how strong fundamentals apply to modern software development.
8. Demonstrate practical experience with modern engineering approaches.
9. Explore emerging technologies from an engineering-first perspective.
10. Build a recognizable personal technical brand.

Prefer: practical > theoretical · clear > complicated · experience > generic
advice · reasoning > memorization · examples > definitions.

## 3. Audience

**Primary** — junior software engineers; developers transitioning into
professional engineering; developers preparing for coding interviews; developers
strengthening fundamentals; engineers learning modern practices; engineers
moving into AI engineering.

**Secondary** — mid-level and senior engineers; product engineers; system
architects; engineering leaders; technical founders; developers interested in
architecture, scalable systems, and AI engineering.

Stay accessible to juniors without becoming simplistic for experienced
engineers: simple language, professional depth (see the Senior Interest and
Learning Value Test above).

## 4. Seven content pillars

Do not create a separate pillar for every technology. There are exactly seven,
in this order, each with its own series label and visual accent. Pillars 1–5
teach from an ordered roadmap. Pillars 6–7 have no roadmap: Building comes from
real work in `sources/project-log.md`; For Business comes from my own apps in
`sources/apps.md` or from a system idea.

| # | Pillar | Series label | Roadmap |
| --- | --- | --- | --- |
| 1 | Problem solving | `DSA SERIES #NN` (+ bonus `DSA QUIZ #NN`) | `pillars/01-dsa-problem-solving.md` |
| 2 | Software engineering | `SOFTWARE ENGINEERING · BACKEND #NN`, `· WEB #NN`, `· MOBILE #NN` (three subsections, each numbered on its own) | `pillars/02-software-engineering.md` (one roadmap section per subsection) |
| 3 | System design | `SYSTEM ARCHITECTURE #NN` | `pillars/03-system-design.md` |
| 4 | AI engineering | `AI ENGINEERING #NN` | `pillars/04-ai-engineering.md` |
| 5 | Dev growth | `DEV GROWTH #NN` | `pillars/05-dev-growth.md` |
| 6 | Building | `BUILDING #NN` | `pillars/06-building.md` (no roadmap) |
| 7 | For business | `FOR BUSINESS #NN` or `SOLUTIONS #NN` | `pillars/07-business.md` (no roadmap) |

Another pillar needs a deliberate decision, its own roadmap file and its own
accent — never a quiet addition.

### Pillar 1 — Problem solving

Data structures, algorithms, problem-solving patterns, interview preparation,
complexity analysis, pattern recognition, algorithm intuition, step-by-step
problem solving.

Examples: hash maps and hashing, two pointers, sliding window, Kadane's
algorithm, Boyer–Moore voting, binary search, sorting, anagrams, group anagrams,
array problems, string problems, trees, graphs, dynamic programming, greedy
algorithms.

**DSA teaching format:**

> Problem → Intuition → Pattern → Example → Solution → Complexity → Interview
> takeaway

Do not simply publish code. Explain **why the solution works** and how an
engineer recognizes the same pattern in another problem.

DSA posts also: state the complexity **and the reason for it**, include a tiny
walkthrough on a real input, and give the invariant or one-line proof when there
is one (e.g. why moving the left pointer in two pointers can never skip the
answer).

**Pattern recognition block (required on every DSA pattern post):** add a
`Spot it when the problem says…` block just before "When to use it / when not
to" — 2–3 `→` lines of clue words or constraints a reader can find in a problem
statement (e.g. `"subarray" + "longest" + "at most K"` → sliding window). Where
two patterns are easy to confuse, one clue says which one to pick.

**Pattern quiz:** optional `DSA QUIZ #NN` bonus posts — one problem, "Which
pattern is this?", answer in the first comment. Use only patterns already taught.

### Pillar 2 — Software engineering

Muhammad's broad experience in traditional and modern software engineering.

*Frontend* — React, Next.js, TypeScript, web architecture, state management,
data fetching, performance, testing.

*Mobile* — React Native, Expo, mobile architecture, offline-first applications,
performance, native integrations.

*Backend* — Node.js, Go, Rust, REST, GraphQL, gRPC, WebSockets, distributed
systems, event-driven systems, microservices.

*Infrastructure* — PostgreSQL, MongoDB, Redis, Docker, AWS, CI/CD,
observability, testing.

Focus on real engineering problems at the level of one service or codebase:
design decisions, trade-offs, performance, scalability, reliability, developer experience,
maintainability, testing strategy, production engineering, lessons from real
products.

Demonstrate **hands-on engineering experience**, not generic framework
tutorials.

### Pillar 3 — System design

How systems are built to scale, stay up and stay simple — one building block and
its trade-off per post: scaling, load balancing, caching, CDNs, replication,
sharding, queues, event-driven architecture, consistency models, reliability
patterns, and full case studies (URL shortener, rate limiter, chat, notifications).

Where software engineering is one service done well, system design is how many
services, stores and networks fit together — and what fails when they do not.
Name real, verifiable systems; never invent throughput or latency figures.

### Pillar 4 — AI engineering

Reflect hands-on AI engineering and active work with modern AI approaches — not
AI as something being learned from scratch.

Topics: LLM applications, AI agents, agent orchestration, agent harnesses, agent
pipelines, RAG, AI memory, context engineering, tool calling, multi-agent
systems, AI evaluation, AI coding agents, AI infrastructure, model selection, AI
application architecture, production AI systems.

Key perspective:

> AI engineering is software engineering applied to systems that use models.

Discuss architecture, reliability, context, memory, cost, latency, evaluation,
observability, security, failure modes, production trade-offs.

Avoid generic "AI is changing everything" posts unless there is a concrete
engineering insight.

### Pillar 5 — Dev growth

How developers grow from student to senior: learning a new technology, reading
unfamiliar code, debugging, asking good questions, interviews, design docs,
estimation, and working well with AI tools. Every post is concrete numbered
steps or a clear comparison — never generic motivation — and draws on real
experience through `[PERSONAL: ...]` markers rather than invented stories.

### Pillar 6 — Building

Real engineering work on personal and client projects, including Pivot, which
is a client's product and is never named: shipped work, decisions, failures, trade-offs and results. Every
post has `MODE: PERSONAL` and a `TYPE:` (UPDATE, STORY, DECISION, POSTMORTEM,
DEMO, RETRO), each with its own structure in `pillars/06-building.md`. Draft
only from `sources/project-log.md`; any missing fact is a `[PERSONAL: ...]`
marker, never a guess. No client names, data or screenshots without
permission. Not a project diary, not a status report.

### Pillar 7 — For business

For business owners, not engineers: what software and AI systems can do for
them, ending in one call to action ("message me" or "contact us"). Two
`TYPE:`s. PRODUCT: an app I own, from `sources/apps.md`, real features only,
`MODE: PERSONAL`. BLUEPRINT: a system described as a concept, `MODE: TEACH` or
`SCENARIO`; it never says or implies it was built or delivered ("I built",
"our client"), and never invents results. Label each post `FOR BUSINESS` or
`SOLUTIONS`, sharing one number sequence. Client apps, including Pivot, are
never PRODUCT posts. Every post still teaches something; no pure advertising.
Rules and structures in `pillars/07-business.md`.

## 5. Connecting the pillars

The pillars should not feel disconnected. Look for intersections:

- **DSA + AI** — why problem-solving fundamentals still matter when AI can write
  code.
- **Software engineering + AI** — what changes when traditional systems start
  using LLMs.
- **System architecture + AI** — how AI capabilities should fit into a
  production system.
- **DSA + software engineering** — how algorithmic thinking affects production
  engineering decisions.
- **All of them** — building reliable AI systems requires strong fundamentals,
  sound architecture, and an understanding of modern AI capabilities.

Overall narrative: **strong fundamentals + practical software engineering +
system architecture + modern AI engineering.**

## 6. Series system

Use recognizable series labels:

```
DSA SERIES #07            Hash Maps: The Pattern Behind Two Sum
DSA QUIZ #01              Which Pattern Is This?
SOFTWARE ENGINEERING · BACKEND #01  Postgres vs MongoDB vs DynamoDB
SOFTWARE ENGINEERING · MOBILE #03   FlatList vs FlashList
SYSTEM ARCHITECTURE #01   What System Design Actually Is
AI ENGINEERING #09        Agents Are Software, Not Magic
DEV GROWTH #01            Junior vs Mid vs Senior: What Actually Changes
BUILDING #01              <a real project story, from the project log>
SOLUTIONS #01             <a system blueprint, with one call to action>
```

Series are different perspectives on the same engineering identity — not
separate personalities or unrelated channels.

## 7. Core positioning principle

> I have strong engineering fundamentals and real-world experience building
> software systems, while continuously adopting and working with modern
> engineering practices and emerging technologies such as AI.

Balance:

- **Fundamentals** — algorithms, data structures, problem solving.
- **Engineering depth** — software architecture, system design, scalability,
  reliability.
- **Technology breadth** — React, React Native, Node.js, Go, Rust, TypeScript.
- **Modern engineering** — AI engineering, agents, context, memory,
  orchestration, LLM applications.

## 8. Tone

Experienced, curious, practical, technically deep, continuously improving.

Never position the author as a beginner, someone discovering software
engineering for the first time, someone merely following trends, or someone who
only consumes AI news. Instead:

> An experienced engineer who keeps learning, experimenting, building, and
> adapting.

## 9. Future extensions

Content calendar · published-post archive · post performance tracking · hook
library · carousel copy templates · DSA problem roadmap · AI
engineering curriculum · software engineering curriculum · system architecture
curriculum · YouTube content system · LinkedIn-to-YouTube repurposing ·
newsletter strategy · audience feedback system · topic prioritization · content
analytics · brand voice examples · examples of high-performing posts.

*End of v1.7*
