> ⚠ NOT READY — resolve these, then delete this block:
> - [FACT_CHECK: Tauri uses the OS web view (WebView2, WKWebView, WebKitGTK) and produces installers of a few MB, while Electron bundles Chromium and Node.js (installers usually 80-150 MB) → tauri.app and electronjs.org docs]
> - [FACT_CHECK: ClickHouse and DuckDB are columnar engines that run queries in parallel across CPU cores → clickhouse.com and duckdb.org docs]
> - [FACT_CHECK: pgvector adds vector similarity search to Postgres; Foundry is a Solidity testing and fuzzing toolkit; viem is a TypeScript client for EVM chains; Anchor is the main Rust framework for Solana programs; OpenZeppelin publishes audited Solidity contracts → each project's docs]
> - [PERSONAL: one of these wrong picks you have seen or fixed in a real project, and what it cost — for example the move from one cross-platform codebase to native apps (BUILDING #01)]

---

A founder needs a web app, an API, iOS and Android apps, an AI assistant and a sales dashboard. The team is four engineers.
What do you build each part with?

The usual answers are "whatever we already know" for every part, or "whatever is new" for every part. Both cost you later: a rewrite, a slow app, or a service only one person can review.

Why a default matters
Most stack mistakes are not visible on day one. They show up 6 to 12 months later, when the app has users and changing the stack means a rewrite.
A default is the pick you start from unless the project gives you a reason not to. It saves you from re-arguing the same choice on every project, and the "pick something else when" line tells you exactly when to leave it.
These are my defaults in 2026. They are opinions with reasons, not rules. DEV GROWTH #10 explains why the runtime matters more now that agents write most of the code; this post is the map.

What do you build the product with?
→ Web app (SaaS, dashboards) → TypeScript + React (Next.js) + Postgres
   Why: one language across UI and server code, the biggest library and hiring pool, server rendering for pages that must load fast and rank in search.
   Pick something else when: the site is mostly content (blog, docs, marketing) → Astro, which ships almost no JavaScript (WEB #01).
→ Mobile app → Swift (SwiftUI) for iOS, Kotlin (Jetpack Compose) for Android
   Why: new OS features on day one, usually the fastest start and smoothest scrolling, and no extra layer between your code and the phone. Agents cut the cost of keeping two codebases (DEV GROWTH #10).
   Pick something else when: simple screens, a very small team and no camera, Bluetooth or widget work → React Native (Expo) or Flutter (MOBILE #01).
→ Desktop app → Tauri (a Rust core with a web UI)
   Why: it uses the web view the operating system already has, so the installer is a few MB, not 100+ MB.
   Pick something else when: you need identical rendering on every OS or Node.js libraries in the app → Electron. A pro tool tied to one OS → native (SwiftUI on macOS, WinUI on Windows).
Takeaway: The product side goes native where users feel it, web where reach matters.

[FACT_CHECK: Tauri uses the OS web view (WebView2, WKWebView, WebKitGTK) and produces installers of a few MB, while Electron bundles Chromium and Node.js (installers usually 80-150 MB) → tauri.app and electronjs.org docs]

What runs behind it?
→ API and services → Go + Postgres
   Why: one small binary, cheap concurrency (goroutines are light threads the runtime schedules for you), fast startup, low memory, and code that is easy to read in review.
   Pick something else when: a hot path burns CPU (parsing, media, compression) → Rust for that part only. An all-TypeScript team with a simple CRUD API that mostly waits on the database → Node.js is fine (BACKEND #02).
→ App data → Postgres
   Why: transactions, joins, JSON columns and full-text search in one database. One store is one thing to back up, secure and keep in sync.
   Pick something else when: a measured access pattern Postgres can't serve, such as a huge key-value workload → DynamoDB (BACKEND #01).
→ Analytics and reporting → ClickHouse, or DuckDB for files and batch jobs
   Why: columnar engines read only the columns a query needs and use every core, so a scan over millions of rows takes seconds, not minutes.
   Pick something else when: the data is small (a few million rows) → a Postgres read replica is enough.
Takeaway: Go and Postgres cover most backends. Add engines only for a measured need.

[FACT_CHECK: ClickHouse and DuckDB are columnar engines that run queries in parallel across CPU cores → clickhouse.com and duckdb.org docs]

What about AI and blockchain?
→ AI features (chat, search, agents) → a hosted model API + your existing backend + Postgres with pgvector + tracing and evals from day one
   Why: most AI features are model calls, context and evaluation, not training. pgvector stores embeddings (lists of numbers that capture meaning) next to the data they describe, so deleting a document can delete its embeddings in the same transaction.
   Pick something else when: you train or fine-tune models → Python (PyTorch). Tens of millions of vectors with heavy filtering → a dedicated vector database.
→ Smart contracts → EVM chains: Solidity + Foundry for tests and fuzzing + viem in the client
   Why: the largest pool of auditors, tools and audited libraries such as OpenZeppelin.
   Pick something else when: you build on Solana for high throughput and low fees → Rust + Anchor.
Takeaway: AI reuses your stack. Blockchain needs audited tools, because deployed bugs stay.

[FACT_CHECK: pgvector adds vector similarity search to Postgres; Foundry is a Solidity testing and fuzzing toolkit; viem is a TypeScript client for EVM chains; Anchor is the main Rust framework for Solana programs; OpenZeppelin publishes audited Solidity contracts → each project's docs]

Where does the usual pick hurt?
Each default exists because the usual pick fails in a known way. Numbers are illustrative.
→ Cross-platform for a hardware-heavy app → the app is mostly camera, Bluetooth and widgets → you write native modules anyway, now in three languages instead of two.
→ Electron for a small tray utility → say a 150 MB download and 200 MB of RAM to show a menu → users uninstall it.
→ Rust for a CRUD API → the service waits on the database 90% of the time → slower to change and fewer reviewers, for no speed you can measure.
→ Dashboards on the main Postgres → a "revenue for the last 90 days" query scans 50 million rows → it competes with checkout for CPU and disk, and checkout slows down while it runs.
→ A separate vector database on day one for 50,000 documents → a second store to keep in sync → a deleted contract still shows up in the assistant's answers.
→ Your own token or access-control contract instead of an audited library → one missed check → funds are lost, and unless you built an upgrade path, a deployed contract can't be patched like a server.
Takeaway: The wrong pick rarely fails on day one. It fails at scale or in review.

[PERSONAL: one of these wrong picks you have seen or fixed in a real project, and what it cost — for example the move from one cross-platform codebase to native apps (BUILDING #01)]

Keep in mind before you pick a stack
→ Start from the default; leave it only for a named reason
→ Write that reason down in one line, with the date
→ One database until a real query proves you need two
→ Fewer languages beat the perfect language per part
→ Check the libraries you need exist before you commit

Watch out: what defaults cost
→ Defaults age → a 2026 pick may be wrong by 2028 → review them at the start of each new project, not in the middle of one
→ A default turns into habit → nobody asks the "something else when" question → ask it for every new part, out loud

Takeaway
Start every part of the app from a default you can defend, and know the one signal that would make you leave it.

Next: Backend by job: TypeScript vs Go vs Rust vs Python.

#SoftwareEngineering #TechStack #Backend #MobileDevelopment #SystemDesign
