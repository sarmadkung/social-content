SERIES:    AI ENGINEERING #13
TITLE:     Agent vs Workflow: Which One Do You Need?
PILLAR:    AI Engineering — for engineers designing LLM features and agents
HEADLINE:  Agent or workflow: who picks the next step?
LAYOUT:    COMPARE
---
Last post said: try the simplest option first. The same rule applies here. Many "agents" would be better as a plain workflow.

What is it?
A workflow is a fixed series of steps in your code. A model may run inside some steps, but your code decides the order.
An agent lets the model decide the next step. It runs in a loop: pick a tool (#08), see the result, decide again, until done.

Think of a recipe and a chef. A recipe has fixed steps and gives the same dish each time. A chef looks in the fridge and decides as they go. More flexible, harder to predict.

Why does the choice matter?
Each loop is another model call, and each call can go wrong. So agents cost more, take longer and fail in more ways. A workflow is easier to test, debug and price, because you know the path.

Key properties
• Workflow: fixed path, predictable cost, testable step by step.
• Agent: open path, cost and time vary per task.
• Both use the same parts: prompts, tools, RAG. Only control of the flow differs.
• Agents need limits: a step cap, a budget and a clear stop condition.

Example
Support email triage, as a workflow:
1. A model labels it: refund, bug or question.
2. Code routes it to the right handler.
3. A model drafts a reply.
4. A human approves.
The steps are known, so no agent is needed.
Fixing a failing test is different. Nobody knows in advance which files to read. That is agent work.

When to use it / when not to
Workflow: you can write the steps down.
Agent: the steps depend on what it finds along the way.

Senior detail: start with a workflow, even if you plan an agent. Where it breaks shows which step truly needs the model to decide. Often you end with a workflow that has one small agent inside.

[PERSONAL: a feature you built as an agent and later turned into a workflow, or the reverse]

Takeaway: if you can draw the flowchart, build a workflow.

Next: context engineering. Choosing what goes into the model's context, and why it beats prompt tweaks.

#AIEngineering #AIAgents #LLM #SoftwareArchitecture
