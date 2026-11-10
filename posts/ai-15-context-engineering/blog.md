---
title: "Context engineering: treat the window as a budget, not a bucket"
description: "Context engineering is deciding what the model sees at each step. Four questions per step, an explicit token budget, and what to measure."
date: 2027-03-12
series: "AI Engineering"
seriesNumber: 15
slug: ai-15-context-engineering
tags: [context-engineering, ai-agents, llm, tokens]
cover: cover.png
---

When a model gets something wrong, the first instinct is to give it more. More documents, more history, a bigger window.

A bigger window is not the fix. A 200k window isn't 200k useful context.

## What context engineering is

**Context engineering** is deciding what the model sees at each step. Not what it could see: what it should see. In an agent, that choice comes back at every step of the loop.

The **context window** is the most tokens a model can see at once (see the post on tokens and context windows). It holds everything: instructions, tool descriptions, documents, chat history and the answer being written.

It is closer to cache design than to prompt writing. You are choosing what enters a working set, what gets evicted, and what gets invalidated because it is out of date.

## Why it matters

Long context is not free memory. It is a search the model has to do before it can solve your problem. Three useful sentences inside a pile of loosely related material are still three sentences the model has to find first.

## The four questions per step

![Four questions per step: is it relevant, can it be summarised, can it be fetched when needed, is it stale](2.png)

Ask these before every step:

- **What is actually relevant to this step,** not to the whole session?
- **What can be summarised instead of carried?** Twelve tool calls become three lines of outcome.
- **What should be retrieved on demand rather than preloaded?** If something is needed once in twenty steps, it is a tool call, not a prompt section.
- **What is stale?** An old plan or a replaced file does not sit there quietly. It competes with the current truth, and sometimes wins.

## Budget it explicitly

![An example budget of 5,600 tokens for one agent step, split into system, tools, retrieved docs and history, inside a 200,000-token window](1.png)

Give each part of the window a number and enforce it. For example: system prompt 800 tokens, tool descriptions 1,200, retrieved documents 3,000, history 600. That is 5,600 tokens for the step, in a window that could hold far more.

When retrieval suddenly wants 9,000 tokens, that is a design decision, not an accident. The budget makes you notice it and decide.

## What to measure

Measure tokens per successful task, not tokens per window. A full window says nothing about whether the task got done.

## Keep in mind when you design an agent's context

- Log the exact context of every step: you can't debug what you never saw.
- Every tool description takes room in the window: drop unused tools.
- Summarise outcomes, but keep IDs, paths and error text exact.
- Test at step 30, not step 1: late steps carry the most context.

**In one line:** the window is a budget, not a bucket. Decide what goes in at every step.

A question to try on your own agent: what is in its context right now that has not been read in ten steps?

## Next in the series

AI memory, short-term vs long-term: what an agent should carry, and what it should store.
