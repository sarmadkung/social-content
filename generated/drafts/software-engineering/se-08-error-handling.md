SERIES:    SOFTWARE ENGINEERING #08
TITLE:     Error Handling: Fail Loudly, Recover Deliberately
PILLAR:    Software Engineering — for students and junior developers moving to production code
LEVEL:     INTERMEDIATE
MODE:      TEACH
FORMAT:    VISUAL
HEADLINE:  Fail loudly. Recover on purpose.
LAYOUT:    COMPARE
STATUS:    draft
---
The worst bug is not the one that crashes. It is the one that fails silently and nobody notices for weeks.

What is it?
Error handling is how your code reacts when something goes wrong.
"Fail loudly" means errors are visible, never hidden. "Recover deliberately" means you only catch an error when you have a real plan for it.
Think of a smoke alarm. A loud one is annoying. A silent one is dangerous.

Why do we need it?
An empty catch block hides the problem. The app keeps running with bad data, and the real cause is gone. Later you see strange results and have no clue where they came from.

Key properties
→ Expected errors (wrong password, item out of stock) are normal. Handle them and show a clear message.
→ Unexpected errors (database down, a bug) should reach a central handler, get logged and trigger an alert.
→ Catch only where you can act: retry, use a fallback, or add context.
→ When you rethrow, keep the original error as the cause.
→ Fail fast at startup. Missing config should stop the app, not break it at 3 a.m.

Where is it used?
Express error middleware, React error boundaries, Node.js, which stops the process on an unhandled promise rejection by default (since v15).

When to use a catch: when you can recover or add useful context.
When not to: just to make the red text go away.

Example
// Bad: the error disappears
try { await saveOrder(order); } catch {}

// Better: add context, keep the cause
try { await saveOrder(order); }
catch (err) {
  throw new Error(`saveOrder failed: ${order.id}`, { cause: err });
}

Now the log says which order failed and still shows the real database error underneath.

Comparison
Fail fast: stop right away when continuing would cause damage (bad config, broken data).
Graceful degradation: keep working with less, like showing cached prices when the pricing service is down. Choose this on purpose, and still log it.

Takeaway: never swallow an error. Handle it, or pass it up with more context.

Next: logging vs metrics vs traces, the basics of seeing what your system is doing.

#SoftwareEngineering #CleanCode #JavaScript #BackendDevelopment
