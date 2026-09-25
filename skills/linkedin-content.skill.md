
---
name: linkedin-content
description: Use when writing, planning, or reviewing LinkedIn content for Muhammad Sarmad — enforces positioning, the three content pillars, series labels, and tone.
version: 1.4
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

For a `COPY` or `FULL` request (see section 0), the text portion is:

1. A series label line (e.g. `DSA SERIES #04`).
2. A title line.
3. The post body, ready to paste — no markdown headers, short paragraphs.
4. A one-line note on which pillar it serves and who it is for.

---

## 0. Request keywords

Every request begins with one keyword that sets what to return. Honor it
exactly — do not return more than asked, and do not return less.

| Keyword | Return | Skills to apply |
| --- | --- | --- |
| `COPY` | Post text only. No image, no HTML. | content skill only |
| `VISUAL` | The generated image itself. No post text. | visual skill only |
| `FULL` | Post text **and** the generated image, in that order. | both skills |
| `VISUAL-HTML` | HTML that renders the image, for pixel-exact output. | visual skill only |

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
engineers.

## 4. Three content pillars

Do not create a separate pillar for every technology. There are three.

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

*Infrastructure / architecture* — PostgreSQL, MongoDB, Redis, Docker, AWS,
CI/CD, scalability, observability, testing.

Focus on real engineering problems: architecture decisions, system design,
trade-offs, performance, scalability, reliability, developer experience,
maintainability, testing strategy, production engineering, lessons from real
products.

Demonstrate **hands-on engineering experience**, not generic framework
tutorials.

### Pillar 3 — AI engineering

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
- **All three** — building reliable AI systems requires strong fundamentals,
  sound architecture, and an understanding of modern AI capabilities.

Overall narrative: **strong fundamentals + practical software engineering +
system architecture + modern AI engineering.**

## 6. Series system

Use recognizable series labels:

```
DSA SERIES #01            Reclaiming Data Structures & Algorithms
DSA SERIES #02            Hash Maps: The Pattern Behind Two Sum
AI ENGINEERING #01        What Actually Makes an AI Agent an Agent?
SOFTWARE ENGINEERING #01  Designing Reliable APIs
SYSTEM ARCHITECTURE #01   Designing Systems That Scale
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

*End of v1.4*
