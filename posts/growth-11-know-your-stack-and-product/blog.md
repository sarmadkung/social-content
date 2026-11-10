---
title: "Building with agents: why stack and product knowledge still matter"
description: "Coding agents build on every answer you give them. Why the stack you know, the product you understand and the big picture you keep still decide the result."
date: 2027-02-09
series: "Dev Growth"
seriesNumber: 11
slug: growth-11-know-your-stack-and-product
tags: [coding-agents, developer-growth, ai-engineering, software-engineering]
cover: cover.png
---

The agent asks: "Should I store sessions in Redis or in Postgres?" You don't know the stack well, so you pick one. The agent builds on it for three weeks: login, logout, rate limits, "remember me". Then you find out the choice does not fit how you deploy. Now you are rewriting auth, not adding features.

The agent did nothing wrong. It asked. The answer was the problem.

## What we'll cover

![In this post: three lessons for building with agents](0.png)

1. **Pick a stack you already know**, so you can judge what the agent picks.
2. **Know the product deeply**, with a one-page brief before the first prompt.
3. **Keep the big picture yourself**, in one progress file the agent reads.

## The question

If agents can write most of the code, why does it still matter what stack you pick and how well you know the product?

## The reason, step by step

1. **Agents ask you questions all the time.** Which database, which library, what happens when a payment fails, who can see this page. Each answer is a decision the agent builds on.
2. **One wrong answer early moves the whole product.** The agent does not push back on a bad choice. It builds on it quickly, so the cost of the mistake grows quickly too.
3. **You can only answer well in a stack you know.** If you have never used a tool, you cannot tell a good suggestion from a bad one. You just accept it.
4. **You can only answer product questions if you know the product.** "Should admins see deleted orders?" has no technical answer. It depends on who the users are and what they need.
5. **Someone has to hold the big picture.** The agent works on one task at a time. It does not track what is done, what is half-done and what is left. If you don't, nobody does.

## Lesson 1: Pick a stack you already know

![The same agent question in a stack you don't know and in one you do](1.png)

**What goes wrong without it:** you accept every choice the agent makes, because you cannot judge any of them.

**What to do:** pick tools you could review a diff in. A boring stack you know beats a new one you don't. Learn new tools on side projects, not on the product you need to ship.

## Lesson 2: Know the product deeply

![An example one-page product brief for an invoicing app](2.png)

**What goes wrong without it:** you answer the agent's questions with guesses, and each guess sends the product a little further from what users need.

**What to do:** before the first prompt, write a one-page product brief:

- who it is for
- the 3 to 5 things it must do
- what it will not do (yet)
- the rules that never change (for example: "a user only sees their own invoices")

Point the agent to this brief. Read it again before you answer a big question.

## Lesson 3: Keep the big picture yourself

![An example progress.md: done, in progress, next and decisions](3.png)

**What goes wrong without it:** you only give commands. You don't know what was built, what is broken or what is left. Every session starts from scratch, and the product never reaches the end.

**What to do:** keep a `progress.md` file in the repo and update it after every session:

- **Done:** what works, and how you checked it
- **In progress:** what is half-built
- **Next:** the next 3 tasks, in order
- **Decisions:** what you chose and why (Postgres for sessions, because we already run it)

The agent reads it at the start. You read it to know where the product stands.

## What goes wrong if you ignore this

- **The product drifts.** Each answer is a little off, and after a month it is not the product you planned.
- **You can't review the work.** Checking an agent's output still needs you to understand the stack (how to review it is Dev Growth #09).
- **You become a person who only gives commands.** Lots of activity, but no finish line.

## Keep in mind when you build a product with agents

- Not sure of an answer? Ask the agent for trade-offs, not a pick.
- Try a new tool in a throwaway branch before it enters the product.
- A new library the agent adds is a stack choice too. Check it.
- Update `progress.md` before you close the session, not tomorrow.
- A request that surprises you? Check the brief before you answer.

**In one line:** agents make building fast. Only you know where it is going.

## Next in the series

Agents changed the case for cross-platform frameworks.
