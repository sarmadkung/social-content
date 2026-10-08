"Add CSV export for invoices." An agent builds it in 20 minutes.

Then "Acme, Inc." downloads their file, and every column after the comma moves right.

The agent did what it was told. The problem is what it wasn't told. A workflow that fixes this:
---
8 stages: discover, spec, plan, build, verify, review, ship, watch.

The agent does the work in each stage. You say yes before the next one. Each stage leaves a file, so the agent remembers through the repo, not the chat.
[images: 1]
---
Why the early checks matter. The same wrong guess costs:
→ in the spec: 1 line
→ in the plan: 1 step
→ in the PR: redo the code
→ in production: undo + tell customers
[images: 2]
---
The spec is the real prompt. Goal, what's not in scope, what it must do. Each line becomes a test.

"handle commas in names" would have stopped the Acme bug.
[images: 3]
---
What breaks: vague specs, long chats that drift, two agents on the same files, and too many PRs to review.
[images: 4]
---
Agents made code cheap. Deciding what to build, and checking it's right, is still your job.

Next: how to break a problem down before you code.

#AIAgents #SoftwareEngineering
