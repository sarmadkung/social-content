SERIES:    SOFTWARE ENGINEERING #02
TITLE:     Timeouts: The Setting Every Network Call Needs
PILLAR:    Software Engineering — for students and junior developers writing their first backend calls
LEVEL:     BEGINNER
FORMAT:    VISUAL
HEADLINE:  Every network call needs a timeout
LAYOUT:    STATEMENT
STATUS:    draft
---
A slow service is more dangerous than a dead one.

A dead service fails fast. A slow one makes your app wait, and wait, and wait.

What is it?
A timeout is the longest time your code will wait for an answer before it gives up.
Think of meeting a friend at a café. You decide: "If they are not here in 15 minutes, I leave." Without that rule, you could sit there all day.

Why do we need it?
Every waiting request holds memory and an open connection. If one service your app depends on gets slow, those waiting requests pile up. Soon your own app runs out of room and slows down too. One slow service can drag down everything that calls it.

Key properties
→ fetch has no timeout option. You add one with an AbortSignal.
→ Pick the number from real data: a bit above your p99 (the time 99 of 100 requests finish within).
→ The timeout of an inner call must be shorter than the timeout of the request that called it.
→ A timeout does not mean the work failed. The server may still finish it. (More on that in #04.)

Where is it used?
HTTP calls to other services, database queries, payment gateways, LLM APIs, message queue consumers.

When to use it: on every call that leaves your process.
When not to: there is no "not". Only the number changes.

Example
const res = await fetch(url, {
  signal: AbortSignal.timeout(2000),
});

After 2 seconds the call stops and throws a TimeoutError you can handle.

Comparison
Timeout: "each call may take at most 2s."
Deadline: "the whole request must finish within 3s." Every inner call gets only what is left of that budget.

[PERSONAL: one line about a slow dependency you saw take down or stall a service]

Takeaway: a missing timeout is a decision to wait forever.

Next: retries with backoff, and why infinite retries cause outages.

#SoftwareEngineering #BackendDevelopment #Reliability #WebDevelopment
