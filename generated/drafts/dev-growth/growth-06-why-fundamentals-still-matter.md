SERIES:    DEV GROWTH #06
TITLE:     Why Fundamentals Still Matter When AI Writes Code
PILLAR:    Career & Developer Growth — for students and junior developers, and seniors deciding what to teach them
LEVEL:     INTERMEDIATE
MODE:      WHY
FORMAT:    VISUAL
HEADLINE:  AI writes code. Fundamentals judge it.
LAYOUT:    STATEMENT
STATUS:    draft
---
An AI tool writes a function. It passes the tests. It runs fine on 100 rows. In production, with 100,000 rows, the page times out.

The question
If AI can write the code, why learn data structures, databases and how networks work?

The reason, step by step
1. Your job moves from typing to judging. You read more code than you write. You cannot judge code you could not have written.
2. AI code looks right. It is clean, named well and confident. The bugs hide one level down: in how it scales, in what runs at the same time, in what happens when the network fails. That level is fundamentals.
3. Your prompt is only as good as your ideas. "Make it faster" gets a guess. "Use a Set for lookups" or "add an index on user_id" gets the fix. You need to know the name of the right idea to ask for it.
4. When it breaks, you debug alone. The tool can suggest causes. You still decide which one is true, using what you know about how the system works.
5. Tools change every few months. Fundamentals change slowly. What you learn about memory, data and networks keeps paying for your whole career.

The proof
Back to that slow page. The generated code did this:

for (const order of orders) {
  if (blockedIds.includes(order.userId)) { ... }
}

includes() checks the list one item at a time. 100,000 orders × 100,000 blocked IDs is up to 10 billion checks. A Set makes each lookup about one step:

const blocked = new Set(blockedIds);
if (blocked.has(order.userId)) { ... }

Someone who knows Big-O (how work grows as the input grows) spots this in review in ten seconds. Someone who does not ships it.

What goes wrong if you skip fundamentals
→ You accept code because it runs, not because it is right.
→ You cannot tell a good suggestion from a bad one, so you try them all.
→ Your growth stalls. Seniority is judgment, and judgment is built on fundamentals.

[PERSONAL: one bug in AI-written code you caught because you knew the underlying concept]

For seniors
Fundamentals are now the review skill. When a junior's diff came from a tool, ask "why this approach?" The answer shows what they understand.

Takeaway
AI makes code cheap. Knowing whether it is right is the skill that stays scarce.

Next: using AI coding tools without losing your skills. The how, step by step.

#DeveloperGrowth #SoftwareEngineering #AIEngineering #CareerGrowth #Programming
