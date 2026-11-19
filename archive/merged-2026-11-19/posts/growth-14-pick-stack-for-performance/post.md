> ⚠ NOT READY — resolve these, then delete this block:
> - [FACT_CHECK: PyTorch and NumPy run their heavy computation in C/C++ (and CUDA on GPUs); Polars is written in Rust; DuckDB and ClickHouse are columnar, vectorised engines → official docs / repos of each project]
> - [FACT_CHECK: WebAssembly runs close to native performance for CPU-heavy code → MDN / webassembly.org and published benchmarks]
> - [FACT_CHECK: DuckDB reads CSV files directly and runs queries in parallel across CPU cores → DuckDB documentation]
> - [PERSONAL: a real case where you picked a stack for performance, data or native support rather than familiarity (a Go or Rust service, a native app, a data engine), and what it changed]

---

Say your app imports a customer's 2 GB CSV file every night.
You wrote the import in Node.js, because the team knows JavaScript. It reads one row at a time on one thread. It takes 40 minutes, and 7 of the server's 8 cores sit idle.
Customers grow. The files grow. Now the import runs into the morning.

Five years ago, moving that job to Go or Rust meant learning a new language or hiring for it. Today an agent writes the first version in a day, and you review it.

The question
If agents write most of the code, why do we still pick a stack because we already know it?

The reason, step by step
1. We picked the stack we knew because writing code was the expensive part. Learning a language took months. Hiring for it took longer.
2. Agents cut that cost. They write Go, Rust, Swift, Kotlin and SQL, and you review the result.
3. Running the code did not get cheaper. Performance, memory use and the cloud bill come from the runtime, not from who typed the code.
4. Apps now carry far more data and computation than before: AI features, search, sync, logs and analytics.
5. So the question moves from "what do we know?" to "what does this job need to run well?"

What used to decide the stack?
The old order of questions:
→ What does the team already know?
→ How fast can we write it?
→ Who can we hire for it?
→ Last, if at all: how fast will it run?
Agents made the first two much cheaper. The third matters less when an agent writes and a person reviews. The last one did not change at all.
Takeaway: writing code got cheap. Running it didn't.

Why do performance and native support matter more now?
→ More data per user: messages, files, events, and embeddings (lists of numbers that capture meaning, used for AI search).
→ More work per request: ranking, AI calls, image processing, real-time sync.
→ AI calls are already slow. A model call can take seconds, so the rest of the request has no time to waste.
→ The cloud bill follows CPU and memory. Say one runtime needs twice the memory per request: under the same load, you pay for about twice the servers.
→ Users feel it: native apps start faster and scroll smoother than apps that run through an extra layer (DEV GROWTH #13).
Takeaway: more data and more compute make the runtime a product decision.

Which stack fits which job?
"Native" here means code that runs directly on the machine or the OS, with no interpreter, embedded browser or extra framework layer in between.
→ Heavy CPU work (parsing, images, video, compression) → Rust, Go, C++ → compiled to machine code, uses every core
→ Many open connections (chat, live updates) → Go, Rust, Elixir → thousands of light tasks at low cost
→ Big data queries → DuckDB, ClickHouse, Polars → columnar engines work on whole columns in batches, not one row at a time
→ AI and ML → Python on top, native code underneath → PyTorch and NumPy do the heavy maths in C, C++ and CUDA; Python is the glue
→ Phone and desktop apps → Swift, Kotlin → native UI and new OS features on day one (DEV GROWTH #13)
→ Heavy work in the browser → WebAssembly, Web Workers → close to native performance, off the UI thread
→ Web UI, simple APIs, glue code → TypeScript is still fine → the database or the network is the bottleneck, not the language
Takeaway: pick per job, not one language for everything.

[FACT_CHECK: PyTorch and NumPy run their heavy computation in C/C++ (and CUDA on GPUs); Polars is written in Rust; DuckDB and ClickHouse are columnar, vectorised engines → official docs / repos of each project]
[FACT_CHECK: WebAssembly runs close to native performance for CPU-heavy code → MDN / webassembly.org and published benchmarks]

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
Takeaway: move the hot path to the right engine. Leave the rest alone.

[FACT_CHECK: DuckDB reads CSV files directly and runs queries in parallel across CPU cores → DuckDB documentation]

What do you still need to know?
Familiarity is no longer the reason to pick a stack. You still need enough of it to own what ships:
→ Read it. You review the agent's diff (DEV GROWTH #10). You can't approve Rust you can't read.
→ Measure it. Run a profiler and a benchmark on real-size data.
→ Run it. Deploy it, monitor it, and debug it when it fails at 2 a.m.
→ Know what sits under every language: memory, threads, I/O and how data is laid out (DEV GROWTH #07). This carries from one stack to the next.
DEV GROWTH #12 said pick tools you can review. That is still the floor. Above it, the job decides, not habit.
Takeaway: you don't need years in a language. You need to read, measure and run it.

[PERSONAL: a real case where you picked a stack for performance, data or native support rather than familiarity (a Go or Rust service, a native app, a data engine), and what it changed]

Watch out: what a faster stack costs
→ Two languages → more builds, and data passed between them → move only the hot path, behind one clear boundary (an API, a queue or a file)
→ Fewer reviewers → only one person on the team reads Rust → don't ship what nobody else can review; Go is often easier to share
→ Faster for nothing → the bottleneck was a slow query or the network → profile first; a missing index is slow in every language
→ Missing libraries → the package you need exists only for Python or JavaScript → check the libraries before you switch

What goes wrong if you ignore this
→ You keep the stack you know out of habit, and pay for it for years in servers, slow screens and night jobs that never finish.
→ Or the opposite: you rewrite everything in Rust because it is fast, and the real problem was one missing database index.

Keep in mind before you pick a stack with agents
→ Profile first: switch only for a measured bottleneck
→ Mix stacks: a Go worker and a TypeScript UI is normal
→ Write the time target before the agent writes code
→ Test with real-size data, not 100 rows
→ Only ship a language someone can review

Takeaway
Agents made code cheap to write, not cheap to run. Pick the stack for what the job needs, then learn enough of it to review, measure and run it.

Next: how to break a problem down before you code.

#SoftwareEngineering #Performance #CodingAgents #DeveloperGrowth #SystemDesign
