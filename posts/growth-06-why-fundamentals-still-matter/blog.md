---
title: "AI writes the code. Fundamentals tell you if it's right."
description: "Why data structures, databases and networks still matter when AI writes your code, shown with one slow page and a one-line fix."
date: 2026-12-22
series: "Dev Growth"
seriesNumber: 6
slug: growth-06-why-fundamentals-still-matter
tags: [career, developer-growth, ai-coding, fundamentals, big-o]
cover: cover.png
---

An AI tool writes a function. It passes the tests. It runs fine on 100 rows. In production, with 100,000 rows, the page times out.

## The question

If AI can write the code, why learn data structures, databases and how networks work?

## The proof

![AI-written code that timed out, the fix with a Set, and how the work grows in each](1.png)

Back to that slow page. The generated code did this:

```js
for (const order of orders) {
  if (blockedIds.includes(order.userId)) { ... }
}
```

`includes()` checks the list one item at a time. 100,000 orders × 100,000 blocked IDs is up to 10 billion checks. A `Set` makes each lookup about one step on average:

```js
const blocked = new Set(blockedIds);
if (blocked.has(order.userId)) { ... }
```

**Big-O** is how the work grows as the input grows. Here, the list check grows with orders × blocked IDs. The Set check grows with orders + blocked IDs. Someone who knows Big-O spots this in review in seconds. Someone who does not ships it.

## The reason, step by step

![Five reasons fundamentals still pay off when AI writes the code](2.png)

1. **Your job moves from typing to judging.** You read more code than you write. You cannot judge code you could not have written.
2. **AI code looks right.** It is clean, well named and confident. The bugs hide one level down: in how it scales, in what runs at the same time, in what happens when the network fails. That level is fundamentals.
3. **Your prompt is only as good as your ideas.** "Make it faster" gets a guess. "Use a Set for lookups" or "add an index on user_id" gets the fix. You need to know the name of the right idea to ask for it.
4. **When it breaks, you debug alone.** The tool can suggest causes. You still decide which one is true, using what you know about how the system works.
5. **Tools change every few months. Fundamentals change slowly.** What you learn about memory, data and networks keeps paying for your whole career.

## What goes wrong if you skip fundamentals

- You accept code because it runs, not because it is right.
- You cannot tell a good suggestion from a bad one, so you try them all.
- Your growth stalls. Seniority is judgment, and judgment is built on fundamentals.

## For seniors

Fundamentals are now the review skill. When a junior's diff came from a tool, ask "why this approach?" The answer shows what they understand.

## Keep in mind when you review AI-written code

- Test with real data sizes. Slow code hides in 100-row tests.
- Ask how the work grows as the input grows, before you accept.
- When the tool fixes something, learn the idea behind the fix.
- Can't explain why it works? Don't merge it yet.

**In one line:** AI makes code cheap. Knowing whether it is right is the skill that stays scarce.

## Next in the series

Using AI coding tools without losing your skills: the how, step by step.
