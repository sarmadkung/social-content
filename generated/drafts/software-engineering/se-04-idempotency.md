SERIES:    SOFTWARE ENGINEERING #04
TITLE:     Idempotency: Making "Try Again" Safe
PILLAR:    Software Engineering — for junior and mid-level developers building payments, orders or queues
HEADLINE:  Make "try again" safe
LAYOUT:    COMPARE
---
Your payment call times out. Did the customer get charged? You don't know. If you retry, you might charge them twice.

What is it?
An operation is idempotent when doing it once or many times gives the same result.
Think of a lift button. Press it once or five times, the lift still comes once.

Why do we need it?
Timeouts and retries (the last two posts) mean the same request can arrive more than once. A timeout does not tell you if the work happened. Without idempotency, "try again" can create two orders, two emails, or two charges.

Key properties
→ In HTTP, GET, PUT and DELETE are idempotent by design. POST is not.
→ Idempotent is about the effect, not the response. A second DELETE may return 404, but nothing new changes.
→ For POST, the client sends an idempotency key: a unique ID for this one action.
→ The server saves the key with the result. Same key again? Return the saved result. Do not repeat the work.
→ Keys need an expiry, so the store does not grow forever.

Where is it used?
Stripe's Idempotency-Key header, message queues that deliver "at least once" (so a message can arrive twice), webhook handlers, background jobs.

When to use it: anything with money, stock, emails or side effects that can be retried.
When not to: pure reads. They are already safe to repeat.

Example
async function charge(key, amount) {
  const saved = await db.findPayment(key);
  if (saved) return saved;
  const payment = await gateway.charge(amount);
  await db.savePayment(key, payment);
  return payment;
}

(db and gateway are placeholders.)

The senior detail: two copies of the same request can arrive at the same moment. Both see "no saved payment" and both charge. Fix it by claiming the key first with a unique database constraint, then doing the work.

Comparison
Without a key: retry = maybe a second charge.
With a key: retry = the first result, returned again.

[PERSONAL: one line about a duplicate order, email or charge you have had to track down]

Takeaway: retries are only safe when the operation is idempotent.

Next: error handling, fail loudly and recover deliberately.

#SoftwareEngineering #APIDesign #DistributedSystems #BackendDevelopment
