An AI tool writes a function. It passes the tests. It runs fine on 100 rows.

In production, with 100,000 rows, the page times out.

Why fundamentals still matter when AI writes the code:
[images: 1]
---
The code checked every order with blockedIds.includes(order.userId).

includes() walks the list one item at a time. 100,000 orders × 100,000 IDs is up to 10 billion checks.

A Set makes each lookup about one step on average.
---
Your job moves from typing to judging. You can't judge code you couldn't have written.

AI code looks right. The bugs hide one level down: scale, things running at the same time, network failures.
[images: 2]
---
Your prompt is only as good as your ideas.

"Make it faster" gets a guess. "Use a Set for lookups" gets the fix. You need to know the name of the right idea to ask for it.
---
AI makes code cheap. Knowing whether it's right is the skill that stays scarce.

Next: using AI coding tools without losing your skills.

#DeveloperGrowth
