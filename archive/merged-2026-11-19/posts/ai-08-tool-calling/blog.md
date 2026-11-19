---
title: "Tool calling: the model asks, your code decides what runs"
description: "How tool calling (function calling) works: the model asks for a function, your code checks it, runs it and sends the result back."
date: 2027-01-04
series: "AI Engineering"
seriesNumber: 8
slug: ai-08-tool-calling
tags: [llm, tool-calling, function-calling, ai-agents]
cover: cover.png
---

A model cannot check your order status. It has no access to your database.

Tool calling is how it asks your code to check.

## What we'll cover

![In this post: the round trip, the anatomy of a tool, and the trust boundary](0.png)

1. **The round trip:** request, run, result, answer.
2. **Anatomy of a tool:** name, description, schema.
3. **The trust boundary:** validate, check, approve.

## What tool calling is

**Tool calling** (also called function calling) lets a model request that your code run a function. A **tool** is a function in your code that you let the model ask for. For example, `getOrder(id)` looks up one order in your database.

You describe the tools you offer. The model replies with a tool name and arguments, as structured output (post #07). Your code runs the function and sends the result back.

Think of a waiter. The waiter does not cook. They write your order on a ticket and pass it to the kitchen. The model writes the ticket. Your code is the kitchen.

## Why we need it

A model only produces text. On its own it cannot read live data, call an API or change anything. Without tools it guesses, and a guessed order status is a wrong answer said with confidence.

## The round trip

![The round trip: your app sends the message and tools, the model asks for getOrder, your code checks and runs it, the result goes back, the model answers](1.png)

1. Send the user message plus your list of tools.
2. The model replies with a request, not an answer: call `getOrder` with `{ "id": "A123" }`.
3. Your code checks the arguments and permissions, then runs `getOrder`.
4. You send the result back to the model.
5. The model writes the answer, or asks for another tool and the trip starts again at step 3.

## Anatomy of a tool

![A tool definition with its name, description and parameter schema, and the tool call the model sends back](2.png)

- **Each tool has a name, a description and a schema for its arguments.** A **schema** is a rule for which fields exist and what type each one is. For example: `id` must be a string, and it is required.
- **The model picks a tool from its description.** "Look up one order by its ID. Use when the user asks where their order is." tells it when to reach for `getOrder`. Write descriptions with care.
- **Arguments can still be wrong.** The model can send an ID that doesn't exist or a field in the wrong shape. Validate them like any model output.

## Treat every tool call as untrusted input

![Your code checks every tool call: valid arguments, permissions, and approval for actions that change things](3.png)

The model's request is input, like a form a user filled in. Your code checks it before anything runs:

1. **Are the arguments valid?** Check them against the schema.
2. **May this user do this?** Check permissions in your code, not in the prompt. A line in the prompt like "only refund the user's own orders" can be talked around by a clever message; a check in your code runs on every call.
3. **Does it change something?** For tools that change things, like refunds or deletes, add limits or a human approval step.

If a check fails, send the error back as the tool result, so the model can tell the user or try something else.

## Where it's used

Support bots that look up orders, coding assistants that read files and run tests, assistants that book meetings. Agents are built on it too.

Use it when the answer needs live data or an action. Skip it when the prompt already holds everything the model needs.

## Keep in mind when you give a model tools

- Offer only the tools this task needs. Fewer tools, fewer wrong picks.
- Send tool errors back as results, so the model can retry or explain.
- Cap tool calls per request, so a confused model can't loop forever.
- Log every call with its arguments. You'll need them to debug.
- Run tools with the user's permissions, never an admin key.

**In one line:** the model decides what to ask for. Your code decides what runs.

## Next in the series

Agents are software, not magic. Put tool calling in a loop and you have an agent.
