SERIES:    SOFTWARE ENGINEERING #03
TITLE:     Retries with Backoff (and Why Infinite Retries Cause Outages)
PILLAR:    Software Engineering — for junior and mid-level developers calling other services
LEVEL:     BEGINNER
HEADLINE:  Retry slower each time, then stop
LAYOUT:    FLOW
STATUS:    draft
---
A retry can fix a small failure. Too many retries can turn it into an outage.

What is it?
A retry means trying a failed call again. Backoff means waiting longer before each new try.
Think of calling a friend whose line is busy. You wait a minute, then five, then ten. You do not redial 100 times in a row.

Why do we need it?
Many failures are short: a network blip, a server restarting. Trying again a moment later often works.
But when a service is overloaded, instant retries add even more load. Now it can never recover. This is called a retry storm.

Key properties
→ Retry only temporary errors: timeouts, 503 (service unavailable), 429 (too many requests).
→ Never retry errors that will fail again, like 400 (bad request).
→ Cap the attempts. Three is a common default.
→ Add jitter: a small random extra wait, so thousands of clients do not retry at the same moment.
→ Retries multiply. Three layers that each try 3 times can send 27 calls to the bottom service.

Where is it used?
AWS SDKs, gRPC retry policies, job queues like BullMQ, HTTP clients that call payment or email providers.

When to use it: short, temporary failures on safe operations.
When not to: validation errors, or actions that are not safe to repeat (next post).

Example
async function withRetry(call) {
  for (let i = 0; i < 3; i++) {
    try { return await call(); }
    catch (e) { if (i === 2) throw e; }
    const wait = 100 * 2 ** i + Math.random() * 100;
    await new Promise((r) => setTimeout(r, wait));
  }
}

Attempt 1 fails, wait about 100ms. Attempt 2 fails, wait about 200ms. Attempt 3 fails, give up and throw.

Comparison
Fixed delay: every client waits the same, then hits the server together.
Exponential backoff with jitter: waits grow and spread out, so the server gets room to breathe.

Takeaway: retry a few times, wait longer each time, add randomness, then stop.

Next: idempotency, the property that makes "try again" safe.

#SoftwareEngineering #DistributedSystems #Reliability #BackendDevelopment
