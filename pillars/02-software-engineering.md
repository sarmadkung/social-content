# Pillar 2 — Software Engineering

Visual accent: green `#4ADE80` · Tag: `ENGINEERING`

## Purpose
Help working engineers choose tools and use them well. Most posts compare
real technologies (X vs Y vs Z: when each wins, what it costs, what to pick)
or show how to use one tool properly in production (the settings that matter,
the patterns that hold up, the mistakes that hurt). No explainers of basics:
never "what is HTTP" or "what is an API".

## Failure scenario rule
Every concept, tool or feature a post explains comes with a concrete
production scenario that shows what breaks without it, then why we adopt it.
Model example: a payment call times out, the client retries, and the customer
is charged twice. That is why payment APIs need idempotency keys. In COMPARE
posts, each option gets its own "this is where it hurts" scenario.

## Audience
Mid-level engineers taking ownership of their stack, and seniors weighing
trade-offs. Language stays plain; the ideas assume a working developer.
Posts are LEVEL: INTERMEDIATE or ADVANCED.

## Subsections
The pillar has three subsections. Each has its own folder, series label,
filename prefix and roadmap, and numbers from #01 on its own.

| Subsection | Folder | Series label | Prefix |
| --- | --- | --- | --- |
| Backend | `generated/drafts/software-engineering/backend/` | `SOFTWARE ENGINEERING · BACKEND #NN` | `be` |
| Web | `generated/drafts/software-engineering/web/` | `SOFTWARE ENGINEERING · WEB #NN` | `web` |
| Mobile | `generated/drafts/software-engineering/mobile/` | `SOFTWARE ENGINEERING · MOBILE #NN` | `mob` |
| Stack | `generated/drafts/software-engineering/stack/` | `SOFTWARE ENGINEERING · STACK #NN` | `stack` |

The posting rotation keeps one Software Engineering slot. Each time it comes
up it takes the next subsection in turn: Backend → Web → Mobile → Stack.

Each roadmap line: `#NN Title · MODE · needs <earlier posts in the same
subsection>`. Modes are defined in the master prompt. Never more than 4 TEACH
posts in a row.

The first version of this pillar (one mixed series of basics, from HTTP to
retries) is kept in `archive/software-engineering-v1/`. Its useful parts are
folded into the Backend posts below.

## Backend roadmap
- #01 Postgres vs MongoDB vs DynamoDB: choose by access pattern · COMPARE · needs —
- #02 Node vs Go vs Python (FastAPI) for API services · COMPARE · needs —
- #03 Kafka vs RabbitMQ vs SQS · COMPARE · needs —
- #04 Redis caching done right: cache-aside, write-through, stampedes · TEACH · needs #01
- #05 Background jobs: BullMQ vs Temporal vs cron · COMPARE · needs #03
- #06 Prisma vs Drizzle vs raw SQL · COMPARE · needs #01
- #07 A payment call times out: timeouts, retries and idempotency keys together · SCENARIO · needs #02
- #08 Connection pooling: why Postgres falls over under serverless · WHY · needs #01, #06
- #09 Sessions vs JWT vs managed auth (Clerk, Auth0) · COMPARE · needs —
- #10 Zero-downtime database migrations (expand and contract) · TEACH · needs #01, #06
- #11 REST vs GraphQL vs gRPC: where each one wins · COMPARE · needs #02
- #12 Logs, metrics and traces with OpenTelemetry: what to set up first · TEACH · needs #07
- #13 8 things I check before shipping a backend service · LIST · needs #01–#12

## Web roadmap
- #01 Next.js vs React Router 7 vs Astro · COMPARE · needs —
- #02 SSR vs SSG vs ISR vs CSR: choose per page, not per app · COMPARE · needs #01
- #03 React Server Components: what actually runs where · WHY · needs #02
- #04 TanStack Query vs Redux Toolkit vs Zustand · COMPARE · needs —
- #05 When memo and useMemo are useless (and when they are not) · WHY · needs #04
- #06 Tailwind vs CSS Modules vs CSS-in-JS · COMPARE · needs #03
- #07 Fixing LCP and INP in a real app · TEACH · needs #02, #05
- #08 Playwright vs Cypress · COMPARE · needs —
- #09 7 web performance mistakes I still see in production · LIST · needs #02–#07

## Mobile roadmap
The React Native vs Flutter vs native comparison ("who draws the pixels")
lives in STACK #01, so the Mobile series starts with the Expo deep dive.
- #01 Expo vs bare React Native: is there still a reason to eject? · WHY · needs —
- #02 FlatList vs FlashList: why your list janks · COMPARE · needs —
- #03 Local storage: MMKV vs SQLite vs WatermelonDB · COMPARE · needs —
- #04 OTA updates (EAS Update) vs store releases · COMPARE · needs #01
- #05 Push notifications: Expo push vs FCM and APNs direct · COMPARE · needs #01
- #06 Expo Router vs React Navigation · COMPARE · needs #01
- #07 EAS Build vs Fastlane for releases · COMPARE · needs #04
- #08 7 reasons mobile releases get rejected or rolled back · LIST · needs #04, #07

Merged on 2026-11-19 (old → new): #01 → folded into STACK #01 · #02 → #01 · #03 → #02 · #04–#09 → #03–#08. The old drafts are in `archive/merged-2026-11-19/`.

## Content opportunities
A tool I replaced and why · A migration between two tools · A benchmark I ran
myself · A production bug caused by a tool's default · A config that saved us

## Stack roadmap
Stack posts are the map; Backend, Web and Mobile posts are the deep dives.
A Stack post gives one default pick per job, in a table, and links to the
deep-dive post for the reasoning. It never repeats a deep dive.

Problem-first still applies: the hook is one real decision ("you are starting
a fintech app tomorrow: what do you build each part with?"), and every row
says what goes wrong if you pick the usual wrong choice.

Picks are opinions, labelled honestly: "my default in 2026", never "the best".
Every pick has a "pick something else when ..." line. Claims about speed,
adoption or who uses what get a [FACT_CHECK: claim → source] marker.

- #01 One default stack for each kind of app (backend, web, mobile with who draws the pixels, desktop, AI, data, blockchain) · LIST · needs —
- #02 Backend by job: TypeScript vs Go vs Rust vs Python (CRUD APIs, high throughput, ML serving, scripts) · LIST · needs #01
- #03 Databases by data shape: Postgres, Redis, ClickHouse, a vector DB, S3 · LIST · needs #01
- #04 Blockchain stack: EVM (Solidity, Foundry, viem) vs Solana (Rust, Anchor) · LIST · needs #01
- #05 AI app stack: model API, orchestration, vector store, evals, tracing · LIST · needs #01, #03
- #06 Desktop: Tauri vs Electron vs native · LIST · needs #01
- #07 Infra by stage: what to host on at 0, 10k and 1M users · LIST · needs #01, #03
- #08 The solo-founder MVP stack vs the stack you move to at scale · LIST · needs #01–#07

Merged on 2026-11-19 (old → new): MOBILE #01 (React Native vs Flutter vs native) → folded into #01 · #03 (Mobile by app type) → folded into #01, which now has the per-app-type mobile picks · #04–#09 → #03–#08.
