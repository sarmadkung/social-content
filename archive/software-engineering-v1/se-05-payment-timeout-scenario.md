SERIES:    SOFTWARE ENGINEERING #05
TITLE:     A Payment Request Times Out. What Should Your Code Do?
PILLAR:    Software Engineering — for junior and mid-level developers wiring up payments or orders
LEVEL:     INTERMEDIATE
MODE:      SCENARIO
FORMAT:    VISUAL
HEADLINE:  Timed out does not mean failed
LAYOUT:    CAROUSEL
SLIDES:
  02 · GRID · Three stories behind one timeout · never arrived / arrived and failed / charged but the reply was lost, all look the same from your side
  03 · COMPARE · A blind retry charges twice · Pay $49 → timeout → retry → $98, the retry struck through
  04 · FLOW · Step 1: mark it pending · order status "pending", screen text "We are confirming your payment"
  05 · FLOW · Step 2: ask before you act · look up by order ID → "charged" = mark paid, "not found" = safe to try again
  06 · FLOW · Step 3: no answer? Check later · queued check with backoff, and the provider's webhook arriving
  07 · STAT · 10 customers a day stuck here · 10,000 payments a day × 0.1% timeouts = 10
  08 · END · Timeout means "I don't know." Find out first.
STATUS:    draft
---
A customer taps "Pay $49". Your server calls the payment provider with a 5-second timeout. 5 seconds pass. No answer.

Did the card get charged? You do not know.

What would you do?

First, what a timeout tells you (#03): only that you stopped waiting. The request may have:
→ never reached the provider,
→ reached it and failed,
→ reached it, charged the card, and the reply got lost on the way back.
From your side, all three look the same.

What NOT to do first
Retry the charge right away. The retry helper from #04 would happily do it. If case 3 happened, the customer now pays $98.
Also not: show "Payment failed, please try again". Same double charge, now started by a human.

The options, in the order I try them
1. Mark the order "payment pending", not "failed". Show "We are confirming your payment." Reason: say only what you know.
2. Ask before you act. Look up the payment by an ID you sent with the first request, like your order ID. Reason: a read is always safe to repeat.
3. Provider says "charged"? Mark the order paid. Says "not found"? Now a new attempt is safe.
4. The lookup also fails? Do not guess. Queue a check for later, with backoff. Reason: time usually answers the question.
5. Listen for the provider's webhook, a call it makes to your server when the payment settles. Reason: it often arrives before your next check.

In code, the first move is small:
try { await chargeCard(order); }
catch (err) {
  if (err.name !== "TimeoutError") throw err;
  await markPending(order.id);
}

(chargeCard and markPending are placeholders.)

Why this matters at scale
At 10,000 payments a day, a 0.1% timeout rate is 10 customers a day stuck in this exact spot. Each blind retry is a possible refund, a support ticket and a lost customer.

The better fix, built in before it happens
Step 2 only works because the first request carried an ID you can look up. Give every payment attempt its own unique key and send the same key on every try. Then the provider can see a repeat and refuse to charge twice. That idea has a name, and it is the next post.

[PERSONAL: one line about a timeout on a money or order call that left you unsure what happened]

Takeaway: a timeout means "I don't know", not "it failed". Find out before you try again.

Next: idempotency, making "try again" safe.

#SoftwareEngineering #BackendDevelopment #Payments #DistributedSystems #Reliability
