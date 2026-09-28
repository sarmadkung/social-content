SERIES:    SOFTWARE ENGINEERING · BACKEND #02
TITLE:     Node vs Go vs Python (FastAPI) for API Services
PILLAR:    Software Engineering · Backend — for mid-level and senior engineers choosing a service runtime
LEVEL:     INTERMEDIATE
MODE:      COMPARE
FORMAT:    VISUAL
HEADLINE:  Your API waits on I/O. Choose accordingly.
LAYOUT:    COMPARE
STATUS:    draft
---
Most API requests spend most of their time waiting: on the database, on another service, on the network.
So the runtime rarely decides your speed. How it handles waiting, and CPU work, does.

Node.js
One main thread runs your code. An event loop switches between requests while they wait on I/O.
Great for I/O-heavy APIs. Same language as your frontend.
The catch: any CPU-heavy work blocks every request on that process.

app.get("/hash", (req, res) => {
  const h = bcrypt.hashSync(req.query.pw, 12); // every other request waits
  res.send(h);
});

Fix: use the async bcrypt.hash, or move heavy work to worker threads.

[FACT_CHECK: bcrypt (npm) async hash runs off the main thread via the libuv thread pool → bcrypt package docs]

Go
Goroutines: very cheap threads that the runtime spreads over all CPU cores.
Blocking code is fine, because only that goroutine waits.
One static binary, low memory, fast startup. More verbose, fewer "batteries included" frameworks.

Python (FastAPI)
Async handlers, type hints, and OpenAPI docs generated for free.
The best fit when the service sits next to ML or data code.
The catch: the GIL (global interpreter lock) lets one thread run Python code at a time, so you scale with several worker processes.

[FACT_CHECK: CPython GIL limits one thread to running Python bytecode at a time; free-threaded builds are optional/experimental → Python docs for the version you run]

The trade-off
→ CPU work in a request: Go handles it; Node and Python need workers
→ Team and code sharing: Node wins with a TypeScript frontend
→ ML and data libraries: Python wins
→ Memory per instance and cold start: Go wins
→ Hiring: Node and Python pools are larger in most markets

When to pick each
→ Node: I/O-heavy APIs, TypeScript full-stack teams
→ Go: high concurrency, CPU-heavy steps, small containers, infra tools
→ Python: services that wrap models, data pipelines, internal tools

Common mistake
In FastAPI, calling a blocking library (like requests) inside an async def handler. It freezes the event loop, just like hashSync in Node. Use an async client, or a plain def handler so it runs in a thread pool.

Common wrong choice
Rewriting in Go "for speed" when 80% of each request is one slow SQL query. Measure first. The fix is often an index.

Takeaway: pick the runtime for your team and your CPU work, not for benchmark charts.

Next: Kafka vs RabbitMQ vs SQS.

#BackendDevelopment #NodeJS #Golang #Python
