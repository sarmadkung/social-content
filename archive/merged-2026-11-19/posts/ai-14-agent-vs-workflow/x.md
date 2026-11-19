Many "agents" would be better as a plain workflow.

Both use the same parts: prompts, tools, RAG. The only difference is who picks the next step: your code, or the model.
[images: 0, 1]
---
Workflow: fixed steps, your code decides the order. A model may run inside a step.

Agent: the model picks the next step in a loop until done.

Each extra loop is another model call: more cost, more time, more ways to fail.
---
Support email triage is a workflow: label, route, draft a reply, human approves. The steps are known.

Fixing a failing test is agent work. Nobody knows in advance which files to read.
[images: 2]
---
Start with a workflow, even if you plan an agent. Where it breaks shows which step needs the model to decide.

Often you end with a workflow that has one small agent inside.
[images: 3]
---
If you can draw the flowchart, build a workflow.

Next: context engineering, and why it beats prompt tweaks.

#AIEngineering #AIAgents
