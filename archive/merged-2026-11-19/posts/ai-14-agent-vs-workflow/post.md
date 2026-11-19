> ⚠ NOT READY — resolve these, then delete this block:
> - [PERSONAL: a feature you built as an agent and later turned into a workflow, or the reverse]

---

Many "agents" would be better as a plain workflow.

Both use the same parts: prompts, tools, RAG.
The only difference is who picks the next step.

In a workflow, your code decides the order.
In an agent, the model decides, in a loop, until it's done.

Why it matters: every extra loop is another model call. Agents cost more, take longer and fail in more ways. A workflow is easier to test, debug and price, because you know the path.

What's in the images:
1. Agent vs workflow: who drives
2. Two real tasks: known steps vs steps you find
3. Start with a workflow, then add one small agent

The takeaway: if you can draw the flowchart, build a workflow.

Next: context engineering. Choosing what goes into the model's context, and why it beats prompt tweaks.

#AIEngineering #AIAgents #LLM #SoftwareArchitecture
