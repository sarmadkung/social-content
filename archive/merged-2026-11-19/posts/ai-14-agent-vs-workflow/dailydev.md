TITLE: Agent or workflow? Ask who picks the next step
COVER: cover.png
---

Many "agents" would be better as a plain workflow. Both use the same parts: prompts, tools, RAG. The only real difference is control of the flow.

- **Workflow:** a fixed series of steps in your code. A model may run inside some steps, but your code decides the order. Like a recipe: same steps, same dish.
- **Agent:** the model picks the next step. It runs in a loop: pick a tool, see the result, decide again, until done. Like a chef deciding as they go.
- **Why it matters:** each loop is another model call, and each call can go wrong. Agents cost more, take longer and fail in more ways. A workflow is easier to test, debug and price, because you know the path.
- **Workflow example:** support email triage. A model labels it (refund, bug or question), code routes it, a model drafts a reply, a human approves. The steps are known.
- **Agent example:** fixing a failing test. Nobody knows in advance which files to read.
- **Agents need limits:** a step cap, a budget and a clear stop condition.

Start with a workflow, even if you plan an agent. Where it breaks shows which step truly needs the model to decide. Often you end with a workflow that has one small agent inside.

If you can draw the flowchart, build a workflow.
