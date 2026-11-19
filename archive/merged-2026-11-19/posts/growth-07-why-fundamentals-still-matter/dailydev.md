TITLE: AI writes the code. Fundamentals tell you if it's right.
COVER: cover.png
---
An AI tool writes a function. It passes the tests and runs fine on 100 rows. In production, with 100,000 rows, the page times out.

The generated code checked each order against a list of blocked IDs with `blockedIds.includes(order.userId)`. `includes()` checks the list one item at a time, so 100,000 orders × 100,000 blocked IDs is up to 10 billion checks. Building a `Set` once and calling `blocked.has(order.userId)` makes each lookup about one step on average.

Anyone who knows Big-O (how the work grows as the input grows) spots this in review. If AI can write the code, this is why fundamentals still matter:

- **You judge more than you type.** You can't judge code you could not have written.
- **AI code looks right.** The bugs hide one level down: how it scales, what runs at the same time, what happens when the network fails.
- **A prompt needs the idea.** "Make it faster" gets a guess. "Use a Set for lookups" or "add an index on user_id" gets the fix.
- **You debug alone.** The tool suggests causes; you decide which one is true.
- **Fundamentals last.** Tools change every few months. Memory, data and networks change slowly.

AI makes code cheap. Knowing whether it is right is the skill that stays scarce.
