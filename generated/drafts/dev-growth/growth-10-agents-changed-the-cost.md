SERIES:    DEV GROWTH #10
TITLE:     Agents Made Code Cheap to Write. Pick the Stack for How It Runs.
PILLAR:    Career & Developer Growth — for mid-level and senior engineers and founders choosing a stack in the agent era
LEVEL:     INTERMEDIATE
MODE:      WHY
FORMAT:    VISUAL
HEADLINE:  Code got cheap to write, not to run
LAYOUT:    COMPARE
VISUALS:   1 = What used to decide the stack? · 2 = What did cross-platform do for us, and who does it now? · 3 = How do separate apps stay in sync? · 4 = Which stack fits which job? · 5 = What changes in a real job? · 6 = What do you still need to know? · rest = text
STATUS:    draft
---
Two habits picked most stacks for the last ten years.

"We need it on every platform" had one answer: one codebase. React Native or Flutter for phones. Electron for desktop. Ionic to wrap the web app in a mobile shell.

"We need it built" had one answer too: the language the team already knows. So the nightly import of a customer's 2 GB CSV file is in Node.js. It reads one row at a time on one thread. It takes 40 minutes, and 7 of the server's 8 cores sit idle. Customers grow, the files grow, and now the import runs into the morning.

Both were the right call. Writing code was the most expensive part of building software. Writing the same feature twice, or learning a new language for one job, cost months.

Coding agents just made that part cheap.

The question
If an agent can build a feature in Swift and port it to Kotlin in an afternoon, or write the Go version of a slow job in a day, why do we still pick a stack for one codebase or for familiarity?

The reason, step by step
1. Cross-platform was never about better apps. It was about cost: one team instead of one per platform.
2. We picked the stack we knew for the same reason. Learning a language took months. Hiring for it took longer.
3. Agents cut both costs. They write Swift, Kotlin, Go, Rust and SQL, and you review the result.
4. Running the code did not get cheaper. Performance, memory use and the cloud bill come from the runtime, not from who typed the code.
5. Apps now carry far more data and computation than before: AI features, search, sync, logs and analytics.
6. So the question moves from "what do we know, and what runs everywhere?" to "what does this job need to run well?"

What used to decide the stack?
The old order of questions:
→ What does the team already know?
→ How fast can we write it?
→ Can one codebase cover every platform?
→ Who can we hire for it?
→ Last, if at all: how fast will it run?
Agents made the first three much cheaper. Hiring matters less when an agent writes and a person reviews. The last one did not change at all.

Why it matters more now:
→ More data per user: messages, files, events, and embeddings (lists of numbers that capture meaning, used for AI search).
→ More work per request: ranking, AI calls, image processing, real-time sync.
→ AI calls are already slow. A model call can take seconds, so the rest of the request has no time to waste.
→ The cloud bill follows CPU and memory. Say one runtime needs twice the memory per request: under the same load, you pay for about twice the servers.
→ Users feel it: native apps start faster and scroll smoother than apps that run through an extra layer.

Takeaway: writing code got cheap. Running it didn't.

What did cross-platform do for us, and who does it now?
A cross-platform framework lets you write an app once and run it on several platforms (iOS, Android, web, desktop). Every job it did now has another owner:
→ One codebase → the agent writes each app from one spec
→ One skill set → the agent knows Swift, Kotlin and C#; you need to review them, not master all of them
→ Feature parity → a shared spec + the same test scenarios on every app
→ Shared business logic → it lives in the backend, or in API clients generated from one contract

The tax you paid for one codebase:
→ Performance: an extra layer sits between your code and the OS (a JS runtime, an embedded browser or a custom renderer). In React Native, one JS thread does the work; when it is busy, lists stutter and animations drop frames. Startup is slower and apps are bigger, because you ship the framework on top of your code.
→ One fix breaks another platform: a shared component fixed for Android looks wrong on iOS; a web fix uses a browser-only API and crashes the mobile app. Every change is tested on every platform.
→ UI that never quite fits: keyboard, safe areas, gestures and scrolling differ per platform, and `if (Platform.OS === 'web')` checks spread until nobody trusts a component.
→ Upgrades and late OS features: a framework upgrade can break half your dependencies, and new OS features arrive weeks or months late.
→ Native code anyway: widgets, share extensions, the camera and background work, and crashes you debug across three layers.

It is not just mobile. Each "write once, run everywhere" tool hurts in its own way:
→ Electron ships its own copy of Chromium and Node.js inside every app. Big downloads, high memory, even for a simple chat window.
→ Flutter draws its own widgets instead of using the platform's. It looks close, but a new OS design arrives only when Flutter redraws it.
→ Ionic runs your web app inside a WebView (a browser view embedded in the app). Scrolling, gestures and the keyboard feel like a website.
→ .NET MAUI replaced Xamarin, and Xamarin support ended. Teams had to migrate whole apps just to stay supported.
→ React Native Web shares components between the browser and the phone. Browser-only code slips into a shared file and crashes the mobile app.

The middle ground: Kotlin Multiplatform can share just the logic and keep each platform's UI native. That is the same split this post argues for.

What you get back: new OS features on day one (widgets, Live Activities, App Intents, new camera APIs), real native look and gestures, platform tools that just work (Xcode Instruments, Android Studio profiler), and smaller apps.

Takeaway: cross-platform solved the cost of writing it twice. Agents solve that cost too.

How do separate apps stay in sync?
This is the part people worry about. Without one codebase, the apps drift apart. Here is the loop that stops it:
1. Write the feature spec once: screens, states, API calls, edge cases. Platform-neutral.
2. The agent builds it on one platform first.
3. The agent ports it to the others, using the spec and the first diff as the reference.
4. One API contract (OpenAPI or protobuf) generates the client code for every app, so the data layer cannot drift.
5. The same test scenarios run on every app (for example, one set of Maestro flows for iOS and Android).
6. Review checks parity: same states, same errors, same edge cases. (How to review agent code: DEV GROWTH #07.)

I've lived this: a product I work on went from one Expo codebase for iOS, Android, web and desktop to native iOS and Android. The full story is its own post (BUILDING #01).

Takeaway: one spec, one API contract and shared tests do the job one codebase used to do.

Which stack fits which job?
"Native" here means code that runs directly on the machine or the OS, with no interpreter, embedded browser or extra framework layer in between.
→ Heavy CPU work (parsing, images, video, compression) → Rust, Go, C++ → compiled to machine code, uses every core
→ Many open connections (chat, live updates) → Go, Rust, Elixir → thousands of light tasks at low cost
→ Big data queries → DuckDB, ClickHouse, Polars → columnar engines work on whole columns in batches, not one row at a time
→ AI and ML → Python on top, native code underneath → PyTorch and NumPy do the heavy maths in C, C++ and CUDA; Python is the glue
→ Phone apps → Swift, Kotlin → native UI and new OS features on day one
→ Desktop → native where the OS is the product, or stay on web where it is fast enough
→ Heavy work in the browser → WebAssembly, Web Workers → close to native performance, off the UI thread
→ Web UI, simple APIs, glue code → TypeScript is still fine → the database or the network is the bottleneck, not the language

[FACT_CHECK: PyTorch and NumPy run their heavy computation in C/C++ (and CUDA on GPUs); Polars is written in Rust; DuckDB and ClickHouse are columnar, vectorised engines → official docs / repos of each project]
[FACT_CHECK: WebAssembly runs close to native performance for CPU-heavy code → MDN / webassembly.org and published benchmarks]

Takeaway: pick per job and per platform, not one language for everything.

What changes in a real job?
Back to the nightly import.
Before: Node.js reads the file row by row on one thread. Say 40 minutes, with 7 cores idle.
Option A: load the CSV into DuckDB and do the totals in SQL. The engine reads in columns and uses every core.
Option B: the agent rewrites only the parser in Go or Rust, with one worker per core.
The rest of the app stays in TypeScript. Only the hot path moves (the small part of the code where most of the time goes).
Your part:
→ Write the spec: input, output, and a time target ("a 2 GB file in under 5 minutes").
→ Give the agent the same test file the old version used.
→ Review the diff, then run the benchmark on the real-size file, before and after.

[FACT_CHECK: DuckDB reads CSV files directly and runs queries in parallel across CPU cores → DuckDB documentation]

Takeaway: move the hot path to the right engine. Leave the rest alone.

What do you still need to know?
Familiarity is no longer the reason to pick a stack. You still need enough of it to own what ships:
→ Read it. You review the agent's diff (DEV GROWTH #07). You can't approve Rust or Kotlin you can't read.
→ Measure it. Run a profiler and a benchmark on real-size data.
→ Run it. Deploy it, monitor it, and debug it when it fails at 2 a.m.
→ Know what sits under every language: memory, threads, I/O and how data is laid out (DEV GROWTH #05). This carries from one stack to the next.
DEV GROWTH #09 said know your stack well enough to review it. That is still the floor. Above it, the job decides, not habit.

Takeaway: you don't need years in a language. You need to read, measure and run it.

[PERSONAL: a real case where you picked a stack for performance, data or native support rather than familiarity (a Go or Rust service, a native app, a data engine), and what it changed]

Watch out: what this costs
→ Review grows → the agent writes two apps or two languages, someone still checks both → have a reviewer who can read each one; don't ship what nobody else can review (Go is often easier to share than Rust)
→ More pipelines → two builds, two store reviews, data passed between languages → automate builds, ship both apps the same day, move only the hot path behind one clear boundary (an API, a queue or a file)
→ Platform-only bugs and drift → a fix lands on iOS and Android still has the bug → one spec, one API contract, the same test scenarios on every app, parity checks in review
→ Faster for nothing → the bottleneck was a slow query or the network → profile first; a missing index is slow in every language
→ Missing libraries → the package you need exists only for Python or JavaScript → check the libraries before you switch

When the old pick still wins
→ You share real logic and UI with a React web app
→ Nobody on the team can review Swift, Kotlin or the other language
→ The app is simple forms and lists, and the OS is not part of the product
→ Desktop, where the web app is fast enough. We kept ours on web.
→ The job waits on the database or the network, not on the language

What goes wrong if you ignore this
→ You start a new app on a cross-platform stack, or keep a slow job in the language you know, out of habit, and pay for years in servers, slow screens and night jobs that never finish.
→ Your app gets new OS features last, after competitors who went native.
→ Or the opposite: you go native with no spec and no shared tests, and the apps drift apart in a month. Or you rewrite everything in Rust, and the real problem was one missing database index.

Keep in mind before you pick a stack with agents
→ Decide per platform and per job: phones, desktop and a nightly import need different answers
→ Profile first: switch only for a measured bottleneck
→ Write the spec and the time target before the agent writes code
→ Generate API clients from one contract, never by hand
→ Test with real-size data, not 100 rows
→ Only ship a language someone can review
→ Keep web where it is fast enough; native has to earn its cost

Takeaway: agents made code cheap to write, not cheap to run. Pick the stack for what each job and each platform needs, then learn enough of it to review, measure and run it.

Next: before you code. How to break a problem down, and 5 questions to ask before any task.

#SoftwareEngineering #CodingAgents #CrossPlatform #Performance #DeveloperGrowth
