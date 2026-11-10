---
title: "Agent or workflow? Ask who picks the next step"
description: "Agents and workflows use the same parts. The difference is who controls the flow, and it decides your cost, testing and failure modes."
date: 2027-03-03
series: "AI Engineering"
seriesNumber: 14
slug: ai-14-agent-vs-workflow
tags: [ai-agents, llm, workflows, software-architecture]
cover: cover.png
---

The last post ended with a simple rule: try the simplest option first. The same rule applies here. Many "agents" would be better as a plain workflow.

## What we'll cover

![In this post: agent vs workflow, two real tasks, and starting with a workflow](0.png)

1. **Agent vs workflow:** the model decides the order, or your code does.
2. **Two real tasks:** known steps vs steps you find along the way.
3. **Start with a workflow:** then add one small agent where it breaks.

## Agent vs workflow

![An agent loops: the model picks a tool, sees the result and decides again. A workflow runs fixed steps in the order your code sets](1.png)

A **workflow** is a fixed series of steps in your code. A model may run inside some steps, but your code decides the order.

An **agent** lets the model decide the next step. It runs in a loop: pick a tool (see the post on tool calling), see the result, decide again, until the task is done.

Think of a recipe and a chef. A recipe has fixed steps and gives the same dish each time. A chef looks in the fridge and decides as they go. More flexible, harder to predict.

Both use the same parts: prompts, tools, RAG. Only control of the flow differs.

- **Workflow:** fixed path, predictable cost, testable step by step.
- **Agent:** open path; cost and time vary per task.
- **Agents need limits:** a step cap, a budget and a clear stop condition.

## Why the choice matters

Each loop is another model call, and each call can go wrong. So agents cost more, take longer and fail in more ways. A workflow is easier to test, debug and price, because you know the path before it runs.

## Two real tasks

![Sorting a support email is four known steps; fixing a failing test is a loop where the model picks each step](2.png)

Support email triage, as a workflow:

1. A model labels it: refund, bug or question.
2. Code routes it to the right handler.
3. A model drafts a reply.
4. A human approves.

The steps are known, so no agent is needed. The model does real work in steps 1 and 3, but your code decides what happens with each answer.

Fixing a failing test is different. Nobody knows in advance which files to read. The next step depends on what the last one found. That is agent work.

The rule that falls out of this:

- **Workflow:** you can write the steps down.
- **Agent:** the steps depend on what it finds along the way.

## Start with a workflow, even for an agent

![Build it as a workflow, run it and see which step breaks, then make only that step a small agent](3.png)

Start with a workflow, even if you plan an agent. Where it breaks shows which step truly needs the model to decide. Often you end with a workflow that has one small agent inside, and everything around it stays easy to test, debug and price.

## Keep in mind before you build an agent

- Log every step: two runs of one task can take different paths.
- Test on many runs, not one: one pass proves little.
- Give each tool only the access it needs: the model picks the calls.
- Ask a human before anything you can't undo: send, pay, delete.

**In one line:** if you can draw the flowchart, build a workflow.

## Next in the series

Context engineering: choosing what goes into the model's context, and why it beats prompt tweaks.
