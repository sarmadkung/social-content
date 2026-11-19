SERIES:    AI ENGINEERING #05
TITLE:     Agents Are Software: The Loop, and When a Workflow Does It Better
PILLAR:    AI Engineering — for engineers designing LLM features and agents
LEVEL:     ADVANCED
MODE:      COMPARE
FORMAT:    VISUAL
HEADLINE:  Agent or workflow: who picks the next step?
LAYOUT:    COMPARE
VISUALS:   1 = What is an agent, under the hood? · 2 = What breaks in the loop? · 3 = Agent or workflow: who picks the next step? · 4 = When is a workflow enough? · 5 = Takeaway · rest = text
STATUS:    draft
---
Strip away the framing and an AI agent is a loop.

That is good news for engineers who feel late to AI. And it leads to a question most teams skip: does this feature need the loop at all? Many "agents" would be better as a plain workflow.

What is an agent, under the hood?
Take tool calling (#04) and put it in a loop:

while (res.stop === 'tool_use') {
  const out = await run(res.tool)
  msgs.push(toolResult(out))
  res = await model(msgs)
}

That's it. The model asks for a tool, you run it, you hand back the result, you ask again. It stops when the model answers instead of asking for a tool. Everything else (planning, memory, orchestration) is structure built around that loop.

Takeaway: an agent is tool calling in a loop, plus the structure around it.

What breaks in the loop?
The hard parts aren't AI problems. They're the problems you already know:
→ The tool call fails? You need retries and timeouts, same as any network call.
→ The loop doesn't terminate? You need a step ceiling, same as any while loop.
→ The context fills up (#03)? You need an eviction strategy, same as any cache.
→ It does the wrong thing at step 14? You need traces, same as any distributed system.

Every one of those is ordinary engineering. The model is a component with unusually high variance. It isn't a different category of software.

The loop takes an afternoon to understand. Making it reliable takes everything you already learned building systems that don't fall over. AI engineering is software engineering applied to systems that use models. The fundamentals didn't get replaced. They got more load.

Takeaway: an agent's hard parts are retries, limits, memory and traces: ordinary engineering.

Agent or workflow: who picks the next step?
The same rule as anywhere in engineering: try the simplest option first.

A workflow is a fixed series of steps in your code. A model may run inside some steps, but your code decides the order.
An agent lets the model decide the next step. It runs the loop above: pick a tool, see the result, decide again, until done.

Think of a recipe and a chef. A recipe has fixed steps and gives the same dish each time. A chef looks in the fridge and decides as they go. More flexible, harder to predict.

Why does the choice matter? Each loop is another model call, and each call can go wrong. So agents cost more, take longer and fail in more ways. A workflow is easier to test, debug and price, because you know the path.

Workflow
→ Fixed path, decided by your code
→ Predictable cost and time
→ Testable step by step

Agent
→ Open path, decided by the model
→ Cost and time vary per task
→ Needs limits: a step cap, a budget and a clear stop condition

Both use the same parts: prompts, tools and, later in this series, RAG. Only control of the flow differs.

Takeaway: if your code picks the next step, it is a workflow. If the model does, an agent.

When is a workflow enough?
Support email triage, as a workflow:
1. A model labels it: refund, bug or question.
2. Code routes it to the right handler.
3. A model drafts a reply.
4. A human approves.
The steps are known, so no agent is needed.

Fixing a failing test is different. Nobody knows in advance which files to read. That is agent work.

The test:
Workflow: you can write the steps down.
Agent: the steps depend on what it finds along the way.

Senior detail: start with a workflow, even if you plan an agent. Where it breaks shows which step truly needs the model to decide. Often you end with a workflow that has one small agent inside.

[PERSONAL: a feature you built as an agent and later turned into a workflow, or the reverse]

Takeaway: if you can draw the flowchart, build a workflow.

Keep in mind before you build an agent
→ Log every step: two runs of one task can take different paths.
→ Test on many runs, not one: one pass proves little.
→ Give each tool only the access it needs: the model picks the calls.
→ Ask a human before anything you can't undo: send, pay, delete.
→ Set the step cap and budget before the first run, not after a bill.

Takeaway
An agent is a loop your code runs and the model steers. Use it only where the steps can't be written down. Everywhere else, a workflow is cheaper, faster and easier to trust.

Next: embeddings. Agents and RAG both need to find the right text, and that starts with turning text into numbers.

#AIEngineering #AIAgents #LLM #SoftwareArchitecture #SoftwareEngineering
