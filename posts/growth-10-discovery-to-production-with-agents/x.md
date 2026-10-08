"Add CSV export for invoices." An agent ships it in 20 minutes.

Then "Acme, Inc." downloads their file, and every column after the comma shifts right.

The agent did what it was told. The problem is what it wasn't told. A workflow that fixes this:
---
8 stages: discover, spec, plan, build, verify, review, ship, watch.

The agent does the work inside each stage. You sign off at the gates between them. Each stage leaves a file, so the agent's memory is the repo, not the chat.
[images: 1]
---
Why the early gates matter. The same wrong guess costs:
→ spec: one line
→ plan: one step
→ PR: a rework
→ production: a rollback + telling customers
[images: 2]
---
The spec is the real prompt. Goal, non-goals, acceptance criteria, edge cases. Each line becomes a test.

"commas and quotes are escaped" would have stopped the Acme bug.
[images: 3]
---
Where it breaks: vague specs, long sessions that drift, parallel agents on the same files, and review backlogs.
[images: 4]
---
Agents made code cheap. Deciding what to build, and checking it's right, is still the job. Put your time at the gates.

Next: how to break a problem down before you code.

#AIAgents #SoftwareEngineering
